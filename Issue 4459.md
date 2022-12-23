# Issue 4459: preparser incorrectly identifies integer methods that start with e

Issue created by migration from https://trac.sagemath.org/ticket/4459

Original creator: mhansen

Original creation time: 2008-11-07 03:19:02

Assignee: cwitty


```
sage: 3.exp()
------------------------------------------------------------
   File "<ipython console>", line 1
     RealNumber('3.e')xp()
                       ^
SyntaxError: invalid syntax

sage: 3.is_square()
False
```




---

Comment by mhansen created at 2008-11-07 03:21:09

The same thing happens for those that start with 'r':


```
sage: 3.rational_reconstruction()
------------------------------------------------------------
   File "<ipython console>", line 1
     3.ational_reconstruction()
```



---

Comment by boothby created at 2009-01-23 22:30:40

Resolution: duplicate


---

Comment by boothby created at 2009-01-23 22:30:40

Rolled into #5079
