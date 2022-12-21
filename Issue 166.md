# Issue 166: incorrect wrapping for modular arithmetic negation

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2006-11-01 22:55:52

Assignee: somebody


```
sage: -Mod(0, 5)
 5
```




---

Attachment

patch that fixes the bug


---

Comment by was created at 2006-11-06 07:44:42

Resolution: fixed


---

Comment by was created at 2006-11-06 07:44:42

I fixed this.  See attached patch.
