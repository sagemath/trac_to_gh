# Issue 6756: Implement ``diff`` format symbolic derivative in new symbolics

Issue created by migration from https://trac.sagemath.org/ticket/6756

Original creator: gmhossain

Original creation time: 2009-08-16 02:02:23

CC:  ncalexan mhansen kcrisman

Implement diff format symbolic derivative in new symbolics as the second form of abstract derivative to be avialable in Sage. See this long thread

http://groups.google.com/group/sage-devel/browse_thread/thread/ff10f99729a74eea/73308bf626ae06b3

for rationale behind it.


---

Attachment

I am interested in reviewing this, but I'm not sure that I can at this time.  I have a heavily modified `Sage Version 4.1.rc1, Release Date: 2009-07-07` tree that I can't really upgrade right now.  I have applied this patch and installed your modified spkg.  I am getting the following doctest failures


```
-*- mode: sage-test; default-directory: "~/sage-4.1-OSX-10.5-Intel-64bit-i386-Darwin/devel/sage-main/sage/symbolic/" -*-
sage-test started at Fri Aug 21 10:18:46

/Users/ncalexan/bin/sage -b >/dev/null && /Users/ncalexan/bin/sage -tp 4 /Users/ncalexan/sage-4.1-OSX-10.5-Intel-64bit-i386-Darwin/devel/sage-main/sage/symbolic/derivative.py

real	0m2.361s
user	0m1.297s
sys	0m0.591s
Global iterations: 1
File iterations: 1
Using cached timings to run longest doctests first.
Doctesting 1 files doing 4 jobs in parallel
sage -t  derivative.py
**********************************************************************
File "/Users/ncalexan/sage-4.1-OSX-10.5-Intel-64bit-i386-Darwin/devel/sage-main/sage/symbolic/derivative.py", line 51:
    sage: f(x).diff(x)
Expected:
    diff(f(x), x, 1)
Got:
    D[0](f)(x)
**********************************************************************
File "/Users/ncalexan/sage-4.1-OSX-10.5-Intel-64bit-i386-Darwin/devel/sage-main/sage/symbolic/derivative.py", line 53:
    sage: diff(f(x), x, 1)
Expected:
    diff(f(x), x, 1)
Got:
    D[0](f)(x)
**********************************************************************
File "/Users/ncalexan/sage-4.1-OSX-10.5-Intel-64bit-i386-Darwin/devel/sage-main/sage/symbolic/derivative.py", line 68:
    sage: h.diff(x)
Expected:
    diff(f(x), x, n + 1)
Got:
    D[0](diff)(f(x), x, n)*D[0](f)(x) + D[1](diff)(f(x), x, n)
**********************************************************************
File "/Users/ncalexan/sage-4.1-OSX-10.5-Intel-64bit-i386-Darwin/devel/sage-main/sage/symbolic/derivative.py", line 112:
    sage: f(x^2).diff(x)
Expected:
    diff(f(x^2), x, 1)
Got:
    2*x*D[0](f)(x^2)
**********************************************************************
File "/Users/ncalexan/sage-4.1-OSX-10.5-Intel-64bit-i386-Darwin/devel/sage-main/sage/symbolic/derivative.py", line 118:
    sage: f(x^2).diff(x)
Expected:
    2*x*diff(f(x^2), x^2, 1)
Got:
    2*x*D[0](f)(x^2)
**********************************************************************
File "/Users/ncalexan/sage-4.1-OSX-10.5-Intel-64bit-i386-Darwin/devel/sage-main/sage/symbolic/derivative.py", line 121:
    sage: f(sin(x^2)).diff(x)
Expected:
    2*x*cos(x^2)*diff(f(sin(x^2)), sin(x^2), 1)
Got:
    2*x*D[0](f)(sin(x^2))*cos(x^2)
**********************************************************************
File "/Users/ncalexan/sage-4.1-OSX-10.5-Intel-64bit-i386-Darwin/devel/sage-main/sage/symbolic/derivative.py", line 124:
    sage: g(x,f(x)).diff(x)
Expected:
    diff(f(x), x, 1)*diff(g(x, f(x)), f(x), 1) + diff(g(x, f(x)), x, 1)
Got:
    D[0](f)(x)*D[1](g)(x, f(x)) + D[0](g)(x, f(x))
**********************************************************************
File "/Users/ncalexan/sage-4.1-OSX-10.5-Intel-64bit-i386-Darwin/devel/sage-main/sage/symbolic/derivative.py", line 129:
    sage: symbolic_diff(f(x^2), x, 1)
Expected:
    diff(f(x^2), x, 1)
Got:
    2*x*D[0](f)(x^2)
**********************************************************************
File "/Users/ncalexan/sage-4.1-OSX-10.5-Intel-64bit-i386-Darwin/devel/sage-main/sage/symbolic/derivative.py", line 138:
    sage: g(x,x).diff(x)
Expected:
    2*diff(g(x, x), x, 1)
Got:
    D[0](g)(x, x) + D[1](g)(x, x)
**********************************************************************
File "/Users/ncalexan/sage-4.1-OSX-10.5-Intel-64bit-i386-Darwin/devel/sage-main/sage/symbolic/derivative.py", line 147:
    sage: h = f(x).diff(x); h
Expected:
    diff(f(x), x, 1)
Got:
    D[0](f)(x)
**********************************************************************
File "/Users/ncalexan/sage-4.1-OSX-10.5-Intel-64bit-i386-Darwin/devel/sage-main/sage/symbolic/derivative.py", line 149:
    sage: h.subs(f(x)==x^4)
Expected:
    4*x^3
Got:
    D[0](f)(x)
**********************************************************************
File "/Users/ncalexan/sage-4.1-OSX-10.5-Intel-64bit-i386-Darwin/devel/sage-main/sage/symbolic/derivative.py", line 155:
    sage: h = f(x^2).diff(x); h
Expected:
    2*x*diff(f(x^2), x^2, 1)
Got:
    2*x*D[0](f)(x^2)
**********************************************************************
File "/Users/ncalexan/sage-4.1-OSX-10.5-Intel-64bit-i386-Darwin/devel/sage-main/sage/symbolic/derivative.py", line 157:
    sage: h.subs(f(x^2)==x^4)
Expected:
    4*x^3
Got:
    2*x*D[0](f)(x^2)
**********************************************************************
File "/Users/ncalexan/sage-4.1-OSX-10.5-Intel-64bit-i386-Darwin/devel/sage-main/sage/symbolic/derivative.py", line 159:
    sage: symbolic_diff(f(x)^2, f(x), 1)
Expected:
    2*f(x)
Got:
    diff(f(x)^2, f(x), 1)
**********************************************************************
File "/Users/ncalexan/sage-4.1-OSX-10.5-Intel-64bit-i386-Darwin/devel/sage-main/sage/symbolic/derivative.py", line 186:
    sage: h = f(x).diff(x) + f(x^2).diff(x); h
Expected:
    2*x*diff(f(x^2), x^2, 1) +  diff(f(x), x, 1)
Got:
    2*x*D[0](f)(x^2) + D[0](f)(x)
**********************************************************************
File "/Users/ncalexan/sage-4.1-OSX-10.5-Intel-64bit-i386-Darwin/devel/sage-main/sage/symbolic/derivative.py", line 217:
    sage: f(x,y).diff(x,y)
Expected:
    diff(f(x, y), x, 1, y, 1)
Got:
    D[0, 1](f)(x, y)
**********************************************************************
File "/Users/ncalexan/sage-4.1-OSX-10.5-Intel-64bit-i386-Darwin/devel/sage-main/sage/symbolic/derivative.py", line 219:
    sage: f(x,y).diff(x,2)
Expected:
    diff(f(x, y), x, 2)
Got:
    D[0, 0](f)(x, y)
**********************************************************************
2 items had failures:
  15 of  40 in __main__.example_1
   2 of  10 in __main__.example_2
***Test Failed*** 17 failures.
For whitespace errors, see the file /Users/ncalexan/sage-4.1-OSX-10.5-Intel-64bit-i386-Darwin/tmp/.doctest_derivative.py
	 [3.8 s]
 
----------------------------------------------------------------------

The following tests failed:

	sage -t  devel/sage-main/sage/symbolic/derivative.py # 17 doctests failed
----------------------------------------------------------------------
Total time for all tests: 4.1 seconds

sage-test finished with failing tests at Fri Aug 21 10:18:53
```


