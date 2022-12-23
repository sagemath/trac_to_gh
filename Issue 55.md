# Issue 55: RealNumber constructor should accept Integer as argument

Issue created by migration from https://trac.sagemath.org/ticket/55

Original creator: dmharvey

Original creation time: 2006-09-13 21:42:09

Assignee: somebody

Currently RealNumber only accepts strings as input. This is a bit odd. Especially since both mpfr and Integer use the same underlying representation (namely GMP)!!!!


```
sage: RealNumber(4)
---------------------------------------------------------------------------
exceptions.TypeError                                 Traceback (most recent call last)

/home/dmharvey/sage-1.3.7/<ipython console> 

/home/dmharvey/sage-1.3.7/mpfr.pyx in mpfr.create_RealNumber()

TypeError: len() of unsized object
```




---

Comment by was created at 2007-01-07 18:18:55

Fixed.

```
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1168193869 28800
# Node ID 01a95c126cbc373b9538f51dc19f32d42419dac6
# Parent  8536e22f8ff3fb30da752d4f4c21dfc2cc5e9b27
Fix trac bug #55:
   RealNumber constructor should accept Integer as argument

diff -r 8536e22f8ff3 -r 01a95c126cbc sage/rings/real_mpfr.pyx
--- a/sage/rings/real_mpfr.pyx  Sun Jan 07 10:05:33 2007 -0800
+++ b/sage/rings/real_mpfr.pyx  Sun Jan 07 10:17:49 2007 -0800
@@ -1683,12 +1683,23 @@ def create_RealNumber(s, int base=10, in
     (controlled by pad) bits than given by s.
 
     INPUT:
-        s -- a string that defines a real number
+        s -- a string that defines a real number (or something whose
+             string representation defines a number)
         base -- an integer between 2 and 36
         pad -- an integer >= 0.
         rnd -- rounding mode: RNDN, RNDZ, RNDU, RNDD
         min_prec -- number will have at least this many bits of precision, no matter what.
+
+    EXAMPLES:
+        sage: RealNumber('2.3')
+        2.29999999999999
+        sage: RealNumber(10)
+        10.0000000000000
+        sage: RealNumber('1.0000000000000000000000000000000000')
+        1.0000000000000000000000000000000000    
     """
+    if not isinstance(s, str):
+        s = str(s)
     if base == 10:
         bits = int(3.32192*len(s))
     else:
```



---

Comment by was created at 2007-01-07 18:18:55

Resolution: fixed
