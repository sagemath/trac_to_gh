# Issue 7359: Methods for degenerated graphs

Issue created by migration from https://trac.sagemath.org/ticket/7359

Original creator: ncohen

Original creation time: 2009-10-31 08:53:48

Assignee: rlm

A graph is said to be k-degenerated if it can be totally decomposed by successively removing vertices of degree <= k.

There should be in Sage a function answering if a graph is k-degenerated, and in this case giving the order in which the vertices should be deleted.


---

Comment by ncohen created at 2010-06-06 11:00:35

Changing status from new to needs_work.


---

Comment by ncohen created at 2010-10-09 08:33:05

This is exactly what the recently-reviewed #9058 does.

Nathann


---

Comment by mpatel created at 2010-10-09 08:43:39

Resolution: duplicate
