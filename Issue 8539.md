# Issue 8539: EllipticCurve('6006j1').sha().p_primary_bound(3) ignores CTRL-C

Issue created by migration from https://trac.sagemath.org/ticket/8539

Original creator: rlm

Original creation time: 2010-03-15 04:01:18

Assignee: cremona

CC:  robertwb was

When reproducing this, make sure to wait about 10 seconds before trying to interrupt, as it takes time earlier in the function elsewhere, which handles the interruption properly.


---

Comment by rlm created at 2010-03-15 23:01:38

Changing component from elliptic curves to linear algebra.


---

Comment by rlm created at 2010-03-15 23:01:38

Changing assignee from cremona to was.


---

Attachment


---

Comment by rlm created at 2010-03-15 23:43:06

Changing status from new to needs_review.


---

Comment by robertwb created at 2010-03-16 00:11:00

I'm not sure if using dense matrices here was an oversight, or if there was a reason for it...

http://hg.sagemath.org/sage-main/annotate/8df7435d1864/sage/matrix/matrix_integer_sparse.pyx#241


---

Comment by was created at 2010-03-26 21:47:57

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-03-26 22:23:20

Enthusiastic positive review!!!!!!!!!! 

This totally rocks, leading to massive speedups in modular symbols (susprisingly).


---

Comment by was created at 2010-03-26 22:23:20

Changing priority from major to blocker.


---

Comment by was created at 2010-03-27 01:02:07

this is a referee patch that fixes a doctest (which was wrong).


---

Attachment

Merged into sage-4.3.5


---

Comment by was created at 2010-03-29 22:08:01

Resolution: fixed
