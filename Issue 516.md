# Issue 516: memory leak in libSINGULAR conversion routine

Issue created by migration from https://trac.sagemath.org/ticket/516

Original creator: malb

Original creation time: 2007-08-29 20:51:38

Assignee: somebody

mabshoff discovered a memleak in the conversion route for rational numbers in the libsingular interface. The attached patch supposedly fixes this.


---

Comment by malb created at 2007-08-29 20:54:16

As trac doesn't accept my attachment, try this: http://sage.math.washington.edu/home/malb/5855.patch


---

Comment by malb created at 2007-08-29 20:54:40

Changing assignee from somebody to malb.


---

Comment by malb created at 2007-08-29 20:54:40

Changing status from new to assigned.


---

Comment by was created at 2007-08-30 00:20:32

Resolution: fixed
