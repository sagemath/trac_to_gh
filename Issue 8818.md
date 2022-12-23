# Issue 8818: Infinite loop in ZZ.range()

Issue created by migration from https://trac.sagemath.org/ticket/8818

Original creator: robertwb

Original creation time: 2010-04-29 07:06:09

Assignee: AlexGhitza


```
sage: ZZ.range(1r, 10r)
...
```



---

Comment by robertwb created at 2010-04-29 07:09:35

Changing status from new to needs_review.


---

Attachment

Looks like it was a typo in that function, easy fix.


---

Comment by leif created at 2010-04-29 10:31:34

Changing status from needs_review to positive_review.


---

Comment by leif created at 2010-04-29 10:31:34

Though I prefer the `trac_` prefix (and the bug doesn't necessarily end up in an infinite loop)... ;-)


---

Comment by leif created at 2010-04-29 10:31:34

Changing keywords from "" to "integer_ring, IntegerRing, range()".


---

Comment by mvngu created at 2010-05-08 21:31:54

Resolution: fixed
