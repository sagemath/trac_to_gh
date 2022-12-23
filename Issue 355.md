# Issue 355: Pari error on finding roots of polynomials over Z/nZ

Issue created by migration from https://trac.sagemath.org/ticket/355

Original creator: boothby

Original creation time: 2007-04-22 18:45:38

Assignee: was

Offending code:

```
R = ZZ.quo(6*ZZ)
S.<x> = R['x']
p = x^2-1
print p.roots()
```



```
Traceback (most recent call last):        R = ZZ.quo(i*ZZ)
  File "/home/boothby/sage_notebook/worksheets/hw4/", line 5, in <module>
    
  File "polynomial_element.pyx", line 1555, in polynomial_element.Polynomial.roots
  File "polynomial_element.pyx", line 989, in polynomial_element.Polynomial.factor
  File "gen.pyx", line 6003, in gen._pari_trap
gen.PariError:  (8)
```



---

Comment by was created at 2007-05-31 15:23:57

Fixed.


```
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1180624938 25200
# Node ID 9cd8b0dbab87eb163e83d04fef4f74ee82a0b273
# Parent  17b01ba4388699829783c761034c51ae4e0f185a
Fix poly root finding mod n error.

diff -r 17b01ba43886 -r 9cd8b0dbab87 sage/rings/polynomial/polynomial_element.pyx
--- a/sage/rings/polynomial/polynomial_element.pyx      Thu May 31 08:21:59 2007 -0700
+++ b/sage/rings/polynomial/polynomial_element.pyx      Thu May 31 08:22:18 2007 -0700
@@ -43,7 +43,7 @@ from sage.structure.factorization import
 from sage.structure.factorization import Factorization

 from sage.interfaces.all import singular as singular_default, is_SingularElement
-from sage.libs.all import pari, pari_gen
+from sage.libs.all import pari, pari_gen, PariError

 from sage.rings.real_mpfr import RealField, is_RealNumber, is_RealField
 RR = RealField()
@@ -1131,7 +1131,10 @@ cdef class Polynomial(CommutativeAlgebra
               sage.rings.integer_ring.is_IntegerRing(R) or \
               sage.rings.rational_field.is_RationalField(R):

-            G = list(self._pari_('x').factor())
+            try:
+                G = list(self._pari_('x').factor())
+            except PariError:
+                raise NotImplementedError

         elif is_NumberField(R) or is_FiniteField(R):

@@ -1685,6 +1688,18 @@ cdef class Polynomial(CommutativeAlgebra
             X^6 - 3*I*X^5 - X^5 + 3*I*X^4 - sqrt(2)*X^4 - 3*X^4 + 3*sqrt(2)*I*X^3 + I*X^3 + sqrt(2)*X^3 + 3*X^3 - 3*sqrt(2)*I*X^2 - I*X^2 + 3*sqrt(2)*X^2 - sqrt(2)*I*X - 3*sqrt(2)*X + sqrt(2)*I
             sage: print f.roots()
             [(I, 3), (-2^(1/4), 1), (2^(1/4), 1), (1, 1)]
+
+        An example where the base ring doesn't have a factorization algorithm (yet).  Note
+        that this is currently done via nave enumeration, so could be very slow:
+            sage: R = Integers(6)
+            sage: S.<x> = R['x']
+            sage: p = x^2-1
+            sage: p.roots()
+            Traceback (most recent call last):
+            ...
+            NotImplementedError: root finding with multiplicities for this polynomial not implemented (try the multiplicities=False option)
+            sage: p.roots(multiplicities=False)
+            [1, 5]
         """
         seq = []

@@ -1703,6 +1718,12 @@ cdef class Polynomial(CommutativeAlgebra
         try:
             rts = self.factor()
         except NotImplementedError:
+            if K.is_finite():
+                if multiplicities:
+                    raise NotImplementedError, "root finding with multiplicities for this polynomial not implemented (try the multiplicities=False option)"
+                else:
+                    return [a for a in K if not self(a)]
+
             raise NotImplementedError, "root finding for this polynomial not implemented"
         for fac in rts:
             g = fac[0]
```



---

Comment by was created at 2007-05-31 15:23:57

Resolution: fixed
