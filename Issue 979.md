# Issue 979: printing error with small reals

Issue created by migration from https://trac.sagemath.org/ticket/979

Original creator: mhansen

Original creation time: 2007-10-24 03:49:28

Assignee: mhansen


```
sage: a = .00000000000000000000001;a
0.000000000000000000000010000000000000000000000
```



---

Comment by mhansen created at 2007-10-24 05:11:00

Changing status from new to assigned.


---

Comment by mhansen created at 2007-10-24 05:11:00

Patch for this will be in the big patch for #962.


---

Comment by mhansen created at 2007-12-06 21:21:50

I believe this has already been taken care of.

In 2.8.15, we have


```
sage: a = .00000000000000000000001;a
1.00000000000000e-23
```



---

Comment by mabshoff created at 2007-12-06 21:32:57

Resolution: fixed


---

Comment by mabshoff created at 2007-12-06 21:32:57

Merged in 2.8.15.
