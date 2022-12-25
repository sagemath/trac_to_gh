# Issue 759: [with patch] graphs: density returns incorrect result for directed graphs.

archive/issues_000759.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: graphs\n\n```\n--- a/sage/graphs/graph.py      Fri Sep 28 10:30:09 2007 -0500\n+++ b/sage/graphs/graph.py      Fri Sep 28 13:48:53 2007 -0500\n@@ -451,7 +451,7 @@ class GenericGraph(SageObject):\n             Looped digraph on 0 vertices\n\n         \"\"\"\n-        if not new is None:\n+        if new is not None:\n             if new:\n                 self._nxg.allow_selfloops()\n             else:\n@@ -467,12 +467,18 @@ class GenericGraph(SageObject):\n             sage: d = {0: [1,4,5], 1: [2,6], 2: [3,7], 3: [4,8], 4: [9], 5: [7, 8], 6: [8,9], 7: [9]}\n             sage: G = Graph(d); G.density()\n             1/3\n+            sage: G = Graph({0:[1,2], 1:[0] }); G.density()\n+            2/3\n+            sage: G = DiGraph({0:[1,2], 1:[0] }); G.density()\n+            1/2\n\n         \"\"\"\n         from sage.rings.rational import Rational\n         n = self.order()\n-        n = (n**2 - n)/2\n-        return Rational(self.size())/Rational(n)\n+        if self.is_directed():\n+            return Rational(self.size())/Rational((n**2 -n))\n+        else:\n+            return Rational(self.size())/Rational((n**2 -n)/2)\n\n     def to_simple(self):\n         \"\"\"\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/759\n\n",
    "closed_at": "2007-10-04T19:52:53Z",
    "created_at": "2007-09-28T18:59:39Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.6",
    "title": "[with patch] graphs: density returns incorrect result for directed graphs.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/759",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

Keywords: graphs

```
--- a/sage/graphs/graph.py      Fri Sep 28 10:30:09 2007 -0500
+++ b/sage/graphs/graph.py      Fri Sep 28 13:48:53 2007 -0500
@@ -451,7 +451,7 @@ class GenericGraph(SageObject):
             Looped digraph on 0 vertices

         """
-        if not new is None:
+        if new is not None:
             if new:
                 self._nxg.allow_selfloops()
             else:
@@ -467,12 +467,18 @@ class GenericGraph(SageObject):
             sage: d = {0: [1,4,5], 1: [2,6], 2: [3,7], 3: [4,8], 4: [9], 5: [7, 8], 6: [8,9], 7: [9]}
             sage: G = Graph(d); G.density()
             1/3
+            sage: G = Graph({0:[1,2], 1:[0] }); G.density()
+            2/3
+            sage: G = DiGraph({0:[1,2], 1:[0] }); G.density()
+            1/2

         """
         from sage.rings.rational import Rational
         n = self.order()
-        n = (n**2 - n)/2
-        return Rational(self.size())/Rational(n)
+        if self.is_directed():
+            return Rational(self.size())/Rational((n**2 -n))
+        else:
+            return Rational(self.size())/Rational((n**2 -n)/2)

     def to_simple(self):
         """
```


Issue created by migration from https://trac.sagemath.org/ticket/759





---

archive/issue_comments_004486.json:
```json
{
    "body": "Same patch as listed in the post.",
    "created_at": "2007-10-03T07:51:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/759#issuecomment-4486",
    "user": "https://github.com/jasongrout"
}
```

Same patch as listed in the post.



---

archive/issue_comments_004487.json:
```json
{
    "body": "Attachment [#759.patch](tarball://root/attachments/some-uuid/ticket759/#759.patch) by @williamstein created at 2007-10-04 14:56:15",
    "created_at": "2007-10-04T14:56:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/759#issuecomment-4487",
    "user": "https://github.com/williamstein"
}
```

Attachment [#759.patch](tarball://root/attachments/some-uuid/ticket759/#759.patch) by @williamstein created at 2007-10-04 14:56:15



---

archive/issue_events_002069.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-04T14:56:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/759",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/759#event-2069"
}
```



---

archive/issue_comments_004488.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-04T14:56:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/759#issuecomment-4488",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_002070.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-04T14:56:15Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/759",
    "milestone": "sage-2.8.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/759#event-2070"
}
```



---

archive/issue_comments_004489.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-10-04T14:56:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/759#issuecomment-4489",
    "user": "https://github.com/williamstein"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_004490.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-10-04T14:56:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/759#issuecomment-4490",
    "user": "https://github.com/williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_events_002071.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-04T14:56:20Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/759",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/759#event-2071"
}
```



---

archive/issue_comments_004491.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-04T19:52:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/759#issuecomment-4491",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_002072.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2007-10-04T19:52:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/759",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/759#event-2072"
}
```



---

archive/issue_events_002073.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2007-10-05T02:11:07Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/759",
    "milestone": "sage-2.8.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/759#event-2073"
}
```



---

archive/issue_events_002074.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2007-10-05T02:11:07Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/759",
    "milestone": "sage-2.8.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/759#event-2074"
}
```
