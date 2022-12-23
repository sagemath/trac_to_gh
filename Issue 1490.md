# Issue 1490: fix numerical noise doctest failure in numerical/test.py

Issue created by migration from https://trac.sagemath.org/ticket/1490

Original creator: mabshoff

Original creation time: 2007-12-13 19:45:33

Assignee: mabshoff

The new aarpack doctest fails on MacIntel OSX. The attached patch fixes that.

Josh: we might need to look into this if it is more than a numerical stability issue.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2007-12-14 03:48:03

Resolution: fixed


---

Comment by mabshoff created at 2007-12-14 03:48:03

Merged in 2.9.alpha7.
