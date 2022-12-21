# Issue 986: sage-2.8.9.rc1: order of .variety() depends on architecture in multi_polynomial_ideal.py

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-10-25 00:57:33

Assignee: was

This doctest fails on 32-bit x86 Linux:

```
File "multi_polynomial_ideal.py", line 1078:
    sage: V = I.variety(); V
Expected:
    [{y: w^2 + 2, x: 2*w}, {y: w^2 + 2*w, x: 2*w + 2}, {y: w^2 + w, x: 2*w + 1}]
Got:
    [{y: w^2 + w, x: 2*w + 1}, {y: w^2 + 2*w, x: 2*w + 2}, {y: w^2 + 2, x: 2*w}]
```


However, the doctest succeeds on 64-bit x86 Linux.


---

Attachment

I've attached a patch that just sorts the output of .variety().


---

Comment by was created at 2007-10-25 06:44:27

Resolution: fixed