When I work from the command line, I get things like

```
sage: default_level=set_diff_derivative_level()
sage: set_diff_derivative_level(1)
sage: f(x) = function('f', x)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/ncalexan/.sage/temp/mero.local/93112/_Users_ncalexan__sage_init_sage_1.py in <module>()

/Users/ncalexan/sage-4.1-OSX-10.5-Intel-64bit-i386-Darwin/local/lib/python2.6/site-packages/sage/calculus/var.so in sage.calculus.var.function (sage/calculus/var.c:709)()

/Users/ncalexan/sage-4.1-OSX-10.5-Intel-64bit-i386-Darwin/local/lib/python2.6/site-packages/sage/symbolic/function.so in sage.symbolic.function.SFunction.__call__ (sage/symbolic/function.cpp:4655)()

TypeError: Symbolic function f takes exactly 2 arguments (1 given)
```


So there must be some calculus or symbolic patches that I'm missing.  Any suggestions?


---

Comment by gmhossain created at 2009-08-21 18:41:37

Replying to [comment:2 ncalexan]:
> I am interested in reviewing this, but I'm not sure that I can at this time.  I have a heavily modified `Sage Version 4.1.rc1, Release Date: 2009-07-07` tree that I can't really upgrade right now.  I have applied this patch and installed your modified spkg.  I am getting the following doctest failures
>

