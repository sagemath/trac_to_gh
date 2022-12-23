# Issue 3138: [with patch, needs review] Singular multivariate polynomial ring has redundant _repr_ method

Issue created by migration from https://trac.sagemath.org/ticket/3138

Original creator: broune

Original creation time: 2008-05-09 00:52:47

Assignee: broune

MPolynomialRing_libsingular in sage/rings/polynomial/multi_polynomial_libsingular.pyx defines a _repr_ method which does the same thing as the _repr_ method that it inherits from MPolynomialRing_generic in sage/rings/polynomial/multi_polynomial_ring_generic.pyx

Thus the _repr_ method is redundant and should be removed.



---

Attachment


---

Comment by broune created at 2008-05-09 01:06:43

Changing status from new to assigned.


---

Comment by malb created at 2008-05-09 08:35:20

Yep, I wrote the libsingular version before the generic one. Positive review.


---

Comment by mabshoff created at 2008-05-09 13:11:56

Merged in Sage 3.0.2.alpha0


---

Comment by mabshoff created at 2008-05-09 13:11:56

Resolution: fixed
