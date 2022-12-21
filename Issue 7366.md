# Issue 7366: fix GF(4,'a').list()

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-11-01 00:11:13

Assignee: AlexGhitza

This should work:


```python
sage: K.<a>=GF(4)
sage: [x for x in K]
[0, a, a + 1, 1]
sage: hasattr(K, '__iter__')
True
sage: K.list()
...
TypeError:
'sage.rings.finite_field_givaro.FiniteField_givaro_iterator' object is not iterable

```



---

Attachment


---

Comment by malb created at 2009-11-01 00:11:43

Changing status from new to needs_review.


---

Comment by rbeezer created at 2009-11-01 03:47:48

Changing status from needs_review to positive_review.


---

Comment by rbeezer created at 2009-11-01 03:47:48

Builds on 4.2, fixes the problem, passes all tests.

Positive review.


---

Comment by mhansen created at 2009-11-01 04:47:08

Resolution: fixed
