# Issue 7945: Class groups of number fields: an_element() not in self

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2010-01-16 12:28:51

Assignee: davidloeffler


```
sage: K.<a> = NumberField(x^2 + 23)
sage: G = K.class_group(); G
Class group of order 3 with structure C3 of Number Field in a with defining polynomial x^2 + 23
sage: G.an_element() in G
False
```


Catched with #7921.


---

Comment by davidloeffler created at 2010-06-29 11:24:18

This is fixed by my patch at #9244.


---

Comment by davidloeffler created at 2010-06-29 11:24:18

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2010-06-29 11:25:05

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2010-06-29 11:25:05

I'm setting this to "positive review" to bring it to the attention of the release maintainer.


---

Comment by mpatel created at 2010-07-20 07:52:02

Resolution: duplicate


---

Comment by mpatel created at 2010-07-20 07:52:02

I'm resolving this ticket as a "duplicate."
