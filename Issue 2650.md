# Issue 2650: matrix() constructor with empty dictionary returns non-empty matrix

Issue created by migration from Trac.

Original creator: rhinton

Original creation time: 2008-03-22 19:31:04

Assignee: was

This ticket depends on the patch from ticket #2649, without which an exception is raised.

The following code

```
sage: matrix({})
```

returns the matrix [0].  I think it should return [].


---

Comment by rhinton created at 2008-03-23 02:16:17

Resolution: duplicate


---

Comment by rhinton created at 2008-03-23 02:16:17

subsumed by #2651
