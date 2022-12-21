# Issue 8628: confusing defaults for p-adic precision types

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2010-03-30 00:50:51

Assignee: roed

(sage 4.3.1)

absolute or relative is the default?


```
sage: R = Zp(5)
sage: R
5-adic Ring with capped relative precision 20
sage: R.<a> = Zq(25)
sage: R
Unramified Extension of 5-adic Ring with capped absolute precision 20 in a defined by (1 + O(5^20))*x^2 + (4 + O(5^20))*x + (2 + O(5^20))
sage: R = Zq(5)
sage: R
5-adic Ring with capped absolute precision 20
```




---

Comment by maurimo created at 2016-03-21 17:14:33

New commits:


---

Comment by maurimo created at 2016-03-21 17:14:33

Changing status from new to needs_review.


---

Comment by marmas created at 2016-03-22 21:14:50

Changing status from needs_review to positive_review.


---

Comment by jen created at 2016-03-26 14:53:47

Changing keywords from "" to "days71".


---

Comment by vbraun created at 2016-04-04 22:06:43

merge conflict, please merge in the next beta


---

Comment by vbraun created at 2016-04-04 22:06:43

Changing status from positive_review to needs_work.


---

Comment by roed created at 2016-11-17 23:08:12

Changing status from needs_work to needs_review.


---

Comment by roed created at 2016-11-17 23:08:12

This now merges.  
----
New commits:


---

Comment by git created at 2016-11-17 23:16:04

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by saraedum created at 2016-11-17 23:18:12

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2016-11-19 22:10:05

Resolution: fixed


---

Comment by roed created at 2016-11-20 00:53:20

Branch change was caused by a bug in the git-trac feature I'm working on.
