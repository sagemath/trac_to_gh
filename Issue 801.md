# Issue 801: [with patch] graphs: Latexify module-level documentation

archive/issues_000801.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: graphs\n\nThis patch puts the module-level documentation into latex.\n\n\n```\n--- a/sage/graphs/graph.py\tMon Oct 01 15:06:55 2007 -0500\n+++ b/sage/graphs/graph.py\tWed Oct 03 02:18:24 2007 -0500\n@@ -1,5 +1,7 @@ r\"\"\"\n r\"\"\"\n Graph Theory\n+\n+This module implements many graph theoretic operations and concepts.\n \n AUTHOR:\n     -- Robert L. Miller (2006-10-22): initial version\n@@ -26,14 +28,9 @@ AUTHOR:\n     -- Bobby Moretti (2007-08-12): fixed up plotting of graphs with\n        edge colors differentiated by label\n \n-\n-TUTORIAL:\n-\n-    I. The Basics\n-    \n-        1. Graph Format\n-        \n-            A. The SAGE Graph Class: NetworkX plus\n+\\subsection{Graph Format}\n+\n+\\subsubsection{The SAGE Graph Class: NetworkX plus}\n             \n             SAGE graphs are actually NetworkX graphs, wrapped in a SAGE class.\n             In fact, any graph can produce its underlying NetworkX graph. For example,\n@@ -51,40 +48,48 @@ TUTORIAL:\n \n             Each dictionary key is a vertex label, and each key in the following\n             dictionary is a neighbor of that vertex. In undirected graphs, there\n-            is reduncancy: for example, the dictionary containing the entry\n-            1: {2: None} implies it must contain 2: {1: None}. The innermost entry\n-            of None is related to edge labelling (see section I.3.).\n-        \n-            B. Supported formats\n+            is redundancy: for example, the dictionary containing the entry\n+            \\verb|1: {2: None}| implies it must contain \\verb|{2: {1: None}|. \n+            The innermost entry of \\var{None} is related to edge labeling \n+            (see section \\ref{Graph:labels}).\n+\n+            \\subsubsection{Supported formats}\n+        \n             \n             SAGE Graphs can be created from a wide range of inputs. A few examples are\n             covered here.\n+\n+            \\begin{itemize}\n             \n-                i.   a. NetworkX dictionary format:\n+                  \\item NetworkX dictionary format:\n                 \n-                sage: d = {0: [1,4,5], 1: [2,6], 2: [3,7], 3: [4,8], 4: [9], 5: [7, 8], 6: [8,9], 7: [9]}\n+                sage: d = {0: [1,4,5], 1: [2,6], 2: [3,7], 3: [4,8], 4: [9], \\\n+                      5: [7, 8], 6: [8,9], 7: [9]}\n                 sage: G = Graph(d); G\n                 Graph on 10 vertices\n                 sage: G.plot().save('sage.png')    # or G.show()\n                 \n-                    b. A NetworkX graph:\n+                    \\item A NetworkX graph:\n                 \n                 sage: K = networkx.complete_bipartite_graph(12,7)\n                 sage: G = Graph(K)\n                 sage: G.degree()\n                 [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 12, 12, 12, 12, 12, 12, 12]\n-                \n-                ii. graph6 or sparse6 format:\n+\n+                \\item graph6 or sparse6 format:\n                 \n                 sage: s = ':I`AKGsaOs`cI]Gb~'\n                 sage: G = Graph(s); G\n                 Looped multi-graph on 10 vertices\n                 sage: G.plot().save('sage.png')    # or G.show()\n                 \n-                iii. adjacency matrix: In an adjacency matrix, each column and each row represent\n+                \\item adjacency matrix In an adjacency matrix, each column and each row represent\n                 a vertex. If a 1 shows up in row i, column j, there is an edge (i,j).\n                 \n-                sage: M = Matrix([(0,1,0,0,1,1,0,0,0,0),(1,0,1,0,0,0,1,0,0,0),(0,1,0,1,0,0,0,1,0,0),(0,0,1,0,1,0,0,0,1,0),(1,0,0,1,0,0,0,0,0,1),(1,0,0,0,0,0,0,1,1,0),(0,1,0,0,0,0,0,0,1,1),(0,0,1,0,0,1,0,0,0,1),(0,0,0,1,0,1,1,0,0,0),(0,0,0,0,1,0,1,1,0,0)])\n+                sage: M = Matrix([(0,1,0,0,1,1,0,0,0,0),(1,0,1,0,0,0,1,0,0,0), \\\n+                (0,1,0,1,0,0,0,1,0,0), (0,0,1,0,1,0,0,0,1,0),(1,0,0,1,0,0,0,0,0,1), \\\n+                (1,0,0,0,0,0,0,1,1,0), (0,1,0,0,0,0,0,0,1,1),(0,0,1,0,0,1,0,0,0,1), \\\n+                (0,0,0,1,0,1,1,0,0,0), (0,0,0,0,1,0,1,1,0,0)])\n                 sage: M\n                 [0 1 0 0 1 1 0 0 0 0]\n                 [1 0 1 0 0 0 1 0 0 0]\n@@ -100,10 +105,15 @@ TUTORIAL:\n                 Graph on 10 vertices\n                 sage: G.plot().save('sage.png')    # or G.show()\n                 \n-                iv. incidence matrix: In an incidence matrix, each row represents a vertex\n+                \\item incidence matrix: In an incidence matrix, each row represents a vertex\n                 and each column reprensents an edge.\n                 \n-                sage: M = Matrix([(-1,0,0,0,1,0,0,0,0,0,-1,0,0,0,0),(1,-1,0,0,0,0,0,0,0,0,0,-1,0,0,0),(0,1,-1,0,0,0,0,0,0,0,0,0,-1,0,0),(0,0,1,-1,0,0,0,0,0,0,0,0,0,-1,0),(0,0,0,1,-1,0,0,0,0,0,0,0,0,0,-1),(0,0,0,0,0,-1,0,0,0,1,1,0,0,0,0),(0,0,0,0,0,0,0,1,-1,0,0,1,0,0,0),(0,0,0,0,0,1,-1,0,0,0,0,0,1,0,0),(0,0,0,0,0,0,0,0,1,-1,0,0,0,1,0),(0,0,0,0,0,0,1,-1,0,0,0,0,0,0,1)])\n+                sage: M = Matrix([(-1,0,0,0,1,0,0,0,0,0,-1,0,0,0,0), \\\n+                (1,-1,0,0,0,0,0,0,0,0,0,-1,0,0,0),(0,1,-1,0,0,0,0,0,0,0,0,0,-1,0,0), \\\n+                (0,0,1,-1,0,0,0,0,0,0,0,0,0,-1,0),(0,0,0,1,-1,0,0,0,0,0,0,0,0,0,-1), \\\n+                (0,0,0,0,0,-1,0,0,0,1,1,0,0,0,0),(0,0,0,0,0,0,0,1,-1,0,0,1,0,0,0), \\\n+                (0,0,0,0,0,1,-1,0,0,0,0,0,1,0,0),(0,0,0,0,0,0,0,0,1,-1,0,0,0,1,0), \\\n+                (0,0,0,0,0,0,1,-1,0,0,0,0,0,0,1)])\n                 sage: M\n                 [-1  0  0  0  1  0  0  0  0  0 -1  0  0  0  0]\n                 [ 1 -1  0  0  0  0  0  0  0  0  0 -1  0  0  0]\n@@ -118,14 +128,16 @@ TUTORIAL:\n                 sage: G = Graph(M); G\n                 Graph on 10 vertices\n                 sage: G.plot().save('sage.png')    # or G.show()\n-        \n-        2. Generators\n+\n+        \\end{itemize}\n+\n+        \\subsection{Generators}\n         \n         For some commonly used graphs to play with, type\n         \n             sage.: graphs.\n         \n-        and hit <tab>. Most of these graphs come with their own custom plot, so you\n+        and hit \\kbd{tab}. Most of these graphs come with their own custom plot, so you\n         can see how people usually visualize these graphs.\n         \n             sage: G = graphs.PetersenGraph()\n@@ -153,7 +165,7 @@ TUTORIAL:\n             sage: L = G.get_list(num_vertices=7, diameter=5)\n             sage.: graphs_list.show_graphs(L)\n         \n-        3. Labels\n+            \\subsection{Labels}\\label{Graph:labels}\n         \n         Each vertex can have any hashable object as a label. These are things like\n         strings, numbers, and tuples. Each edge is given a default label of \\var{None}, but\n@@ -171,7 +183,8 @@ TUTORIAL:\n         However, if one wants to define a dictionary, with the same keys and arbitrary objects\n         for entries, one can make that association:\n         \n-            sage: d = {0 : graphs.DodecahedralGraph(), 1 : graphs.FlowerSnark(),2 : graphs.MoebiusKantorGraph(), 3 : graphs.PetersenGraph() }\n+            sage: d = {0 : graphs.DodecahedralGraph(), 1 : graphs.FlowerSnark(), \\\n+                  2 : graphs.MoebiusKantorGraph(), 3 : graphs.PetersenGraph() }\n             sage: d[2]\n             Moebius-Kantor Graph: Graph on 16 vertices\n             sage: T = graphs.TetrahedralGraph()\n@@ -181,7 +194,7 @@ TUTORIAL:\n             sage: T.obj(1)\n             Flower Snark: Graph on 20 vertices\n         \n-        4. Database\n+        \\subsection{Database}\n         \n         There is a database available for searching for graphs that satisfy a certain set\n         of parameters, including number of vertices and edges, density, maximum and minimum\n@@ -190,28 +203,27 @@ TUTORIAL:\n         \n             sage.: graphs_query.\n         \n-        and hit tab.\n+        and hit \\kbd{tab}.\n \n             sage: graphs_query = GraphDatabase()\n             sage: L = graphs_query.get_list(num_vertices=7, diameter=5)\n             sage.: graphs_list.show_graphs(L)\n         \n-        5. Visualization\n-        \n-        To see a graph G you are working with, right now there are two main options:\n-        \n+        \\subsection{Visualization}\n+        \n+        To see a graph G you are working with, right now there are two main options.\n+        You can view the graph in two dimensions via matplotlib with \\method{show()}.\n+                \n             sage: G = graphs.RandomGNP(15,.3)\n-        \n-        You can view the graph in two dimensions via matplotlib:\n-        \n             sage.: G.show()\n         \n-        Or you can view it in three dimensions via Tachyon:\n+        Or you can view it in three dimensions via Tachyon with \\method{show3d()}.\n         \n             sage.: G.show3d()\n \n-NOTE: Many functions are passed directly on to NetworkX, and in this\n-case the documentation is based on the NetworkX docs.\n+            \\note{Many functions are passed directly on to NetworkX.\n+              In these cases, the documentation is based on the\n+              NetworkX docs.}\n \n \"\"\"\n \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/801\n\n",
    "created_at": "2007-10-03T07:30:06Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.6",
    "title": "[with patch] graphs: Latexify module-level documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/801",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

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


Issue created by migration from https://trac.sagemath.org/ticket/801





---

archive/issue_comments_004818.json:
```json
{
    "body": "Same patch as listed in the post.",
    "created_at": "2007-10-03T08:03:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/801#issuecomment-4818",
    "user": "https://github.com/jasongrout"
}
```

Same patch as listed in the post.



---

archive/issue_comments_004819.json:
```json
{
    "body": "Attachment [#801.patch](tarball://root/attachments/some-uuid/ticket801/#801.patch) by @williamstein created at 2007-10-04 14:56:43",
    "created_at": "2007-10-04T14:56:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/801#issuecomment-4819",
    "user": "https://github.com/williamstein"
}
```

Attachment [#801.patch](tarball://root/attachments/some-uuid/ticket801/#801.patch) by @williamstein created at 2007-10-04 14:56:43



---

archive/issue_comments_004820.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-04T19:53:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/801#issuecomment-4820",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_000912.json:
```json
{
    "actor": "@rlmill",
    "created_at": "2007-10-04T19:53:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/801",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/801#event-912"
}
```
