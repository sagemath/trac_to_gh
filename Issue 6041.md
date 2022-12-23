# Issue 6041: update NetworkX to version 0.99

Issue created by migration from https://trac.sagemath.org/ticket/6041

Original creator: mvngu

Original creation time: 2009-05-15 06:14:08

Assignee: rlm

CC:  rlm jason

As the subject says. This is a follow-up to #5934.


---

Comment by mvngu created at 2009-05-19 11:16:48

A new spkg is up at



http://sage.math.washington.edu/home/mvngu/patch/networkx-0.99.p1.spkg



Unfortunately, as I suspected version 0.99 of NetworkX breaks a lot of doctests:

```
The following tests failed:


        sage -t -long "devel/sage-main/sage/graphs/graph_bundle.py"
        sage -t -long "devel/sage-main/sage/graphs/graph_generators.py"
        sage -t -long "devel/sage-main/sage/graphs/planarity.pyx"
        sage -t -long "devel/sage-main/sage/graphs/graph_fast.pyx"
        sage -t -long "devel/sage-main/sage/graphs/graph_isom.pyx"
        sage -t -long "devel/sage-main/sage/graphs/schnyder.py"
        sage -t -long "devel/sage-main/sage/graphs/graph_coloring.py"
        sage -t -long "devel/sage-main/sage/graphs/graph.py"
        sage -t -long "devel/sage-main/sage/graphs/chrompoly.pyx"
        sage -t -long "devel/sage-main/sage/graphs/print_graphs.py"
        sage -t -long "devel/sage-main/sage/graphs/graph_plot.py"
        sage -t -long "devel/sage-main/sage/graphs/graph_list.py"
        sage -t -long "devel/sage-main/sage/graphs/graph_database.py"
        sage -t -long "devel/sage-main/sage/graphs/base/graph_backends.py"
        sage -t -long "devel/sage-main/sage/graphs/base/dense_graph.pyx"
        sage -t -long "devel/sage-main/sage/graphs/base/sparse_graph.pyx"
        sage -t -long "devel/sage-main/sage/graphs/base/c_graph.pyx"
        sage -t -long "devel/sage-main/sage/graphs/bipartite_graph.py"
        sage -t -long "devel/sage-main/sage/graphs/linearextensions.py"
Total time for all tests: 63.8 seconds
```

I'll upload patches against the relevant modules shortly, unless someone who is awake beats me to it (I'm going to sleep now :-).


---

Comment by rlm created at 2009-05-19 14:21:21

You should definitely get a good night's sleep before you tackle that!

I would suggest you start by seeing what needs to be fixed to get the doctests in

```
devel/sage-main/sage/graphs/base/graph_backends.py
```

to work properly. This is where Sage and NetworkX mainly plug in to each other. Once those are fixed, I expect much of the rest will be already done.


---

Comment by mvngu created at 2009-05-20 06:26:28

I managed to get all doctests in `sage/graphs/base/graph_backends.py` to pass, but at the expense of deleting the following methods from the class `NetworkXGraphBackend`. Here I assume that `NetworkXGraphBackend` is an undirected graph without multiple edges.
 1. `loops` -- This is irrelevant with the API changes in NetworkX 0.99, since the class `Graph` from NetworkX 0.99 allows for self-loops without having to explicitly set it with a boolean.
 1. `multiple_edges` -- Again irrelevant since the class `Graph` doesn't allow multiple edges. Graphs with multiple edges should now be constructed via the class `MultiGraph` (not directed), or `MultiDiGraph` which allows for directed arcs.
Here's a diff of the changes to `sage/graphs/base/graph_backends.py`:

