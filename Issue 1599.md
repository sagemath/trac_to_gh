# Issue 1599: another preparser edge case

Issue created by migration from https://trac.sagemath.org/ticket/1599

Original creator: dmharvey

Original creation time: 2007-12-26 15:21:56

Assignee: cwitty


```
sage: 3.xgcd(0)
(3, 1, 0)
sage: 3._xgcd(0)
------------------------------------------------------------
   File "<ipython console>", line 1
     RealNumber('3.')_xgcd(Integer(0))
                         ^
<type 'exceptions.SyntaxError'>: invalid syntax
```




---

Comment by boothby created at 2009-01-23 22:30:24

Rolled into #5079


---

Comment by boothby created at 2009-01-23 22:30:24

Resolution: duplicate
