# Issue 5654: [with patch, needs review] Boundary/interior points of vertices were computed wrong.

Issue created by migration from Trac.

Original creator: novoselt

Original creation time: 2009-04-01 02:00:01

Assignee: mhampton

This is wrong:

```
sage: ReflexivePolytope(2,0).faces(dim=0)[0].nboundary_points()
1
```

because vertices do not have boundary points. 

The patch fixes the function that caused this error.


---

Attachment

This passes doctests, and is a simple change that makes sense to me.


---

Comment by mabshoff created at 2009-04-15 00:55:17

Resolution: fixed


---

Comment by mabshoff created at 2009-04-15 00:55:17

Merged in Sage 3.4.1.rc3.

Cheers,

Michael
