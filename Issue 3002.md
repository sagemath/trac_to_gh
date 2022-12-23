# Issue 3002: A lot of  spkgs check for fortran even if they don't need it

Issue created by migration from https://trac.sagemath.org/ticket/3002

Original creator: dfdeshom

Original creation time: 2008-04-22 16:52:04

Assignee: mabshoff


```
A lot of configure scripts seem to check for
fortran, even if they don't use it. It appears the relevant
environment variables are F77 and FFLAGS. Anyway, the variable
SAGE_FORTRAN seems to be honored fine for the packages that actually
need fortran.
```



---

Comment by mabshoff created at 2008-04-22 16:54:49

Changing component from spkg-check to packages.


---

Comment by mabshoff created at 2008-04-22 16:54:49

This is not the case and if we don't use an F77 compiler we shouldn't use the F77 env variable. The fact that a lot of them check for a Fortran compiler and don't use them is also something that doesn't matter since the configure process will not fail. So, the whole ticket is clearly "won't fix" to me.

Thoughts?

Cheers,

Michael


---

Comment by was created at 2008-04-22 17:08:48

Resolution: wontfix
