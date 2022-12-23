# Issue 8833: fix riemann.pyx numerical noise issues on t2 (etc.)

Issue created by migration from https://trac.sagemath.org/ticket/8833

Original creator: was

Original creation time: 2010-05-01 06:01:55

Assignee: burcin

A new patch introduced some new noise.


---

Attachment


---

Comment by was created at 2010-05-01 06:03:24

Changing status from new to needs_review.


---

Comment by rbeezer created at 2010-05-01 14:37:59

I had these failures on 64-bit Ubuntu 9.10 Intel Core Duo 2 with 4.4.1.alpha2.  This patch was rolled into 4.4.1.alpha3 and as part of building that (with long tests enabled) this change passed the tests.  And it looks harmless, just shortening up precision by a digit or two.  So, positive review.


---

Comment by rbeezer created at 2010-05-01 14:37:59

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-05-01 19:18:59

Resolution: fixed
