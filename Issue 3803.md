# Issue 3803: prime_range takes WAY WAY too long to convert its data back to PARI

Issue created by migration from https://trac.sagemath.org/ticket/3803

Original creator: was

Original creation time: 2008-08-11 04:03:23

Assignee: was


```
d142-058-050-205:src was$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: review2
sage: timeit('prime_range(10^6)')
5 loops, best of 3: 214 ms per loop
sage: timeit('prime_range(10^6,leave_pari=True)')
125 loops, best of 3: 4.29 ms per loop
sage: 214/4.29
49.8834498834499
```



---

Comment by craigcitro created at 2009-01-23 13:21:08

Since we removed the `leave_pari` option altogether, this ticket is now invalid.


---

Comment by craigcitro created at 2009-01-23 13:21:08

Resolution: invalid
