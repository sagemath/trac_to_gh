# Issue 8260: valuation of zero is wrong for Qq

Issue created by migration from https://trac.sagemath.org/ticket/8260

Original creator: dmharvey

Original creation time: 2010-02-14 02:25:43

Assignee: roed

CC:  roed robertwb

This is ok:


```
sage: K = Qp(5)
sage: x = K(0)
sage: x.valuation()
+Infinity
```


This is bad:


```
sage: K.<a> = Qq(25)
sage: x = K(0)
sage: x.valuation()
1073741823
```




---

Comment by robertwb created at 2010-02-21 03:40:44

Changing status from new to needs_review.


---

Attachment

There were inconsistent definitions of maxordp.


---

Comment by roed created at 2010-02-21 18:27:29

Yep, that should do it.  Doctests all pass.


---

Comment by roed created at 2010-02-21 18:27:29

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-03 14:47:14

Resolution: fixed