```
 
 **********************************************************************
 File "/Users/ncalexan/sage-4.1-OSX-10.5-Intel-64bit-i386-Darwin/devel/sage-main/sage/symbolic/derivative.py", line 51:
     sage: f(x).diff(x)
 Expected:
     diff(f(x), x, 1)
 Got:
     D[0](f)(x)
```






Thanks Nick for trying it out. From this error, it seems "diff_derivative_level" flag wasn't set to
value greater than "0". It could be that "set_diff_derivative_level()" failed to set it properly.




> When I work from the command line, I get things like
> {{{
> sage: default_level=set_diff_derivative_level()
> sage: set_diff_derivative_level(1)
> sage: f(x) = function('f', x)
> ---------------------------------------------------------------------------
> TypeError: Symbolic function f takes exactly 2 arguments (1 given)
> }}}




This looks really weired to me. Does it work before calling "set_diff_derivative_level()"?


I can suggest you to check three things

  (1) Ensure in "symbolic/pynac.pyx" you have a line:

```
      "cdef public int diff_derivative_level = 0"
```

   May be you can set it to "1", to enable "diff" by default.


  (2) In "symbolic/all.py" you have a line:

```
     "from derivative import symbolic_diff"
```

  (3) In "calculus/calculus.py" the following line is commented out or removed

```
      "syms['diff'] = dummy_diff"
```

If these three lines are fine then it should work. Some doctests may it still
fail if "set_diff_derivative_level()" isn't working properly but you can
always change value in (1) manually without using it.

Please let me know if that works.

Best,


---

Comment by ncalexan created at 2009-08-26 05:00:03

Sorry, same problems with a new 4.1.1 binary.  It's possible I'm building in the wrong order (patch, failed tests, then new spkg, touch patch, rebuild) but that's two systems not working.


---

Attachment


---

Comment by ncalexan created at 2009-08-26 19:03:02

The second patch makes this at least work for me, and fixes (maybe an ordering issue?) a test that doesn't pass on my box.  I'm not done reviewing yet, but at least it works as advertised.  Question: how do I pattern match on this?


---

Comment by ncalexan created at 2009-08-26 19:16:57

Aha, very interesting, you pattern match via the `symbolic_diff` object.  This is pretty slick, but it irritates me that there's no way to match *any* derivative.  Ie, handle `diff(f(x, y), x, 2)` and `diff(f(x, y), x, 1, y, 1)` uniformly for pattern matching.


---

Comment by ncalexan created at 2009-08-26 19:35:55

I would like to evaluate various derivatives numerically, but there's no obvious way to do so.

```
sage: def f(v, n): print v; return v**n
....: 
sage: g(x, y).derivative(x, 1).subs( symbolic_diff(g(x, y), w0, w1) == f(w0, w1) )
$0
x
```


