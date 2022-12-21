# Issue 2452: heaviside step function needed

Issue created by migration from Trac.

Original creator: gfurnish

Original creation time: 2008-03-10 07:52:27

Assignee: was

CC:  gmhossain

Symbolic heaviside step function is needed for ease of plotting.  Right now you must 


```
sage: def u(x):
    if(x<0):
        return 0
    else:
        return 1*cos(x)
sage: plot(u,-5,5)
```

instead of

```
 plot(heaviside(t)*cos(t),t,-5,5)
```



---

Comment by wdj created at 2008-03-10 11:05:35

You can make a Heaviside function with Piecewise. 
sage: f0 = lambda x: 0; f1 = lambda x:x^0; Heaviside = Piecewise([[(-infinity,0),f0],[(0,infinity),f1]])
sage: Heaviside(3)
1
sage: Heaviside(-23)
0
However, plotting is broken. You have to make a truncated function to plot:
sage: f0 = lambda x: 0; f1 = lambda x:x^0; Heaviside = Piecewise([[(-10,0),f0],[(0,10),f1]])
sage: Heaviside.plot()
works.
Of course, improvements to Piecewise would be great...


---

Comment by gfurnish created at 2008-03-16 20:12:08

Changing assignee from was to gfurnish.


---

Comment by gfurnish created at 2008-03-16 20:12:08

Changing status from new to assigned.


---

Comment by jason created at 2008-10-21 16:59:45

What is the status of this?  I noticed something else when trying to do a diffeq lesson:


```
sage: def unit_step(c):
....:         return piecewise( [( (-oo,c), 0), ((c, oo), 1)] )
....:
sage: unit_step(2)
Piecewise defined function with 2 parts, [((-Infinity, 2), 0), ((2, +Infinity), 1)]
sage: unit_step(2)*unit_step(3)
Piecewise defined function with 3 parts, [[(2, 3), 0], [(3, -Infinity), 0], [(-Infinity, +Infinity), 1]]
```


That last multiplication just plain does not make sense.  Even the intervals are all messed up.


---

Comment by wdj created at 2008-10-21 17:28:23

This might explain the problem:


```
sage: def unit_step(c):
    return piecewise( [( (-Infinity,c), 0), ((c, Infinity), 1)] )
....:
sage: unit_step(1)
Piecewise defined function with 2 parts, [((-Infinity, 1), 0), ((1, +Infinity), 1)]
sage: unit_step(1)(1/2)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/wdj/sagefiles/sage-3.2.alpha0/<ipython console> in <module>()

/home/wdj/sagefiles/sage-3.2.alpha0/local/lib/python2.5/site-packages/sage/functions/piecewise.pyc in __call__(self, x0)
    591         for i in range(n):
    592             if endpts[i] < x0 < endpts[i+1]:
--> 593                 return self.functions()[i](x0)
    594         raise ValueError,"Value not defined outside of domain."
    595

TypeError: 'sage.rings.integer.Integer' object is not callable
```



---

Comment by gmhossain created at 2009-06-28 11:30:12

Descriptions/title are updated and a patch (sage-4.0.2) implementing Dirac delta, Heaviside step and Unit step function is attached.


---

Comment by gmhossain created at 2009-06-28 11:30:12

Changing component from calculus to symbolics.


---

Comment by wdj created at 2009-06-28 11:53:11

Patch applies to 3.1.alpha1. Running tests now.

One possible problem: Is


```
sage: dirac_delta.integral(0)
heaviside(0)
```

mathematically correct?


---

Comment by gmhossain created at 2009-06-28 12:29:33

Replying to [comment:7 wdj]:
> Is
> 

```
sage: dirac_delta.integral(0)
heaviside(0)
```

> mathematically correct?
> 

Thanks, its a good point. I agree, it is ambiguous at best. I guess, it may be a good 
idea to remove .integral() methods from their definitions. Specialized integration 
algorithm involving these functions will handle the situation much better.
I will wait for your remaining comments before updating the patch.


---

Comment by wdj created at 2009-06-28 17:22:08

The testing didn't reveal any failures related to the patch. However, I'm also wondering about
this output:


```
sage: f(x) = heaviside(x)+dirac_delta(x)
sage: f(1)
dirac_delta(1) + heaviside(1)
sage: f = heaviside+dirac_delta
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/wdj/.sage/temp/hera/14949/_home_wdj__sage_init_sage_0.py in <module>()

TypeError: unsupported operand type(s) for +: 'FunctionHeaviside' and 'FunctionDiracDelta'
```

even though it has no problem evaluating them:


```
sage: heaviside(1); dirac_delta(1)
1
0
```


I don't see a problem with the integral methods but I'd prefer definite integrals over indefinite ones.
In any case, 


```
sage: dirac_delta.integral(0)
heaviside(0)
```

seems odd. 

If you can address these comments I'd be happy to look at it again.


