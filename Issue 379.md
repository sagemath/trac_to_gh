# Issue 379: bug in formal equality

Issue created by migration from https://trac.sagemath.org/ticket/379

Original creator: was

Original creation time: 2007-05-26 02:27:53

Assignee: was

Timothy Clemans found the following bug:

```
sage: 3 == x
False
sage: x == 3
x == 3
```



---

Comment by was created at 2007-05-31 14:49:08

Resolution: fixed


---

Comment by was created at 2007-05-31 14:49:08

fixed.


```
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1180622669 25200
# Node ID 872bacf13e2081c7f731ce8f4e23a244eba23ecb
# Parent  84924f963b06ddc18de29c7d7f803a4554e46d81
Fix comparison bug in notebook where 3 == x and x == 3 were different.

diff -r 84924f963b06 -r 872bacf13e20 sage/calculus/calculus.py
--- a/sage/calculus/calculus.py Thu May 31 07:07:20 2007 -0700
+++ b/sage/calculus/calculus.py Thu May 31 07:44:29 2007 -0700
@@ -570,6 +570,34 @@ class SymbolicExpression(RingElement):
             0
         """
         return cmp(maxima(self), maxima(right))
+
+    def _richcmp_(left, right, op):
+        """
+        TESTS:
+            sage: 3 < x
+            3 < x
+            sage: 3 <= x
+            3 <= x
+            sage: 3 == x
+            3 == x
+            sage: 3 >= x
+            3 >= x
+            sage: 3 > x
+            3 > x
+        """
+        if op == 0:  #<
+            return left < right
+        elif op == 2: #==
+            return left == right
+        elif op == 4: #>
+            return left > right
+        elif op == 1: #<=
+            return left <= right
+        elif op == 3: #!=
+            return left != right
+        elif op == 5: #>=
+            return left >= right
+

     def _neg_(self):
         """
```

