# Issue 188: Python's builtin round function is funny since it always coerces to float

Issue created by migration from https://trac.sagemath.org/ticket/188

Original creator: was

Original creation time: 2006-12-28 05:10:25

Assignee: somebody

From Susan Addington:

```
I just downloaded SAGE and am trying it out on MacOS 10.4.
So far the only weirdness I have found is the behavior of the round
function:
round(sqrt(2),2) gives 1.4099999999999999.
While this is correct, it looks strange.
```


Here is some further I/O that illustrates more what is going on:

```
sage: a = sqrt(2)
sage: type(a)
<type 'sage.rings.real_mpfr.RealNumber'>
sage: b = round(a,2); b
1.4099999999999999
sage: type(b)
<type 'float'>
sage: round?
Namespace:      Python builtin
Docstring [source file open failed]:
    round(number[, ndigits]) -> floating point number
    
    Round a number to a given precision in decimal digits (default 0 digits).
    This always returns a floating point number.  Precision may be negative.
```


Note that round is a python builtin and it always outputs a float. 
It would make way more sense if round on a mpfr or complex number, etc.,
were to output a number of that type.  Thus in SAGE the round function
should be replaced by our own, which first tries to call a _round_ function,
and if that doesn't work, calls the builtin round function.


---

Comment by was created at 2007-01-19 09:41:46

Changing type from defect to enhancement.


---

Comment by was created at 2007-01-25 18:55:40

Fixed

```
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1169751099 28800
# Node ID 07471d5dfebfbed422959b60efed67f10ddb028c
# Parent  8faeaa5cc7cbc2f90c980a2011c354ba5479f615
Trac #188 -- wrap builtin round in RDF.

diff -r 8faeaa5cc7cb -r 07471d5dfebf sage/misc/functional.py
--- a/sage/misc/functional.py   Thu Jan 25 10:32:04 2007 -0800
+++ b/sage/misc/functional.py   Thu Jan 25 10:51:39 2007 -0800
@@ -30,7 +30,10 @@ import sage.interfaces.expect
 import sage.interfaces.expect
 
 from sage.rings.complex_double import CDF
-from sage.rings.real_double import RDF
+from sage.rings.real_double import RDF, RealDoubleElement
+import sage.rings.real_mpfr
+
+import __builtin__
 
 ##############################################################################
 # There are many functions on elements of a ring, which mathematicians
@@ -759,6 +762,26 @@ def regulator(x):
     """
     return x.regulator()
 
+def round(x, ndigits=0):
+    """
+    round(number[, ndigits]) -> mpfr real number
+    
+    Round a number to a given precision in decimal digits (default 0
+    digits).  This always returns a real double field element.
+
+    EXAMPLES:
+        sage: round(sqrt(2),2)
+        1.41
+        sage: round(sqrt(2),5)
+        1.41421
+        sage: round(pi)
+        3.0
+
+    IMPLEMENTATION:  Calls Python's builtin round function, and converts
+    the result to a real double field element. 
+    """
+    return RealDoubleElement(__builtin__.round(x, ndigits))
+
 def quotient(x, y, *args, **kwds):
     """
     Return the quotient object x/y, e.g., a quotient of numbers or of
diff -r 8faeaa5cc7cb -r 07471d5dfebf sage/rings/number_field/number_field_ideal.py
--- a/sage/rings/number_field/number_field_ideal.py     Thu Jan 25 10:32:04 2007 -0800
+++ b/sage/rings/number_field/number_field_ideal.py     Thu Jan 25 10:51:39 2007 -0800
@@ -538,7 +538,7 @@ class NumberFieldIdeal_rel(NumberFieldId
         Compute the relative norm of this extension L/K as an ideal of K.
 
         EXAMPLE:
-            sage: R.<x> = PolynomialRing(QQ)
+            sage: R.<x> = QQ[]
             sage: K.<a> = NumberField(x^2+6)
             sage: L.<b> = K.extension(K['x'].gen()^4 + a)
             sage: L.ideal(b).norm()
```



---

Comment by was created at 2007-01-25 18:58:14

Resolution: fixed
