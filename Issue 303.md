# Issue 303: modular forms bug

Issue created by migration from https://trac.sagemath.org/ticket/303

Original creator: was

Original creation time: 2007-03-01 17:58:02

Assignee: was


```
sage: m = CuspForms(64,2)
sage: m.integral_basis()
Traceback (most recent call last):
...
ArithmeticError: basis vectors must be linearly independent.
```



---

Comment by was created at 2007-08-19 01:08:59

Resolution: fixed


---

Comment by was created at 2007-08-19 01:08:59

Fixed for sage-2.8.2 (same fix as for #304).
