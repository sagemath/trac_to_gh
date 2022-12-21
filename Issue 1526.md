# Issue 1526: conversion from gap matrix over finite field to sage matrix is VERY VERY VERY slow -- but robust.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-15 23:10:22

Assignee: was

E.g., in linear_code.py line 780 (in extended_code()), this line dominates:


```
        Gxs = Gx._matrix_(F)           # this is the killer
```


That is dumb.  Optimize this a lot.


---

Comment by embray created at 2019-01-15 18:01:47

The exact code in question no longer exists in that module, though this issue might still be relevant, and would probably be resolved by #26902.

Indeed, this is (unsurprisingly) much faster using the libgap interface.

I wasn't sure exactly how to construct a matrix over a finite field in GAP, so I made it first in Sage, and the passed it to both GAP interfaces, and then back to Sage again:


```
sage: F = GF(2)
sage: M = matrix(F, [[1,0,0],[1,1,0]])
sage: M_gap = gap(M); M_gap
[ [ Z(2)^0, 0*Z(2), 0*Z(2) ], [ Z(2)^0, Z(2)^0, 0*Z(2) ] ]
sage: M_libgap = libgap(M); M_libgap
[ [ Z(2)^0, 0*Z(2), 0*Z(2) ], [ Z(2)^0, Z(2)^0, 0*Z(2) ] ]
sage: %timeit M_gap._matrix_(F)
10 loops, best of 3: 22.3 ms per loop
sage: %timeit M_libgap._matrix_(F)
1000 loops, best of 3: 902 µs per loop
```


I think that about speaks for itself.  Repeated experiments showed similar results.


---

Comment by embray created at 2019-03-25 10:56:15

Ticket retargeted after milestone closed (if you don't believe this ticket is appropriate for the Sage 8.8 release please retarget manually)


---

Comment by embray created at 2019-06-14 14:54:19

As the Sage-8.8 release milestone is pending, we should delete the sage-8.8 milestone for tickets that are not actively being worked on or that still require significant work to move forward.  If you feel that this ticket should be included in the next Sage release at the soonest please set its milestone to the next release milestone (sage-8.9).