```
diff -r 21c6c829ea32 sage/graphs/base/graph_backends.py
--- a/sage/graphs/base/graph_backends.py	Sat May 16 09:46:59 2009 -0700
+++ b/sage/graphs/base/graph_backends.py	Tue May 19 23:47:29 2009 -0700
@@ -499,13 +499,12 @@
         """
         if N is None:
             import networkx
-            N = networkx.XGraph()
+            N = networkx.Graph()
         self._nxg = N
 
-    def add_edge(self, u, v, l, directed):
+    def add_edge(self, u, v, l):
         """
-        Add an edge (u,v) to self, with label l.  If directed is True, this is
-        interpreted as an arc from u to v.
+        Add an edge (u,v) to self, with label l.
         
         INPUT:
             u,v:      vertices
@@ -514,11 +513,11 @@
         
         DOCTEST:
             sage: G = sage.graphs.base.graph_backends.NetworkXGraphBackend()
-            sage: G.add_edge(1,2,'a',True)
+            sage: G.add_edge(1, 2, "a")
          """
         self._nxg.add_edge(u, v, l)
 
-    def add_edges(self, edges, directed):
+    def add_edges(self, edges):
         """
         Add a sequence of edges to self.  If directed is True, these are
         interpreted as arcs.
@@ -529,7 +528,7 @@
         
         DOCTEST:
             sage: G = sage.graphs.base.graph_backends.NetworkXGraphBackend()
-            sage: G.add_edges([],True)
+            sage: G.add_edges([])
         """
         for e in edges:
             try:
@@ -537,7 +536,7 @@
             except:
                 u,v = e
                 l = None
-            self.add_edge(u,v,l,directed)
+            self.add_edge(u, v, l)
 
     def add_vertex(self, name):
         """
@@ -589,7 +588,7 @@
         """
         return self._nxg.degree(v)
 
-    def del_edge(self, u, v, l, directed):
+    def del_edge(self, u, v, l):
         """
         Deletes the edge (u,v) with label l.
 
@@ -600,9 +599,10 @@
         
         DOCTEST:
             sage: G = sage.graphs.base.graph_backends.NetworkXGraphBackend()
-            sage: G.del_edge(1,2,'a',True)
+            sage: G.add_edge(1, 2, "a")
+            sage: G.del_edge(1, 2, "a")
         """
-        self._nxg.delete_edge(u, v, l)
+        self._nxg.delete_edge(u, v)
 
     def del_vertex(self, v):
         """
@@ -649,16 +649,16 @@
         
         DOCTEST:
             sage: G = sage.graphs.base.graph_backends.NetworkXGraphBackend()
-            sage: G.get_edge_label(1,2)
+            sage: G.get_edge_label(1, 2)
             Traceback (most recent call last):
             ...
-            NetworkXError: Edge (1,2) requested via get_edge does not exist.
+            NetworkXError: edge (1,2) not in graph
         """
         return self._nxg.get_edge(u, v)
 
-    def has_edge(self, u, v, l):
+    def has_edge(self, u, v):
         """
-        True if self has an edge (u,v) with label l.
+        True if self has an edge (u,v).
 
         INPUT:
             u,v: vertex labels
@@ -669,10 +669,19 @@
         
         DOCTEST:
             sage: G = sage.graphs.base.graph_backends.NetworkXGraphBackend()
-            sage: G.has_edge(1,2,'a')
+            sage: G.has_edge(1, 2)
             False
         """
-        return self._nxg.has_edge(u, v, l)
+        return self._nxg.has_edge(u, v)
+
+    def has_selfloops(self):
+        """
+        Returns ``True`` if this graph has self-loops; ``False`` otherwise.
+        """
+        if self._nxg.number_of_selfloops() > 0:
+            return True
+        else:
+            return False
 
     def has_vertex(self, v):
         """
@@ -781,8 +790,9 @@
             
         DOCTEST:
             sage: G = sage.graphs.base.graph_backends.NetworkXGraphBackend()
+            sage: G.add_edges([(0,1), (0,2), (1,2)])
             sage: G.iterator_nbrs(0)
-            <generator object at ...>
+            <dictionary-keyiterator object at ...>
         """
         return self._nxg.neighbors_iter(v)
 
@@ -802,7 +812,7 @@
             sage: G.iterator_in_nbrs(0)
             Traceback (most recent call last):
             ...
-            AttributeError: 'XGraph' object has no attribute 'predecessors_iter'
+            AttributeError: 'Graph' object has no attribute 'predecessors_iter'
         """
         return self._nxg.predecessors_iter(v)
 
@@ -822,7 +832,7 @@
             sage: G.iterator_out_nbrs(0)
             Traceback (most recent call last):
             ...
-            AttributeError: 'XGraph' object has no attribute 'successors_iter'
+            AttributeError: 'Graph' object has no attribute 'successors_iter'
         """
         return self._nxg.successors_iter(v)
 
@@ -839,49 +849,9 @@
         DOCTEST:
             sage: G = sage.graphs.base.graph_backends.NetworkXGraphBackend()
             sage: G.iterator_verts(0)
-            <listiterator object at ...>
+            <generator object at ...>
         """
-        return iter(self._nxg.prepare_nbunch(verts))
-
-    def loops(self, new):
-        """
-        Get/set whether or not self allows loops.        
-        
-        INPUT:
-            new: boolean or None
-        
-        DOCTEST:
-            sage: G = sage.graphs.base.graph_backends.NetworkXGraphBackend()
-            sage: G.loops(True)
-            sage: G.loops(None)
-            True
-        """
-        if new is None:
-            return self._nxg.selfloops
-        if new:
-            self._nxg.allow_selfloops()
-        else:
-            self._nxg.ban_selfloops()
-
-    def multiple_edges(self, new):
-        """
-        Get/set whether or not self allows multiple edges.
-        
-        INPUT:
-            new: boolean or None
-        
-        DOCTEST:
-            sage: G = sage.graphs.base.graph_backends.NetworkXGraphBackend()
-            sage: G.multiple_edges(True)
-            sage: G.multiple_edges(None)
-            True
-        """
-        if new is None:
-            return self._nxg.multiedges
-        if new:
-            self._nxg.allow_multiedges()
-        else:
-            self._nxg.ban_multiedges()
+        return iter(self._nxg.nbunch_iter(verts))
 
     def name(self, new):
         """
@@ -969,39 +939,24 @@
                 newd[perm[v]] = newtempd
             self._nxg.adj = newd
 
-    def set_edge_label(self, u, v, l, directed):
+    def set_edge_label(self, u, v, l):
         """
         Label the edge (u,v) by l.
         
         INPUT:
             u,v:      vertices
             l:        edge label
-            directed: boolean
         
         DOCTEST:
             sage: G = sage.graphs.base.graph_backends.NetworkXGraphBackend()
-            sage: G.set_edge_label(1,2,'a',True)
+            sage: # G is empty graph, so it doesn't have the edge (1,2)
+            sage: G.set_edge_label(1, 2, "a")
+            sage: # add some edges to G
+            sage: G.add_edges([(1,2), (1,3), (2,3)])
+            sage: G.set_edge_label(1, 2, "b")
         """        
-        if not self.has_edge(u, v, None):
+        if not self.has_edge(u, v):
             return
-        if self.multiple_edges(None):
-            if directed:
-                self._nxg.succ[u][v] = [l]
-                self._nxg.pred[v][u] = [l]
-            else:
-                self._nxg.adj[u][v] = [l]
-                self._nxg.adj[v][u] = [l]
         else:
-            if directed:
-                self._nxg.succ[u][v] = l
-                self._nxg.pred[v][u] = l
-            else:
-                self._nxg.adj[u][v] = l
-                self._nxg.adj[v][u] = l
-
-
-
-
-
-
-
+            self._nxg.adj[u][v] = l
+            self._nxg.adj[v][u] = l

```

