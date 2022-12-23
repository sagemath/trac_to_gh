# Issue 1350: sage-2.8.15.alpha0 doctest error in plot.py

Issue created by migration from https://trac.sagemath.org/ticket/1350

Original creator: mhansen

Original creation time: 2007-12-01 16:38:23

Assignee: mhansen

This is due to the fact that we now wrap sage.functions.constant.Constants with SymbolicConstant.


---

Comment by mhansen created at 2007-12-01 16:39:52

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2007-12-01 17:22:28

Merged in 2.8.15.alpha1.


---

Comment by mabshoff created at 2007-12-01 17:22:28

Resolution: fixed
