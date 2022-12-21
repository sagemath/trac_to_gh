# Issue 9775: Cygwin: GLPK extension module needs to be more explicit in its linking

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2010-08-21 18:24:21

Assignee: tbd

CC:  ncohen




---

Comment by mhansen created at 2010-08-21 18:25:08

I have a patch for this which I will post shortly.


---

Comment by mhansen created at 2010-08-21 18:26:55

Changing status from new to needs_review.


---

Attachment


---

Comment by ncohen created at 2010-08-23 02:17:34

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-08-23 02:17:34

Everything is fine, and it just explicits a dependency which was already present in the "deps" file. Approved ! `:-)`

Thanks

Nathann


---

Comment by mpatel created at 2010-09-15 11:13:12

Resolution: fixed
