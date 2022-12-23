# Issue 7601: Graph.edge_connectivity

Issue created by migration from https://trac.sagemath.org/ticket/7601

Original creator: ncohen

Original creation time: 2009-12-04 08:42:25

Assignee: rlm

As the title says, this patch implements the function edge_connectivity for Graphs.


---

Comment by ncohen created at 2009-12-04 08:42:31

Changing status from new to needs_review.


---

Comment by rlm created at 2009-12-15 17:53:50

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2009-12-15 17:53:50

same as #7594 and #7599 - more doctests!


---

Comment by ncohen created at 2009-12-16 01:20:54

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2009-12-16 01:20:54

updated !


---

Comment by rlm created at 2009-12-16 03:18:21

The point of doctests is partially to test each use case of a function. This function has three different inputs, and all of your tests use the default value. This isn't testing certain code paths in your function, and if someone messed up that part in a future patch, the tests as is wouldn't catch them. Please check and make sure you're testing each case.


---

Comment by rlm created at 2009-12-16 03:18:21

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by ncohen created at 2009-12-16 10:50:06

Updated !! :-)


---

Comment by ncohen created at 2009-12-16 10:50:06

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2009-12-16 18:25:27

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-19 20:35:32

Resolution: fixed
