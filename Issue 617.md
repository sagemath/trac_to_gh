# Issue 617: hyperelliptic_padic.py failure

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2007-09-07 09:15:47

Assignee: was

Segfault on new doctest


---

Comment by robertwb created at 2007-09-07 09:16:49

Changing status from new to assigned.


---

Comment by robertwb created at 2007-09-07 09:16:49

Changing assignee from was to robertwb.


---

Attachment

Turns out this was due to a bug in the rational __pow__ function. Fixed.


---

Comment by was created at 2007-09-07 17:35:12

Resolution: fixed
