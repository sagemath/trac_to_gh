# Issue 3878: Constructing a c_graph from a DiGraph doubles the edges.

Issue created by migration from Trac.

Original creator: saliola

Original creation time: 2008-08-16 08:30:54

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

Attachment


---

Comment by rlm created at 2008-08-16 09:29:42

D'OH


---

Comment by mabshoff created at 2008-08-16 21:49:26

Resolution: fixed


---

Comment by mabshoff created at 2008-08-16 21:49:26

Merged in Sage 3.1.final