But the following doctests failed:

```
sage -t -long "devel/sage-6041/sage/graphs/graph_bundle.py"
sage -t -long "devel/sage-6041/sage/graphs/graph_generators.py"
sage -t -long "devel/sage-6041/sage/graphs/planarity.pyx"
sage -t -long "devel/sage-6041/sage/graphs/graph_fast.pyx"
sage -t -long "devel/sage-6041/sage/graphs/graph_isom.pyx"
sage -t -long "devel/sage-6041/sage/graphs/schnyder.py"
sage -t -long "devel/sage-6041/sage/graphs/graph_coloring.py"
sage -t -long "devel/sage-6041/sage/graphs/graph.py"
sage -t -long "devel/sage-6041/sage/graphs/chrompoly.pyx"
sage -t -long "devel/sage-6041/sage/graphs/print_graphs.py"
sage -t -long "devel/sage-6041/sage/graphs/graph_plot.py"
sage -t -long "devel/sage-6041/sage/graphs/graph_list.py"
sage -t -long "devel/sage-6041/sage/graphs/graph_database.py"
sage -t -long "devel/sage-6041/sage/graphs/base/dense_graph.pyx"
sage -t -long "devel/sage-6041/sage/graphs/base/sparse_graph.pyx"
sage -t -long "devel/sage-6041/sage/graphs/base/c_graph.pyx"
sage -t -long "devel/sage-6041/sage/graphs/bipartite_graph.py"
sage -t -long "devel/sage-6041/sage/graphs/linearextensions.py"
sage -t -long "devel/sage-6041/sage/graphs/base/dense_graph.pyx"
sage -t -long "devel/sage-6041/sage/graphs/base/sparse_graph.pyx"
sage -t -long "devel/sage-6041/sage/graphs/base/c_graph.pyx"
```

