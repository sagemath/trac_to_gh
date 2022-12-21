# Issue 3747: incorrect power in modular arithmetic

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2008-07-30 14:14:21

Assignee: somebody


```
sage: R = Integers(17^5)
sage: R(17)^5
1419857
```


The answer should be zero.



---

Attachment


---

Comment by was created at 2008-07-30 14:37:05

looks good!


---

Comment by cremona created at 2008-07-30 23:13:10

Looks good to me too.  I note that only the 32-bit code had this bug, not the 64-bit code.


---

Comment by mabshoff created at 2008-07-30 23:15:51

Resolution: fixed


---

Comment by mabshoff created at 2008-07-30 23:15:51

Merged in Sage 3.1.alpha0
