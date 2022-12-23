# Issue 878: [with patch] graphs: Correct a doctest failing on some systems due to different output ordering.

archive/issues_000878.json:
```json
{
    "body": "Assignee: was\n\nKeywords: graphs\n\n\n```\ndiff -r 04e9996b0332 sage/graphs/graph.py\n--- a/sage/graphs/graph.py      Sat Oct 13 13:12:24 2007 -0500\n+++ b/sage/graphs/graph.py      Sat Oct 13 13:39:03 2007 -0500\n@@ -2114,11 +2114,13 @@ class GenericGraph(SageObject):\n             (2, 3, None),\n             (2, 4, None),\n             (3, 4, None)]\n-            sage: h.edges()\n-            [((2, 3, None), (3, 4, None), None),\n-            ((1, 2, None), (2, 4, None), None),\n-            ((1, 2, None), (2, 3, None), None),\n-            ((1, 3, None), (3, 4, None), None)]\n+            sage: sage: h.am()\n+            [0 0 0 1 1 0]\n+            [0 0 0 0 0 1]\n+            [0 0 0 0 0 0]\n+            [0 0 0 0 0 1]\n+            [0 0 0 0 0 0]\n+            [0 0 0 0 0 0]\n\n         \"\"\"\n         if self.is_directed():\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/878\n\n",
    "created_at": "2007-10-13T18:44:34Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "[with patch] graphs: Correct a doctest failing on some systems due to different output ordering.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/878",
    "user": "jason"
}
```
Assignee: was

Keywords: graphs


```
diff -r 04e9996b0332 sage/graphs/graph.py
--- a/sage/graphs/graph.py      Sat Oct 13 13:12:24 2007 -0500
+++ b/sage/graphs/graph.py      Sat Oct 13 13:39:03 2007 -0500
@@ -2114,11 +2114,13 @@ class GenericGraph(SageObject):
             (2, 3, None),
             (2, 4, None),
             (3, 4, None)]
-            sage: h.edges()
-            [((2, 3, None), (3, 4, None), None),
-            ((1, 2, None), (2, 4, None), None),
-            ((1, 2, None), (2, 3, None), None),
-            ((1, 3, None), (3, 4, None), None)]
+            sage: sage: h.am()
+            [0 0 0 1 1 0]
+            [0 0 0 0 0 1]
+            [0 0 0 0 0 0]
+            [0 0 0 0 0 1]
+            [0 0 0 0 0 0]
+            [0 0 0 0 0 0]

         """
         if self.is_directed():
```



Issue created by migration from https://trac.sagemath.org/ticket/878





---

archive/issue_comments_005438.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2007-10-13T19:17:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/878#issuecomment-5438",
    "user": "cwitty"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_005439.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-14T04:21:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/878#issuecomment-5439",
    "user": "was"
}
```

Resolution: fixed
