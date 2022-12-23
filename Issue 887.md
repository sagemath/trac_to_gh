# Issue 887: 2.8.7-alpha0: doctest failure in rings/polynomial/real_roots.pyx

Issue created by migration from https://trac.sagemath.org/ticket/887

Original creator: cwitty

Original creation time: 2007-10-13 20:31:31

Assignee: failure

All three errors are essentially the same; here's one of them:

```
File "real_roots.pyx", line 797:
    sage: str(dbp)
Expected:
    '<IBP: (-1, 148, 901) + [0 .. 4); level 1; slope_err [-24.000000000000000 .. 24.000000000000000]>'
Got:
    '<IBP: (-1, 148, 901) + [0 .. 4); level 1>'
```




---

Attachment


---

Comment by cwitty created at 2007-10-13 22:12:32

This one was all my fault :-)

My original code was buggy, but the bug was masked by a Cython bug.  But I was the one who reported the Cython bug and triggered the fix, exposing this bug...


---

Comment by was created at 2007-10-14 22:56:30

Resolution: fixed