It looks like anything under `sage/graphs/` that uses `sage/graphs/base/graph_backends.py` should be changed accordingly.


---

Comment by rlm created at 2009-05-20 13:57:16

Replying to [comment:3 mvngu]:
> I managed to get all doctests in `sage/graphs/base/graph_backends.py` to pass, but at the expense of deleting the following methods from the class `NetworkXGraphBackend`. Here I assume that `NetworkXGraphBackend` is an undirected graph without multiple edges.

Incorrect. NetworkXGraphBackend is simply a wrapper for a NetworkX graph, which can be directed, or have multiple edges.

>  1. `loops` -- This is irrelevant with the API changes in NetworkX 0.99, since the class `Graph` from NetworkX 0.99 allows for self-loops without having to explicitly set it with a boolean.
>  1. `multiple_edges` -- Again irrelevant since the class `Graph` doesn't allow multiple edges. Graphs with multiple edges should now be constructed via the class `MultiGraph` (not directed), or `MultiDiGraph` which allows for directed arcs.

This isn't irrelevant, as *Sage* graphs can have loops or multiedges set. What needs to happen is for loops and multiedges to become properties of the backend, and for the appropriate work to go on there. We still need to support these options. You should be working on top of the `part-1` patch at #6085, since it implements part of this in `graph.py` (and so that we're less likely to be stepping on each other's toes).

> Here's a diff of the changes to `sage/graphs/base/graph_backends.py`: 

Next time you could probably attach the diff to the ticket... :)

> It looks like anything under `sage/graphs/` that uses `sage/graphs/base/graph_backends.py` should be changed accordingly.

Don't forget all of the rest of Sage! I think you'll find it much easier to adapt the backend to behave exactly as before. Then, all the other doctests should pass - that's what they're there for!


---

Comment by mvngu created at 2009-05-21 05:56:28

Replying to [comment:4 rlm]:
> Replying to [comment:3 mvngu]:
> > I managed to get all doctests in `sage/graphs/base/graph_backends.py` to pass, but at the expense of deleting the following methods from the class `NetworkXGraphBackend`. Here I assume that `NetworkXGraphBackend` is an undirected graph without multiple edges.
> 
> Incorrect. NetworkXGraphBackend is simply a wrapper for a NetworkX graph, which can be directed, or have multiple edges.
Agreed. Version 0.99 now has:
 * `Graph` --- An undirected graph class without multiple (parallel) edges.
 * `DiGraph` --- A directed graph that allows self-loops, but not multiple (parallel) edges.
 * `MultiGraph` --- An undirected graph that allows multiple (parallel) edges with arbitrary data on the edges.
 * `MultiDiGraph` --- A directed graph that allows multiple (parallel) edges with arbitrary data on the edges.
