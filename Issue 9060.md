# Issue 9060: break symmetries in subgraph search

Issue created by migration from https://trac.sagemath.org/ticket/9060

Original creator: ncohen

Original creation time: 2010-05-26 22:37:24

Assignee: jason, ncohen, rlm

Useless, when looking for a triangle, to test both abc, bca, and cab. The same is true when looking for Cycles, for complete graphs, etc...

There may be a way to generally deal with those symmetries to improve the speed of subgraph search.

If not, it is still possible to manually improve it for cycles, complete graphs, and other "common" graphs.

Nathann


---

Comment by ncohen created at 2010-06-06 11:01:16

Changing status from new to needs_work.
