# Issue 373: pi coercion issues

archive/issues_000373.json:
```json
{
    "body": "Assignee: @bobmoretti\n\nKeywords: constants, pi\n\n\n\n```\ng = pi == 2*x\ng.solve()\n///\nTraceback (most recent call last):    g.solve()\n File \"element.pyx\", line 413, in element.Element.__richcmp__\n File \"element.pyx\", line 376, in element.Element._richcmp\n File \"/sage/local/lib/python2.5/site-packages/sage/functions/functions.py\",\nline 269, in __cmp__\n   c = cmp(R(self), R(right))\n File \"real_mpfr.pyx\", line 222, in real_mpfr.RealField.__call__\n File \"/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py\",\nline 2461, in _mpfr_\n   return self.simplify()._mpfr_(field)\n File \"/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py\",\nline 2462, in _mpfr_\n   rops = [op._mpfr_(field) for op in self._operands]\n File \"/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py\",\nline 652, in _mpfr_\n   raise TypeError\nTypeError\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/373\n\n",
    "created_at": "2007-05-22T00:12:04Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.5.3",
    "title": "pi coercion issues",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/373",
    "user": "https://github.com/bobmoretti"
}
```
Assignee: @bobmoretti

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

Issue created by migration from https://trac.sagemath.org/ticket/373





---

archive/issue_comments_001775.json:
```json
{
    "body": "Note that the following works,\n\n```\nsage: g = 2*x == pi\nsage: g\n2*x == pi\nsage: g.solve()\n[x == (pi/2)]\n```\n\nthus the bug is in the __cmp__ function for pi, which is probably wrong / left over\nfrom before the symbolic package.  This function should be updated. \n\nWilliam",
    "created_at": "2007-05-23T01:58:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/373#issuecomment-1775",
    "user": "https://github.com/williamstein"
}
```

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

archive/issue_comments_001776.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-05-23T04:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/373#issuecomment-1776",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000864.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-05-23T04:40:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/373",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/373#event-864"
}
```



---

archive/issue_comments_001777.json:
```json
{
    "body": "OK, fixed.\n\n```\nwas@ubuntu:~/d/sage/sage/functions$ hg export 4574\n# HG changeset patch\n# User William Stein <wstein@gmail.com>\n# Date 1179895122 25200\n# Node ID 3d5ff8c3011e00f4cd45615429c05416fa52646d\n# Parent  6219a384a063254b7da5c5ec53736e9899e8e980\nSymbolics: fixed issue with constant comparisons.\n\ndiff -r 6219a384a063 -r 3d5ff8c3011e sage/functions/constants.py\n--- a/sage/functions/constants.py       Tue May 22 15:24:49 2007 -0700\n+++ b/sage/functions/constants.py       Tue May 22 21:38:42 2007 -0700\n@@ -351,6 +351,32 @@ class Constant(Function):\n         \"\"\"\n         return False\n\n+    def __lt__(self, right):\n+        return self._ser().__lt__(right)\n+\n+    def __le__(self, right):\n+        return self._ser().__le__(right)\n+\n+    def __eq__(self, right):\n+        \"\"\"\n+        EXAMPLES:\n+            sage: solve(pi == 2*x)\n+            [x == (pi/2)]\n+            sage: solve(cos(x^2) == pi)\n+            [x == (-sqrt(acos(pi))), x == sqrt(acos(pi))]\n+        \"\"\"\n+        return self._ser().__eq__(right)\n+\n+    def __ne__(self, right):\n+        return self._ser().__ne__(right)\n+\n+    def __ge__(self, right):\n+        return self._ser().__ge__(right)\n+\n+    def __gt__(self, right):\n+        return self._ser().__gt__(right)\n+\n+\n\n class Constant_gen(Constant, Function_gen):\n     def __init__(self, x):\n```",
    "created_at": "2007-05-23T04:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/373#issuecomment-1777",
    "user": "https://github.com/williamstein"
}
```

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
