# Issue 8576: Categories for QQ, CC, RR and friends

Issue created by migration from https://trac.sagemath.org/ticket/8576

Original creator: nthiery

Original creation time: 2010-03-22 10:16:15

Assignee: AlexGhitza

CC:  sage-combinat

Keywords: categories, real fields

After this patch, QQ,ZZ,... inherit properly from categories: 


```
sage: QQ.category()
Category of fields
sage: TestSuite(QQ).run()
```


This patch also documents the following effect discovered by TestSuite:

```
    sage: CDF = ComplexDoubleField()
    sage: x = CDF.an_element()
    sage: x
    1.0*I
    sage: x*x, x**2, x*x == x**2
    (-1.0, -1.0 + 1.22460635382e-16*I, False)
```

This effect won't be touched by this patch. Should anyone consider this as a bug, please open a new ticket.


---

Attachment

All test passed for me.


---

Comment by nthiery created at 2010-03-22 22:25:55

Changing status from new to needs_review.


---

Comment by cremona created at 2010-04-05 14:09:50

Applies fine to 4.3.5 and all tests pass.


---

Comment by cremona created at 2010-04-05 14:09:50

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2010-04-06 05:56:00

Thanks for the review!


---

Comment by jhpalmieri created at 2010-04-16 18:49:06

Merged "trac_8576-category-QQ-RR-CC-nt.patch" in 4.4.alpha0


---

Comment by jhpalmieri created at 2010-04-16 18:49:06

Resolution: fixed
