# Issue 7674: fix bug in c_graph backends in_degree and out_degree

Issue created by migration from https://trac.sagemath.org/ticket/7674

Original creator: rlm

Original creation time: 2009-12-12 20:27:53

Assignee: rlm

CC:  ncohen

This was still using the old check to see whether a vertex was in the graph.


---

Comment by rlm created at 2009-12-12 20:28:15

Changing status from new to needs_review.


---

Attachment


---

Comment by ncohen created at 2009-12-13 10:52:39

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2009-12-13 10:52:39

Well done ! Positive review :-)


---

Comment by mhansen created at 2009-12-14 16:04:11

Resolution: fixed
