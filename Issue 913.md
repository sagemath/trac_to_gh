# Issue 913: real_roots code fails if polynomial obviously has no roots

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-10-17 15:38:15

Assignee: cwitty

The following test case will loop forever:

```
sage: x = polygen(ZZ)
sage: (x^2 + 1).real_root_intervals()
```




---

Attachment

Fixed.


---

Comment by was created at 2007-10-21 00:49:39

Resolution: fixed
