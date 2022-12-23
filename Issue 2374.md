# Issue 2374: sage-ptest must run in $SAGE_ROOT

Issue created by migration from https://trac.sagemath.org/ticket/2374

Original creator: gfurnish

Original creation time: 2008-03-03 15:59:56

Assignee: gfurnish

sage-ptest only works from $SAGE_ROOT


---

Comment by gfurnish created at 2008-03-03 16:00:02

Changing status from new to assigned.


---

Attachment


---

Comment by gfurnish created at 2008-03-10 07:17:38

This allows you to test a file (as opposed to a directory) and contains a ui fix for some cases in which file tested is in a higher directory.


---

Comment by mabshoff created at 2008-03-10 07:19:53

Patch looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-10 07:20:47

Resolution: fixed


---

Comment by mabshoff created at 2008-03-10 07:20:47

Merged in Sage 2.10.3.rc4
