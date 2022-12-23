# Issue 2379: Merge sage-ptest into sage-test

Issue created by migration from https://trac.sagemath.org/ticket/2379

Original creator: gfurnish

Original creation time: 2008-03-03 22:42:17

Assignee: gfurnish

When stable, merge sage-ptest into sage-test. This will also give us tex file failures in the list of failures when testing.  


---

Comment by gfurnish created at 2008-03-03 22:42:25

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-03-20 11:26:50

Required: Fix hang on test segfault


---

Comment by gfurnish created at 2008-03-21 14:24:51

Hang on segfault appears to be fixed


---

Attachment


---

Attachment

Patches look good to me. Let's merge this now.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-08 11:02:55

Merged in Sage 3.0.alpha3


---

Comment by mabshoff created at 2008-04-08 11:02:55

Resolution: fixed


---

Attachment

this fixes the makefile so that "make check" and friends work
