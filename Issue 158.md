# Issue 158: missing sage-make_relative's

Issue created by migration from https://trac.sagemath.org/ticket/158

Original creator: was

Original creation time: 2006-10-27 21:02:30

Assignee: was

sage-make_relative needs to be called after any "sage -i".  E.g., installing pyrex
then moving sage results in a broken sage.


---

Attachment


---

Comment by was created at 2006-11-06 07:52:28

Resolution: fixed


---

Comment by was created at 2006-11-06 07:52:28

fixed -- was an easy addition to sage-spkg
