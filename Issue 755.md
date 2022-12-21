# Issue 755: graphs: adjacency_matrix() does not call multiple_edges correctly.

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-09-26 15:49:08

Assignee: was

Keywords: graphs

A line in adjacency_matrix() calls self.multiple_edges instead of self.multiple_edges(), causing adjacency_matrix() to never return a matrix over IntegerModRing(2), like it apparently was designed to return.  However, kirchhoff_matrix() relies on this bug, as it does a list(-M), where M is the adjacency matrix, which doesn't work when M is a binary matrix.  So kirchhoff_matrix() needs to be fixed (so it doesn't rely on the faulty behavior).


---

Comment by jason created at 2007-09-28 19:15:20


```
--- a/sage/graphs/graph.py      Fri Sep 28 13:48:48 2007 -0500
+++ b/sage/graphs/graph.py      Fri Sep 28 14:06:51 2007 -0500
`@``@` -3411,6 +3411,9 `@``@` class Graph(GenericGraph):
         represented by its position in the list returned by the vertices()
         function.

+        If the graph does not allow multiple edges, then the returned matrix is over
+        the ring with two elements, otherwise it is over the integers.
+
         EXAMPLE:
             sage: G = graphs.CubeGraph(4)
             sage: G.adjacency_matrix()
`@``@` -3448,7 +3451,7 `@``@` class Graph(GenericGraph):
         from sage.rings.integer_mod_ring import IntegerModRing
         from sage.rings.integer_ring import IntegerRing
         from sage.matrix.constructor import matrix
-        if self.multiple_edges:
+        if self.multiple_edges():
             R = IntegerRing()
         else:
             R = IntegerModRing(2)
`@``@` -3552,10 +3555,13 `@``@` class Graph(GenericGraph):
             [-1  0  0  1]

         """
+        from sage.matrix.constructor import matrix
+        from sage.rings.integer_ring import IntegerRing
+
         if weighted:
             M = self.weighted_adjacency_matrix()
         else:
-            M = self.am()
+            M = matrix(self,IntegerRing())
         A = list(-M)
         S = [sum(M[i]) for i in range(M.nrows())]
         for i in range(len(A)):
`@``@` -5344,8 +5350,8 `@``@` class DiGraph(GenericGraph):

     def adjacency_matrix(self, sparse=True):
         """
-        Returns the adjacency matrix of the digraph. Each vertex is
-        represented by its position in the list returned by the vertices()
+        Returns the adjacency matrix of the digraph as a matrix over the field of two elements.
+        Each vertex is represented by its position in the list returned by the vertices()
         function.

         EXAMPLE:
```



---

Comment by jason created at 2007-10-03 07:50:27

Same patch as listed in the post.


---

Attachment


---

Comment by rlm created at 2007-10-04 19:52:39

Resolution: fixed
