# Issue 3257: Pbuild ignores gcc specific default settings

Issue created by migration from https://trac.sagemath.org/ticket/3257

Original creator: gfurnish

Original creation time: 2008-05-19 18:53:19

Assignee: gfurnish

For most arguments to GCC_Compiler, gccc will completely ignore them and use the enviromental defaults instead.


---

Comment by gfurnish created at 2008-05-19 18:57:16

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2008-05-21 13:26:45

Patch looks good to me. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-21 13:27:35

Merged in Sage 3.0.2.rc0


---

Comment by mabshoff created at 2008-05-21 13:27:35

Resolution: fixed
