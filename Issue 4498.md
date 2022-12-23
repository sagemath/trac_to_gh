# Issue 4498: The argument function does not work with variables.

Issue created by migration from https://trac.sagemath.org/ticket/4498

Original creator: TimothyClemans

Original creation time: 2008-11-11 23:21:48

Assignee: somebody

CC:  kcrisman ktkohl

"The function should return the argument of a complex function." - Ronan Paixão


---

Comment by TimothyClemans created at 2008-11-11 23:24:52


```
arg(x)
///

Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
 File "/home/ronan/.sage/sage_notebook/worksheets/admin/0/code/127.py",
line 6, in <module>
   exec compile(ur'arg(x)' + '\n', '', 'single')
 File
"/home/ronan/progs/sage/local/lib/python2.5/site-packages/ZODB3-3.7.0-py2.5-linux-i686.egg/", line 1, in <module>

 File
"/home/ronan/progs/sage/local/lib/python2.5/site-packages/sage/misc/functional.py", line 67, in arg
   except AttributeError: return CDF(x).arg()
 File "complex_double.pyx", line 286, in
sage.rings.complex_double.ComplexDoubleField_class.__call__
(sage/rings/complex_double.c:3324)
 File
"/home/ronan/progs/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 1454, in _complex_double_
   raise TypeError
TypeError
```



---

Comment by mabshoff created at 2008-11-12 14:16:18

Please post a complete session. As is the above is not very clear.

Cheers,

Michael


---

Comment by was created at 2008-11-12 17:13:16

Changing type from defect to enhancement.


---

Comment by ronanpaixao created at 2008-11-15 17:17:03

Is this really an enchancement? As it is, just using arg(x) already raises an error and everything that needs arg() must be implemented numerically.


---

Comment by was created at 2008-11-16 19:42:06

> Is this really an enchancement? As it is, just using arg(x) already 
> raises an error and everything that needs arg() must be implemented numerically. 

Yes, this is an enhancement since it is implementing new functionality. 
It would be a bug fix if there were a bug in the existing arg function, where it produced invalid results on supported input.

 -- William


---

Comment by kcrisman created at 2010-05-26 21:00:15

Changing component from basic arithmetic to symbolics.


---

Comment by burcin created at 2010-05-27 10:25:40

This was also reported in #6220. I will close that as duplicate.


---

Comment by burcin created at 2010-08-28 16:14:31

Changing keywords from "" to "beginner".


---

Comment by ktkohl created at 2012-01-11 15:39:09

Changing keywords from "beginner" to "beginner, sd35.5".


---

Comment by ktkohl created at 2012-01-12 04:54:04

symbolic arg function


---

Attachment


---

Comment by ktkohl created at 2012-01-12 04:54:33

Changing status from new to needs_review.


---

Comment by kcrisman created at 2012-01-12 15:06:45

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2012-01-12 15:06:45

There are a few small formatting issues, and it would be good to add an example showing that `arg(sqrt(2)+i)` remaining symbolic (as opposed to `arctan(1/sqrt(2))`) still evaluates correctly numerically.  Otherwise looks fine.  Currently running tests, as `arg` is likely used in a _lot_ of places in Sage...


---

Comment by kcrisman created at 2012-01-12 15:08:45


```

File "/Users/karl-dietercrisman/Downloads/sage-4.8.alpha5/devel/sage-main/sage/symbolic/random_tests.py", line 16:
    sage: [f for (one,f,arity) in _mk_full_functions()]
Expected:
    [Ei, abs, arccos, arccosh, arccot, arccoth, arccsc, arccsch,
    arcsec, arcsech, arcsin, arcsinh, arctan, arctan2, arctanh,
    binomial, ceil, conjugate, cos, cosh, cot, coth, csc, csch,
    dickman_rho, dilog, dirac_delta, elliptic_e, elliptic_ec,
    elliptic_eu, elliptic_f, elliptic_kc, elliptic_pi, erf, exp,
    factorial, floor, heaviside, imag_part, integrate,
    kronecker_delta, log, polylog, real_part, sec, sech, sgn, sin,
    sinh, tan, tanh, unit_step, zeta, zetaderiv]
Got:
    [Ei, abs, arccos, arccosh, arccot, arccoth, arccsc, arccsch, arcsec, arcsech, arcsin, arcsinh, arctan, arctan2, arctanh, arg, binomial, ceil, conjugate, cos, cosh, cot, coth, csc, csch, dickman_rho, dilog, dirac_delta, elliptic_e, elliptic_ec, elliptic_eu, elliptic_f, elliptic_kc, elliptic_pi, erf, exp, factorial, floor, heaviside, imag_part, integrate, kronecker_delta, log, polylog, real_part, sec, sech, sgn, sin, sinh, tan, tanh, unit_step, zeta, zetaderiv]
**********************************************************************
File "/Users/karl-dietercrisman/Downloads/sage-4.8.alpha5/devel/sage-main/sage/symbolic/random_tests.py", line 238:
    sage: random_expr(5, verbose=True)
Expected:
    About to apply dirac_delta to [1]
    About to apply arccsch to [0]
    About to apply <built-in function add> to [0, arccsch(0)]
    arccsch(0)
Got:
    About to apply dirac_delta to [1]
    About to apply arcsec to [0]
    About to apply <built-in function add> to [0, arcsec(0)]
    arcsec(0)
```



