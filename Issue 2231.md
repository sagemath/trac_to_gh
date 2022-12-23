# Issue 2231: sage-2.10.2-alpha1: doctest failure in partition_algebra.py

Issue created by migration from https://trac.sagemath.org/ticket/2231

Original creator: mhansen

Original creation time: 2008-02-20 09:15:41

Assignee: mhansen

CC:  sage-combinat




---

Attachment


---

Comment by mhansen created at 2008-02-20 09:18:36

Changing status from new to assigned.


---

Attachment

apply this after 2231.patch


---

Comment by was created at 2008-02-20 15:58:10

I added an additional patch with documentation and a docstring, since it took me a while to figure out what your new code actually does, and I wanted to make it easy for others.


---

Comment by mabshoff created at 2008-02-20 17:29:00

Resolution: fixed


---

Comment by mabshoff created at 2008-02-20 17:29:00

Merged both patches in Sage 2.10.2.alpha2