---

Comment by gmhossain created at 2009-06-29 14:45:12

Thanks David,

> The testing didn't reveal any failures related to the patch. However, I'm also wondering about
> this output:

```
sage: f(x) = heaviside(x)+dirac_delta(x)
sage: f(1)
dirac_delta(1) + heaviside(1)
```


It seems, you have hit a bug in new symbolics. The similar non-evaluation
of symbolic function is happening even with other functions such as sin, cos. 
I posted this issue here

http://groups.google.com/group/sage-devel/browse_thread/thread/3936d1290ee933a6

Burcin wrote that this is a bug and it is to be fixed in the new version of pynac.

>

```
sage: f = heaviside+dirac_delta
...
TypeError
```

>
It seems in new symbolics, arithmetic of bare-bone functions is no-longer allowed. 
For example, if I try

```
f = sin + cos 
```

then I get the same error. 

> I don't see a problem with the integral methods but I'd prefer definite integrals over indefinite ones.
> In any case,  

```
sage: dirac_delta.integral(0)
heaviside(0)
```

> seems odd. 

I agree this is odd. I have removed the integral methods from this patch. Integration algorithm
that I am implementing will do both definite and indefinite integrals involving these functions.
So I guess, it is better to avoid code-duplication.

Apart from above, I have clarified two sentences in doc-strings. The updated patch is attached.


---

Comment by burcin created at 2009-06-29 17:36:18

Changing priority from critical to major.


---

Comment by burcin created at 2009-06-29 17:36:18

Replying to [comment:11 gmhossain]:
> > The testing didn't reveal any failures related to the patch. However, I'm also wondering about
> > this output:
 {{{
 sage: f(x) = heaviside(x)+dirac_delta(x)
 sage: f(1)
 dirac_delta(1) + heaviside(1)
 }}}
> 
> It seems, you have hit a bug in new symbolics. The similar non-evaluation
> of symbolic function is happening even with other functions such as sin, cos. 
> I posted this issue here
> 
> http://groups.google.com/group/sage-devel/browse_thread/thread/3936d1290ee933a6
> 
> Burcin wrote that this is a bug and it is to be fixed in the new version of pynac.

This is a different issue than the one you posted on sage-devel. 

In your patch, you are not telling pynac how to evaluate the function you define. This is done by defining an `_eval_` method, so if you move the contents of your `__call__` function to `_eval_` and remove the last `SFunction.__call__` line things should work fine. I agree that this is confusing. It's one of the main points I wanted to address while refactoring symbolic functions.

I would also like to see a `.sub()` test added, since this is the easiest way to test if the `_eval_` function is defined properly. E.g.,


```
sage: dirac_delta(x).sub(x=1)
0
sage: heaviside(x).sub(x=1)
1
```



---

Comment by wdj created at 2009-06-29 20:30:34

I finished testing the patch. It seems to pass tests okay but I totally agree with Burcin's comments above and would appreciate it if you could try to address them. Thanks!


---

Comment by gmhossain created at 2009-06-29 21:55:53

Replying to [comment:12 burcin]:

*(1)*
> so if you move the contents of your `__call__` function to `_eval_` and 
> remove the last `SFunction.__call__` line things should work fine. 

Thanks Burcin! Thats what it needed. As you suggested, I have made those changes and
explicit evaluation is now working.


*(2)*
> I would also like to see a `.sub()` test added, 

I am assuming you meant ".subs()". Several new tests are added as you 
suggested.


*(3)* Doctstrings are updated suitably as `__call__` methods are now removed.


---

Comment by burcin created at 2009-06-30 10:08:29

Sorry for doing this in such small pieces, but I have one more suggestion. 

You can change the calls to the `_is_real()` function by `x in RR` where you import `RR` from `sage.rings.real_mpfr`. The semantics of the `__contains__()` method in Sage is similar to your `_is_real()`, though it also checks that `approx_x == x` in your code.

BTW, the reason `exp(-100000000000)` is evaluated to be 0 is that we don't use interval fields to do the numerical approximation. This is also ##5993.


---

Comment by gmhossain created at 2009-06-30 13:29:40

Replying to [comment:15 burcin]:
> Sorry for doing this in such small pieces, but I have one more suggestion. 
> 
> You can change the calls to the `_is_real()` function by `x in RR` where you import `RR` from `sage.rings.real_mpfr`. 
> The semantics of the `__contains__()` method in Sage is similar to your `_is_real()`, though it also checks that `approx_x == x` in your code.

Hi Burcin. I tried your suggestion. I am not sure whats going wrong but it slows down massively. Could
you please check this out?

*With: `_is_real(x)`*


```
sage: timeit( 'dirac_delta(1 + I*exp(-10000))')
125 loops, best of 3: 6.47 ms per loop
sage: timeit( 'dirac_delta(1 + I*exp(-10000000000000000))')
125 loops, best of 3: 6.23 ms per loop
```


