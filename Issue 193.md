# Issue 193: implement E.b2() etc for elliptic curves

archive/issues_000193.json:
```json
{
    "body": "Assignee: was\n\nElliptic curves have `a_invariants()` and `b_invariants()` methods. They also have `a1()`, `a3()` etc. Would be convenient if they also had `b2()` through `b8()`.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/193\n\n",
    "created_at": "2007-01-15T16:42:33Z",
    "labels": [
        "algebraic geometry",
        "minor",
        "enhancement"
    ],
    "title": "implement E.b2() etc for elliptic curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/193",
    "user": "dmharvey"
}
```
Assignee: was

Elliptic curves have `a_invariants()` and `b_invariants()` methods. They also have `a1()`, `a3()` etc. Would be convenient if they also had `b2()` through `b8()`.


Issue created by migration from https://trac.sagemath.org/ticket/193





---

archive/issue_comments_000885.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-15T22:05:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/193#issuecomment-885",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_000886.json:
```json
{
    "body": "Implemented for sage-1.7.\n\n```\n\n# HG changeset patch\n# User William Stein <wstein@gmail.com>\n# Date 1168898653 28800\n# Node ID 75cdec5df871b9e727c740e0f86564463d2a309b\n# Parent  337295b604b3a69a052aeb12cb913b11caf0238d\nImplemented Trac #193 -- b2,b4,b6,b8 for elliptic curves.\n\ndiff -r 337295b604b3 -r 75cdec5df871 sage/schemes/elliptic_curves/ell_generic.py\n--- a/sage/schemes/elliptic_curves/ell_generic.py       Mon Jan 15 13:04:26 2007 -0800\n+++ b/sage/schemes/elliptic_curves/ell_generic.py       Mon Jan 15 14:04:13 2007 -0800\n@@ -366,6 +366,18 @@ class EllipticCurve_generic(plane_curve.\n             sage: E.b_invariants()\n             (0, -8, 0, -16)\n \n+            sage: E = EllipticCurve([1,2,3,4,5])\n+            sage: E.b_invariants()\n+            (9, 11, 29, 35)\n+            sage: E.b2()\n+            9\n+            sage: E.b4()\n+            11\n+            sage: E.b6()\n+            29\n+            sage: E.b8()\n+            35\n+            \n         ALGORITHM: These are simple functions of the a invariants.\n \n         AUTHOR: William Stein, 2005-04-25\n@@ -379,6 +391,54 @@ class EllipticCurve_generic(plane_curve.\n                                   a3**2 + 4*a6, \\\n                                   a1**2 * a6 + 4*a2*a6 - a1*a3*a4 + a2*a3**2 - a4**2\n             return self.__b_invariants\n+\n+    def b2(self):\n+        \"\"\"\n+        EXAMPLES:\n+            sage: E = EllipticCurve([1,2,3,4,5])\n+            sage: E.b2()\n+            9\n+        \"\"\"\n+        try:\n+            return self.__b_invariants[0]\n+        except AttributeError:\n+            return self.b_invariants()[0]\n+        \n+    def b4(self):\n+        \"\"\"\n+        EXAMPLES:\n+            sage: E = EllipticCurve([1,2,3,4,5])\n+            sage: E.b4()\n+            11\n+        \"\"\"\n+        try:\n+            return self.__b_invariants[1]\n+        except AttributeError:\n+            return self.b_invariants()[1]\n+\n+    def b6(self):\n+        \"\"\"\n+        EXAMPLES:\n+            sage: E = EllipticCurve([1,2,3,4,5])\n+            sage: E.b6()\n+            29\n+        \"\"\"\n+        try:\n+            return self.__b_invariants[2]\n+        except AttributeError:\n+            return self.b_invariants()[2]\n+\n+    def b8(self):\n+        \"\"\"\n+        EXAMPLES:\n+            sage: E = EllipticCurve([1,2,3,4,5])\n+            sage: E.b8()\n+            35\n+        \"\"\"\n+        try:\n+            return self.__b_invariants[3]\n+        except AttributeError:\n+            return self.b_invariants()[3]\n \n     def c_invariants(self):\n         \"\"\"\n@@ -489,10 +549,6 @@ class EllipticCurve_generic(plane_curve.\n         \"\"\"\n         return self.__ainvs[4]\n \n-\n-\n-\n-    \n     def gens(self):\n         raise NotImplementedError\n```\n",
    "created_at": "2007-01-15T22:05:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/193#issuecomment-886",
    "user": "was"
}
```

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

