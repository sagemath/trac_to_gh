# Issue 7802: Mention that RNDN is the "ties toward even" version in RealField

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-01-01 10:52:06

Assignee: mvngu

CC:  robertwb mvngu

The IEEE754 standard has two versions of "round to nearest".  It appears that ours is the "ties toward even" version (see http://www.mpfr.org/mpfr-current/mpfr.html#MPFR-Basics).  We ought to mention this in the docs to RealField when it talks about the rounding modes.


---

Comment by jason created at 2010-01-20 06:14:08

Changing status from new to needs_review.


---

Attachment


---

Comment by mvngu created at 2010-01-20 08:00:15

Looks good. Applies OK against Sage 4.3.1.rc1. Just make sure you first merge #7999 before applying [trac-7802-ties-to-even-doc.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7802/trac-7802-ties-to-even-doc.patch). Otherwise, the HTML version of the reference manual won't build successfully.


---

Comment by mvngu created at 2010-01-20 08:00:15

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-23 16:57:39

Resolution: fixed
