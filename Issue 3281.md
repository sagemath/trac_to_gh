# Issue 3281: libecm fails to pbuild

Issue created by migration from https://trac.sagemath.org/ticket/3281

Original creator: gfurnish

Original creation time: 2008-05-23 16:30:17

Assignee: gfurnish

libecm was moved without updating pbuild and thus pbuild fails to compile sage.


---

Attachment


---

Comment by gfurnish created at 2008-05-23 16:31:27

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-05-23 16:36:32

Resolution: fixed


---

Comment by mabshoff created at 2008-05-23 16:36:32

The patch is obviously correct. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-23 16:39:03

Merged in Sage 3.0.2.rc1
