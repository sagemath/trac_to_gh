# Issue 6960: silly inconsistency in pari versus magma interface

Issue created by migration from https://trac.sagemath.org/ticket/6960

Original creator: was

Original creation time: 2009-09-19 06:13:32

Assignee: was


```
sage: a = pari('393')
sage: a.python()
393
sage: a = magma('393')
sage: a.sage()
393     
```



---

Attachment


---

Comment by was created at 2010-01-19 06:36:02

Changing status from new to needs_review.


---

Comment by rlm created at 2010-01-19 06:49:49

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-19 06:50:00

Resolution: fixed