*with: `x in RR`*
 

```
sage: timeit( 'dirac_delta(1 + I*exp(-10000))')
125 loops, best of 3: 6.56 ms per loop
sage: timeit( 'dirac_delta(1 + I*exp(-10000000000000000))')
5 loops, best of 3: 154 ms per loop
```


Thanks,


---

Comment by burcin created at 2009-06-30 19:18:45

Hi Golam,

You're right! When using high precision we start calling maxima to decide if two expressions are equal. This kills performance as you observed.

Now I suggest using `CIF(x).imag() == 0` where `x` is the element you want to test for. This is consistent in timings, and produces correct results:


```
sage: u = 1 + I*exp(-10000000000000000)
sage: CIF(u).imag() == 0
False
sage: timeit('b = (CIF(u).imag() == 0)')
625 loops, best of 3: 761 µs per loop
sage: t = 1 + I*exp(-10000)
sage: CIF(t).imag() == 0
False
sage: timeit('b = (CIF(t).imag() == 0)')
625 loops, best of 3: 784 µs per loop
```


Thanks.


---

Attachment


---

Comment by gmhossain created at 2009-07-01 00:58:07

Replying to [comment:17 burcin]:
> Now I suggest using `CIF(x).imag() == 0` where `x` is the element you want to test for. 

Thats great. It now works much faster even for very very small numbers. Here are the 
changes in the updated patch:

*(1)*:  _is_real(x) removed

*(2)*:  CIF(x) is now being used

*(3)*: Notes on finite precision size removed.

*(4)*: new doctests for very small numbers added


---

Comment by wdj created at 2009-07-01 13:22:27

This applies to 4.1.alpha1 on an amd64 ubuntu 9.04 machine and passes all tests except for three which seem unrelated (darwin_utilities, random_tests, and the French programming tutorial).

```
sage: t = var("t")
sage: plot(heaviside(t)+2*heaviside(t-1),t,-5,5)
sage: P1 = plot(t*heaviside(t)+(2-t)*heaviside(t-1),t,-5,5)
sage: P2 = plot(heaviside(t)*cos(t),t,-5,5, linestyle="--", rgbcolor=(1,0,0), thickness=3)
sage: show(P1+P2)

```

I like the fact that plotting like this works so well!


---

Comment by burcin created at 2009-07-02 09:53:37

fix doctests in random_tests.py


---

Attachment

The failing doctests in sage/symbolic/random_tests.py is caused by this ticket. That function constructs a random expression, given all the symbolic functions defined in Sage. Since this patch adds new functions, the probability distribution, hence the result changes.

I attached a small patch to fix these doctests.


---

Comment by rlm created at 2009-07-03 17:26:09

The second patch needs to be rebased. The following hunk fails, applying to my 4.1.rc0 branch:

```
--- random_tests.py
+++ random_tests.py
`@``@` -202,12 +202,11 `@``@`

         sage: from sage.symbolic.random_tests import *
         sage: random_expr(50, nvars=3, coeff_generator=CDF.random_element)
-        ceil(arctanh(-sinh(v2)/floor(-(0.615863165633 + 0.879368031485*I)*v1^2*v3) - gamma(pi) + floor(-(0.708874026302
 - 0.954135400334*I)*v3)))^sinh(arctan2(arcsinh((0.723896589334 + 0.799038508886*I)*(v2 + 0.913564344312 + 0.08980401603
36*I)*v2), -1/v3)/(v3/v2 + 1.36062750308 - 1.05383406182*I))
+        arctanh(sinh(-arcsech(v2)/floor(-(0.615863165633 + 0.879368031485*I)*v1^2*v3) - gamma(pi) + floor(-(0.708874026
302 - 0.954135400334*I)*v3)))^arcsech(-cosh(-polylog((v2 + 0.913564344312 + 0.0898040160336*I)^(-(0.723896589334 - 0.799
038508886*I)*v2),-v1 - v3))/sin(-(0.0263902659909 + 0.153261789843*I)*arctan2(pi, e^pi)))
         sage: random_expr(5, verbose=True)
-        About to apply sec to [1]
-        About to apply exp to [sec(1)]
-        About to apply <built-in function mul> to [e^sec(1), v1]
-        v1*e^sec(1)
+        About to apply <built-in function add> to [v1, v1]
+        About to apply <built-in function div> to [-1/3, 2*v1]
+        -1/6/v1
     """
     vars = [(1.0, sage.calculus.calculus.var('v%d' % (n+1))) for n in range(nvars)]
     if ncoeffs is None:
```



---

Comment by burcin created at 2009-07-04 07:30:05

The second patch depends on #6421. Since #6421 was merged in 4.1.rc0, this can be applied without problems.

Sorry for the inconvenience.


---

Comment by rlm created at 2009-07-04 19:54:26

Resolution: fixed
