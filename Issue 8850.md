# Issue 8850: Cython should link against BLAS instead of ATLAS on Cygwin

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2010-05-03 12:23:21

Assignee: tbd

This is the same behavior as in OS X


---

Attachment


---

Comment by mhansen created at 2010-05-03 13:17:33

Changing status from new to needs_review.


---

Comment by was created at 2010-05-25 02:22:03

looks fine and safe; it can't break anything.


---

Comment by was created at 2010-05-25 02:22:03

Resolution: fixed


---

Comment by drkirkby created at 2010-08-02 04:37:18

ATLAS is faster than BLAS, so this is not an ideal solution.
