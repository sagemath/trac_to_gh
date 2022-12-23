# Issue 478: completely eliminate the dependence of sage on openssl

Issue created by migration from https://trac.sagemath.org/ticket/478

Original creator: was

Original creation time: 2007-08-22 07:01:43

Assignee: was

SAGE should not depend on openssl, since openssl is gpl-incompatible.

Unfortunately, gnutls's presence isn't enough for Python to build the "md5" module, and
SAGE needs that module.


---

Comment by was created at 2008-01-27 17:31:17

Resolution: fixed


---

Comment by was created at 2008-01-27 17:31:17

We did this in May, 2007.