I would like to have my `f` examine w0 and w1 to determine the correct variable, derivative, etc.  But if you look, f gets evaluated with the wild card objects (it must -- that's how python works.)

So I need to match the wild cards, then calculate the function, then substitute.  Just longer, that's all.


---

Comment by gmhossain created at 2009-08-27 01:17:23

Hi Nick,

As you suggested, I moved the "set_diff_derivative_level" into pynac library.
Now I just wrap the function from cython code. I will update the patches,spkg after
you finish your first round of reviewing.


---

Attachment

Apply only this patch and ignore first two patches


---

Comment by gmhossain created at 2009-09-05 14:46:41

Patches updated to include Nick's suggestion to move "set_diff_derivative_level" into pynac library.


---

Comment by burcin created at 2009-09-06 12:58:51

It seems that applying chain rule to these inert derivatives can lead to wrong answers:


```
sage: f = function('f')
sage: set_diff_derivative_level(2)
sage: f(y,y).diff(y,1)
2*diff(f(y, y), y, 1)
```


Compare with the answer we get now:

```
sage: set_diff_derivative_level(0)
sage: f(y,y).diff(y,1)
D[0](f)(y, y) + D[1](f)(y, y)
```


This example is from p. 26 (second page) in


```
Wester, M. and Steinberg, S. 1983. An extension to MACSYMA's concept of functional differentiation.
   SIGSAM Bull. 17, 3-4 (Aug. 1983), 25-30.
```


You can get the article here:  http://doi.acm.org/10.1145/1089338.1089343 

It was the first reference on the paper mentioned by RJF in this post:

http://groups.google.com/group/sage-devel/msg/6db333cbf8ea0a53

The paper RJF cites is


```
Golden, J. P. 1985. Differentiation of unknown functions in MACSYMA.
   SIGSAM Bull. 19, 2 (May. 1985), 19-24.
```


which you can get here:

http://doi.acm.org/10.1145/1089402.1089405


I suggest removing the chain rule from this implementation altogether and keeping it as an alternative _inert_ derivative. Then the implementation can be moved within the Sage library completely as a subclass of SFunction. We should also implement conversions between the partial derivative format and this one. This page gives a recipe on how this can be done:

http://209.85.129.132/search?q=cache%3Ahttp%3A%2F%2Fwww.mapleprimes.com%2Fforum%2Fd-diff-conversion%23comment-8243

(The link points to the google cache since mapleprimes.com is down.)

Nick, if you give examples of how you want pattern matching on derivatives to work, we can see how to make the current implementation support these. Pattern matching capabilities of `fderivative` in GiNaC definitely need to be improved. Looking at what functionality maple and MMA provides could also help.


---

Comment by gmhossain created at 2009-09-06 20:02:24

Replying to [comment:10 burcin]:
> It seems that applying chain rule to these inert derivatives can lead to wrong answers:
> 

```
sage: f = function('f')
sage: set_diff_derivative_level(2)
sage: f(y,y).diff(y,1)
2*diff(f(y, y), y, 1)
```

> 
> Compare with the answer we get now:

```
sage: set_diff_derivative_level(0)
sage: f(y,y).diff(y,1)
D[0](f)(y, y) + D[1](f)(y, y)
```

> 
> This example is from p. 26 (second page) in ....

> I suggest removing the chain rule from this implementation altogether and keeping it as an alternative _inert_ 


Thanks for the reference and I am certainly aware of this issue. If you read the
docstring then you will find that I have even documented it. Furthermore, I also 
posted this issue for discussion to sage-devel (but without any definite conclusion)

http://groups.google.com/group/sage-devel/browse_thread/thread/c8d257981e3e3d98

Following are my comments:

  (1) f(y,y) is not a genuine function of two variables. So asking for its chain rule, pretending it to be a function of multiple variables, is itself incorrect assertion.

  (2) I don't think even D[] derivative output is much better in this regard, specially if you implement and allow substitution of f(y,y). For example. consider the substitution: f(y,y) = y in "D[0](f)(y, y) + D[1](f)(y, y)", then you will get the same wrong answer from D[] as from "diff".
      
  (3) Applying chain rule is just an option in new diff implementation and certainly not the default option. However, this could be useful sometime (for example in computing Euler-Lagrange equation using functional derivative of a formal functional "S(f(y), g(y))" this feature is needed. In fact, this was the reason for implementing this feature.)

So I am sorry to differ from your opinion about removing this feature.


  

> Then the implementation can be moved within the Sage library completely as a 
> subclass of SFunction. 




As I posted in the sage-devel, I initially implemented this within Sage as SFunction 
sub-class (as you suggest). Then I re-implemented this in c++ as pynac native implementation 
because this is 10-15 times faster than the Sage implementation.


Why do you want to have a slower implementation of diff than a faster one?




> We should also implement conversions between the partial derivative format and this one. 
> This page gives a recipe on how this can be done:
> 
> http://209.85.129.132/search?q=cache%3Ahttp%3A%2F%2Fwww.mapleprimes.com%2Fforum%2Fd-diff-conversion%23comment-8243




I agree that we need this conversion at least to restore compatibility of D[] with Maxima which is badly broken now because of D[] derivative. However, I don't agree that I should implement this conversion and certainly not as a pre-requirement for accepting this patch.   

Given above arguments, I am reverting back to "needs review" status.


---

Comment by burcin created at 2009-09-06 21:47:47

Replying to [comment:11 gmhossain]:
>   (2) I don't think even D[] derivative output is much better in this regard, specially if you implement and allow substitution of f(y,y). For example. consider the substitution: f(y,y) = y in "D[0](f)(y, y) + D[1](f)(y, y)", then you will get the same wrong answer from D[] as from "diff".

This substitution doesn't make sense mathematically. D[0](f)(y,y) doesn't contain f(y,y), there is nothing to substitute.

Bill Page had answered this point earlier:

http://groups.google.com/group/sage-devel/msg/e6ded8f5e28a5aab

This message by him in the same thread might be more helpful:

http://groups.google.com/group/sage-devel/msg/98cc070640578f0c


Note that with these patches, the result of `f(y,y).diff(y)` is twice that of the current implementation.


---

Comment by gmhossain created at 2009-09-06 22:42:44

Replying to [comment:12 burcin]:
> Replying to [comment:11 gmhossain]:
>  For example. consider the substitution: f(y,y) = y 
> 
> This substitution doesn't make sense mathematically.

Hmm, if you bring mathematical sense into argument then does it
make mathematical sense asking for applying chain rule at the
first place for this case?

> Note that with these patches, the result of `f(y,y).diff(y)` is twice that of the current implementation.

This is not accurate. 

Above will happen only when an user wants to apply chain rule by explicitly setting 
diff_derivative_level to "2" or more and certainly NOT in default diff level of "1". 
If some user wants to use some setting that are not default then its reasonable to
expect users to read the documentation to be aware of the assumptions associated with
the settings.


---

Comment by burcin created at 2009-09-06 23:01:15

Replying to [comment:13 gmhossain]:
> Replying to [comment:12 burcin]:
> > Note that with these patches, the result of `f(y,y).diff(y)` is twice that of the current implementation.
> 
> This is not accurate. 
> 
> Above will happen only when an user wants to apply chain rule by explicitly setting 
> diff_derivative_level to "2" or more and certainly NOT in default diff level of "1". 
> If some user wants to use some setting that are not default then its reasonable to
> expect users to read the documentation to be aware of the assumptions associated with
> the settings.

So you agree that setting this level to 2 gives wrong results. In comment:10, I tried to say that this option that gives wrong results should be removed.

We can then merge this _inert_ derivative with the global `diff` command by adding a keyword option `hold`. E.g.,


```
sage: f(y,y).diff(y,1)
D[0](f)(y, y) + D[1](f)(y, y)
sage: f(y,y).diff(y,1,hold=True)
diff(f(y, y), y, 1)
```



---

Comment by gmhossain created at 2009-09-07 03:34:47

Replying to [comment:14 burcin]:
>
> So you agree that setting this level to 2 gives wrong results. 

Yes, but ONLY for mathematically dubious inputs. Please don't generalize, it doesn't help anyone.

I have been working on a patch that will check the arguments of the function while applying chain
rule and can warn/raise appropriate errors. However, I am planning to do this in next 
revision and after having some feedbacks from its users.
   
> We can then merge this _inert_ derivative with the global `diff` command by 
> adding a keyword option `hold`. E.g.,

Sure. However, it would be premature to merge this with global "diff" now, given its a 
new implementation and there could be issue which are not yet known. So I would prefer 
to wait couple of release cycles before considering such a move.


---

Comment by burcin created at 2009-09-08 08:32:33

Replying to [comment:15 gmhossain]:
> Replying to [comment:14 burcin]:
> >
> > So you agree that setting this level to 2 gives wrong results. 
> 
> Yes, but ONLY for mathematically dubious inputs. Please don't generalize, it doesn't help anyone.

What do you think is "mathematically dubious"?

Using the notation and definitions for derivatives and partial derivatives from here respectively:

http://books.google.at/books?id=e54cqeAmf4QC&pg=PA267#v=onepage

http://books.google.at/books?id=e54cqeAmf4QC&pg=PA495#v=onepage

Let U be an open subset of the complex numbers, f: UxU -> C, y in U. Then by Proposition 3.5 here

http://books.google.at/books?id=LzhkCF9ZsUgC&&pg=PA10#v=onepage

we have

\frac{df}{dy} (y,y) = D_1 f(y, y) + D_2 f(y, y).

Note that on the left hand side there is a _total_ derivative.

In the current Sage syntax, "diff" denotes a total derivative, and "D" denotes a partial derivative. The statement above translates to the Sage notation as:

diff(f(y,y), y) = D[0](f)(y,y) + D[1](f)(y,y)

Which you can also calculate by:


```
sage: diff(f(y,y),y)
D[0](f)(y, y) + D[1](f)(y, y)
```


----

With your patch we get:


```
sage: set_diff_derivative_level(2)
sage: diff(f(y,y),y)
2*diff(f(y, y), y, 1)
sage: latex(diff(f(y,y),y))
2 \, {\frac{\partial}{\partial y}f\left(y, y\right)}
```


Can you explain what `diff(f(y,y), y, 1)` or in typeset form `\frac{\partial}{\partial y}f(y,y)` means?

----

> I have been working on a patch that will check the arguments of the function while applying chain
> rule and can warn/raise appropriate errors. However, I am planning to do this in next 
> revision and after having some feedbacks from its users.

Are you saying that we should merge this problematic version, and you'll fix things later? This is not how the development process works. We can review and merge the known good parts from your patch, and you can submit the rest in a different ticket later. 


> > We can then merge this _inert_ derivative with the global `diff` command by 
> > adding a keyword option `hold`. E.g.,
> 
> Sure. However, it would be premature to merge this with global "diff" now, given its a 
> new implementation and there could be issue which are not yet known. So I would prefer 
> to wait couple of release cycles before considering such a move. 

Should it really be merged into Sage if it's so premature? The point of the review to make sure that it doesn't have these problems.

I don't have any more time to waste on this. I suggest you either 
 * read the references I linked to in comment:10, and explain clearly what you do to remedy the problems discussed there or,
 * remove the problematic parts from your patch.


---

Comment by mhansen created at 2009-09-29 06:37:33

I tend to agree with the points that Burcin made.

It seems a better way to implement this within GiNaC would be to have a class parallel to fderivative which just stores the (evaluated) function as well as the list of symbols.  It is trivial to go from this data structure to partial derivative one.


---

Comment by burcin created at 2010-02-07 14:10:22

Changing status from needs_review to needs_work.


---

Comment by nbruin created at 2021-09-23 17:21:20

We have this now. Close?

```
sage: var('x,y,z')                                                                                                          
(x, y, z)
sage: function('f')                                                                                                         
f
sage: f(x,y,z).diff(x,z,y,z)                                                                                                
diff(f(x, y, z), x, y, z, z)
```



---

Comment by nbruin created at 2021-09-23 17:21:20

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2021-09-23 17:52:33

It's hard to tell exactly the scope of this ticket, but from the thread, it seems like one of the primary things wanted was a way to represent 

```
sage: f(g(x)).diff(x)
diff(f(g(x)), x)
```

instead of what's in Sage now:

```
sage: f(g(x)).diff(x)
D[0](f)(g(x))*diff(g(x), x)
```



---

Comment by kcrisman created at 2021-09-23 17:55:58

I think Mike has it correct.

(Though this ticket is so old, and involved an unresolved discussion, so that it could conceivably be helpful to start over.)


---

Comment by kcrisman created at 2021-09-23 17:55:58

Changing status from needs_review to needs_info.
