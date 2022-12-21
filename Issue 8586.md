# Issue 8586: Integer overflow in vector_space_dimension()

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2010-03-23 11:29:29

Assignee: malb


```python
sage: P.<x> = PolynomialRing(GF(32003),1)
sage: sage.rings.ideal.FieldIdeal(P).vector_space_dimension()
32003

sage: P.<x,y> = PolynomialRing(GF(32003),2)
sage: sage.rings.ideal.FieldIdeal(P).vector_space_dimension()
1024192009

sage: P.<x,y,z> = PolynomialRing(GF(32003),3)
sage: sage.rings.ideal.FieldIdeal(P).vector_space_dimension()
-1973539045 # 2^32 - (32003^3) % 2^32 == 1973539045
```



---

Comment by malb created at 2010-03-23 11:32:39

The *Reported upstream* field makes it sound so negative ("little or no feedback"), so to clarify: I just now reported this bug upstream at

   http://www.singular.uni-kl.de:8002/trac/ticket/218


---

Comment by @kliem created at 2020-05-27 19:32:35

Changing status from new to needs_review.


---

Comment by @kliem created at 2020-05-27 19:32:35

With #29746 I would vote to close this ticket.

The bug is reported upstream, we have documented it. There is already a ticket for it on the singular trac.


---

Comment by @kliem created at 2020-05-27 19:32:35

Changing keywords from "" to "sd109".


---

Comment by mmezzarobba created at 2021-09-18 09:47:22

Changing status from needs_review to positive_review.


---

Comment by mkoeppe created at 2021-09-18 17:51:47

Resolution: invalid
