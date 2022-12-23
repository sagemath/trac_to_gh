# Issue 6394: Fix fallout from removal of graph_isom in 4.1.alpha1

Issue created by migration from https://trac.sagemath.org/ticket/6394

Original creator: rlm

Original creation time: 2009-06-24 11:56:39

Assignee: rlm

These are the failing tests:

```
        sage -t  devel/sage-main/sage/databases/database.py # 20 doctests failed
        sage -t  devel/sage-main/sage/geometry/polyhedra.py # 1 doctests failed
        sage -t  devel/sage-main/sage/graphs/graph.py # 25 doctests failed

```



---

Comment by rlm created at 2009-06-24 19:26:57

Changing priority from critical to blocker.


---

Attachment


---

Comment by boothby created at 2009-06-25 17:49:40

works for me


---

Comment by rlm created at 2009-06-25 17:53:06

Resolution: fixed
