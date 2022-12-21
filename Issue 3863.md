# Issue 3863: numerical integration of x^2.7 * e^(-2.4*x) fails

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2008-08-15 00:46:06

Assignee: gfurnish

Keywords: integration integral calculus symbolic


```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0.6, Release Date: 2008-07-30                       |
| Type notebook() for the GUI, and license() for information.        |
sage: x = var('x')
sage: integrate(x^2.7 * e^(-2.4*x), x, 0, 3).n()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/drake/sage-3.0.6.final/<ipython console> in <module>()

/home/was/s/local/lib/python2.5/site-packages/sage/calculus/calculus.py in numerical_approx(self, prec, digits)
   1266         except TypeError:
   1267             # try to return a complex result
-> 1268             approx = self._complex_mpfr_field_(ComplexField(prec))
   1269 
   1270         return approx

/home/was/s/local/lib/python2.5/site-packages/sage/calculus/calculus.py in _complex_mpfr_field_(self, field)
   1419 
   1420     def _complex_mpfr_field_(self, field):
-> 1421         raise TypeError
   1422 
   1423     def _complex_double_(self, C):

TypeError: 
sage: 
```


Oddly, the `plot` function has no difficulty, so *some* part of Sage can numerically evaluate the function:


```
plot(x^2.7 * e^(-2.4*x), x, 0, 3)
```

works fine.

Some values for the exponents do work -- it seems like the exponent of `x` needs to be an integer or half-integer:


```
(2.7, -2.4): this is the above example
(27/10, -2.4): same error as above
(1.5, -2.4): works
(1.6, -2.4): same error as above
(1.6, -2.0): same error as above
(1.0, -2.4): works
(5.5, -2.4): works
```



---

Comment by ddrake created at 2009-05-21 11:44:20

With the new symbolics in 4.0.rc0, this still doesn't work; the error is now:

```
sage: integrate(x^2.7 * exp(-2.4*x), x, 0, 3).n()
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (10003, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/drake/.sage/temp/sage.math.washington.edu/22166/_home_drake__sage_init_sage_0.py in <module>()

/scratch/drake/4.0.rc0/local/lib/python2.5/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:15691)()

/scratch/drake/4.0.rc0/local/lib/python2.5/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.pyobject (sage/symbolic/expression.cpp:2641)()

TypeError: self must be a numeric expression
```

Putting parentheses around the 2.7 and -2.4 didn't change anything.


---

Comment by kcrisman created at 2009-05-22 15:49:28

The essential problem is that with half-integer or integer exponents of x, Maxima can symbolically integrate this using Erf.   Otherwise it can't (that doesn't mean it's not possible, just that Maxima doesn't know).  Before, Sage tried to turn the expression into a complex one if it couldn't evaluate it, but that doesn't do much for a real (unevaluated) integral; now the new symbolics just complain that it's not numeric, which of course it isn't.

My view is that the correct fix is to put some kind of check in for when "integrate" is part of the output string fed into .n() and in that case at least attempt to use numerical_integral or something.  Of course that has the problem that things like 

```
sage: integrate(1/(1+x^7))
1/7*log(x + 1) - 1/7*integrate((x^5 - 2*x^4 + 3*x^3 - 4*x^2 + 5*x - 6)/(x^6 - x^5 + x^4 - x^3 + x^2 - x + 1), x)
```

Maxima is able to partly symbolically integrate, leaving

```
sage: integrate(1/(1+x^7),x,0,1)
```

in trouble.  But at least a check for "integrate" at the beginning could help.


---

Comment by ddrake created at 2009-05-23 01:50:06

Replying to [comment:2 kcrisman]:
> The essential problem is that with half-integer or integer exponents of x, Maxima can symbolically integrate this using Erf.   Otherwise it can't (that doesn't mean it's not possible, just that Maxima doesn't know).  Before, Sage tried to turn the expression into a complex one if it couldn't evaluate it, but that doesn't do much for a real (unevaluated) integral; now the new symbolics just complain that it's not numeric, which of course it isn't.

