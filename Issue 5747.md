# Issue 5747: improve doctest coverage for schemes/generic/ambient_space.py

Issue created by migration from https://trac.sagemath.org/ticket/5747

Original creator: AlexGhitza

Original creation time: 2009-04-11 05:19:59

Assignee: AlexGhitza

Keywords: doctest scheme ambient space




---

Comment by AlexGhitza created at 2009-04-11 05:20:09

Changing status from new to assigned.


---

Attachment


---

Comment by AlexGhitza created at 2009-04-11 06:12:26

The patch brings the doctest coverage from 11% to 100% (17 of 17).

There is some interaction with #5631, since I had to add the missing method `_check_verifies_equations()` to `affine_space.py`.  I will rebase this patch in case #5631 gets merged in the mean time.


---

Comment by mabshoff created at 2009-04-12 21:25:24

Resolution: fixed


---

Comment by mabshoff created at 2009-04-12 21:25:24

Merged in Sage 3.4.1.rc3.

Cheers,

Michael
