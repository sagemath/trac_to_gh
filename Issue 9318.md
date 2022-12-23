# Issue 9318: Fix S-Box CNF generation for non permutations

Issue created by migration from https://trac.sagemath.org/ticket/9318

Original creator: malb

Original creation time: 2010-06-23 15:41:09

Assignee: AlexGhitza

This should work:


```python
sage: o = range(8) + range(8)
sage: shuffle(o)
sage: S = mq.SBox(o)
sage: S.is_permutation()
False

sage: len(S.cnf()) == 3*2^4
True
```




---

Attachment


---

Comment by ylchapuy created at 2010-06-28 21:47:06

Applies fine to sage-4.5.alpha0, and does the job. If it was "needs_review" I would give a positive one...


---

Comment by malb created at 2010-06-29 10:19:36

Changing status from new to needs_review.


---

Comment by malb created at 2010-06-29 10:20:30

Changing status from needs_review to positive_review.


---

Comment by malb created at 2010-06-29 10:20:30

sorry, my bad


---

Comment by mpatel created at 2010-07-20 09:30:00

Resolution: fixed
