# Issue 8932: Shortest circuit in digraphs

Issue created by migration from https://trac.sagemath.org/ticket/8932

Original creator: ncohen

Original creation time: 2010-05-08 15:51:09

Assignee: jason, ncohen, rlm

** Update the multiflow method
 * replace topological_sort to use Sage instead of NetworkX


---

Comment by ncohen created at 2010-06-06 11:01:03

Changing status from new to needs_work.


---

Comment by dcoudert created at 2021-10-01 17:01:25

Changing status from needs_work to positive_review.


---

Comment by dcoudert created at 2021-10-01 17:01:25

Since #28142, we have a bfs based algorithm to compute the girth of directed graphs, and so to find the shortest circuit.

So we can close this ticket.


---

Comment by mkoeppe created at 2021-10-04 23:44:13

Resolution: invalid
