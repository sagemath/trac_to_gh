# Issue 5013: Solaris 10/x86: Fix numerical noise failure in sage/ext/fast_eval.py

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-01-18 13:47:47

Assignee: mabshoff

This patch is due to libm differences. Patch coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-18 13:48:04

Changing status from new to assigned.


---

Attachment

This is a standard fix for numerical noise issues, positive review (although I have not tested this on Solaris).


---

Comment by mabshoff created at 2009-01-19 01:36:01

Resolution: fixed


---

Comment by mabshoff created at 2009-01-19 01:36:01

Merged in Sage 3.3.alpha0
