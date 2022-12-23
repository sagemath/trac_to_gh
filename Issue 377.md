# Issue 377: major bug in number fields if defining poly has denoms

Issue created by migration from https://trac.sagemath.org/ticket/377

Original creator: was

Original creation time: 2007-05-23 18:35:04

Assignee: somebody


```
swas@ubuntu:~$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.5.2-alpha, Release Date: 2007-05-20                 |
| Type notebook() for the GUI, and license() for information.        |
sage: G.<a> = NumberField(x^3 + 2/3*x + 1)
sage: a^3 + a
MulMod: bad args
Aborted
was@ubuntu:~$
```



---

Comment by was created at 2007-05-31 14:09:02

Resolution: fixed


---

Comment by was created at 2007-05-31 14:09:02

Joel mostly fixed this and I finished it off for sage-2.5.4.
