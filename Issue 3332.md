# Issue 3332: Switch pbuild to -O2

Issue created by migration from Trac.

Original creator: gfurnish

Original creation time: 2008-05-29 19:27:26

Assignee: gfurnish

Keywords: pbuild

pbuild and sbuild currently compile with -O3; we should use -O2 for stability reasons (and -O3 may result in larger, slower code).


---

Attachment


---

Comment by gfurnish created at 2008-05-29 19:28:16

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-06-09 21:18:30

Positive review.


---

Comment by mabshoff created at 2008-06-09 21:20:21

Resolution: fixed


---

Comment by mabshoff created at 2008-06-09 21:20:21

Merged in Sage 3.0.3.alpha0
