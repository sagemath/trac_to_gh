# Issue 1727: truth value of inequalities not as expected

Issue created by migration from Trac.

Original creator: wjp

Original creation time: 2008-01-09 00:47:29

Assignee: was

As reported by ncalexan on IRC:


```
sage: bool(x == x)
True
sage: bool(x != x)
True
sage: bool(x > x)
True
```


This appears to be caused by `SymbolicEquation.__nonzero__()` assuming in various places that the operator of the equation is ==.


---

Comment by was created at 2008-01-09 04:16:10

This is really serious.


---

Comment by was created at 2008-01-09 04:16:10

Changing priority from major to critical.


---

Comment by mhansen created at 2008-01-16 04:54:52

Changing assignee from was to mhansen.


---

Attachment


---

Comment by mhansen created at 2008-01-16 04:54:52

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-01-16 05:09:34

Looks good to me.


---

Comment by mabshoff created at 2008-01-16 05:16:45

Merged in Sage 2.10.alpha4


---

Comment by mabshoff created at 2008-01-16 05:16:45

Resolution: fixed
