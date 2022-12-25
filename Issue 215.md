# Issue 215: Pari comparison with None crashes

archive/issues_000215.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: pari, comparison\n\nI'm not sure what the correct outcome of this should be:\n\n```\npari(2.5) > None\n```\n\nbut it shouldn't crash SAGE, which is what it does now.\n\nIssue created by migration from https://trac.sagemath.org/ticket/215\n\n",
    "created_at": "2007-01-24T23:49:19Z",
    "labels": [
        "component: interfaces",
        "trivial",
        "bug"
    ],
    "title": "Pari comparison with None crashes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/215",
    "user": "https://github.com/kedlaya"
}
```
Assignee: @williamstein

Keywords: pari, comparison

I'm not sure what the correct outcome of this should be:

```
pari(2.5) > None
```

but it shouldn't crash SAGE, which is what it does now.

Issue created by migration from https://trac.sagemath.org/ticket/215





---

archive/issue_comments_000957.json:
```json
{
    "body": "fixed for sage > 1.8.2.1\n\n```\n# HG changeset patch\n# User William Stein <wstein@gmail.com>\n# Date 1169737969 28800\n# Node ID 77fad05c682bd6d4d76524f689941195f82778e6\n# Parent  9839fc0f4341de039cb16097a9d1b70f89a2ba9b\nFix trac issue #215 -- pari(2.5) > None caused crash.\n\ndiff -r 9839fc0f4341 -r 77fad05c682b sage/libs/pari/gen.pxd\n--- a/sage/libs/pari/gen.pxd    Thu Jan 25 06:36:25 2007 -0800\n+++ b/sage/libs/pari/gen.pxd    Thu Jan 25 07:12:49 2007 -0800\n@@ -12,7 +12,6 @@ cdef class gen:\n     cdef GEN _deepcopy_to_python_heap(self, GEN x, pari_sp* address)\n     cdef int get_var(self, v)    \n \n-\n cdef class PariInstance:\n     cdef gen ZERO, ONE, TWO\n     cdef gen new_gen(self, GEN x)\ndiff -r 9839fc0f4341 -r 77fad05c682b sage/libs/pari/gen.pyx\n--- a/sage/libs/pari/gen.pyx    Thu Jan 25 06:36:25 2007 -0800\n+++ b/sage/libs/pari/gen.pyx    Thu Jan 25 07:12:49 2007 -0800\n@@ -451,28 +451,44 @@ cdef class gen:\n         \n \n     ###########################################\n-    # ?\n+    # comparisions\n+    # I had to put the call to gcmp in another\n+    # function since otherwise I can't trap\n+    # the PariError it will sometimes raise.\n+    # (This might be a bug/shortcoming to SageX.)\n+    # Annoyingly the _cmp method always has\n+    # to be not cdef'd. \n     ###########################################\n+\n+    def _cmp(gen self, gen other):\n+        cdef int result\n+        _sig_on\n+        result = gcmp(self.g, other.g)\n+        _sig_off\n+        return result\n     \n     def __cmp__(gen self, gen other):\n         \"\"\"\n         Comparisons\n \n-        Compares the underlying strings unless the inputs\n-        are integer, real, or fraction (quotient of integers).\n-        \"\"\"\n-        if gegal(self.g, other.g):\n-            return 0\n-        cdef int tg, to, a\n-        tg = typ(self.g)\n-        to = typ(other.g)\n-\n-        cdef int t_g, t_o\n-        t_g = typ(self.g); t_o = typ(other.g)\n-        if (t_g == t_INT or t_g == t_REAL or t_g == t_FRAC) and \\\n-           (t_o == t_INT or t_g == t_REAL or t_g == t_FRAC):\n-            return gcmp(self.g, other.g)\n-\n+        First uses PARI's cmp routine; if it decides the objects are\n+        not comparable, it then compares the underlying strings (since\n+        in Python all objects are supposed to be comparable).\n+\n+        EXAMPLES:\n+            sage: pari(2.5) > None\n+            False\n+            sage: pari(3) == pari(3)\n+            True\n+            sage: pari('x^2 + 1') == pari('I-1')\n+            False\n+            sage: pari(I) == pari(I)\n+            True           \n+        \"\"\"\n+        try:\n+            return self._cmp(other)\n+        except PariError:\n+            pass\n         return cmp(str(self),str(other))\n \n     def __richcmp__(gen self, other, int op):\n```\n",
    "created_at": "2007-01-25T15:16:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/215",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/215#issuecomment-957",
    "user": "https://github.com/williamstein"
}
```

fixed for sage > 1.8.2.1

```
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1169737969 28800
# Node ID 77fad05c682bd6d4d76524f689941195f82778e6
# Parent  9839fc0f4341de039cb16097a9d1b70f89a2ba9b
Fix trac issue #215 -- pari(2.5) > None caused crash.

diff -r 9839fc0f4341 -r 77fad05c682b sage/libs/pari/gen.pxd
--- a/sage/libs/pari/gen.pxd    Thu Jan 25 06:36:25 2007 -0800
+++ b/sage/libs/pari/gen.pxd    Thu Jan 25 07:12:49 2007 -0800
@@ -12,7 +12,6 @@ cdef class gen:
     cdef GEN _deepcopy_to_python_heap(self, GEN x, pari_sp* address)
     cdef int get_var(self, v)    
 
-
 cdef class PariInstance:
     cdef gen ZERO, ONE, TWO
     cdef gen new_gen(self, GEN x)
diff -r 9839fc0f4341 -r 77fad05c682b sage/libs/pari/gen.pyx
--- a/sage/libs/pari/gen.pyx    Thu Jan 25 06:36:25 2007 -0800
+++ b/sage/libs/pari/gen.pyx    Thu Jan 25 07:12:49 2007 -0800
@@ -451,28 +451,44 @@ cdef class gen:
         
 
     ###########################################
-    # ?
+    # comparisions
+    # I had to put the call to gcmp in another
+    # function since otherwise I can't trap
+    # the PariError it will sometimes raise.
+    # (This might be a bug/shortcoming to SageX.)
+    # Annoyingly the _cmp method always has
+    # to be not cdef'd. 
     ###########################################
+
+    def _cmp(gen self, gen other):
+        cdef int result
+        _sig_on
+        result = gcmp(self.g, other.g)
+        _sig_off
+        return result
     
     def __cmp__(gen self, gen other):
         """
         Comparisons
 
-        Compares the underlying strings unless the inputs
-        are integer, real, or fraction (quotient of integers).
-        """
-        if gegal(self.g, other.g):
-            return 0
-        cdef int tg, to, a
-        tg = typ(self.g)
-        to = typ(other.g)
-
-        cdef int t_g, t_o
-        t_g = typ(self.g); t_o = typ(other.g)
-        if (t_g == t_INT or t_g == t_REAL or t_g == t_FRAC) and \
-           (t_o == t_INT or t_g == t_REAL or t_g == t_FRAC):
-            return gcmp(self.g, other.g)
-
+        First uses PARI's cmp routine; if it decides the objects are
+        not comparable, it then compares the underlying strings (since
+        in Python all objects are supposed to be comparable).
+
+        EXAMPLES:
+            sage: pari(2.5) > None
+            False
+            sage: pari(3) == pari(3)
+            True
+            sage: pari('x^2 + 1') == pari('I-1')
+            False
+            sage: pari(I) == pari(I)
+            True           
+        """
+        try:
+            return self._cmp(other)
+        except PariError:
+            pass
         return cmp(str(self),str(other))
 
     def __richcmp__(gen self, other, int op):
```




---

archive/issue_comments_000958.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-25T15:16:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/215",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/215#issuecomment-958",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
