# Issue 759: [patch] graphs: density returns incorrect result for directed graphs.

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-09-28 18:59:39

Assignee: was

Keywords: graphs


```
--- a/sage/graphs/graph.py      Fri Sep 28 10:30:09 2007 -0500
+++ b/sage/graphs/graph.py      Fri Sep 28 13:48:53 2007 -0500
`@``@` -451,7 +451,7 `@``@` class GenericGraph(SageObject):
             Looped digraph on 0 vertices

         """
-        if not new is None:
+        if new is not None:
             if new:
                 self._nxg.allow_selfloops()
             else:
`@``@` -467,12 +467,18 `@``@` class GenericGraph(SageObject):
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




---

Comment by jason created at 2007-10-03 07:51:45

Same patch as listed in the post.


---

Attachment


---

Comment by was created at 2007-10-04 14:56:15

Resolution: fixed


---

Comment by was created at 2007-10-04 14:56:20

Resolution changed from fixed to 


---

Comment by was created at 2007-10-04 14:56:20

Changing status from closed to reopened.


---

Comment by rlm created at 2007-10-04 19:52:53

Resolution: fixed
