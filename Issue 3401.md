# Issue 3401: extend li to work with complex input

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-06-11 17:46:09

Assignee: gfurnish

CC:  myurko benjaminfjones

Here is some example code from M. Yurko that explains how to do this.
I think something based on this should be put into the Li function itself.


```
O.K. I defined li(x) as follows:

def li(z): #def log integral for real and complex variables
   if z in RR and z >= 2: #check if real number greater than 2
       return Li(z) +
1.045163780117492784844588889194613136522615578151 #adjust for offset
in SAGE def
   elif z == 1:
       return -infinity
   else: #mode for complex and below 2 from incomplete gamma
       z = CDF(z)
       return -gamma_inc(0,-log(z)) + (log(log(z))-log(1/log(z)))/2-
log(-log(z))

The first part uses SAGE's built in Li(x) but adjusts for the offset.
The second part should be self explanatory. The third part uses a
formula involving the incomplete gamma function which I found on the
Wolfram Functions website. On testing different values with an
external calculator,  the third statement appears to only be valid for
negative reals and complex numbers. This leaves the interval [0,2)
undefined. Please note that I have no background in complex analysis
and that my above statements about domain are only based upon
experimentation.
```



---

Comment by was created at 2008-06-11 18:53:04

No version

```
def li(z): #def log integral for real and complex variables
   if z in RR and z >= 2: #check if real number greater than 2
       return Li(z) +
1.045163780117492784844588889194613136522615578151 #adjust for offset
in SAGE def
   elif z == 0:
       return 0
   elif z > 1 and z < 2:
       return Ei(log(z))
   elif z == 1:
       return -infinity
   elif z > 0 and z < 1:
       return
   else: #mode for complex and below 2 from incomplete gamma
       z = CDF(z)
       return -gamma_inc(0,-log(z)) + (log(log(z))-log(1/log(z)))/2-
log(-log(z))

```



---

Comment by AlexGhitza created at 2009-01-22 18:21:39

Changing type from defect to enhancement.


---

Attachment


---

Attachment


---

Comment by myurko created at 2009-10-29 23:23:52

Changing status from new to needs_review.


---

Attachment

Sorry in advance to the reviewer and release manager, but I couldn't figure out how to flatten the patches without applying them.


---

Comment by mhansen created at 2009-11-04 09:15:41

I've added a patch which folds the above patches together and deprecates the eps_rel and err_bound parameters so that code that uses them won't "break", but will get a deprecation warning.

I'm okay with myurko's changes so if someone could sign off on the deprecation warning, that'd be great.


---

Comment by kcrisman created at 2009-11-10 13:12:33

Overall looks good, but there should be at least one doctest for the new DeprecationWarnings (I think this was agreed upon somewhere on sage-devel), and there should also be documentation that this actually fulfills the ticket - namely, to extend Li to complex input!  It certainly does, but I have no idea if the output is correct (I assume it is):

```
sage: Li(1+i)
-0.431252110896297 + 2.05958421419258*I
sage: Li(2+i)
0.366095261900308 + 1.22470693841030*I
sage: Li(2+2*i)
0.875423840014232 + 1.96947430597102*I
sage: Li(-2-2*i)
-0.333825651054542 - 3.94714365810975*I
sage: Li(-8)
-1.74509249432858 + 5.26897573517771*I
sage: Li(-10)
-2.04384864349662 + 5.69678038115052*I
sage: Li(-100)
-15.9214591889007 + 17.3366538615045*I
```

Something like that should be added.


---

Comment by kcrisman created at 2009-11-10 13:12:33

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by mhansen created at 2010-01-16 17:58:10

I've put up a new patch which address the above concerns.


---

Comment by mhansen created at 2010-01-16 17:58:10

Changing status from needs_work to needs_review.


---

Attachment

Looks good - sometimes slower, sometimes faster, but it's much better to have the complex functionality than worry about the rest.  I removed an auxiliary function which only existed to allow the previous implementation.  Positive review!


---

Comment by kcrisman created at 2010-01-18 16:48:18

Changing status from needs_review to positive_review.


---

Comment by burcin created at 2010-01-18 18:02:08

Changing status from positive_review to needs_work.


---

Comment by burcin created at 2010-01-18 18:02:08

Sorry to come in this late to the discussion, but this needs more work.

The `prec` argument to symbolic functions is deprecated, adding it to `Li` now doesn't make sense.


