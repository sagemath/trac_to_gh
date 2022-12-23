# Issue 8021: ref manual for 4.3.1: error when building (Undefined control sequence \cross)

Issue created by migration from https://trac.sagemath.org/ticket/8021

Original creator: jhpalmieri

Original creation time: 2010-01-21 06:26:45

Assignee: mvngu

In several places in the Sage code, "\cross" is used, and one of those instances causes an error when building the reference manual.  This is not a standard LaTeX command, and I think "\times" is what is intended, so this patch makes that change.


---

Comment by jhpalmieri created at 2010-01-21 06:30:23

Changing status from new to needs_review.


---

Attachment


---

Comment by mvngu created at 2010-01-22 02:37:16

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-22 02:37:16

This allows the HTML version of the reference manual to build without errors.


---

Comment by mvngu created at 2010-01-23 16:58:37

Resolution: fixed
