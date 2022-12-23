# Issue 159: bessel function bug

Issue created by migration from https://trac.sagemath.org/ticket/159

Original creator: wdj

Original creation time: 2006-10-28 16:22:30

Assignee: wdj

Keywords: bessel functions

Inconsistent behaviour:


```
sage: bessel_J(2,5.135,"maxima")
0.00021138927993558099
sage: bessel_J(2,5.136,"maxima")
-0.00012828753895466338
sage: bessel_J(2,5.135)
0.0056034700919736996
sage: bessel_J(2,5.136)
0.0055939359540343476
sage: bessel_J(2,5.136,"pari")
0.0055939359540343476
```




---

Comment by was created at 2007-01-13 00:30:01

According to the docs (that wdj wrote) PARI and Maxima define the bessel_J function differently.  I added something about this to the documentation.


```
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1168648166 28800
# Node ID 4ee645ba1eb61c95dbc383f05e8ea09da8682b7a
# Parent  c7164849d131e768a44b8c02da9bde74bed9f801
addressed ticket #159 -- inconsistent bessel_j by documenting behavior.

diff -r c7164849d131 -r 4ee645ba1eb6 sage/functions/special.py
--- a/sage/functions/special.py Fri Jan 12 16:17:20 2007 -0800
+++ b/sage/functions/special.py Fri Jan 12 16:29:26 2007 -0800
@@ -419,9 +419,12 @@ def bessel_I(nu,z,alg = "pari",prec=53):
         
 def bessel_J(nu,z,alg="pari",prec=53):
     r"""
-    Implements the "J-Bessel function", or
+    Return value of the "J-Bessel function", or
     "Bessel function, 1st kind", with
     index (or "order") nu and argument z.
+
+    WARNING: The pari and maxima definitions of ``the'' J-Bessel
+    function are different (see below).
 
     \begin{verbatim}
     Defn:
@@ -459,6 +462,12 @@ def bessel_J(nu,z,alg="pari",prec=53):
         0.719622018527510801
         sage: bessel_J(0,1)    # last few digits are random
         0.765197686557966605
+
+    We illustrate that the pari and maxima definitions differ:
+        sage: bessel_J(3,10,"maxima")   # last few digits are random
+        0.0583793793051869
+        sage: bessel_J(3,10,"pari")     # last few digits are random
+        0.0000129283516457158
 
     """
     if alg=="pari":
```



---

Comment by was created at 2007-01-13 00:30:01

Resolution: fixed
