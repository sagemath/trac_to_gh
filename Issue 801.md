# Issue 801: [with patch] graphs: Latexify module-level documentation

Issue created by migration from https://trac.sagemath.org/ticket/801

Original creator: jason

Original creation time: 2007-10-03 07:30:06

Assignee: was

Keywords: graphs

This patch puts the module-level documentation into latex.


```
--- a/sage/graphs/graph.py	Mon Oct 01 15:06:55 2007 -0500
+++ b/sage/graphs/graph.py	Wed Oct 03 02:18:24 2007 -0500
@@ -1,5 +1,7 @@ r"""
 r"""
 Graph Theory
+
+This module implements many graph theoretic operations and concepts.
 
 AUTHOR:
     -- Robert L. Miller (2006-10-22): initial version
@@ -26,14 +28,9 @@ AUTHOR:
     -- Bobby Moretti (2007-08-12): fixed up plotting of graphs with
        edge colors differentiated by label
 
-
-TUTORIAL:
-
-    I. The Basics
-    
-        1. Graph Format
-        
-            A. The SAGE Graph Class: NetworkX plus
+\subsection{Graph Format}
+
+\subsubsection{The SAGE Graph Class: NetworkX plus}
             
             SAGE graphs are actually NetworkX graphs, wrapped in a SAGE class.
             In fact, any graph can produce its underlying NetworkX graph. For example,
@@ -51,40 +48,48 @@ TUTORIAL:
 
             Each dictionary key is a vertex label, and each key in the following
             dictionary is a neighbor of that vertex. In undirected graphs, there
-            is reduncancy: for example, the dictionary containing the entry
-            1: {2: None} implies it must contain 2: {1: None}. The innermost entry
-            of None is related to edge labelling (see section I.3.).
-        
-            B. Supported formats
+            is redundancy: for example, the dictionary containing the entry
+            \verb|1: {2: None}| implies it must contain \verb|{2: {1: None}|. 
+            The innermost entry of \var{None} is related to edge labeling 
+            (see section \ref{Graph:labels}).
+
+            \subsubsection{Supported formats}
+        
             
             SAGE Graphs can be created from a wide range of inputs. A few examples are
             covered here.
+
+            \begin{itemize}
             
-                i.   a. NetworkX dictionary format:
+                  \item NetworkX dictionary format:
                 
-                sage: d = {0: [1,4,5], 1: [2,6], 2: [3,7], 3: [4,8], 4: [9], 5: [7, 8], 6: [8,9], 7: [9]}
+                sage: d = {0: [1,4,5], 1: [2,6], 2: [3,7], 3: [4,8], 4: [9], \
+                      5: [7, 8], 6: [8,9], 7: [9]}
                 sage: G = Graph(d); G
                 Graph on 10 vertices
                 sage: G.plot().save('sage.png')    # or G.show()
                 
-                    b. A NetworkX graph:
+                    \item A NetworkX graph:
                 
                 sage: K = networkx.complete_bipartite_graph(12,7)
                 sage: G = Graph(K)
                 sage: G.degree()
                 [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 12, 12, 12, 12, 12, 12, 12]
-                
-                ii. graph6 or sparse6 format:
+
+                \item graph6 or sparse6 format:
                 
                 sage: s = ':I`AKGsaOs`cI]Gb~'
                 sage: G = Graph(s); G
                 Looped multi-graph on 10 vertices
                 sage: G.plot().save('sage.png')    # or G.show()
                 
-                iii. adjacency matrix: In an adjacency matrix, each column and each row represent
+                \item adjacency matrix In an adjacency matrix, each column and each row represent
                 a vertex. If a 1 shows up in row i, column j, there is an edge (i,j).
                 
-                sage: M = Matrix([(0,1,0,0,1,1,0,0,0,0),(1,0,1,0,0,0,1,0,0,0),(0,1,0,1,0,0,0,1,0,0),(0,0,1,0,1,0,0,0,1,0),(1,0,0,1,0,0,0,0,0,1),(1,0,0,0,0,0,0,1,1,0),(0,1,0,0,0,0,0,0,1,1),(0,0,1,0,0,1,0,0,0,1),(0,0,0,1,0,1,1,0,0,0),(0,0,0,0,1,0,1,1,0,0)])
+                sage: M = Matrix([(0,1,0,0,1,1,0,0,0,0),(1,0,1,0,0,0,1,0,0,0), \
+                (0,1,0,1,0,0,0,1,0,0), (0,0,1,0,1,0,0,0,1,0),(1,0,0,1,0,0,0,0,0,1), \
+                (1,0,0,0,0,0,0,1,1,0), (0,1,0,0,0,0,0,0,1,1),(0,0,1,0,0,1,0,0,0,1), \
+                (0,0,0,1,0,1,1,0,0,0), (0,0,0,0,1,0,1,1,0,0)])
                 sage: M
                 [0 1 0 0 1 1 0 0 0 0]
                 [1 0 1 0 0 0 1 0 0 0]
@@ -100,10 +105,15 @@ TUTORIAL:
                 Graph on 10 vertices
                 sage: G.plot().save('sage.png')    # or G.show()
                 
-                iv. incidence matrix: In an incidence matrix, each row represents a vertex
+                \item incidence matrix: In an incidence matrix, each row represents a vertex
                 and each column reprensents an edge.
                 
-                sage: M = Matrix([(-1,0,0,0,1,0,0,0,0,0,-1,0,0,0,0),(1,-1,0,0,0,0,0,0,0,0,0,-1,0,0,0),(0,1,-1,0,0,0,0,0,0,0,0,0,-1,0,0),(0,0,1,-1,0,0,0,0,0,0,0,0,0,-1,0),(0,0,0,1,-1,0,0,0,0,0,0,0,0,0,-1),(0,0,0,0,0,-1,0,0,0,1,1,0,0,0,0),(0,0,0,0,0,0,0,1,-1,0,0,1,0,0,0),(0,0,0,0,0,1,-1,0,0,0,0,0,1,0,0),(0,0,0,0,0,0,0,0,1,-1,0,0,0,1,0),(0,0,0,0,0,0,1,-1,0,0,0,0,0,0,1)])
+                sage: M = Matrix([(-1,0,0,0,1,0,0,0,0,0,-1,0,0,0,0), \
+                (1,-1,0,0,0,0,0,0,0,0,0,-1,0,0,0),(0,1,-1,0,0,0,0,0,0,0,0,0,-1,0,0), \
+                (0,0,1,-1,0,0,0,0,0,0,0,0,0,-1,0),(0,0,0,1,-1,0,0,0,0,0,0,0,0,0,-1), \
+                (0,0,0,0,0,-1,0,0,0,1,1,0,0,0,0),(0,0,0,0,0,0,0,1,-1,0,0,1,0,0,0), \
+                (0,0,0,0,0,1,-1,0,0,0,0,0,1,0,0),(0,0,0,0,0,0,0,0,1,-1,0,0,0,1,0), \
+                (0,0,0,0,0,0,1,-1,0,0,0,0,0,0,1)])
                 sage: M
                 [-1  0  0  0  1  0  0  0  0  0 -1  0  0  0  0]
                 [ 1 -1  0  0  0  0  0  0  0  0  0 -1  0  0  0]
@@ -118,14 +128,16 @@ TUTORIAL:
                 sage: G = Graph(M); G
                 Graph on 10 vertices
                 sage: G.plot().save('sage.png')    # or G.show()
-        
-        2. Generators
+
+        \end{itemize}
+
+        \subsection{Generators}
         
         For some commonly used graphs to play with, type
         
             sage.: graphs.
         
-        and hit <tab>. Most of these graphs come with their own custom plot, so you
+        and hit \kbd{tab}. Most of these graphs come with their own custom plot, so you
         can see how people usually visualize these graphs.
         
             sage: G = graphs.PetersenGraph()
@@ -153,7 +165,7 @@ TUTORIAL:
             sage: L = G.get_list(num_vertices=7, diameter=5)
             sage.: graphs_list.show_graphs(L)
         
-        3. Labels
+            \subsection{Labels}\label{Graph:labels}
         
         Each vertex can have any hashable object as a label. These are things like
         strings, numbers, and tuples. Each edge is given a default label of \var{None}, but
@@ -171,7 +183,8 @@ TUTORIAL:
         However, if one wants to define a dictionary, with the same keys and arbitrary objects
         for entries, one can make that association:
         
-            sage: d = {0 : graphs.DodecahedralGraph(), 1 : graphs.FlowerSnark(),2 : graphs.MoebiusKantorGraph(), 3 : graphs.PetersenGraph() }
+            sage: d = {0 : graphs.DodecahedralGraph(), 1 : graphs.FlowerSnark(), \
+                  2 : graphs.MoebiusKantorGraph(), 3 : graphs.PetersenGraph() }
             sage: d[2]
             Moebius-Kantor Graph: Graph on 16 vertices
             sage: T = graphs.TetrahedralGraph()
@@ -181,7 +194,7 @@ TUTORIAL:
             sage: T.obj(1)
             Flower Snark: Graph on 20 vertices
         
-        4. Database
+        \subsection{Database}
         
         There is a database available for searching for graphs that satisfy a certain set
         of parameters, including number of vertices and edges, density, maximum and minimum
@@ -190,28 +203,27 @@ TUTORIAL:
         
             sage.: graphs_query.
         
-        and hit tab.
+        and hit \kbd{tab}.
 
             sage: graphs_query = GraphDatabase()
             sage: L = graphs_query.get_list(num_vertices=7, diameter=5)
             sage.: graphs_list.show_graphs(L)
         
-        5. Visualization
-        
-        To see a graph G you are working with, right now there are two main options:
-        
+        \subsection{Visualization}
+        
+        To see a graph G you are working with, right now there are two main options.
+        You can view the graph in two dimensions via matplotlib with \method{show()}.
+                
             sage: G = graphs.RandomGNP(15,.3)
-        
-        You can view the graph in two dimensions via matplotlib:
-        
             sage.: G.show()
         
-        Or you can view it in three dimensions via Tachyon:
+        Or you can view it in three dimensions via Tachyon with \method{show3d()}.
         
             sage.: G.show3d()
 
-NOTE: Many functions are passed directly on to NetworkX, and in this
-case the documentation is based on the NetworkX docs.
+            \note{Many functions are passed directly on to NetworkX.
+              In these cases, the documentation is based on the
+              NetworkX docs.}
 
 """
 
```



---

Comment by jason created at 2007-10-03 08:03:08

Same patch as listed in the post.


---

Attachment


---

Comment by rlm created at 2007-10-04 19:53:06

Resolution: fixed
