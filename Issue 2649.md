# Issue 2649: [with patch, needs review] matrix() constructor fails to find ring for empty dict

Issue created by migration from https://trac.sagemath.org/ticket/2649

Original creator: rhinton

Original creation time: 2008-03-22 19:26:58

Assignee: was

Try the following:

```
sage: D = {}
sage: matrix(D)
```

Currently this throws an exception.  With this patch, it returns [0] when it should return [].  I don't know how to fix this, so I will open a separate ticket.


---

Comment by rhinton created at 2008-03-23 02:17:49

Resolution: duplicate


---

Attachment

subsumed by #2651
