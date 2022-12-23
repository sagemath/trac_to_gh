# Issue 6657: EllipticCurve(..., j=...) shouldn't ignore field argument if given.

Issue created by migration from https://trac.sagemath.org/ticket/6657

Original creator: was

Original creation time: 2009-07-29 23:06:58

Assignee: was


```
I found the following to be rather unexpected:

EllipticCurve(GF(144169),j=1728)
Elliptic Curve defined by y^2 = x^3 - x over Rational Field

 - Victor Miller

[I understand that 1728 is considered an Integer, yet the first
argument seems to be ignored]
```



---

Comment by cremona created at 2009-08-01 18:17:33

Easy to fix:  where EllipticCurve calls `EllipticCurve_from_j(j)` it should in fact coerce j into the parent of x (if x is not none).


---

Comment by wuthrich created at 2009-10-20 22:05:41

This issue only appears in the deprecated function `EllipticCurve(..,j=..)`. The right function to call here is `EllipticCurve_from_j(GF(144169)(1728))`.

My proposal for a change is to finally eliminate the deprecated function.


---

Comment by wuthrich created at 2010-01-12 14:49:43

Changing component from number theory to elliptic curves.


---

Comment by wuthrich created at 2010-01-12 14:49:43

Changing assignee from was to cremona.


---

Comment by cremona created at 2010-01-12 20:19:34

Chris,

You are not quite right.  What is deprecated is EllipticCurve(j0), not EllipticCurve(j=j0):

```
sage: EllipticCurve(GF(101)(1728))
/home/john/sage-4.3.1.alpha1/local/bin/sage-ipython:1: DeprecationWarning: 'EllipticCurve(j)' is deprecated; use 'EllipticCurve_from_j(j)' or 'EllipticCurve(j=j)' instead.
  #!/usr/bin/env python
Elliptic Curve defined by y^2 = x^3 + x over Finite Field of size 101
sage: EllipticCurve(j=GF(101)(1728))
Elliptic Curve defined by y^2 = x^3 + x over Finite Field of size 101
```

Now I cannot remember when that deprecation was put in, hence when it should be removed.

Anyway, Victor's point is a valid one, and I'll put up a patch!


---

Comment by cremona created at 2010-01-12 20:52:15

Applies to 4.3.1.alpha1


---

Attachment

The attached patch sorts this out, with appropriate tests.


---

Comment by cremona created at 2010-01-12 20:53:15

Changing status from new to needs_review.


---

Comment by wuthrich created at 2010-01-15 16:43:48

Yes, that is fine. Thanks John.

Chris.


---

Comment by wuthrich created at 2010-01-15 16:43:48

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-19 00:08:13

Resolution: fixed
