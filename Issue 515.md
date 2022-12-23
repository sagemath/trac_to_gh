# Issue 515: memory leak in libSINGULAR conversion routine

Issue created by migration from https://trac.sagemath.org/ticket/515

Original creator: malb

Original creation time: 2007-08-29 20:50:02

Assignee: somebody

mabshoff discovered a memleak in the conversion route for rational numbers in the libsingular interface. The attached patch supposedly fixes this.


---

Comment by mabshoff created at 2007-08-29 21:26:04

Resolution: duplicate
