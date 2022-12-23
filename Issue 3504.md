# Issue 3504: sage sometimes leaves matlab processes that eat 100% cpu time

Issue created by migration from https://trac.sagemath.org/ticket/3504

Original creator: cwitty

Original creation time: 2008-06-24 20:47:54

Assignee: was

I've found a way to somewhat reproducibly leave a matlab process eating 100% cpu time.

I log on to sage.math, start Sage, and run the following commands:

```
sage: m = matlab(matrix(RR, [[1]]))
sage: m.det()
```

Then I kill my local ssh client with "kill -9" (to make a non-clean ssh shutdown).

Often (not always, but I think more than half the time) this leaves a matlab process eating 100% of the cpu time.


---

Comment by jdemeyer created at 2015-06-23 13:49:26

Changing component from interfaces to interfaces: optional.
