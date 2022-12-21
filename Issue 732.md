# Issue 732: graphs: enum changes behavior depending on boundary vertices

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-09-21 19:03:06

Assignee: was

Keywords: graphs

The enum() function for graphs will change behavior depending on if the boundary is set and if 'quick' is passed.


```
sage: from sage.graphs.graph import enum
sage: g=Graph({0:[1,2],1:[3]})
sage: g.set_boundary([1])
sage: enum(g)
23112
sage: enum(g,quick=True)
27012
```


This unexpected behavior happens because g.vertices() returns the boundary vertices first, I think.


---

Comment by jason created at 2007-10-13 16:58:09

Resolution: fixed


---

Comment by jason created at 2007-10-13 16:58:09

This works now that vertices() sorts the vertices it returns (as of 2.8.6, I believe).
