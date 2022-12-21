# Issue 1949: rewrite the mwrank interface to get rid of wrap.* and use C++

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-27 19:44:58

Assignee: was

CC:  cremona




---

Comment by was created at 2008-01-27 20:42:15

Changing status from new to assigned.


---

Attachment

this is part 1 -- it doesn't even build yet, but all functions are there...


---

Comment by was created at 2008-06-16 00:26:11

NOTE: There is code in ell_rational_field.pyx that refers to trac #1949 that should be changed/removed when this ticket (#1949) gets finished.


---

Comment by chapoton created at 2018-05-19 07:52:06

Maybe we should close this very old one ?


---

Comment by chapoton created at 2018-05-19 07:52:06

Changing status from new to needs_review.


---

Comment by cremona created at 2018-05-19 08:04:26

Replying to [comment:7 chapoton]:
> Maybe we should close this very old one ?

Surely, yes.  I don't think I have ever see it but eclib has changed enough in 10 years that anything in this direction (whatever it was) would need to be done again from scratch.


---

Comment by chapoton created at 2018-05-19 10:04:10

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2018-07-21 09:40:53

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2018-07-21 09:40:53

The first part of the title is certainly still relevant.
