# Issue 3527: Build python with "-O2" instead of "-O3" on Itanium

Issue created by migration from https://trac.sagemath.org/ticket/3527

Original creator: mabshoff

Original creation time: 2008-06-28 09:32:34

Assignee: mabshoff

When building Sage's pyhton and extensions with gcc 4.3 on Itanium we get some doctest failures that disappear with "-O2"

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-28 09:32:39

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-07-07 22:28:50

This is starting to look invalid since all failures I see seem to be triggered by bugs not normally observed on non-Itanium, but valgrind finds faults in those cases on x86-64.

Cheers,

Michael


---

Comment by was created at 2008-07-09 16:09:25

Resolution: fixed


---

Comment by was created at 2008-07-09 16:09:25

positive review.


---

Comment by mabshoff created at 2008-07-09 16:18:11

Merged in Sage 3.0.4.rc2
