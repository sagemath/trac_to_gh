# Issue 9180: Absolute interval arithmetic

Issue created by migration from https://trac.sagemath.org/ticket/9180

Original creator: robertwb

Original creation time: 2010-06-07 20:40:08

Assignee: jason, jkantor

CC:  rishi jdemeyer

Needed for #4475, but quite self contained and doesn't require any number theory to understand or review. 


---

Attachment


---

Comment by robertwb created at 2010-06-07 21:27:04

Changing status from new to needs_review.


---

Comment by robertwb created at 2010-06-09 01:50:54

apply on top of previous


---

Attachment


---

Comment by kedlaya created at 2011-06-18 13:32:44

Changing status from needs_review to positive_review.


---

Attachment

Applies against 4.7, no long doctest failures. Looks fine to me.


---

Comment by jdemeyer created at 2011-06-19 08:42:35

Should all 3 patches be applied?


---

Comment by kedlaya created at 2011-06-19 14:13:36

All three patches should be applied in order, yes.


---

Comment by jdemeyer created at 2011-07-22 12:49:05

Resolution: fixed


---

Comment by kcrisman created at 2011-08-25 16:59:50

This broke Cygwin, just FYI.  Needs library 'gmp'.  See #11744.  Patch should be very similar to one at #11499.