These have been lifted off from the NetworkX 0.99 documentation. `MultiGraph` is the successor to `XGraph` where we allow `XGraph` to have multiple edges. And `MultiDiGraph` is the successor to `XDiGraph` with multiple edges. According to the API change log at



http://networkx.lanl.gov/reference/api_changes.html



Previously `XGraph` handle undirected graphs with or without multiple edges, and `XDiGraph` handle directed graphs with or without multiple edges. Now there are four graph classes instead of two, for handling the different types of graphs.




> >  1. `loops` -- This is irrelevant with the API changes in NetworkX 0.99, since the class `Graph` from NetworkX 0.99 allows for self-loops without having to explicitly set it with a boolean.
> >  1. `multiple_edges` -- Again irrelevant since the class `Graph` doesn't allow multiple edges. Graphs with multiple edges should now be constructed via the class `MultiGraph` (not directed), or `MultiDiGraph` which allows for directed arcs.
> 
> This isn't irrelevant, as *Sage* graphs can have loops or multiedges set. What needs to happen is for loops and multiedges to become properties of the backend, and for the appropriate work to go on there. We still need to support these options. You should be working on top of the `part-1` patch at #6085, since it implements part of this in `graph.py` (and so that we're less likely to be stepping on each other's toes).
Thanks you for the pointer.




> > Here's a diff of the changes to `sage/graphs/base/graph_backends.py`: 
> 
> Next time you could probably attach the diff to the ticket... :)
No, the diff isn't meant to be committed in the future. It's there for discussion and to explore ways to maintain compatibility with the existing API in `graph_backends.py`. But as you can see, the diff clearly breaks compatibility :-)




> > It looks like anything under `sage/graphs/` that uses `sage/graphs/base/graph_backends.py` should be changed accordingly.
> 
> Don't forget all of the rest of Sage! I think you'll find it much easier to adapt the backend to behave exactly as before. Then, all the other doctests should pass - that's what they're there for!
OK, let me see what I can do.


---

Comment by rlm created at 2009-05-21 14:32:13

Replying to [comment:5 mvngu]:
> Replying to [comment:4 rlm]:
> > Replying to [comment:3 mvngu]:
> Previously `XGraph` handle undirected graphs with or without multiple edges, and `XDiGraph` handle directed graphs with or without multiple edges. Now there are four graph classes instead of two, for handling the different types of graphs.

Actually, there were also `Graph` and `DiGraph`, which did not have labels...

> > > Here's a diff of the changes to `sage/graphs/base/graph_backends.py`: 
> > 
> > Next time you could probably attach the diff to the ticket... :)
> No, the diff isn't meant to be committed in the future. It's there for discussion and to explore ways to maintain compatibility with the existing API in `graph_backends.py`.

You can still post diffs as attachments. It makes the discussion much easier to follow when you're reading the ticket, and it keeps clutter down. Just add the note "not to be applied" if you're worried...

> > > It looks like anything under `sage/graphs/` that uses `sage/graphs/base/graph_backends.py` should be changed accordingly.
> > 
> > Don't forget all of the rest of Sage! I think you'll find it much easier to adapt the backend to behave exactly as before. Then, all the other doctests should pass - that's what they're there for!
> OK, let me see what I can do.

It should be possible to get all of the doctests in Sage working by changing only things which call `networkx` directly (i.e. things involving `import networkx`), and the `NetworkXGraphBackend` class in `graph_backends.py`. Keep in mind that there are several interchangeable backends. In your diff, you were actually changing the signature of some of the backend functions-- this is bad.


---

Comment by rlm created at 2009-05-21 14:50:40

There is another patch at #6085 now: You should be working on top of `part-1` and `part-2`.


---

Comment by mvngu created at 2009-12-05 23:29:54

This ticket is now a duplicate of #7608. The latter has a patch and an updated NetworkX 1.0rc1 package.


---

Comment by mvngu created at 2009-12-05 23:29:54

Resolution: duplicate
