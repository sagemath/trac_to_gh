# Issue 4773: determinants of non-square matrices over GF(p) (p odd) should raise an error -- instead they silently give nonsense

Issue created by migration from https://trac.sagemath.org/ticket/4773

Original creator: was

Original creation time: 2008-12-12 19:34:29

Assignee: was


```
sage: w = random_matrix(GF(3),3,4)
sage: w.determinant()
0
```



---

Attachment

Trivial patch is attached.


---

Comment by mabshoff created at 2008-12-13 06:29:07

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-13 09:36:19

Resolution: fixed


---

Comment by mabshoff created at 2008-12-13 09:36:19

Merged in Sage 3.2.2.alpha2
