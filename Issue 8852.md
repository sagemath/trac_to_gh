# Issue 8852: minor doctest fix in fast_eval.pyx for Cygwin

Issue created by migration from https://trac.sagemath.org/ticket/8852

Original creator: mhansen

Original creation time: 2010-05-03 12:27:37

Assignee: tbd




---

Attachment


---

Comment by mhansen created at 2010-05-03 13:17:48

Changing status from new to needs_review.


---

Comment by was created at 2010-05-25 02:19:11

Resolution: fixed


---

Comment by was created at 2010-05-25 02:19:11

This seems reasonably harmless. It's the result of getting 2.0000...0004 on cygwin.
