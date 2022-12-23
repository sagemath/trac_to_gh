# Issue 7077: variables() inconsistently returns a list or tuple

Issue created by migration from https://trac.sagemath.org/ticket/7077

Original creator: jason

Original creation time: 2009-09-29 19:51:09

Assignee: tbd

CC:  mhansen

with 4.1.1:


```
sage: x,y,z=polygens(QQ,'x,y,z')
sage: (x^2).variables()
[x]
sage: x=polygen(QQ)
sage: (x^2).variables()
(x,)
```



---

Attachment

There are a number of methods called `variables()` in the Sage library.  The attached patch makes sure that all of them return tuples.  (This is what univariate polynomials, and symbolics return.)


---

Comment by AlexGhitza created at 2009-10-19 23:38:29

Changing status from new to needs_review.


---

Comment by kcrisman created at 2009-10-20 06:06:09

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2009-10-20 06:06:09

Seems to perform as advertised, passes relevant tests, as far as I can tell catches all the cases.  Positive review.


---

Comment by mhansen created at 2009-10-21 04:21:37

Resolution: fixed
