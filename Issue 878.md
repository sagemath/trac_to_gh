# Issue 878: [with patch] graphs: Correct a doctest failing on some systems due to different output ordering.

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-10-13 18:44:34

Assignee: was

Keywords: graphs


```
diff -r 04e9996b0332 sage/graphs/graph.py
--- a/sage/graphs/graph.py      Sat Oct 13 13:12:24 2007 -0500
+++ b/sage/graphs/graph.py      Sat Oct 13 13:39:03 2007 -0500
`@``@` -2114,11 +2114,13 `@``@` class GenericGraph(SageObject):
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




---

Comment by cwitty created at 2007-10-13 19:17:02

Changing priority from major to blocker.


---

Comment by was created at 2007-10-14 04:21:21

Resolution: fixed
