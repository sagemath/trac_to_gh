# Issue 176: sagex -- add support for the "//" --> floordiv operator

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-12-02 23:36:36

Assignee: was




---

Comment by mabshoff created at 2007-08-22 19:53:48

Hello,

I have the impression this works unless I misunderstood the definition of the floordiv operator. From Sage 2.8.2

```
sage: 12//6
2
sage: 13//6
2
sage: 18//6
3
```


Can anyone confirm this?

Cheers,

Michael


---

Comment by was created at 2007-08-23 05:47:04

Resolution: fixed


---

Comment by was created at 2007-08-23 05:47:04

This works in cython.
