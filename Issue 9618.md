# Issue 9618: Slight improvement to vertex_coloring

Issue created by migration from https://trac.sagemath.org/ticket/9618

Original creator: ncohen

Original creation time: 2010-07-28 04:00:50

Assignee: jason, ncohen, rlm

We know that the chromatic number of a graph is more than its number of vertices divided by te size of its maximum independent set.

Sage did not.

Computations of max clique/independent set are way faster than coloring thanks to Cliquer, by the way !

Nathann


---

Attachment


---

Comment by ncohen created at 2010-07-28 04:08:12

Changing status from new to needs_review.


---

Comment by rlm created at 2010-11-26 16:58:16

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-12-02 16:09:18

Resolution: fixed
