# Issue 746: graphs: graph name is not reset using clear()

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-09-24 20:54:44

Assignee: was

Keywords: graphs

Since networkX uses the empty string for an unset name, while the current SAGE code uses None for an unset name, calling _nxg.clear() in the clear() function will not reset the name to None, but to ''.

There are also other problems with having an unset name represented by None (mostly because networkX assumes that '' is an unset name).


---

Comment by jason created at 2007-09-28 18:55:19

--- a/sage/graphs/graph.py      Wed Sep 26 09:37:18 2007 -0700
+++ b/sage/graphs/graph.py      Fri Sep 28 13:45:19 2007 -0500
`@``@` -684,10 +684,34 `@``@` class GenericGraph(SageObject):

     def clear(self):
         """
-        Empties the graph of vertices and edges, removes name.
+        Empties the graph of vertices and edges and removes name,
+        boundary, associated objects, and position information.
+
+        EXAMPLE:
+            sage: G=graphs.CycleGraph(4); G.associate({0:'vertex0'})
+            sage: G.order(); G.size()
+            4
+            4
+            sage: len(G._pos)
+            4
+            sage: G.name()
+            'Cycle graph'
+            sage: G.obj(0)
+            'vertex0'
+            sage: G.clear()
+            sage: G.order(); G.size()
+            0
+            0
+            sage: len(G._pos)
+            0
+            sage: G.name()
+            sage: G.obj(0)

         """
         self._nxg.clear()
+        self._pos=[]
+        self._boundary=[]
+        self._assoc=None

     def neighbors(self, vertex):
         """


---

Comment by jason created at 2007-09-28 18:55:50

Let's try that again:


```
--- a/sage/graphs/graph.py      Wed Sep 26 09:37:18 2007 -0700
+++ b/sage/graphs/graph.py      Fri Sep 28 13:46:41 2007 -0500
`@``@` -684,10 +684,34 `@``@` class GenericGraph(SageObject):

     def clear(self):
         """
-        Empties the graph of vertices and edges, removes name.
+        Empties the graph of vertices and edges and removes name,
+        boundary, associated objects, and position information.
+
+        EXAMPLE:
+            sage: G=graphs.CycleGraph(4); G.associate({0:'vertex0'})
+            sage: G.order(); G.size()
+            4
+            4
+            sage: len(G._pos)
+            4
+            sage: G.name()
+            'Cycle graph'
+            sage: G.obj(0)
+            'vertex0'
+            sage: G.clear()
+            sage: G.order(); G.size()
+            0
+            0
+            sage: len(G._pos)
+            0
+            sage: G.name()
+            sage: G.obj(0)

         """
         self._nxg.clear()
+        self._pos=[]
+        self._boundary=[]
+        self._assoc=None

     def neighbors(self, vertex):
         """
```



---

Comment by rlm created at 2007-10-04 19:52:29

Resolution: fixed
