# Issue 5477: Make R.quotient_ring(I) normalize generator in the univariate case (easy to fix!)

Issue created by migration from https://trac.sagemath.org/ticket/5477

Original creator: was

Original creation time: 2009-03-11 03:19:20

Assignee: malb

From a Sage Days 14 user (see below).

In short, in the univariate over-a-field case, `R.quotient_ring(I)` should normalize the generator of the ideal before forming the quotient. 


```
In each case below "I" and "J" are defined by different choices of
generators and are recognized as the same ideal.  In case 1 the
quotients are considered equal and in case 2 they are considered
unequal.

(I checked this with the latest version)

Case 1:
----------

sage: R.<x> = PolynomialRing(QQ)
sage: I = R.ideal([x + x^2, x])
sage: J = R.ideal([2*x + 2*x^2, x])
sage: S = R.quotient_ring(I)
sage: U = R.quotient_ring(J)
sage: I==J
True
sage: S==U
True

Case 2:
----------

sage: R.<x> = PolynomialRing(QQ)
sage: I = R.ideal([x + x^2])
sage: J = R.ideal([2*x + 2*x^2])
sage: S = R.quotient_ring(I)
sage: U = R.quotient_ring(J)
sage: I==J
True
sage: S==U
False
```



---

Comment by AlexGhitza created at 2010-01-02 10:53:31

Changing status from new to needs_review.


---

Comment by AlexGhitza created at 2010-01-02 10:53:31

See attached patch for a fix.


---

Attachment

Fixes by taking gcd with itself when only one generator is given, thus assuring a normalized generator.


---

Comment by rishi created at 2010-01-21 15:22:33

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-23 08:39:45

Resolution: fixed
