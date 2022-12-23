# Issue 2226: sage-2.10.2.alpha1 -- integral is now wrong (imho) for polynomials

Issue created by migration from https://trac.sagemath.org/ticket/2226

Original creator: was

Original creation time: 2008-02-20 07:00:39

Assignee: was

This doctest fails:

```
	 [2.5 s]
sage -t  devel/sage-main/sage/misc/functional.py            **********************************************************************
File "functional.py", line 438:
    sage: integral(f)
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_29[1]>", line 1, in <module>
        integral(f)###line 438:
    sage: integral(f)
      File "/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/site-packages/sage/misc/functional.py", line 452, in integral
        return x.integral(*args, **kwds)
      File "polynomial_element.pyx", line 1499, in sage.rings.polynomial.polynomial_element.Polynomial.integral
    ArithmeticError: coefficients of integral cannot be coerced into the base ring
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_29
***Test Failed*** 1 failures.
```


This is caused because cyclotomic polys are now over ZZ instead of QQ.
Also, integral *should* coerce to the fraction field.  This is really
dumb to have this fail.


```
bsd:sage-2.10.2.alpha1 was$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.2.alpha1, Release Date: 2008-02-19               |
| Type notebook() for the GUI, and license() for information.        |
sage:         sage: f = cyclotomic_polynomial(10)                                                                                                                             
sage:         sage: integral(f)   
---------------------------------------------------------------------------
<type 'exceptions.ArithmeticError'>       Traceback (most recent call last)

/Users/was/build/sage-2.10.2.alpha1/<ipython console> in <module>()

/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/site-packages/sage/misc/functional.py in integral(x, *args, **kwds)
    450     """
    451     if hasattr(x, 'integral'):
--> 452         return x.integral(*args, **kwds)
    453     else:
    454         from sage.calculus.calculus import SR

/Users/was/build/sage-2.10.2.alpha1/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial.integral()

<type 'exceptions.ArithmeticError'>: coefficients of integral cannot be coerced into the base ring
```



---

Attachment

The attached patch adds a bunch of much-needed docstrings to polynomial_element.pyx.  It also, more to the point, fixes f.integrate() to pass to the fraction field if needed.


---

Comment by mabshoff created at 2008-02-21 17:41:59

Patch looks good to me, nice improvement docstring and test-wise.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-21 17:53:17

Resolution: fixed


---

Comment by mabshoff created at 2008-02-21 17:53:17

Merged in Sage 2.10.2.rc0
