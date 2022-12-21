# Issue 397: ZZ.digits(base) and inverse

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-06-30 18:27:03

Assignee: somebody

The attache file is a patch to allow the following code to work:

```
sage: e = 7
sage: e.digits(2)
[1, 1, 1]
sage: e.digits(3)
[1, 2]
sage: e.digits(10)
[7]
sage: ZZ(e.digits(3),3)
7
```

The return type of ZZ.digits() is a list with Integer entries in little endian order.


---

Comment by malb created at 2007-06-30 18:27:38

main patch


---

Attachment

follow-up patch for faster ZZ.digits()


---

Attachment

Added follow-up patch based on William's input.


---

Comment by malb created at 2007-08-09 13:32:36

Resolution: fixed
