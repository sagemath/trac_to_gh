# Issue 1709: [with patch] Make experimental jmol graph plotting work

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-01-07 09:09:18

Assignee: rlm

For example, you can do

```
sage: G = graphs.DodecahedralGraph()
sage: G.plot3d_new()
```


This still needs to be cleaned up, but at least now it works instead of giving confusing errors.


---

Attachment

Yep, I've been using this and it works great.


---

Comment by mabshoff created at 2008-01-08 23:20:58

Resolution: fixed


---

Comment by mabshoff created at 2008-01-08 23:20:58

Merged in Sage 2.10.alpha1.
