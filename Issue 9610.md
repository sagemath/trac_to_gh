# Issue 9610: int(finite field element) should only work when it is in the prime subfield

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2010-07-27 12:01:24

Assignee: was

CC:  malb

This was the real cause of #8406, and the fix there introduced the following bug:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: n = 20
sage: k = 3
sage: g = DiGraph()
sage: g.add_edges( (i,Mod(i+j,n)) for i in range(n) for j in range(1,k+1) )
sage: g.vertices()
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
sage: g.strongly_connected_components()
[[0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]
```



---

Attachment


---

Comment by malb created at 2010-07-27 12:25:36

Looks good.


---

Comment by malb created at 2010-07-27 12:25:36

Changing status from new to needs_review.


---

Comment by malb created at 2010-07-27 12:25:44

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-09 09:40:36

Resolution: fixed
