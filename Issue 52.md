# Issue 52: O(5) prints as "0"

Issue created by migration from https://trac.sagemath.org/ticket/52

Original creator: dmharvey

Original creation time: 2006-09-13 19:04:57

Assignee: somebody


```
sage: O(5)
 0
```


Perhaps it would be better if it printed as `0 + O(5)`. Especially because otherwise there's no way to tell the difference between O(5) and O(25).



---

Comment by was created at 2007-01-13 02:11:55

Fixed.

```
sage: O(5)
O(5^1)
```



---

Comment by was created at 2007-01-13 02:11:55

Resolution: fixed
