# Issue 9441: Atkin-Lehner operators for Cremona modular symbols

Issue created by migration from https://trac.sagemath.org/ticket/9441

Original creator: cremona

Original creation time: 2010-07-06 20:34:58

Assignee: craigcitro

CC:  was

Keywords: modular symbols

The code in sage/libs/cremona wraps some of Cremona's modular symbols code, including Hecke operators.  The wrapping function incorrectly assumes that the function heckeop(p) only works for primes p not dividing the level, when in fact it works fine for primes dividing the level, in that case returning the matrix of the Atkin-Lehner involution.

The patch remedies this, with some tests.


---

Attachment

Applies to 4.5.alpha3


---

Comment by cremona created at 2010-07-06 20:37:19

Changing status from new to needs_review.


---

Comment by rlm created at 2010-07-17 12:10:21

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-07-17 12:10:21

Looks good to me! Applies, passes tests.


---

Comment by mpatel created at 2010-07-20 07:47:39

Resolution: fixed
