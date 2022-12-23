# Issue 759: [patch] graphs: density returns incorrect result for directed graphs.

archive/issues_000759.json:
```json
{
    "body": "Assignee: was\n\nKeywords: graphs\n\n\n```\n--- a/sage/graphs/graph.py      Fri Sep 28 10:30:09 2007 -0500\n+++ b/sage/graphs/graph.py      Fri Sep 28 13:48:53 2007 -0500\n@@ -451,7 +451,7 @@ class GenericGraph(SageObject):\n             Looped digraph on 0 vertices\n\n         \"\"\"\n-        if not new is None:\n+        if new is not None:\n             if new:\n                 self._nxg.allow_selfloops()\n             else:\n@@ -467,12 +467,18 @@ class GenericGraph(SageObject):\n             sage: d = {0: [1,4,5], 1: [2,6], 2: [3,7], 3: [4,8], 4: [9], 5: [7, 8], 6: [8,9], 7: [9]}\n             sage: G = Graph(d); G.density()\n             1/3\n+            sage: G = Graph({0:[1,2], 1:[0] }); G.density()\n+            2/3\n+            sage: G = DiGraph({0:[1,2], 1:[0] }); G.density()\n+            1/2\n\n         \"\"\"\n         from sage.rings.rational import Rational\n         n = self.order()\n-        n = (n**2 - n)/2\n-        return Rational(self.size())/Rational(n)\n+        if self.is_directed():\n+            return Rational(self.size())/Rational((n**2 -n))\n+        else:\n+            return Rational(self.size())/Rational((n**2 -n)/2)\n\n     def to_simple(self):\n         \"\"\"\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/759\n\n",
    "created_at": "2007-09-28T18:59:39Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "[patch] graphs: density returns incorrect result for directed graphs.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/759",
    "user": "jason"
}
```
Assignee: was

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

archive/issue_comments_004502.json:
```json
{
    "body": "Same patch as listed in the post.",
    "created_at": "2007-10-03T07:51:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/759#issuecomment-4502",
    "user": "jason"
}
```

Same patch as listed in the post.



---

archive/issue_comments_004503.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-10-04T14:56:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/759#issuecomment-4503",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_004504.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-04T14:56:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/759#issuecomment-4504",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_004505.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-10-04T14:56:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/759#issuecomment-4505",
    "user": "was"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_004506.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-10-04T14:56:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/759#issuecomment-4506",
    "user": "was"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_004507.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-04T19:52:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/759#issuecomment-4507",
    "user": "rlm"
}
```

Resolution: fixed
