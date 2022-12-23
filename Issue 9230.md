# Issue 9230: Broken docstrings in Travelling Salesman Problem

Issue created by migration from https://trac.sagemath.org/ticket/9230

Original creator: ncohen

Original creation time: 2010-06-12 22:09:57

Assignee: jason, mvngu, ncohen, rlm

CC:  mvngu

Still those annoying default {} instead of None. This patch was not merged when the fix for {} was written ^^;

Nathann


---

Attachment

Here it is !

Nathann


---

Comment by ncohen created at 2010-06-12 22:11:08

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-06-13 09:24:28

Looks good. The relevant failure was discovered when testing #8781, so I'm making #8781 a prerequisite of the current ticket. That way, if the current ticket is merged, then #8781 must first be merged.


---

Comment by mvngu created at 2010-06-13 09:24:28

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-06-29 16:45:47

Resolution: fixed
