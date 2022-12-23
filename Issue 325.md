# Issue 325: LLL for integer matrices

Issue created by migration from https://trac.sagemath.org/ticket/325

Original creator: nbruin

Original creation time: 2007-03-21 00:54:16

Assignee: was

Currently, if you make an integer matrix:

```
A=Matrix(Integers(),3,3,[1,2,3,4,5,6,7,8,9])
```

there seems no direct way to get an LLL reduced basis of its row or column space (whichever is appropriate for SAGE).
There is `ntl.mat_ZZ.LLL`, which may or may not be good. pari also has LLL implementations.

It's really worth it to have a good integer LLL easily accessible in SAGE.


---

Comment by mabshoff created at 2007-09-06 23:11:09

I believe this might also be available via IML.

Cheers,

Michael


---

Attachment


---

Comment by was created at 2007-09-20 23:29:16

Resolution: fixed
