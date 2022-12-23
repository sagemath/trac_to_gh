# Issue 7508: hash collisions for derivatives of symbolic functions - act 3

Issue created by migration from https://trac.sagemath.org/ticket/7508

Original creator: burcin

Original creation time: 2009-11-21 12:56:52

Assignee: burcin

Keywords: pynac

Reported by Alex Raichev on sage-support:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: X= var('x,y,z')
sage: f= function('f',*X); f
f(x, y, z)
sage: d= {}
sage: for l in [1..2]:
....:     for s in UnorderedTuples(X,l):
....:         print diff(f,s)
....:         d[diff(f,s)]= 69
....:
D[0](f)(x, y, z)
D[1](f)(x, y, z)
D[2](f)(x, y, z)
D[0, 0](f)(x, y, z)
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call
last)
...
/Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/
expression_conversions.py in derivative(self, ex, operator)
    344             NotImplementedError: derivative
    345         """
--> 346         raise NotImplementedError, "derivative"  
    347
    348     def arithmetic(self, ex, operator):
| Sage Version 4.2.1, Release Date: 2009-11-14                       |
| Type notebook() for the GUI, and license() for information.        |
NotImplementedError: derivative
```


This is another form of the problem I couldn't fix in #6243 and #6851.


---

Comment by burcin created at 2009-11-22 17:09:27

add doctests


---

Attachment

This is fixed (hopefully, for good) in the new pynac package here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.10.spkg

attachment:trac_7508-fderivative_hash_collision_doctest.patch adds doctests for the fix.

Note that the new pynac version also contains fixes for #7264 and #7406. Tests should be run with the patches from those tickets also applied in this order:

 * #7508 (this ticket)
 * #7264
 * #7406

This ticket now depends on #7490.


---

Comment by burcin created at 2009-11-22 17:24:32

Changing status from new to needs_review.


---

Comment by kcrisman created at 2009-12-05 13:51:22

Positive review.


---

Comment by kcrisman created at 2009-12-05 13:51:22

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2009-12-05 13:53:17

I should point out that #7264 has a problem, so the spkg should not be merged until that is resolved.


---

Comment by mhansen created at 2009-12-10 14:22:35

Resolution: fixed
