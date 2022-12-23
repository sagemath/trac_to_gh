# Issue 8110: fix issue with multi_polynomial.pyx in sage-4.3.2.alpha0

Issue created by migration from https://trac.sagemath.org/ticket/8110

Original creator: AlexGhitza

Original creation time: 2010-01-28 12:30:54

Assignee: malb

The patch at #7109 mistakenly removed some code from `rings/polynomial/multi_polynomial.pyx`, which causes doctest trouble in sage-4.3.2.alpha0.

A patch fixing this is on its way.



---

Comment by AlexGhitza created at 2010-01-28 12:35:51

Changing status from new to needs_review.


---

Attachment


---

Comment by malb created at 2010-01-28 13:18:24

Changing status from needs_review to positive_review.


---

Comment by malb created at 2010-01-28 13:18:24

* patch looks good
 * applies cleanly against alpha0
 * doctests pass on sage.math


---

Comment by mvngu created at 2010-01-30 23:33:35

Resolution: fixed