```
sage: gamma(10,prec=100)
.../_home_burcin__sage_init_sage_0.py:1: DeprecationWarning: The prec keyword argument is deprecated. Explicitly set the precision of the input, for example gamma(RealField(300)(1)), or use the prec argument to .n() for exact inputs, e.g., gamma(1).n(300), instead.
  # -*- coding: utf-8 -*-
362880.00000000000000000000000
```


You can get the precision from the argument provided by the user. If the user needs a higher precision, they should explicitly convert the argument to a higher precision, for example by using `RealFiel(300)(val)`.

We should also start converting these to proper symbolic functions that remain symbolic on exact input, but that can be left to another ticket.


---

Comment by myurko created at 2010-02-10 15:36:38

What is wrong with the prec argument? By default it is left as None and will get the precision from the argument as you said.


---

Comment by burcin created at 2010-08-28 16:15:39

Changing keywords from "" to "beginner".


---

Comment by kcrisman created at 2011-10-09 01:28:48

Possibly related to #11143.


---

Comment by benjaminfjones created at 2011-10-09 01:54:57

In #11143 a fully symbolic function is defined for `li(x)` called `exp_integral_li`, the non-offset logarithmic integral. It would be very easy to add `Li` by simply returning `exp_integral_li(x) - exp_integral_li(2)`. On the other hand, adding a symbolic version of `Li`  would be equally easy by copying the definition of `exp_integral_li` and making one simple change. 

If so, what would a good name for the offset `Li` be? Maybe `exp_integral_li_offset`? 

Another thought is that in #11143, we could add an optional parameter `offset` to the init method for `exp_integral_li` which would return `Li` instead of `li`. The eval and evalf methods could be bound in the init call to return the right values and the derivative is obviously the same for both.

Either of these solutions could be put into #11143 without much effort and that would take care of the issue in this ticket because evaluation at complex inputs is handled by mpmath for all the functions defined there.


---

Comment by kcrisman created at 2011-10-10 02:16:18

My understanding is that the offset `Li` is the same as `li`.  But maybe I've missed something while looking into this - I'm not a special functions expert.  

I think that as long as we have both of these, and not named super-crazily - such as just being named `Li` and `li` - this would be fine.  I think the parameter is not needed.


---

Comment by leif created at 2011-10-12 06:44:20

Just for the record:


```python
sage: import mpmath
sage: mpmath.li(1+i)
mpc(real='0.61391166922119556', imag='2.0595842141925775')
sage: mpmath.li(1+i, offset=True)
mpc(real='-0.43125211089629728', imag='2.0595842141925775')
```


But maybe I've missed something (tl;dr).


---

Comment by kcrisman created at 2011-10-12 12:29:20

I don't think you're missing anything.   In #11143 I think Benjamin is using mpmath as much as possible (though we should be checking timings...).  In principle, the hope is that #11143 will render this ticket obsolete, but I like to keep things complete for trollers :)


---

Comment by kcrisman created at 2012-05-26 17:20:39

I'm changing this to make the (offset) Li symbolic and to work with complex input.  Simply using the ideas of #11143 should be sufficient.


---

Attachment

Symbolic Li


---

Comment by martinx created at 2012-07-28 21:31:25

I have created a symbolic Li patch on top of #11143 on sage-5.2.rc1 .  This is my first go at a patch so no doubt will need a good scrubbing...

Please note doing this is a hobby for me and I have little or no time weekdays to do anything so my responses are likely to be slow.


---

Comment by kcrisman created at 2012-07-29 01:37:15

> I have created a symbolic Li patch on top of #11143 on sage-5.2.rc1 .  This is my first go at a patch so no doubt will need a good scrubbing...
That's okay, we all have to start somewhere!
> Please note doing this is a hobby for me and I have little or no time weekdays to do anything so my responses are likely to be slow.  
That's also _very_ true for many of us.  So we may also be slow to respond.


---

Comment by benjaminfjones created at 2012-08-03 20:42:58

Hi `@`martinx, your patch looks very good. I spotted a few whitespace issues to clean up (I'll post a reviewer patch to do that). I'm running full tests now, but I expect a positive review. 

----

I wonder if we really need three aliases at the top level for this function. Having `log_integral_eulerian` in addition to `Li` and `log_integral_offset` seems excessive to me, but if that's a common name for the function I'm OK with it.


---

Attachment

reviewer patch


---

Comment by benjaminfjones created at 2012-08-03 20:44:29

Changing status from needs_work to needs_review.


---

Comment by leif created at 2012-08-04 11:42:18

Replying to [comment:22 benjaminfjones]:
> I wonder if we really need three aliases at the top level for this function. Having `log_integral_eulerian` in addition to `Li` and `log_integral_offset` seems excessive to me, but if that's a common name for the function I'm OK with it.

There's also "European Li" (for the offset one) IIRC... ;-)


---

Comment by martinx created at 2012-08-04 14:45:04

I will go with whatever the sagemath intelligentsia thinks appropriate for the number and name of any aliases. 

And I had better read up on coding conventions before my next efforts :)


---

Comment by benjaminfjones created at 2012-08-04 15:20:51

Don't worry about the coding conventions, some of them are unwritten and some of them are subtle. I found a few doctest errors after running `make ptestlong` with the patches applied. These should be simple to fix:

Change 9 to 10:

```
File "/home/jonesbe/sage/sage-5.2/devel/sage-11143/sage/misc/sagedoc.py", line 971:
    sage: len(search_src('log', 'derivative', interact=False).splitlines()) < 9
Expected:
    True
Got:
    False
```


simple change, `Li` is now fully symbolic:

```
File "/home/jonesbe/sage/sage-5.2/devel/sage-11143/sage/functions/transcendental.py", lin
e 195:
    sage: Li(100)
Expected:
    29.080977804
Got:
    -log_integral(2) + log_integral(100)
```


This one is more mysterious:

```
File "/home/jonesbe/sage/sage-5.2/devel/sage-11143/sage/symbolic/random_tests.py", line 2
36:
    sage: print "ignore this";  random_expr(50, nvars=3, coeff_generator=CDF.random_eleme
nt) # random
Exception raised:
    Traceback (most recent call last):      File "/home/jonesbe/sage/sage-5.2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jonesbe/sage/sage-5.2/local/bin/sagedoctest.py", line 38, in run_one_ex
ample
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jonesbe/sage/sage-5.2/local/bin/ncadoctest.py", line 1172, in run_one_e
xample
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[4]>", line 1, in <module>
        print "ignore this";  random_expr(Integer(50), nvars=Integer(3), coeff_generator=CDF.random_element) # random###line 236:
    sage: print "ignore this";  random_expr(50, nvars=3, coeff_generator=CDF.random_element) # random

    sage: print "ignore this";  random_expr(50, nvars=3, coeff_generator=CDF.random_element) # random
      File "/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/random_tests.py", line 258, in random_expr
        return random_expr_helper(size, internal, leaves, verbose)
      File "/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/random_tests.py", line 206, in random_expr_helper
        children = [random_expr_helper(n+1, internal, leaves, verbose) for n in nodes_per_child]
      File "/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/random_tests.py", line 209, in random_expr_helper
        return r[1](*children)
      File "function.pyx", line 432, in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4941)
        res = g_function_evalv(self._serial, vec, hold)
      File "/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/integration/integral.py", line 173, in _eval_
        return integrator(*args)
      File "/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/integration/external.py", line 21, in maxima_integrator
        result = maxima.sr_integral(expression, v, a, b)
      File "/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/interfaces/maxima_lib.py", line 746, in sr_integral
        raise error
    RuntimeError: ECL says: Error executing code in Maxima: defint: upper limit of integration must be real; found 
     elliptic_eu(.18648175298340663*I-.7457199773032457,
                 coth(v3)*(v3*(.12348638361486497*I+.29875723285490263)
                          +v1*(.12348638361486497*I+.29875723285490263)
                          -sinh(v3^(.5481180571998028*I-.5534231539946481))))
```



---

Comment by leif created at 2012-08-04 15:28:40

Replying to [comment:25 martinx]:
> I will go with whatever the sagemath intelligentsia thinks appropriate for the number and name of any aliases. 

Well, with names put into the global namespace, the most important thing is that tab completion is likely to suggest you what you're looking for, i.e., the _prefix_ of each name matters.  So in this case I think a single instance of `log_int*` (in addition to `[Ll]i*`, maybe more) would be sufficent.

With Sage 5.3.beta0, I currently get:

