# Issue 3291: [with patch, needs review] pbuild doesn't properly compile mwrank.so on some systems

Issue created by migration from Trac.

Original creator: gfurnish

Original creation time: 2008-05-23 22:38:03

Assignee: gfurnish

On some systems pbuild seems to leave out wrap.o of mwrank.so, resulting in a undefined symbol error


---

Comment by gfurnish created at 2008-05-23 22:41:11

Changing status from new to assigned.


---

Attachment


---

Comment by jsp created at 2008-05-23 23:28:46

The patch fixed the issue with build on Fedora 9, 32 bits, 2 cpu's

Jaap


---

Comment by mabshoff created at 2008-05-24 00:27:43

Merged in Sage 3.0.2.rc3


---

Comment by mabshoff created at 2008-05-24 00:27:43

Resolution: fixed
