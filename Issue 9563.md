# Issue 9563: Remove the English-language tutorial's Makefile

Issue created by migration from https://trac.sagemath.org/ticket/9563

Original creator: mpatel

Original creation time: 2010-07-21 10:54:50

Assignee: mvngu

The file `SAGE_DOC/en/tutorial/Makefile` appears to be superfluous.  If this is correct, we can remove it.

See [comment:ticket:9323:7 this comment] at #9323.


---

Comment by mhansen created at 2010-07-21 12:09:51

Yep, we should be able to delete it.


---

Attachment


---

Comment by mhansen created at 2012-03-29 07:22:38

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2012-04-03 06:56:59

Agreed, all documentation (PDF and HTML) builds fine without this file.


---

Comment by jdemeyer created at 2012-04-03 06:56:59

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-04-07 15:10:00

Resolution: fixed
