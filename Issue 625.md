# Issue 625: check for system gfortran, g95 or g77 when no binary is available

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-09-08 23:34:04

Assignee: mabshoff

The number of binaries in the current Sage 2.8.4 is limited. But many systems, especially more exotic Unixes, have fortran compilers installed. So instead of failing look for one of those, warn user and select them in the order 

```
gfortran > g95 > g77
```

Cheers,

Michael


---

Comment by mabshoff created at 2007-09-08 23:34:11

Changing status from new to assigned.


---

Comment by was created at 2007-09-12 21:19:49

Resolution: fixed
