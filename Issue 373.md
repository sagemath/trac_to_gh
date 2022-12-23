# Issue 373: pi coercion issues

Issue created by migration from https://trac.sagemath.org/ticket/373

Original creator: moretti

Original creation time: 2007-05-22 00:12:04

Assignee: moretti

Keywords: constants, pi




```
g = pi == 2*x
g.solve()
///
Traceback (most recent call last):    g.solve()
 File "element.pyx", line 413, in element.Element.__richcmp__
 File "element.pyx", line 376, in element.Element._richcmp
 File "/sage/local/lib/python2.5/site-packages/sage/functions/functions.py",
line 269, in __cmp__
   c = cmp(R(self), R(right))
 File "real_mpfr.pyx", line 222, in real_mpfr.RealField.__call__
 File "/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py",
line 2461, in _mpfr_
   return self.simplify()._mpfr_(field)
 File "/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py",
line 2462, in _mpfr_
   rops = [op._mpfr_(field) for op in self._operands]
 File "/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py",
line 652, in _mpfr_
   raise TypeError
TypeError
```



---

Comment by was created at 2007-05-23 01:58:36

Note that the following works,

```
sage: g = 2*x == pi
sage: g
2*x == pi
sage: g.solve()
[x == (pi/2)]
```


thus the bug is in the __cmp__ function for pi, which is probably wrong / left over
from before the symbolic package.  This function should be updated. 

William


---

Comment by was created at 2007-05-23 04:40:25

Resolution: fixed


---

Comment by was created at 2007-05-23 04:40:25

OK, fixed.

```
was@ubuntu:~/d/sage/sage/functions$ hg export 4574
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1179895122 25200
# Node ID 3d5ff8c3011e00f4cd45615429c05416fa52646d
# Parent  6219a384a063254b7da5c5ec53736e9899e8e980
Symbolics: fixed issue with constant comparisons.

diff -r 6219a384a063 -r 3d5ff8c3011e sage/functions/constants.py
--- a/sage/functions/constants.py       Tue May 22 15:24:49 2007 -0700
+++ b/sage/functions/constants.py       Tue May 22 21:38:42 2007 -0700
@@ -351,6 +351,32 @@ class Constant(Function):
         """
         return False

+    def __lt__(self, right):
+        return self._ser().__lt__(right)
+
+    def __le__(self, right):
+        return self._ser().__le__(right)
+
+    def __eq__(self, right):
+        """
+        EXAMPLES:
+            sage: solve(pi == 2*x)
+            [x == (pi/2)]
+            sage: solve(cos(x^2) == pi)
+            [x == (-sqrt(acos(pi))), x == sqrt(acos(pi))]
+        """
+        return self._ser().__eq__(right)
+
+    def __ne__(self, right):
+        return self._ser().__ne__(right)
+
+    def __ge__(self, right):
+        return self._ser().__ge__(right)
+
+    def __gt__(self, right):
+        return self._ser().__gt__(right)
+
+

 class Constant_gen(Constant, Function_gen):
     def __init__(self, x):
```

