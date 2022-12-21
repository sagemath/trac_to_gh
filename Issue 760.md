# Issue 760: [patch] graphs: a small change to subgraphs allow it to default to the original graph.

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-09-28 19:43:44

Assignee: was


```
--- a/sage/graphs/graph.py      Fri Sep 28 14:05:12 2007 -0500
+++ b/sage/graphs/graph.py      Fri Sep 28 14:35:19 2007 -0500
`@``@` -3974,7 +3974,7 `@``@` class Graph(GenericGraph):
         """
         self._nxg.add_path(vertices)

-    def subgraph(self, vertices, inplace=False, create_using=None):
+    def subgraph(self, vertices=None, inplace=False, create_using=None):
         """
         Returns the subgraph induced by the given vertices.

`@``@` -3983,7 +3983,7 `@``@` class Graph(GenericGraph):
         and edges from the current graph. This will modify the graph, and re-
         turn itself.
         vertices -- Vertices can be a single vertex or an iterable container
-        of vertices, e.g. a list, set, graph, file or numeric array.
+        of vertices, e.g. a list, set, graph, file or numeric array.  If not passed, defaults to the entire graph.
         create_using -- Can be an existing graph object or a call to a graph
         object, such as create_using=DiGraph(). Must be a NetworkX object.

`@``@` -3998,6 +3998,8 `@``@` class Graph(GenericGraph):
             sage: G
             Subgraph of (Complete graph): Graph on 3 vertices
             sage: G is K
+            True
+            sage: G.subgraph()==G
             True

         """
`@``@` -5424,7 +5426,7 `@``@` class DiGraph(GenericGraph):
         G = DiGraph(NXG)
         return G

-    def subgraph(self, vertices, inplace=False, create_using=None):
+    def subgraph(self, vertices=None, inplace=False, create_using=None):
         """
         Returns the subgraph induced by the given vertices.

`@``@` -5433,7 +5435,7 `@``@` class DiGraph(GenericGraph):
         and edges from the current graph. This will modify the graph, and re-
         turn itself.
         vertices -- Vertices can be a single vertex or an iterable container
-        of vertices, e.g. a list, set, graph, file or numeric array.
+        of vertices, e.g. a list, set, graph, file or numeric array.  If not passed, defaults to the entire graph.
         create_using -- Can be an existing graph object or a call to a graph
         object, such as create_using=DiGraph().

```



---

Comment by jason created at 2007-09-28 19:44:00

Changing priority from major to trivial.


---

Comment by jason created at 2007-10-03 07:52:51

Same patch as listed in the post.


---

Attachment


---

Comment by rlm created at 2007-10-04 19:54:10

Resolution: fixed
