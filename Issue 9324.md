# Issue 9324: bug in Tate's algorithm over number fields

Issue created by migration from https://trac.sagemath.org/ticket/9324

Original creator: cremona

Original creation time: 2010-06-24 05:39:36

Assignee: cremona

CC:  robertwb rlm


```
sage: K.<a> = NumberField(x^2-x+6)
sage: K.disc()
-23
sage: E = EllipticCurve([0,0,0,-53160*a-43995,-5067640*a+19402006])
sage: E.conductor()
[boom!]
```




---

Comment by cremona created at 2010-06-24 06:26:23

Applies to 4.4.4.alpha1


---

Attachment


---

Comment by cremona created at 2010-06-24 06:27:44

Changing status from new to needs_review.


---

Comment by rlm created at 2010-06-24 17:41:12

Works as advertised.


---

Comment by rlm created at 2010-06-24 17:41:12

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-20 07:13:36

Resolution: fixed
