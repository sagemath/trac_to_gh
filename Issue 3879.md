# Issue 3879: Constructing a c_graph from a DiGraph doubles the edges.

Issue created by migration from Trac.

Original creator: saliola

Original creation time: 2008-08-16 08:49:18

Assignee: rlm

Keywords: c_graph


```
sage: D = DiGraph({0:[1]})
sage: D.edges()
[(0, 1, None)]
sage: DiGraph(D).edges()
[(0, 1, None)]
sage: DiGraph(D,implementation="c_graph").edges()
[(0, 1, None), (1, 0, None)]
```



---

Comment by saliola created at 2008-08-16 08:52:09

Resolution: duplicate


---

Comment by saliola created at 2008-08-16 08:52:09

Opps. Browser issues caused a re-submission. This is identical to #3878.
