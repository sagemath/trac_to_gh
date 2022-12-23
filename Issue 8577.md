# Issue 8577: Fix ETuple.eadd_p

Issue created by migration from https://trac.sagemath.org/ticket/8577

Original creator: malb

Original creation time: 2010-03-22 11:51:35

Assignee: AlexGhitza

CC:  mjo

This should return `True` not `False` (reported by
Michael Bachtold)


```python
sage: from sage.rings.polynomial.polydict import ETuple
sage: ETuple([0,1]).eadd_p(1, 0)==ETuple([1,1])
```




---

Attachment


---

Comment by mjo created at 2012-01-16 03:16:56

Changing status from new to needs_review.


---

Comment by mhansen created at 2012-03-28 21:49:09

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2012-03-28 21:49:09

Looks good to me.


---

Comment by jdemeyer created at 2012-04-19 06:43:57

Resolution: fixed
