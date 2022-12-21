# Issue 9006: Segfault evaluating large degree polynomials

Issue created by migration from Trac.

Original creator: johanbosman

Original creation time: 2010-05-21 12:12:03

Assignee: AlexGhitza

sage: f = ZZ!['x'](1000000 * ![1])
sage: f(1)
/home/bosman/sage-4.4.2/local/bin/sage-sage: Zeile 206: 32438 Segmentation fault      sage-ipython "$`@`" -i


It might be in sage/rings/polynomial/polynomial_compiled.pyx: binary_pd has methods that use a recursive implementation, causing a stack overflow (but I don't have time now, so I'll try to look at it more carefully later).


---

Attachment


---

Comment by johanbosman created at 2010-05-24 16:05:43

Changing status from new to needs_review.


---

Comment by AlexGhitza created at 2010-06-05 00:53:08

Looks good.


---

Comment by AlexGhitza created at 2010-06-05 00:53:08

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-06 01:15:39

Resolution: fixed
