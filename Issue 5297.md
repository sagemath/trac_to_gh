# Issue 5297: [with patch, needs review] sparse vectors and free module elements: pairwise_product is broken

Issue created by migration from https://trac.sagemath.org/ticket/5297

Original creator: jhpalmieri

Original creation time: 2009-02-17 20:55:05

Assignee: jhpalmieri


```
sage: v = vector({1: 1, 3: -2})  
sage: w = vector({3: 3})       
sage: v
(0, 1, 0, -2)
sage: w
(0, 0, 0, 3)
sage: v.pairwise_product(w)
(0, 1, 0, -6)
sage: v.dense_vector().pairwise_product(w)
(0, 0, 0, -6)
```

(The last line illustrates that dense vectors seem to work okay.)



---

Attachment


---

Comment by mhansen created at 2009-02-18 00:02:23

Looks good to me.


---

Comment by mabshoff created at 2009-02-18 00:17:17

Resolution: fixed


---

Comment by mabshoff created at 2009-02-18 00:17:17

Merged in Sage 3.3.rc2.

Cheers,

Michael
