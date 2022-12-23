# Issue 1112: Integer.__pow__

Issue created by migration from https://trac.sagemath.org/ticket/1112

Original creator: malb

Original creation time: 2007-11-06 16:22:17

Assignee: somebody

the attached patch makes this work:


```
sage: pow(10,20,17)
4
sage: pow?
    pow(x, y[, z]) -> number

    With two arguments, equivalent to x**y.  With three arguments,
    equivalent to (x**y) % z, but may be more efficient (e.g. for longs).
```


this is required such that e.g. the Crypto.RSA module works with SAGE integers.


---

Attachment


---

Comment by mabshoff created at 2007-11-06 22:14:12

Resolution: fixed


---

Comment by mabshoff created at 2007-11-06 22:14:12

applied to 2.8.12.rc0
