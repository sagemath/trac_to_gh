# Issue 3025: Sparse vector spaces don't cast on assignment.

Issue created by migration from https://trac.sagemath.org/ticket/3025

Original creator: boothby

Original creation time: 2008-04-25 20:57:56

Assignee: was


```
sage: V = VectorSpace(GF(2),10, sparse=True)
sage: w = V(0)
sage: w[0] = 2
sage: print w[0]
2
sage: print type(w[0])
<type 'sage.rings.integer.Integer'>
```




---

Attachment

this fixes the bug!


---

Comment by boothby created at 2008-04-25 21:23:56

works for me


---

Comment by mabshoff created at 2008-04-25 23:32:07

Merged in Sage 3.0.1.alpha0


---

Comment by mabshoff created at 2008-04-25 23:32:07

Resolution: fixed
