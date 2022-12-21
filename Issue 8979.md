# Issue 8979: spelling mistake in sage/gsl/ode.pyx

Issue created by migration from Trac.

Original creator: Moredread

Original creation time: 2010-05-16 16:57:58

Assignee: mvngu

There is a small spelling mistake in the ode documentation:

The default algorithm if ``rkf45``.

Instead of.

The default algorithm is ``rkf45``.


---

Attachment


---

Comment by Moredread created at 2010-05-17 01:59:07

Changing assignee from mvngu to tba.


---

Comment by mvngu created at 2010-05-17 03:11:25

Is this ready for review?


---

Comment by Moredread created at 2010-05-17 12:39:50

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-05-18 02:12:40

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-05-18 02:12:40

I'm happy with your patch. But it cannot be merged into the Sage library until you have put your real name in the ticket field "Author(s):", and also put your contact email address somewhere in the patch header. Your real name and contact email address will be used to credit you for your contribution.


---

Comment by mvngu created at 2010-05-18 02:12:40

Changing priority from major to trivial.


---

Attachment


---

Comment by Moredread created at 2010-05-18 19:03:08

Thank you for the review. I added an updated patch file.


---

Comment by mvngu created at 2010-05-19 07:51:11

Merged [trac_8979_2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8979/trac_8979_2.patch).


---

Comment by mvngu created at 2010-05-19 07:51:11

Resolution: fixed
