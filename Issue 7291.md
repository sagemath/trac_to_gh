# Issue 7291: Max Cut

Issue created by migration from https://trac.sagemath.org/ticket/7291

Original creator: ncohen

Original creation time: 2009-10-25 09:20:40

Assignee: rlm

Max cut is a NP-Hard problem, which could as usual be written as a LP if no better solution is found.

http://en.wikipedia.org/wiki/Maximum_cut


---

Comment by ncohen created at 2009-12-14 17:54:00

Changing status from new to needs_review.


---

Comment by rlm created at 2009-12-15 16:59:29

You should include more examples in your doctests. At least make sure that each input is tested. For example:

```
sage: g.max_cut(vertices=True)
30.0
```

Shouldn't this be returning two sets of vertices?


---

Comment by rlm created at 2009-12-15 16:59:29

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2009-12-16 11:28:59

I had forgotten the implication : vertices=True => value_only=True :-)

Updated !


---

Comment by ncohen created at 2009-12-16 11:28:59

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by rlm created at 2009-12-16 18:36:15

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-19 22:53:05

Resolution: fixed
