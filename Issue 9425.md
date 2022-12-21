# Issue 9425: bug in kernel_on() in "matrix2.pyx"

Issue created by migration from Trac.

Original creator: GeorgSWeber

Original creation time: 2010-07-04 21:31:40

Assignee: jason, was


```
sage: V = span([[1/7,0,0] ,[0,1,0]], ZZ); V
Free module of degree 3 and rank 2 over Integer Ring
Echelon basis matrix:
[1/7   0   0]
[  0   1   0]
sage: T = matrix(ZZ,3,[1,0,0,0,0,0,0,0,0]); T
[1 0 0]
[0 0 0]
[0 0 0]
sage: W = T.kernel_on(V); W.basis()
[
(0, 1, 0)
]
sage: W.is_submodule(V)
False
```

This is surprising, isn't it? (Patch comes up in a minute, but I need to create the ticket first.)


---

Attachment

created against the older Sage-4.4.2, but that shouldn't matter


---

Comment by GeorgSWeber created at 2010-07-04 21:46:26

Changing status from new to needs_review.


---

Comment by was created at 2010-07-05 10:53:16

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-07-05 10:53:16

Looks good to me.  Thanks!


---

Comment by mpatel created at 2010-07-20 08:21:11

Resolution: fixed
