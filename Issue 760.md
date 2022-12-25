# Issue 760: [patch] graphs: a small change to subgraphs allow it to default to the original graph.

archive/issues_000760.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\n--- a/sage/graphs/graph.py      Fri Sep 28 14:05:12 2007 -0500\n+++ b/sage/graphs/graph.py      Fri Sep 28 14:35:19 2007 -0500\n@@ -3974,7 +3974,7 @@ class Graph(GenericGraph):\n         \"\"\"\n         self._nxg.add_path(vertices)\n\n-    def subgraph(self, vertices, inplace=False, create_using=None):\n+    def subgraph(self, vertices=None, inplace=False, create_using=None):\n         \"\"\"\n         Returns the subgraph induced by the given vertices.\n\n@@ -3983,7 +3983,7 @@ class Graph(GenericGraph):\n         and edges from the current graph. This will modify the graph, and re-\n         turn itself.\n         vertices -- Vertices can be a single vertex or an iterable container\n-        of vertices, e.g. a list, set, graph, file or numeric array.\n+        of vertices, e.g. a list, set, graph, file or numeric array.  If not passed, defaults to the entire graph.\n         create_using -- Can be an existing graph object or a call to a graph\n         object, such as create_using=DiGraph(). Must be a NetworkX object.\n\n@@ -3998,6 +3998,8 @@ class Graph(GenericGraph):\n             sage: G\n             Subgraph of (Complete graph): Graph on 3 vertices\n             sage: G is K\n+            True\n+            sage: G.subgraph()==G\n             True\n\n         \"\"\"\n@@ -5424,7 +5426,7 @@ class DiGraph(GenericGraph):\n         G = DiGraph(NXG)\n         return G\n\n-    def subgraph(self, vertices, inplace=False, create_using=None):\n+    def subgraph(self, vertices=None, inplace=False, create_using=None):\n         \"\"\"\n         Returns the subgraph induced by the given vertices.\n\n@@ -5433,7 +5435,7 @@ class DiGraph(GenericGraph):\n         and edges from the current graph. This will modify the graph, and re-\n         turn itself.\n         vertices -- Vertices can be a single vertex or an iterable container\n-        of vertices, e.g. a list, set, graph, file or numeric array.\n+        of vertices, e.g. a list, set, graph, file or numeric array.  If not passed, defaults to the entire graph.\n         create_using -- Can be an existing graph object or a call to a graph\n         object, such as create_using=DiGraph().\n\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/760\n\n",
    "created_at": "2007-09-28T19:43:44Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.6",
    "title": "[patch] graphs: a small change to subgraphs allow it to default to the original graph.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/760",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

```
--- a/sage/graphs/graph.py      Fri Sep 28 14:05:12 2007 -0500
+++ b/sage/graphs/graph.py      Fri Sep 28 14:35:19 2007 -0500
@@ -3974,7 +3974,7 @@ class Graph(GenericGraph):
         """
         self._nxg.add_path(vertices)

-    def subgraph(self, vertices, inplace=False, create_using=None):
+    def subgraph(self, vertices=None, inplace=False, create_using=None):
         """
         Returns the subgraph induced by the given vertices.

@@ -3983,7 +3983,7 @@ class Graph(GenericGraph):
         and edges from the current graph. This will modify the graph, and re-
         turn itself.
         vertices -- Vertices can be a single vertex or an iterable container
-        of vertices, e.g. a list, set, graph, file or numeric array.
+        of vertices, e.g. a list, set, graph, file or numeric array.  If not passed, defaults to the entire graph.
         create_using -- Can be an existing graph object or a call to a graph
         object, such as create_using=DiGraph(). Must be a NetworkX object.

@@ -3998,6 +3998,8 @@ class Graph(GenericGraph):
             sage: G
             Subgraph of (Complete graph): Graph on 3 vertices
             sage: G is K
+            True
+            sage: G.subgraph()==G
             True

         """
@@ -5424,7 +5426,7 @@ class DiGraph(GenericGraph):
         G = DiGraph(NXG)
         return G

-    def subgraph(self, vertices, inplace=False, create_using=None):
+    def subgraph(self, vertices=None, inplace=False, create_using=None):
         """
         Returns the subgraph induced by the given vertices.

@@ -5433,7 +5435,7 @@ class DiGraph(GenericGraph):
         and edges from the current graph. This will modify the graph, and re-
         turn itself.
         vertices -- Vertices can be a single vertex or an iterable container
-        of vertices, e.g. a list, set, graph, file or numeric array.
+        of vertices, e.g. a list, set, graph, file or numeric array.  If not passed, defaults to the entire graph.
         create_using -- Can be an existing graph object or a call to a graph
         object, such as create_using=DiGraph().

```

Issue created by migration from https://trac.sagemath.org/ticket/760





---

archive/issue_comments_004492.json:
```json
{
    "body": "Changing priority from major to trivial.",
    "created_at": "2007-09-28T19:44:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/760#issuecomment-4492",
    "user": "https://github.com/jasongrout"
}
```

Changing priority from major to trivial.



---

archive/issue_comments_004493.json:
```json
{
    "body": "Same patch as listed in the post.",
    "created_at": "2007-10-03T07:52:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/760#issuecomment-4493",
    "user": "https://github.com/jasongrout"
}
```

Same patch as listed in the post.



---

archive/issue_comments_004494.json:
```json
{
    "body": "Attachment [#760.patch](tarball://root/attachments/some-uuid/ticket760/#760.patch) by @williamstein created at 2007-10-04 14:57:55",
    "created_at": "2007-10-04T14:57:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/760#issuecomment-4494",
    "user": "https://github.com/williamstein"
}
```

Attachment [#760.patch](tarball://root/attachments/some-uuid/ticket760/#760.patch) by @williamstein created at 2007-10-04 14:57:55



---

archive/issue_events_002075.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-04T14:57:55Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/760",
    "milestone": "sage-2.8.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/760#event-2075"
}
```



---

archive/issue_events_002076.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2007-10-04T19:54:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/760",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/760#event-2076"
}
```



---

archive/issue_comments_004495.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-04T19:54:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/760#issuecomment-4495",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_002077.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2007-10-05T02:11:45Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/760",
    "milestone": "sage-2.8.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/760#event-2077"
}
```



---

archive/issue_events_002078.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2007-10-05T02:11:45Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/760",
    "milestone": "sage-2.8.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/760#event-2078"
}
```
