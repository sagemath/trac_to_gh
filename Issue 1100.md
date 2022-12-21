# Issue 1100: polynomial roots() method can return rational roots for polynomials over ZZ

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-11-04 04:28:28

Assignee: cwitty

According to the documentation, .roots() is only supposed to return values from the base ring, so this is a bug:


```
sage: x = polygen(ZZ)
sage: f = 2*x-3
sage: f.roots()
[(3/2, 1)]
```




---

Attachment


---

Comment by cwitty created at 2007-11-04 04:52:00

This patch was developed after #995, and may not apply cleanly if the patch from #995 has not yet been applied.


---

Comment by mabshoff created at 2007-11-06 21:46:21

applied to 2.8.12.rc0


---

Comment by mabshoff created at 2007-11-06 21:46:21

Resolution: fixed