Ah, that makes sense. I don't mind that just naively running `.n()` doesn't work; we could have, like Mathematica, some sort of numerical_integrate that would try to evaluate the integral, and then punt to something like Simpson's rule to just estimate it. I'm sure, though, that there's vastly better ways to actually do numerical integrals than just a plain vanilla Calculus 1 application of Simpson's Rule.


---

Comment by kcrisman created at 2009-05-23 18:52:41

Oh, totally, and of course we have numerical_integrate and nintegral (one is Maxima, one is GSL I think).  So I guess what I'm saying is that when someone has time (which won't be me until June due to the (US) holiday and then a conference) it should be relatively straightforward to at least do something in the generic code for .n() on whatever kind of object (symbolic?) an expression like integrate(f(x),x,a,b) is like

```
try:
    usual code
except TypeError:
    if "integrate" is in the string:
        either reraise the TypeError with a message suggesting the use of numerical_integrate
        or actually try to string-magic replace "integrate" with "numerical_integrate", which should be possible (you'd have to take [0] of that result, of course)
    else:
        do whatever used to happen with a TypeError
```

I think that it is reasonable for a user to expect that .n() numerically evaluates an expression as best as possible, even one Maxima can't evaluate!  And all these methods are much more sophisticated than Simpson, certainly, so that's not the issue.


---

Comment by mhansen created at 2009-06-04 23:28:02

Actually, the solution is much cleaner since .n() will call the _evalf_ method on the integrate function which we can just have resort to a numerical integral if it is definite and has no free variables.

I'll look into this later.


---

Comment by mhansen created at 2009-06-04 23:28:02

Changing status from new to assigned.


---

Comment by mhansen created at 2009-06-04 23:28:02

Changing assignee from gfurnish to mhansen.


---

Comment by kcrisman created at 2009-12-22 17:27:45

Changing keywords from "integration integral calculus symbolic" to "integration integral calculus symbolic numerical".


---

Comment by kcrisman created at 2009-12-22 17:27:45

Update: in 4.3.alpha1 with Maxima 5.20.1, we now get

```
sage: integrate(x^2.7 * e^(-2.4*x), x, 0, 3)
119/6144*2^(3/5)*3^(3/10)*5^(7/10)*gamma(7/10) - 125/20736*2^(3/5)*3^(3/10)*5^(7/10)*gamma_incomplete(37/10, 36/5)
```

But it won't evaluate the gamma_incomplete, since for some reason we aren't translating it to gamma_inc or incomplete_gamma, which are the supported functions; however, otherwise it is correct (as comparing with results of numerical_integral).

This does not fix the problem, of course, but I will change the summary to get at the fundamental thing mhansen and I discussed, and open a separate ticket (if it doesn't exist) for the gamma_incomplete not being translated correctly from Maxima.  That is #7748.

Do we in the meantime have the _evalf_ method on a symbolic integral that can be changed?


---

Comment by burcin created at 2009-12-22 22:50:53

Replying to [comment:6 kcrisman]:
> Do we in the meantime have the _evalf_ method on a symbolic integral that can be changed?

#6465 has a patch with such an `_evalf_` method. It needs a rebase though. I'm still playing with the symbolic functions in pynac. If nobody gets to it, I'll update those patches after I'm done with pynac.


---

Attachment

trivial doctest


---

Comment by burcin created at 2010-04-05 13:07:57

This was fixed by #6465. Despite the fact that we still have problems with numerical integration (#8321), the problem addressed here is solved. I suggest that we add a doctest and close this ticket.

attachment:trac_3863-doctest.patch adds a trivial doctest. Here is the same computation in Maple: 


```
    |\^/|     Maple 12 (IBM INTEL LINUX)
._|\|   |/|_. Copyright (c) Maplesoft, a division of Waterloo Maple Inc. 2008
 \  MAPLE  /  All rights reserved. Maple is a trademark of
 <____ ____>  Waterloo Maple Inc.
      |       Type ? for help.
> Digits:=30;                             
                                 Digits := 30

> evalf(Int(x^2.7 * exp(-2.4*x), x=0..3));
memory used=3.8MB, alloc=3.1MB, time=0.06
memory used=7.6MB, alloc=4.4MB, time=0.13
memory used=11.4MB, alloc=4.4MB, time=0.21
                       0.154572952320789711837207551604
```



---

Comment by burcin created at 2010-04-05 13:07:57

Changing status from new to needs_review.


---

Comment by ddrake created at 2010-04-06 11:45:29

Changing status from needs_review to needs_work.


---

Comment by ddrake created at 2010-04-06 11:45:29

Hrm, the doctest from the patch doesn't work for me:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: review
sage: integrate(x^2.7 * e^(-2.4*x), x, 0, 3).n() 
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 4.3.5, Release Date: 2010-03-28                       |
| Type notebook() for the GUI, and license() for information.        |
/scratch/sage-4.3.5/<ipython console> in <module>()

/scratch/sage-4.3.5/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:17049)()

