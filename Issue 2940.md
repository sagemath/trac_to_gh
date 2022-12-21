# Issue 2940: symbolic equation arithmetic is to restrictive

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-04-16 09:07:51

Assignee: was

The following should all work 


```
sage: var('x,y')
(x, y)
sage: (a < 1) + (b < 2)
b + a < 3
sage: (a < 1) + (b <= 2)
a + b < 3
sage: (a <= 1) + (b == 2)
a + b <= 3
```



---

Comment by AlexGhitza created at 2009-01-22 18:21:14

Changing type from defect to enhancement.


---

Comment by burcin created at 2009-06-10 11:17:12

This can be closed as fixed. 

Support for this was added by Robert during the symbolics push before 4.0. There are similar doctests to the ones in the description in sage/symbolic/expression.pyx lines 1526 and 6006.


---

Comment by rlm created at 2009-06-24 15:15:58

Resolution: fixed
