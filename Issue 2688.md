# Issue 2688: Kuratowski subgraph isolator for planarity checking

Issue created by migration from https://trac.sagemath.org/ticket/2688

Original creator: rlm

Original creation time: 2008-03-27 20:54:59

Assignee: rlm




---

Attachment


---

Comment by rlm created at 2008-03-29 17:21:49

Passes all tests after applying cleanly to 2.11.alpha1. I'll give it a try on alpha2 once it finishes building.


---

Comment by mabshoff created at 2008-03-29 18:28:24

Well, against my 2.11.rc0 build I got the following doctest failure:

```
sage -t  devel/sage-main/sage/graphs/graph.py
**********************************************************************
File "graph.py", line 1695:
    sage: cube.is_circular_planar()
Expected:
    False
Got:
    (False, Graph on 9 vertices)
**********************************************************************
```

It seems easy enough to fix. Care to update the patch?

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-03-29 21:54:43

Resolution: fixed


---

Comment by mabshoff created at 2008-03-29 21:54:43

Merged 2688-kuratowski-isolator.patch and 2688-fix.patch in Sage 2.11.rc0
