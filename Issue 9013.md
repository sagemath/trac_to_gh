# Issue 9013: Fix graph.loops() to not return all edges

Issue created by migration from https://trac.sagemath.org/ticket/9013

Original creator: boothby

Original creation time: 2010-05-21 21:19:23

Assignee: jason, ncohen, rlm


```
sage: G = graphs.PetersenGraph()
sage: G.loops()
[(0, 1, None), (0, 4, None), (0, 5, None), (0, 1, None), (1, 2, None),
(1, 6, None), (1, 2, None), (2, 3, None), (2, 7, None), (2, 3, None),
(3, 4, None), (3, 8, None), (0, 4, None), (3, 4, None), (4, 9, None),
(0, 5, None), (5, 7, None), (5, 8, None), (1, 6, None), (6, 8, None),
(6, 9, None), (2, 7, None), (5, 7, None), (7, 9, None), (3, 8, None),
(5, 8, None), (6, 8, None), (4, 9, None), (6, 9, None), (7, 9, None)]
```


...but... the Petersen graph is loop free...


---

Comment by rlm created at 2010-05-21 21:34:43

Changing status from new to needs_review.


---

Comment by boothby created at 2010-05-21 21:39:26

Changing status from needs_review to needs_work.


---

Comment by boothby created at 2010-05-21 21:39:26

No new doctests... please add some that verify that the problem has been fixed.


---

Comment by rlm created at 2010-05-21 21:44:00

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by boothby created at 2010-05-22 04:53:46

Several doctest failures when applied against 4.4.2 in attachment "out".


---

Comment by boothby created at 2010-05-22 04:53:46

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by rlm created at 2010-05-25 23:45:14

Try this one.


---

Comment by rlm created at 2010-05-25 23:45:14

Changing status from needs_work to needs_review.


---

Comment by boothby created at 2010-05-26 22:05:19

Changing status from needs_review to positive_review.


---

Comment by boothby created at 2010-05-26 22:05:19

Works for me.


---

Comment by mhansen created at 2010-06-06 07:05:29

Resolution: fixed
