# Issue 8853: fix M_PI_4 in complex_double on Cygwin

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2010-05-03 12:29:15

Assignee: tbd

Apparently, it is not picked up from math.h.


---

Comment by mhansen created at 2010-05-03 13:18:04

Changing status from new to needs_review.


---

Attachment


---

Comment by was created at 2010-05-25 02:08:48

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-05-25 02:08:48

works, but I created a referee patch that has more precision (using the #define on OS X; this can't hurt)...


---

Comment by was created at 2010-05-25 02:09:41

Resolution: fixed


---

Attachment
