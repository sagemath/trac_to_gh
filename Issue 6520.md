# Issue 6520: [with patch, needs work] Implement cached_function with weakref cache

Issue created by migration from https://trac.sagemath.org/ticket/6520

Original creator: nthiery

Original creation time: 2009-07-13 06:16:28

Assignee: cwitty

CC:  sage-combinat roed simonking

Keywords: cached function, weakref




---

Comment by nthiery created at 2009-07-13 06:22:25

Changing assignee from cwitty to nthiery.


---

Comment by nthiery created at 2009-07-13 06:22:25

Changing status from new to assigned.


---

Comment by nthiery created at 2009-07-13 06:22:25

Changing type from defect to enhancement.


---

Attachment


---

Comment by mmezzarobba created at 2014-02-11 15:05:53

Changing status from needs_work to needs_review.


---

Comment by mmezzarobba created at 2014-02-11 15:05:53

Done in #12215?


---

Comment by SimonKing created at 2014-02-11 15:17:49

Replying to [comment:3 mmezzarobba]:
> Done in #12215?

I think so.


---

Comment by tscrim created at 2014-02-11 19:49:55

This is the same feature as ``@`weak_cached_method` from #12215.


---

Comment by tscrim created at 2014-02-11 19:49:55

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-02-11 21:21:39

Resolution: fixed
