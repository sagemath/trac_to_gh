# Issue 32: missing coercion functionality

Issue created by migration from https://trac.sagemath.org/ticket/32

Original creator: was

Original creation time: 2006-09-12 23:27:50

Assignee: somebody


```
R.<x,y> = PolynomialRing(QQ,2)
    S = PolynomialRing(GF(7),2)
  S(x)
    Boom!
```



---

Comment by was created at 2007-01-19 11:09:37

Resolution: fixed


---

Comment by was created at 2007-01-19 11:09:37

This was easy to add

```
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1169204832 28800
# Node ID 4c0bbf3706fad3a37607129c520366de1b20e452
# Parent  061691096b76580a55a655e654aa046f2071ebc4
fix trac #32 -- a missing coercin.

diff -r 061691096b76 -r 4c0bbf3706fa sage/rings/multi_polynomial_ring.py
--- a/sage/rings/multi_polynomial_ring.py       Fri Jan 19 02:58:30 2007 -0800
+++ b/sage/rings/multi_polynomial_ring.py       Fri Jan 19 03:07:12 2007 -0800
@@ -407,7 +407,14 @@ class MPolynomialRing_polydict( MPolynom
 
         Coerce works and gets the right parent. 
             sage: parent(S2._coerce_(S.0)) is S2
-            True        
+            True
+
+        Coercion to reduce modulo a prime between rings with different variable names:
+            sage: R.<x,y> = PolynomialRing(QQ,2)
+            sage: S.<a,b> = PolynomialRing(GF(7),2)
+            sage: f = x^2 + 2/3*y^3
+            sage: S(f)
+            3*b^3 + a^2        
         """
         if isinstance(x, multi_polynomial_element.MPolynomial_polydict):
             P = x.parent()
@@ -415,13 +422,19 @@ class MPolynomialRing_polydict( MPolynom
                 return x
             elif P == self:
                 return multi_polynomial_element.MPolynomial_polydict(self, x.element().dict())
-            elif P.variable_names() == self.variable_names():
+            elif len(P.variable_names()) == len(self.variable_names()):
+                # Map the variables in some crazy way (but in order,
+                # of course).  This is here since R(blah) is supposed
+                # to be "make an element of R if at all possible with
+                # no guarantees that this is mathematically solid."
                 K = self.base_ring()
                 D = x.element().dict()
                 for i, a in D.iteritems():
                     D[i] = K(a)
                 return multi_polynomial_element.MPolynomial_polydict(self, D)
-            raise TypeError
+            else:
+                raise TypeError
+
         elif isinstance(x, polydict.PolyDict):
             return multi_polynomial_element.MPolynomial_polydict(self, x)
         elif isinstance(x, fraction_field_element.FractionFieldElement) and x.parent().ring() == self:
```

