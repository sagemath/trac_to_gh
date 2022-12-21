# Issue 761: [patch] graphs: Lots of various doc changes and additional doc tests.

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-09-28 20:31:49

Assignee: was

No new functionality should be added here.  Rather, here are lots of documentation changes and a few new doctests.


```
--- a/sage/graphs/graph.py	Fri Sep 28 14:43:22 2007 -0500
+++ b/sage/graphs/graph.py	Fri Sep 28 15:22:25 2007 -0500
`@``@` -241,6 +241,8 `@``@` class GenericGraph(SageObject):
         settings for loops and multiedges, output the same vertex list (in order)
         and the same adjacency matrix.
         
+        Note that this is _not_ an isomorphism test.
+
         EXAMPLES:
             sage: G = graphs.EmptyGraph()
             sage: H = Graph()
`@``@` -349,6 +351,9 `@``@` class GenericGraph(SageObject):
 
     def _matrix_(self, R=None):
         """
+
+        Returns the adjacency matrix of the graph over the specified ring.
+
         EXAMPLES:
             sage: G = graphs.CompleteBipartiteGraph(2,3)
             sage: m = matrix(G); m.parent()
`@``@` -369,7 +374,7 `@``@` class GenericGraph(SageObject):
 
     def networkx_graph(self):
         """
-        Creates a NetworkX graph from the SAGE graph.
+        Creates a new NetworkX graph from the SAGE graph.
         
         EXAMPLE:
             sage: G = graphs.TetrahedralGraph()
`@``@` -377,14 +382,6 `@``@` class GenericGraph(SageObject):
             sage: type(N)
             <class 'networkx.xgraph.XGraph'>
 
-        Note that this returns a copy of the actual internal object,
-        not the actual internal networkX object.
-
-            sage: G = graphs.TetrahedralGraph()
-            sage: N = G.networkx_graph()
-            sage: G._nxg is N
-            False
-
         """
         return self._nxg.copy()
 
`@``@` -396,9 +393,17 `@``@` class GenericGraph(SageObject):
         self._nxg.info(vertex)
 
     def __get_pos__(self):
+        """
+        Returns the position dictionary, a dictionary specifying the coordinates
+        of each vertex.
+        """
         return self._pos
     
     def __set_pos__(self, pos):
+        """
+        Sets the position dictionary, a dictionary specifying the
+        coordinates of each vertex.
+        """
         self._pos = pos
 
     ### General properties
`@``@` -536,13 +541,17 `@``@` class GenericGraph(SageObject):
 
     def add_vertex(self, name=None):
         """
-        Creates an isolated vertex.
+        Creates an isolated vertex.  If the vertex already exists, then nothing is done.
 
         INPUT:
         n -- Name of the new vertex. If no name is specified, then the vertex
         will be represented by the least integer not already representing a
         vertex. Name must be an immutable object.
         
+        As it is implemented now, if a graph $G$ has a large number of
+        vertices with numeric labels, then G.add_vertex() could
+        potentially be slow.
+
         EXAMPLES:
             sage: G = Graph(); G.add_vertex(); G
             Graph on 1 vertex
`@``@` -562,6 +571,7 `@``@` class GenericGraph(SageObject):
     def add_vertices(self, vertices):
         """
         Add vertices to the (di)graph from an iterable container of vertices.
+        Vertices that already exist in the graph will not be added again.
         
         EXAMPLES:
             sage: d = {0: [1,4,5], 1: [2,6], 2: [3,7], 3: [4,8], 4: [9], 5: [7,8], 6: [8,9], 7: [9]}
`@``@` -578,7 +588,8 `@``@` class GenericGraph(SageObject):
 
     def delete_vertex(self, vertex):
         """
-        Deletes vertex, removing all incident edges.
+        Deletes vertex, removing all incident edges.  Deleting a non-existant
+        vertex will raise an exception.
         
         EXAMPLES:
             sage: G = graphs.WheelGraph(9)
`@``@` -587,6 +598,12 `@``@` class GenericGraph(SageObject):
             sage: D = DiGraph({0:[1,2,3,4,5],1:[2],2:[3],3:[4],4:[5],5:[1]})
             sage: D.delete_vertex(0); D
             Digraph on 5 vertices
+            sage: D.vertices()
+            [1, 2, 3, 4, 5]
+            sage: D.delete_vertex(0)
+            Traceback (most recent call last):
+            ...
+            NetworkXError: node 0 not in graph
 
         """
         self._nxg.delete_node(vertex)
`@``@` -594,12 +611,18 `@``@` class GenericGraph(SageObject):
     def delete_vertices(self, vertices):
         """
         Remove vertices from the (di)graph taken from an iterable container of
-        vertices.
+        vertices.  Deleting a non-existant vertex will raise an exception.
         
         EXAMPLE:
             sage: D = DiGraph({0:[1,2,3,4,5],1:[2],2:[3],3:[4],4:[5],5:[1]})
             sage: D.delete_vertices([1,2,3,4,5]); D
             Digraph on 1 vertex
+            sage: D.vertices()
+            [0]
+            sage: D.delete_vertices([1])
+            Traceback (most recent call last):
+            ...
+            NetworkXError: node 1 not in graph
 
         """
         self._nxg.delete_nodes_from(vertices)
`@``@` -614,7 +637,14 `@``@` class GenericGraph(SageObject):
         """
         Returns a list of all vertices in the external boundary of vertices1,
         intersected with vertices2. If vertices2 is None, then vertices2 is the
-        complement of vertices1.
+        complement of vertices1.  This is much faster if vertices1 is smaller than
+        vertices2.
+        
+        The external boundary of a set of vertices is the union of the
+        neighborhoods of each vertex in the set.  Note that in this
+        implementation, since vertices2 defaults to the complement of
+        vertices1, if a vertex $v$ has a loop, then vertex_boundary(v)
+        will not contain $v$.
         
         EXAMPLE:
             sage: G = graphs.CubeGraph(4)
`@``@` -933,8 +963,8 `@``@` class GenericGraph(SageObject):
     
     def cliques(self):
         """
-        Returns the list of maximal cliques of which each are members
-        of the clique.
+        Returns the list of maximal cliques.  Each maximal clique is
+        represented by a list of vertices.
         
         Currently only implemented for undirected graphs.  Use to_undirected
         to convert a digraph to an undirected graph.  (See examples below).
```



---

Attachment

Same patch as listed in the post.


---

Comment by rlm created at 2007-10-04 19:53:39

Resolution: fixed
