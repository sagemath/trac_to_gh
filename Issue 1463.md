# Issue 1463: polymake package has wrong cddlib,gmp versions

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2007-12-11 22:33:50

Assignee: mhampton

Keywords: polymake, cddlib, gmp

In the spkg-install script for polymake, the versions need to be updated: the correct script variables are:

```
SAGE_GMP_VERSION="4.2.1.p12"
CDDLIB_VERSION="094b.p0"
```





---

Comment by mhampton created at 2007-12-11 22:33:57

Changing status from new to assigned.


---

Comment by was created at 2007-12-12 00:59:18

I've done what this ticket says to do.  This ticket can be closed.


---

Comment by mabshoff created at 2007-12-12 03:59:48

Resolution: fixed