TypeError: cannot evaluate symbolic expression numerically
```



---

Comment by burcin created at 2010-04-06 12:53:09

Thanks for the quick feedback Dan.

Now I remember why I didn't suggest to close this ticket earlier. Conversion of the result back from maxima was broken (#7661). Can you try with the patch from #7661 applied. Here is a quick link attachment:trac_7661-maxima_convert_back.patch:ticket:7661.


---

Comment by burcin created at 2010-04-06 12:53:09

Changing status from needs_work to needs_review.


---

Comment by ddrake created at 2010-04-06 13:38:49

Replying to [comment:10 burcin]:
> Thanks for the quick feedback Dan.
> 
> Now I remember why I didn't suggest to close this ticket earlier. Conversion of the result back from maxima was broken (#7661). Can you try with the patch from #7661 applied. Here is a quick link attachment:trac_7661-maxima_convert_back.patch:ticket:7661.

Uh oh...that patch doesn't apply. On top of vanilla 4.3.5, it fails in calculus.py and random_tests.py. I tried to fix the failing hunk in calculus.py (and ignored random_tests.py, since that seemed like a harmless change), but with that applied, it still fails for me.

I tried applying the patches from #7748 on top of the #7661 patch, but Sage doesn't even properly start:

```
/scratch/sage-4.3.5/local/lib/python2.6/site-packages/sage/functions/other.py in <module>()
    540 # We have to add the wrapper function manually to the symbol_table when we have

    541 # two functions with different number of arguments and the same name

--> 542 symbol_table['functions']['gamma'] = gamma
    543 
    544 class Function_gamma_inc(BuiltinFunction):

NameError: name 'gamma' is not defined
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.
```


Any ideas?


---

Comment by burcin created at 2010-04-06 15:54:39

Apparently #7661 depends on #7748, which already has a positive review, but requires 3 patches to be applied. Instructions are here: comment:15:ticket:7748

I'm sorry for the inconvenience. Many thanks for helping me sort through the dependencies.


---

Comment by ddrake created at 2010-04-07 02:28:09

Replying to [comment:12 burcin]:
> Apparently #7661 depends on #7748, which already has a positive review, but requires 3 patches to be applied. Instructions are here: comment:15:ticket:7748

Success! With vanilla 4.3.5 and the following patches applied, the doctest passes!

```
$ hg qapplied
trac_7748-exp_integral_ver2.4.3.3.alpha1.patch
trac_7748-incomplete_gamma_ver2.4.3.3.alpha1.patch
trac_7748-gamma_wrapper.3.patch
trac_7661-maxima_convert_back.patch
trac_3863-doctest.patch
```

With the same set of patches applied to 4.3.3 on bsd.math, the doctest also passes. Positive review here.


---

Comment by ddrake created at 2010-04-07 02:28:09

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-04-07 02:46:30

Release manager: this ticket depends on #7748 and #7761.


---

Comment by ddrake created at 2010-04-07 02:47:33

Replying to [comment:14 ddrake]:
> Release manager: this ticket depends on #7748 and #7761. 

Ack, typo: it's #7748 and #7661.


---

Comment by jhpalmieri created at 2010-04-15 20:16:07

Merged "trac_3863-doctest.patch" in 4.4.alpha0.


---

Comment by jhpalmieri created at 2010-04-15 20:16:07

Resolution: fixed
