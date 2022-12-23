# Issue 1860: arrow -- 2d plot truncates badly

Issue created by migration from https://trac.sagemath.org/ticket/1860

Original creator: was

Original creation time: 2008-01-20 02:24:47

Assignee: was

Try

```
sage: arrow((0,1), (2,3))
```

The top of the arrow is completely not visible.  It's like 1/2 a unit off the screen.  Terrible. 


---

Comment by jason created at 2008-10-18 03:59:40

This works now (3.1.3), so should be closed.


---

Comment by mabshoff created at 2008-10-18 09:05:18

Resolution: fixed


---

Comment by mabshoff created at 2008-10-18 09:05:18

Closed due to fixes via other tickets. Thanks Jason.

Cheers,

Michael
