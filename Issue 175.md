# Issue 175: ceil or something is broken

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2006-12-02 17:01:48

Assignee: somebody


```
sage: ceil(10^16 * 1.0)
 10000000000000000

sage: ceil(10^17 * 1.0)
 3125000000000000
```


right.......



---

Comment by was created at 2007-01-25 19:37:00

Resolution: fixed


---

Comment by was created at 2007-01-25 19:37:00

Fixed.

This was a potentially terrible bug.  I'm glad you found it!!


```
# HG changeset patch
# User William Stein <wstein`@`gmail.com>
# Date 1169753572 28800
# Node ID 7b1e4c3ea615683c3062256c16e72327c037117c
# Parent  0652688d22a71a106562e9e3c10508365d663512
Trac #175 -- fix ceil problem (really integer_part)

diff -r 0652688d22a7 -r 7b1e4c3ea615 sage/rings/real_mpfr.pyx
--- a/sage/rings/real_mpfr.pyx  Thu Jan 25 11:27:04 2007 -0800
+++ b/sage/rings/real_mpfr.pyx  Thu Jan 25 11:32:52 2007 -0800
`@``@` -745,11 +745,20 `@``@` cdef class RealNumber(sage.structure.ele
         EXAMPLE:
             sage: a = 119.41212
             sage: a.integer_part()
-            119             
+            119
+
+        A big number with no decimal point:
+            sage: a = RR(10^17); a
+            100000000000000000
+            sage: a.integer_part()
+            100000000000000000
         """
         s = self.str(base=32, no_sci=True)
         i = s.find(".")
-        return Integer(s[:i], base=32)
+        if i != -1:
+            return Integer(s[:i], base=32)
+        else:
+            return Integer(s, base=32)
 
     ########################
     #   Basic Arithmetic
`@``@` -981,6 +990,11 `@``@` cdef class RealNumber(sage.structure.ele
             2
             sage: (2.01).ceil()
             3
+
+            sage: ceil(10^16 * 1.0)
+            10000000000000000
+            sage: ceil(10^17 * 1.0)
+            100000000000000000
         """
         cdef RealNumber x
         x = self._new()
```

