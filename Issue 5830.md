# Issue 5830: [with patch, not ready for review] reducible root system fixes

Issue created by migration from https://trac.sagemath.org/ticket/5830

Original creator: bump

Original creation time: 2009-04-20 05:09:53

Assignee: bump

CC:  sage-combinat

The methods simple_roots(), fundamental_weights() and simple_coroots() for the ambient space of a root system are supposed to return a family. This was never correctly implemented for the reducible types, and the patch corrects this.

There are also some changes in weyl_characters.py, where it was assumed that the root system was irreducible in a few places. The patch corrects this.

The patch is probably correct but I haven't confirmed that it applies cleanly to sage-3.4.1.rc3 or that it passes `sage --testall` so wait to review.


---

Comment by mabshoff created at 2009-04-20 06:03:17

Resolution: duplicate


---

Comment by mabshoff created at 2009-04-20 06:03:17

For the record: This is a dupe of #5832.

Cheers,

Michael
