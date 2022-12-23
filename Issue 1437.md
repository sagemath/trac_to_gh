# Issue 1437: FLINT 1.01.spkg: spkg-check broken

Issue created by migration from https://trac.sagemath.org/ticket/1437

Original creator: mabshoff

Original creation time: 2007-12-09 16:14:21

Assignee: mabshoff

Since FLINT builds its test code only once make check is invoked, but the spkg-check script doesn't define a bunch of env variables, the stand alone script fails.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-10 04:14:12

Merged in 2.9.alpha3.


---

Comment by mabshoff created at 2007-12-10 04:14:12

Resolution: fixed
