# Issue 9289: Implement Puiseux polynomials

Issue created by migration from https://trac.sagemath.org/ticket/9289

Original creator: nthiery

Original creation time: 2010-06-21 07:34:53

Assignee: AlexGhitza

CC:  sage-combinat

Implement the ring of Puiseux polynomials. Those are usual
polynomials, except that exponents can be any rational number.


```
   sage: S = PolynomialRing(QQ, ['a','b','c']); S
   Multivariate Puiseux Polynomial Ring in a, b, c over Rational Field
```



See also: http://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Puiseux, http://en.wikipedia.org/wiki/Puiseux_series


---

Comment by chapoton created at 2014-03-06 15:25:03

Changing keywords from "" to "Puiseux".


---

Comment by rws created at 2014-03-16 16:18:18

Changing status from new to needs_review.


---

Comment by rws created at 2014-03-16 16:18:18

Never mind. I thought this was a duplicate.


---

Comment by rws created at 2014-03-16 16:20:23

Changing status from needs_review to needs_info.


---

Comment by kcrisman created at 2015-02-12 15:01:58

See also #4618.


---

Comment by chapoton created at 2018-07-05 14:39:36

New commits:
