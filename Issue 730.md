# Issue 730: graphs: fickle equality testing

Issue created by migration from https://trac.sagemath.org/ticket/730

Original creator: jason

Original creation time: 2007-09-21 18:42:54

Assignee: was

Keywords: graphs

Because the order returned by iterkeys is not guaranteed, enum, and therefore, `__cmp__` do not seem to behave well.  This could possibly be fixed by sorting the boundary vertices in the vertices() function.


```
sage: g=Graph({0:[1,2],'a':[1],1:[0,2],2:[0,1]})
sage: h=Graph({'a':[1],0:[1,2],1:[0,2],2:[0,1]})
sage: enum(g)
9174
sage: enum(h)
9174
sage: g.set_boundary([0,'a'])
sage: h.set_boundary([0,'a'])
sage: enum(g)
13018
sage: enum(h)
9174
sage: g==h
False
sage: g.vertices()
[0, 'a', 1, 2]
sage: h.vertices()
['a', 0, 1, 2]
```


It seems that since the graphs are the same, with the same labels and everything, the equality test should return True.  However, the boundary vertices are not sorted, so g.vertices() and h.vertices() return in a non-specified order.

Why do we return the boundary vertices first anyway?



---

Comment by was created at 2007-09-21 18:50:58

Changing assignee from was to rlmiller.


---

Comment by jason created at 2007-09-28 20:48:50

This patch fixes the problem noted above by redefining vertices() to return just a list of vertices and then patching various places to explicitly sort the output of vertices().  An option to vertices, boundary_first=True, outputs the boundary vertices first (but sorts the boundary vertices, so it still is deterministic).

The patch takes this approach so that vertices() can be more efficient (it doesn't have to loop through and separate out the boundary vertices any time someone wants a list of vertices).  However, this does break backward compatibility (previous versions returned the boundary first by default).


```
--- a/sage/graphs/graph.py	Fri Sep 28 15:21:56 2007 -0500
+++ b/sage/graphs/graph.py	Fri Sep 28 15:34:18 2007 -0500
@@ -275,7 +275,9 @@ class GenericGraph(SageObject):
         else:
             if self.multiple_edges() != other.multiple_edges():
                 return 1
-        if self.vertices() != other.vertices():
+
+        # If the vertices have different labels, the graphs are not equal.
+        if sorted(self.vertices()) != sorted(other.vertices()):
             return 1
         comp = enum(self) - enum(other)
         if comp < 0:
@@ -777,12 +779,17 @@ class GenericGraph(SageObject):
         """
         return self._nxg.prepare_nbunch(vertices)
 
-    def vertices(self):
-        """
-        Return a list of the vertex keys. If the graph is a graph with
-        boundary, boundary vertices are listed first.
-
-        """
+    def vertices(self, boundary_first=False):
+        """
+        Return a list of the vertices.
+
+        INPUT:
+            boundary_first -- Return the boundary vertices first.
+
+        """
+        if not boundary_first:
+            return list(self.vertex_iterator())
+        
         bdy_verts = []
         int_verts = []
         for v in self.vertex_iterator():
@@ -790,7 +797,7 @@ class GenericGraph(SageObject):
                 bdy_verts.append(v)
             else:
                 int_verts.append(v)
-        return bdy_verts + sorted(int_verts)
+        return sorted(bdy_verts) + sorted(int_verts)
 
     def relabel(self, perm, inplace=True, quick=False):
         r"""
@@ -2327,7 +2334,7 @@ class GenericGraph(SageObject):
         elif layout == 'circular':
             from math import sin, cos, pi
             n = self.order()
-            verts = self.vertices()
+            verts = sorted(self.vertices())
             pos = {}
             for i in range(n):
                 x = float(cos((pi/2) + ((2*pi)/n)*i))
@@ -3466,7 +3473,7 @@ class Graph(GenericGraph):
 
         """
         n = len(self._nxg.adj)
-        verts = self.vertices()
+        verts = sorted(self.vertices())
         D = {}
         for e in self.edge_iterator():
             i,j,l = e
@@ -3509,7 +3516,7 @@ class Graph(GenericGraph):
         from sage.matrix.constructor import matrix
         from copy import copy
         n = len(self._nxg.adj)
-        verts = self.vertices()
+        verts = sorted(self.vertices())
         d = [0]*n
         cols = []
         for i, j, l in self.edge_iterator():
@@ -3904,7 +3911,7 @@ class Graph(GenericGraph):
         if n > 262143:
             raise ValueError, 'sparse6 format supports graphs on 0 to 262143 vertices only.'
         else:
-            vertices = self.vertices()
+            vertices = sorted(self.vertices())
             n = len(vertices)
             edges = self.edges(labels=False)
             for i in range(len(edges)): # replace edge labels with natural numbers (by index in vertices)
@@ -4340,7 +4347,7 @@ class Graph(GenericGraph):
             from sage.graphs.graph_isom import search_tree, perm_group_elt
             from sage.groups.perm_gps.permgroup import PermutationGroup
             if partition is None:
-                partition = [self.vertices()]
+                partition = [sorted(self.vertices())]
             if translation:
                 a,b = search_tree(self, partition, dict=True, lab=False, dig=self.loops(), verbosity=verbosity)
             else:
@@ -5398,7 +5405,7 @@ class DiGraph(GenericGraph):
 
         """
         n = len(self._nxg.adj)
-        verts = self.vertices()
+        verts = sorted(self.vertices())
         D = {}
         for i,j,l in self.edge_iterator():
             i = verts.index(i)
@@ -5428,7 +5435,7 @@ class DiGraph(GenericGraph):
         from sage.matrix.constructor import matrix
         from copy import copy
         n = len(self._nxg.adj)
-        verts = self.vertices()
+        verts = sorted(self.vertices())
         d = [0]*n
         cols = []
         for i, j, l in self.edge_iterator():
@@ -5715,7 +5722,7 @@ class DiGraph(GenericGraph):
             from sage.graphs.graph_isom import search_tree, perm_group_elt
             from sage.groups.perm_gps.permgroup import PermutationGroup
             if partition is None:
-                partition = [self.vertices()]
+                partition = [sorted(self.vertices())]
             if translation:
                 a,b = search_tree(self, partition, dict=True, lab=False, dig=True, verbosity=verbosity)
             else:
```



---

Comment by jason created at 2007-09-28 20:50:48

The above patch breaks a doctest.  A determinant has the opposite sign, which would happen if two rows of the adjacency matrix were reversed because boundary vertices aren't returned first anymore.  It would be good to check if the failed doctest can be changed or if there is a problem in the patch.


---

Comment by rlm created at 2007-10-04 19:53:27

Resolution: fixed
