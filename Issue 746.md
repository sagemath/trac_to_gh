# Issue 746: graphs: graph name is not reset using clear()

archive/issues_000746.json:
```json
{
    "body": "Assignee: was\n\nKeywords: graphs\n\nSince networkX uses the empty string for an unset name, while the current SAGE code uses None for an unset name, calling _nxg.clear() in the clear() function will not reset the name to None, but to ''.\n\nThere are also other problems with having an unset name represented by None (mostly because networkX assumes that '' is an unset name).\n\nIssue created by migration from https://trac.sagemath.org/ticket/746\n\n",
    "created_at": "2007-09-24T20:54:44Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "graphs: graph name is not reset using clear()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/746",
    "user": "jason"
}
```
Assignee: was

Keywords: graphs

Since networkX uses the empty string for an unset name, while the current SAGE code uses None for an unset name, calling _nxg.clear() in the clear() function will not reset the name to None, but to ''.

There are also other problems with having an unset name represented by None (mostly because networkX assumes that '' is an unset name).

Issue created by migration from https://trac.sagemath.org/ticket/746





---

archive/issue_comments_004370.json:
```json
{
    "body": "--- a/sage/graphs/graph.py      Wed Sep 26 09:37:18 2007 -0700\n+++ b/sage/graphs/graph.py      Fri Sep 28 13:45:19 2007 -0500\n`@``@` -684,10 +684,34 `@``@` class GenericGraph(SageObject):\n\n     def clear(self):\n         \"\"\"\n-        Empties the graph of vertices and edges, removes name.\n+        Empties the graph of vertices and edges and removes name,\n+        boundary, associated objects, and position information.\n+\n+        EXAMPLE:\n+            sage: G=graphs.CycleGraph(4); G.associate({0:'vertex0'})\n+            sage: G.order(); G.size()\n+            4\n+            4\n+            sage: len(G._pos)\n+            4\n+            sage: G.name()\n+            'Cycle graph'\n+            sage: G.obj(0)\n+            'vertex0'\n+            sage: G.clear()\n+            sage: G.order(); G.size()\n+            0\n+            0\n+            sage: len(G._pos)\n+            0\n+            sage: G.name()\n+            sage: G.obj(0)\n\n         \"\"\"\n         self._nxg.clear()\n+        self._pos=[]\n+        self._boundary=[]\n+        self._assoc=None\n\n     def neighbors(self, vertex):\n         \"\"\"",
    "created_at": "2007-09-28T18:55:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/746#issuecomment-4370",
    "user": "jason"
}
```

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

archive/issue_comments_004371.json:
```json
{
    "body": "Let's try that again:\n\n\n```\n--- a/sage/graphs/graph.py      Wed Sep 26 09:37:18 2007 -0700\n+++ b/sage/graphs/graph.py      Fri Sep 28 13:46:41 2007 -0500\n@@ -684,10 +684,34 @@ class GenericGraph(SageObject):\n\n     def clear(self):\n         \"\"\"\n-        Empties the graph of vertices and edges, removes name.\n+        Empties the graph of vertices and edges and removes name,\n+        boundary, associated objects, and position information.\n+\n+        EXAMPLE:\n+            sage: G=graphs.CycleGraph(4); G.associate({0:'vertex0'})\n+            sage: G.order(); G.size()\n+            4\n+            4\n+            sage: len(G._pos)\n+            4\n+            sage: G.name()\n+            'Cycle graph'\n+            sage: G.obj(0)\n+            'vertex0'\n+            sage: G.clear()\n+            sage: G.order(); G.size()\n+            0\n+            0\n+            sage: len(G._pos)\n+            0\n+            sage: G.name()\n+            sage: G.obj(0)\n\n         \"\"\"\n         self._nxg.clear()\n+        self._pos=[]\n+        self._boundary=[]\n+        self._assoc=None\n\n     def neighbors(self, vertex):\n         \"\"\"\n```\n",
    "created_at": "2007-09-28T18:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/746#issuecomment-4371",
    "user": "jason"
}
```

Let's try that again:


```
--- a/sage/graphs/graph.py      Wed Sep 26 09:37:18 2007 -0700
+++ b/sage/graphs/graph.py      Fri Sep 28 13:46:41 2007 -0500
@@ -684,10 +684,34 @@ class GenericGraph(SageObject):

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

archive/issue_comments_004372.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-04T19:52:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/746#issuecomment-4372",
    "user": "rlm"
}
```

Resolution: fixed
