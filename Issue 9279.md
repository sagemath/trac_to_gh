# Issue 9279: remove databases/tables.py since superseded by newer code

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2010-06-19 23:12:55

Assignee: jason

The code from `databases/tables.py` was long ago split into `databases/odlyzko.py` and `databases/cremona.py`, and these have been documented and improved.  For some reason the old file is still around, undocumented and untested.

It's time to get rid of it.


---

Attachment


---

Comment by AlexGhitza created at 2010-06-19 23:14:55

Changing status from new to needs_review.


---

Comment by was created at 2010-06-22 04:36:54

Milestone sage-4.4.5 deleted


---

Comment by rlm created at 2010-06-22 17:58:08

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-07-22 07:57:16

Resolution: fixed
