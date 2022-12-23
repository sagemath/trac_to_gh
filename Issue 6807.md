# Issue 6807: bug in blocks_and_cut_vertices() of a graph where a cut vertex can be listed more than once

Issue created by migration from https://trac.sagemath.org/ticket/6807

Original creator: hartke

Original creation time: 2009-08-22 21:30:28

Assignee: rlm

CC:  rlm jason

There is another bug in blocks_and_cut_vertices() where cut vertices can appear more than once in the returned list of cut vertices.  Jason Grout pointed out this problem in ticket [#6632](http://trac.sagemath.org/sage_trac/ticket/6632#comment:5).


```
sage: graphs.StarGraph(3).blocks_and_cut_vertices()
([[1, 0], [2, 0], [3, 0]], [0, 0, 0])
```


The problem occurs because the list C of cut vertices should be treated as a set, not a list: membership should be tested before adding a vertex to the list.

Following a suggestion of Jason's, I also changed the initialization of the parent array to None.

Patch will be attached below.



---

Comment by hartke created at 2009-08-22 21:35:42

Patch to fix bug in blocks_and_cut_vertices() in graph.py where cut vertices are repeated.


---

Attachment


---

Comment by ncohen created at 2009-08-25 15:00:15

Applies ok, fixes the bug... ;-)


---

Comment by mvngu created at 2009-08-25 22:25:44

Resolution: fixed