```
sage: log<TAB>
log             log_b           log_gamma       log_text        logstr          
log2            log_dvi         log_html        lognormvariate  
sage: li<TAB>
license                lim                    linear_program         list                   list_plot_semilogx
lie                    limit                  linear_relation        list_composition       list_plot_semilogy
lie_console            line                   linear_transformation  list_plot              
lift                   line2d                 lisp                   list_plot3d            
lift_to_sl2z           line3d                 lisp_console           list_plot_loglog       
sage: Li<TAB>  
Li                         LinearCode                 LinearCodeFromVectorSpace  
LiE                        LinearCodeFromCheckMatrix  Lisp                       
sage: euler<TAB>
euler_gamma             euler_phi               eulers_method_2x2       
euler_number            eulers_method           eulers_method_2x2_plot  
```



(Of course also the docstring for e.g. `li`, perhaps that of `Ei`, too, should refer to `Li` and vice versa.)


---

Comment by leif created at 2012-08-04 15:48:01

(Also on top of the reviewer patch: ;-) )

`s/eulerian/Eulerian/`

`s/for `x > 1`/for `x \geq 2`/`


---

Comment by leif created at 2012-08-04 16:03:20

Nice theorem:

\exists x : `\pi(x) > \operatorname{Li}(z)`

(`s/z/x/`)




`s/`

```
However it is a theorem that there are very large, (e.g., around `10^{316}`) values of `x`
```

`/`

```
However, it is a theorem that there are very large values of `x` (e.g., around `10^{316}`)
```

`/`


---

Comment by leif created at 2012-08-04 16:19:35

More nitpicking:  `s/"polylog()"/``polylog()``/` and/or make (it) a cross-reference (`:func:`polylog`` -- not sure whether it has to be `:class:`sage.functions.log.Function_polylog``).


---

Comment by leif created at 2012-08-04 16:23:40

Replying to [comment:30 leif]:
> ... not sure whether it has to be `:class:`sage.functions.log.Function_polylog``).

... or rather `:class:`polylog <sage.functions.log.Function_polylog>`` or something like that.


---

Comment by martinx created at 2012-08-04 23:17:00

Replying to [comment:26 benjaminfjones]:
> Don't worry about the coding conventions, some of them are unwritten and some of them are subtle.

and I am a slow learner anyway :)

>I found a few doctest errors after running `make ptestlong` with the patches applied. These should be simple to fix:
> 
> Change 9 to 10:
Agreed.

> 
> simple change, `Li` is now fully symbolic:
> {{{
> File "/home/jonesbe/sage/sage-5.2/devel/sage-11143/sage/functions/transcendental.py", lin
> e 195:
>     sage: Li(100)
> Expected:
>     29.080977804
> Got:
>     -log_integral(2) + log_integral(100)
> }}}

The function can be removed since it was just a convenience one to support the original li and Li.
> 
> This one is more mysterious:
> {{{
> File "/home/jonesbe/sage/sage-5.2/devel/sage-11143/sage/symbolic/random_tests.py", line 2
> 36:
>     sage: print "ignore this";  random_expr(50, nvars=3, coeff_generator=CDF.random_eleme
> nt) # random
> Exception raised:
>     Traceback (most recent call last):      File "/home/jonesbe/sage/sage-5.2/local/bin/ncadoctest.py", line 1231, in run_one_test
>         self.run_one_example(test, example, filename, compileflags)
>       File "/home/jonesbe/sage/sage-5.2/local/bin/sagedoctest.py", line 38, in run_one_ex
> ample
>         OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
>       File "/home/jonesbe/sage/sage-5.2/local/bin/ncadoctest.py", line 1172, in run_one_e
> xample
>         compileflags, 1) in test.globs
>       File "<doctest __main__.example_5[4]>", line 1, in <module>
>         print "ignore this";  random_expr(Integer(50), nvars=Integer(3), coeff_generator=CDF.random_element) # random###line 236:
>     sage: print "ignore this";  random_expr(50, nvars=3, coeff_generator=CDF.random_element) # random
> 
>     sage: print "ignore this";  random_expr(50, nvars=3, coeff_generator=CDF.random_element) # random
>       File "/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/random_tests.py", line 258, in random_expr
>         return random_expr_helper(size, internal, leaves, verbose)
>       File "/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/random_tests.py", line 206, in random_expr_helper
>         children = [random_expr_helper(n+1, internal, leaves, verbose) for n in nodes_per_child]
>       File "/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/random_tests.py", line 209, in random_expr_helper
>         return r[1](*children)
>       File "function.pyx", line 432, in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4941)
>         res = g_function_evalv(self._serial, vec, hold)
>       File "/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/integration/integral.py", line 173, in _eval_
>         return integrator(*args)
>       File "/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/symbolic/integration/external.py", line 21, in maxima_integrator
>         result = maxima.sr_integral(expression, v, a, b)
>       File "/home/jonesbe/sage/sage-5.2/local/lib/python/site-packages/sage/interfaces/maxima_lib.py", line 746, in sr_integral
>         raise error
>     RuntimeError: ECL says: Error executing code in Maxima: defint: upper limit of integration must be real; found 
>      elliptic_eu(.18648175298340663*I-.7457199773032457,
>                  coth(v3)*(v3*(.12348638361486497*I+.29875723285490263)
>                           +v1*(.12348638361486497*I+.29875723285490263)
>                           -sinh(v3^(.5481180571998028*I-.5534231539946481))))
> }}}

