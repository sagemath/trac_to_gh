# Issue 255: hilarious bug in p-adics

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2007-02-09 21:38:10

Assignee: somebody


```
sage: pAdicField(5)(10000, 2)
 0.04*5^4 + O(5^2)
```




---

Comment by roed created at 2007-05-20 04:06:35

This is fixed by the new p-adics.


---

Comment by roed created at 2007-05-20 04:06:35

Resolution: fixed