---

Comment by kcrisman created at 2012-01-12 16:25:23

I think the Maxima translation may not be correct.

```

 -- Function: carg (<z>)
     Returns the complex argument of <z>.  The complex argument is an
     angle `theta' in `(-%pi, %pi]' such that `r exp (theta %i) = <z>'
     where `r' is the magnitude of <z>.

     `carg' is a computational function, not a simplifying function.

     See also `abs' (complex magnitude), `polarform', `rectform',
     `realpart', and `imagpart'.

     Examples:

          (%i1) carg (1);
          (%o1)                           0
          (%i2) carg (1 + %i);
                                         %pi
          (%o2)                          ---
                                          4
          (%i3) carg (exp (%i));
          (%o3)                           1
          (%i4) carg (exp (%pi * %i));
          (%o4)                          %pi
          (%i5) carg (exp (3/2 * %pi * %i));
                                          %pi
          (%o5)                         - ---
                                           2
          (%i6) carg (17 * exp (2 * %i));
          (%o6)                           2


(%o3)                                true
```

See also Barton Willis' [parg](http://maxima.sourceforge.net/docs/manual/en/maxima_80.html#Item_003a-parg), though that only works if having loaded `to_poly_solve`.


---

Comment by kcrisman created at 2012-01-12 16:31:33

Otherwise, all tests pass!


---

Comment by kcrisman created at 2012-01-12 16:37:23

Do this to check the fix works.

```
sage: maxima(arg(x))
atan2(0,x)
sage: maxima(arg(2+i))
atan(1/2)
sage: maxima(arg(sqrt(2)+i))
atan(1/sqrt(2))
sage: arg(2+i)
arctan(1/2)
sage: arg(sqrt(2)+i)
arg(sqrt(2) + I)
```

It also seems to help with the sqrt(2) issue, in a manner of speaking.  One could tell someone to do 

```
sage: arg(sqrt(2)+i).simplify()
arctan(1/2*sqrt(2))
```



---

Comment by ktkohl created at 2012-01-12 17:06:14

revision of arg function--apply instead of the previous patch


---

Attachment


---

Comment by ktkohl created at 2012-01-12 17:06:43

Changing status from needs_work to needs_review.


---

Attachment

symbolic arg--fixed whitespace issues--use this one instead of others


---

Attachment


---

Comment by burcin created at 2012-02-07 10:30:13

I uploaded a new patch with minor modifications to Karen's. In particular, it

 * removes the duplicate commands that appear in the `EXAMPLES` and `TESTS` blocks for `Function_arg`.
 * import `CC` directly instead of calling `ComplexField` in `_evalf_()`.

I give a positive review to Karen's patch. If someone can take a quick look at my changes to check if I didn't mess anything up, this can be merged.


---

Comment by kcrisman created at 2012-02-07 14:14:44

It doesn't appear that you messed anything up, except ...

```
sage: arg(3.0)
---------------------------------------------------------------------------
<snip>
   1426             return x.arg()
   1427         except AttributeError:
-> 1428             from sage.rings.complex_field import CC
   1429             x = CC(x)
   1430             return x.arg()

ImportError: cannot import name CC
```

So apparently that won't work.  Otherwise the changes are fine.


---

Comment by kcrisman created at 2012-02-07 14:14:44

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by burcin created at 2012-02-07 15:54:48

Changing status from needs_work to needs_review.


---

Comment by burcin created at 2012-02-07 15:54:48

Apparently I didn't run tests, latex output was also broken.

attachment:trac_4498-arg_evalf.patch, to be applied after attachment:trac_4498-symbolic_arg.cleanup.patch, implements a new `_evalf_()` function which keeps the precision of the input. This one needs a real review. :)


---

Comment by kcrisman created at 2012-02-07 16:08:25

This makes a lot more sense.  Running tests...

Why `parent_d` and not `parent`?  Just wondering in case there is a convention I should be aware of.


---

Comment by burcin created at 2012-02-07 16:13:12

Using `parent` as the name of the keyword argument masks the imported `parent()` function, which I used in the function body.


---

Comment by kcrisman created at 2012-02-07 16:39:00

I wondered; that makes sense.

All looks well.  Just a question - do you want to include any of the following as tests?

```
sage: arg(long(1000))
0
sage: arg(1j)
1.57079632679490
sage: arg(1J)
1.57079632679490
sage: arg(complex(0,1))
1.57079632679490
sage: arg(complex(1,0))
0.000000000000000
sage: arg(int(10))
0
```

It's not a big deal to me either way, I just wanted to test them.


---

Comment by kcrisman created at 2012-02-07 16:39:00

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-02-12 12:47:41

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2012-02-12 12:47:41

This patch conflicts with #9130.  Either this one or #9130 should be rebased.


---

Comment by jdemeyer created at 2012-02-13 09:35:59

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2012-02-14 14:20:11

Resolution: fixed


---

Comment by chapoton created at 2017-07-19 08:21:56

standard form for name