The function randomly selects from a list of all Pynac functions, to which is now added Li, and so now the functions chosen have changed.  The docs state that it will often raise an error because it tries to create an erroneous expression.  In this case it is trying to pass a complex expression to Maxima. Trial and error and got a return result setting the seed to 1.

When I have worked out how to merge patches I'll post a revised patch for review that addresses all comments made so far.


---

Comment by martinx created at 2012-08-04 23:18:53

Replying to [comment:31 leif]:
> Replying to [comment:30 leif]:
> > ... not sure whether it has to be `:class:`sage.functions.log.Function_polylog``).
> 
> ... or rather `:class:`polylog <sage.functions.log.Function_polylog>`` or something like that.

Both seem to be allowed:   http://www.sagemath.org/doc/developer/sage_manuals.html#chapter-sage-manuals-links


---

Comment by martinx created at 2012-08-05 00:58:04

Revised Li including reviewer patch


---

Attachment

I think v2 addresses all comments made so far and includes reviewer patch.  ptestlong passes I think;  I had some issues with sagedoc.py but that now passes all tests.  Too tired to run ptestlong yet again...........


---

Comment by benjaminfjones created at 2012-08-06 23:12:15

There are lots of lines touched in `sage/functions/transcendental.py` that don't seem to show any difference.  What's going on there? Have invisible non-whitespace characters been deleted?

I looked over the command line and HTML docs for Li and they look good. Running tests now.


---

Comment by benjaminfjones created at 2012-08-07 04:33:54

I see, it's just whitespace at the beginnings of lines. I guess that doesn't get highlighted by trac when you view the patch. Anyway, I think it's a good thing to clean up trailing whitespace, but you'll have to watch out that touching so many lines of the file doesn't cause conflicts with other patches that modify `sage/functions/transcendental.py`. In this case I think it's probably OK, I don't know of any other currently pending  positively reviewed patches that touch that file.

If leif is happy with the patch, I'll give it a positive review.


---

Comment by martinx created at 2012-08-07 06:33:46

Replying to [comment:36 benjaminfjones]:
> I see, it's just whitespace at the beginnings of lines. I guess that doesn't get highlighted by trac when you view the patch. Anyway, I think it's a good thing to clean up trailing whitespace, but you'll have to watch out that touching so many lines of the file doesn't cause conflicts with other patches that modify `sage/functions/transcendental.py`. In this case I think it's probably OK, I don't know of any other currently pending  positively reviewed patches that touch that file.

I got carried away with strip trailing whitespace command in Geany, in response to the previous review comments.  Will try to be more restrained next time ;-)
Martin


---

Comment by benjaminfjones created at 2012-08-07 17:37:58

Patches apply cleanly on top of those at #11143 on top of sage-5.3.beta0. All long tests pass. I think this is ready to go.


---

Comment by benjaminfjones created at 2012-08-11 02:08:07

Ok, I'm giving the most recent patch a positive review. If someone can quickly review the small, most recent fix at #11143, perhaps both of these tickets can be closed in sage-5.3.


---

Comment by benjaminfjones created at 2012-08-11 02:08:07

Changing keywords from "beginner" to "beginner, Li, log, integral, symbolics, calculus".


---

Comment by benjaminfjones created at 2012-08-11 02:08:07

Changing status from needs_review to positive_review.


---

Comment by benjaminfjones created at 2012-08-11 02:08:07

Changing component from calculus to symbolics.


---

Comment by jdemeyer created at 2012-08-23 12:45:34

Resolution: fixed
