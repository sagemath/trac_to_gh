# Issue 3614: pbuild broken by finance

Issue created by migration from https://trac.sagemath.org/ticket/3614

Original creator: gfurnish

Original creation time: 2008-07-08 18:03:43

Assignee: gfurnish

pbuild is broken by finance compiled modules in 3.0.4.rc0.  The fix is going to be adding the right libraries to the finance include/linker options


---

Comment by mabshoff created at 2008-07-08 18:35:37

Changing priority from blocker to major.


---

Comment by mabshoff created at 2008-07-08 18:35:37

Gary,

this is not a blocker for 3.0.5, but will get merged if it is ready in time.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-07-11 04:18:29

Patch looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-15 01:31:32

Merged in Sage 3.0.6.alpha0


---

Comment by mabshoff created at 2008-07-15 01:31:32

Resolution: fixed
