# Issue 193: implement E.b2() etc for elliptic curves

Issue created by migration from https://trac.sagemath.org/ticket/193

Original creator: dmharvey

Original creation time: 2007-01-15 16:42:33

Assignee: was

Elliptic curves have `a_invariants()` and `b_invariants()` methods. They also have `a1()`, `a3()` etc. Would be convenient if they also had `b2()` through `b8()`.



---

Comment by was created at 2007-01-15 22:05:51

Resolution: fixed


---

Comment by was created at 2007-01-15 22:05:51

Implemented for sage-1.7.

```

# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1168898653 28800
# Node ID 75cdec5df871b9e727c740e0f86564463d2a309b
# Parent  337295b604b3a69a052aeb12cb913b11caf0238d
Implemented Trac #193 -- b2,b4,b6,b8 for elliptic curves.

diff -r 337295b604b3 -r 75cdec5df871 sage/schemes/elliptic_curves/ell_generic.py
--- a/sage/schemes/elliptic_curves/ell_generic.py       Mon Jan 15 13:04:26 2007 -0800
+++ b/sage/schemes/elliptic_curves/ell_generic.py       Mon Jan 15 14:04:13 2007 -0800
@@ -366,6 +366,18 @@ class EllipticCurve_generic(plane_curve.
             sage: E.b_invariants()
             (0, -8, 0, -16)
 
+            sage: E = EllipticCurve([1,2,3,4,5])
+            sage: E.b_invariants()
+            (9, 11, 29, 35)
+            sage: E.b2()
+            9
+            sage: E.b4()
+            11
+            sage: E.b6()
+            29
+            sage: E.b8()
+            35
+            
         ALGORITHM: These are simple functions of the a invariants.
 
         AUTHOR: William Stein, 2005-04-25
@@ -379,6 +391,54 @@ class EllipticCurve_generic(plane_curve.
                                   a3**2 + 4*a6, \
                                   a1**2 * a6 + 4*a2*a6 - a1*a3*a4 + a2*a3**2 - a4**2
             return self.__b_invariants
+
+    def b2(self):
+        """
+        EXAMPLES:
+            sage: E = EllipticCurve([1,2,3,4,5])
+            sage: E.b2()
+            9
+        """
+        try:
+            return self.__b_invariants[0]
+        except AttributeError:
+            return self.b_invariants()[0]
+        
+    def b4(self):
+        """
+        EXAMPLES:
+            sage: E = EllipticCurve([1,2,3,4,5])
+            sage: E.b4()
+            11
+        """
+        try:
+            return self.__b_invariants[1]
+        except AttributeError:
+            return self.b_invariants()[1]
+
+    def b6(self):
+        """
+        EXAMPLES:
+            sage: E = EllipticCurve([1,2,3,4,5])
+            sage: E.b6()
+            29
+        """
+        try:
+            return self.__b_invariants[2]
+        except AttributeError:
+            return self.b_invariants()[2]
+
+    def b8(self):
+        """
+        EXAMPLES:
+            sage: E = EllipticCurve([1,2,3,4,5])
+            sage: E.b8()
+            35
+        """
+        try:
+            return self.__b_invariants[3]
+        except AttributeError:
+            return self.b_invariants()[3]
 
     def c_invariants(self):
         """
@@ -489,10 +549,6 @@ class EllipticCurve_generic(plane_curve.
         """
         return self.__ainvs[4]
 
-
-
-
-    
     def gens(self):
         raise NotImplementedError
```

