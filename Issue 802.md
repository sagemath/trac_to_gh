# Issue 802: [with patch] graphs: Streamline and document _cmp_ more

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-10-03 07:35:11

Assignee: was


```
--- a/sage/graphs/graph.py      Wed Oct 03 02:18:16 2007 -0500
+++ b/sage/graphs/graph.py      Wed Oct 03 02:25:05 2007 -0500
`@``@` -255,6 +255,9 `@``@` class GenericGraph(SageObject):

         Note that this is _not_ an isomorphism test.

+        Note that the less-than and greater-than value returned here
+        doesn't mean much.  The equality test is the useful thing.
+
         EXAMPLES:
             sage: G = graphs.EmptyGraph()
             sage: H = Graph()
`@``@` -280,17 +283,19 `@``@` class GenericGraph(SageObject):
             False

         """
+        # If the graphs have different properties, they are not equal.
         if type(self) != type(other):
             return 1
         elif self.loops() != other.loops():
             return 1
-        else:
-            if self.multiple_edges() != other.multiple_edges():
-                return 1
+        elif self.multiple_edges() != other.multiple_edges():
+            return 1

         # If the vertices have different labels, the graphs are not equal.
         if sorted(self.vertices()) != sorted(other.vertices()):
             return 1
+
+        # Check that the edges are the same.
         comp = enum(self) - enum(other)
         if comp < 0:
             return -1
```



---

Comment by jason created at 2007-10-03 07:41:39

One more Latexifying thing in a function's documentation (to be applied after the patch above):


```
--- a/sage/graphs/graph.py      Wed Oct 03 02:24:56 2007 -0500
+++ b/sage/graphs/graph.py      Wed Oct 03 02:31:49 2007 -0500
`@``@` -336,7 +336,7 `@``@` class GenericGraph(SageObject):

     def __iter__(self):
         """
-        Return an iterator over the vertices. Allows 'for v in G'.
+        Return an iterator over the vertices which allows \code{for v in G} syntax.

         """
         return self.vertex_iterator()
```



---

Comment by rlm created at 2007-10-04 19:54:00

Resolution: fixed
