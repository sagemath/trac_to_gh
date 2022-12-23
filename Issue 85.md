# Issue 85: p-adic coercion incorrect for negative numbers

Issue created by migration from https://trac.sagemath.org/ticket/85

Original creator: dmharvey

Original creation time: 2006-09-26 19:23:17

Assignee: dmharvey


```
sage: pAdicField(5, 3)(-1)
 4 + 4*5 + 4*5^2 + O(5^Infinity)
```


I know where the bug is.... it's all my fault....



---

Comment by dmharvey created at 2006-09-26 19:31:29

I've fixed this (patch to be submitted soon), but the problem is deeper, it's not just to do with coercion, e.g.

```
sage: K = pAdicField(5, 3)
sage: K(2) - K(3)
 4 + 4*5 + 4*5^2 + O(5^Infinity)
```



---

Comment by dmharvey created at 2006-10-10 23:57:26

Resolution: fixed


---

Comment by dmharvey created at 2006-10-10 23:57:26

fixed in sage 1.4
