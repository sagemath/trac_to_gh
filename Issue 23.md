# Issue 23: (Z/nZ)^k problem

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-09-12 23:22:28

Assignee: somebody

maybe adding elements of (Z/nZ)^k is broken if one isn't in there.
   See line 66 of free_module_element.py


---

Comment by was created at 2007-01-13 02:02:02

Resolution: fixed


---

Comment by was created at 2007-01-13 02:02:02

This works fine now (I'm not really sure what the error is from the error report).


```
sage: V = Integers(18)^3
sage: a = V([1,2,3])
sage: a+a
(2, 4, 6)
```

