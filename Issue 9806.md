# Issue 9806: merge_vertices behavior in a graph with loops

Issue created by migration from Trac.

Original creator: tobiasljohnson

Original creation time: 2010-08-26 18:41:52

Assignee: jason, ncohen, rlm

CC:  brunellus

Keywords: merge_vertices, loops

Suppose G is a graph with loops permitted containing the edge (0, 1).  I would expect that G.merge_vertices([0, 1]) would create a loop (0, 0), but it doesn't:

```
sage: G = Graph(loops = True)
sage: G.add_edge(0, 1)
sage: G.merge_vertices([0, 1])
sage: G.edges()
[]
```

I think either we should change this, or we should write explicitly in the documentation that merge_vertices doesn't create self-loops even when G allows them.




---

Comment by brunellus created at 2012-01-31 14:49:19

See #7304.
