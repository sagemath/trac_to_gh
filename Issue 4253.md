# Issue 4253: polybori interface: equality operator for navigators

Issue created by migration from https://trac.sagemath.org/ticket/4253

Original creator: PolyBoRi

Original creation time: 2008-10-08 06:42:41

Assignee: malb

Keywords: polybori


```
sage: r.<x,y>=BooleanPolynomialRing(2)

sage: p=r("0")
sage: p.navigation()==p.navigation()
False
```

Should be True, probably `__eq__` not implemented.

Michael


---

Attachment


---

Comment by PolyBoRi created at 2008-10-09 06:48:43

thanks, works :-)


---

Comment by mabshoff created at 2008-10-11 06:40:49

Resolution: fixed


---

Comment by mabshoff created at 2008-10-11 06:40:49

Merged in Sage 3.1.3.rc0
