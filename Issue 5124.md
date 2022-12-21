# Issue 5124: xmin ignored when plotting elliptic curves

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-01-28 23:15:08

Assignee: was


This doesn't depend on xmin!?


```
E = EllipticCurve('37a')
E.plot(xmin=-10, xmax=10)
```



---

Comment by rws created at 2014-04-10 17:11:25

Changing status from new to needs_review.


---

Comment by rws created at 2014-04-10 17:11:25

duplicate of #13368 (where more information is available)


---

Comment by pbruin created at 2014-04-11 00:39:19

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-04-12 07:35:04

Resolution: duplicate
