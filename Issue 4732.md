# Issue 4732: TypeError in converting from SR matrix to RR, but *only* in doctesting

Issue created by migration from https://trac.sagemath.org/ticket/4732

Original creator: jason

Original creation time: 2008-12-06 23:26:49

Assignee: mabshoff


```
[17:21] <jason->  matrix(SR,[e]).change_ring(RR) works fine from the Sage command line
[17:21] <jason-> but gives a huge type error when it is a doctest
```




---

Comment by mhansen created at 2009-01-22 08:08:28

Resolution: invalid


---

Comment by mhansen created at 2009-01-22 08:08:28

Neither of us can reproduce this.  I'm going to mark this as invalid.


---

Comment by jason created at 2009-01-22 08:09:17

I agree.  I should have put the version and pasted output.
