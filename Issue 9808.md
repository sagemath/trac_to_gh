# Issue 9808: Graph.num_edges() gives wrong answer

Issue created by migration from Trac.

Original creator: tobiasljohnson

Original creation time: 2010-08-26 20:32:56

Assignee: someone

Keywords: num_edges,multiedges

If G is a graph with multiedges that contains two copies of an edge e, and you delete one of the copies, num_edges() doesn't go down by one.  For example,

```
sage: G = Graph(multiedges = True)
sage: G.add_edges([(0,1), (0,1)])
sage: G.delete_edge(0,1)
sage: G.num_edges()
2
sage: G.edges()
[(0, 1, None)]
```




---

Comment by tobiasljohnson created at 2010-08-26 20:35:10

Changing assignee from someone to somebody.


---

Comment by mvngu created at 2010-12-04 13:07:21

The problem is fixed at #8395.


---

Comment by jdemeyer created at 2010-12-05 11:45:06

Resolution: duplicate
