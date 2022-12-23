# Issue 968: graph_isom: memory management, legibility

Issue created by migration from https://trac.sagemath.org/ticket/968

Original creator: rlm

Original creation time: 2007-10-22 01:22:09

Assignee: rlm

These are a few changesets to increase readability and eliminate some pointer arithmetic in memory allocation.


---

Comment by rlm created at 2007-10-22 01:23:12

Changing type from defect to enhancement.


---

Attachment


---

Comment by rlm created at 2007-10-22 01:24:33

I should mention I found another bug like #939 when I cleaned up the allocation, too.


---

Attachment

This should be patched on top of the bundle...


---

Comment by malb created at 2007-10-23 22:18:11

applied to 2.8.9.alpha0


---

Comment by malb created at 2007-10-23 22:18:11

Resolution: fixed
