# Issue 215: Pari comparison with None crashes

Issue created by migration from Trac.

Original creator: kedlaya

Original creation time: 2007-01-24 23:49:19

Assignee: was

Keywords: pari, comparison

I'm not sure what the correct outcome of this should be:

```
pari(2.5) > None
```

but it shouldn't crash SAGE, which is what it does now.


---

Comment by was created at 2007-01-25 15:16:43

fixed for sage > 1.8.2.1

```
# HG changeset patch
# User William Stein <wstein`@`gmail.com>
# Date 1169737969 28800
# Node ID 77fad05c682bd6d4d76524f689941195f82778e6
# Parent  9839fc0f4341de039cb16097a9d1b70f89a2ba9b
Fix trac issue #215 -- pari(2.5) > None caused crash.

diff -r 9839fc0f4341 -r 77fad05c682b sage/libs/pari/gen.pxd
--- a/sage/libs/pari/gen.pxd    Thu Jan 25 06:36:25 2007 -0800
+++ b/sage/libs/pari/gen.pxd    Thu Jan 25 07:12:49 2007 -0800
`@``@` -12,7 +12,6 `@``@` cdef class gen:
     cdef GEN _deepcopy_to_python_heap(self, GEN x, pari_sp* address)
     cdef int get_var(self, v)    
 
-
 cdef class PariInstance:
     cdef gen ZERO, ONE, TWO
     cdef gen new_gen(self, GEN x)
diff -r 9839fc0f4341 -r 77fad05c682b sage/libs/pari/gen.pyx
--- a/sage/libs/pari/gen.pyx    Thu Jan 25 06:36:25 2007 -0800
+++ b/sage/libs/pari/gen.pyx    Thu Jan 25 07:12:49 2007 -0800
`@``@` -451,28 +451,44 `@``@` cdef class gen:
         
 
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

Comment by was created at 2007-01-25 15:16:43

Resolution: fixed
