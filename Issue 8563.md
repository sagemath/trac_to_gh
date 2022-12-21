# Issue 8563: R interpreter starts (seemingly) without reason

Issue created by migration from Trac.

Original creator: rishi

Original creation time: 2010-03-20 01:48:46

Assignee: burcin

CC:  mhansen


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: var('r')
r
sage: simplify((r-1)^3 *r)
(r - 1)^3*r
sage: quit
Exiting SAGE (CPU time 0m0.08s, Wall time 0m32.87s).
Exiting spawned R Interpreter process.
Exiting spawned Maxima process.
```



---

Comment by burcin created at 2010-04-05 18:27:48

This is a duplicate of #7661. After applying the patch attached to that ticket we get the response from `simplify()` faster and there is no R interpreter on exit.


---

Comment by burcin created at 2010-04-05 18:27:48

Resolution: duplicate
