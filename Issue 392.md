# Issue 392: round() ignores the innate precision of a real number

Issue created by migration from Trac.

Original creator: jonhanke

Original creation time: 2007-06-28 06:03:57

Assignee: was

Keywords: round, real, arithmetic

The function round() seems to ignore precision information slightly beyond the default 53 bits for a real number.  This leads to some incorrect rounding results for close calls.


```
sage: a = 5.499999999999999 
sage: a.prec()
56
sage: round(a)  ## This is ok
5.0

sage: b = 5.4999999999999999
sage: b.prec()
59
sage: round(b)  ## This isn't ok 
6.0
```



---

Comment by jonhanke created at 2007-06-28 06:04:37

Changing keywords from "round, real, arithmetic" to "round, real, precision, arithmetic".


---

Comment by was created at 2007-08-18 22:25:01

Resolution: fixed
