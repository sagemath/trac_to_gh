# Issue 1645: erf doesn't evaluate with intervals

Issue created by migration from https://trac.sagemath.org/ticket/1645

Original creator: schilly

Original creation time: 2007-12-31 12:05:23

Assignee: jkantor

This should either raise an error or give a result:



```
a = RealInterval('2.3')
erf(a)
```



CPU is at about 0%, so it is doing nothing.
----
maybe there are other unsupported functions, should be checked out!


---

Attachment

This actually has nothing to do with erf really -- it's that converting a real interval to Maxima (or any other system) should raise a TypeError, but doesn't.   

Of course, erf could be implemented for intervals, but that's not done yet; that would be an enhancement not a bug.


---

Comment by cwitty created at 2008-01-15 03:21:32

Resolution: fixed


---

Comment by cwitty created at 2008-01-15 03:21:32

Looks good to me; and this patch was already applied in 2.9.2.
