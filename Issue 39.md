# Issue 39: Misleading polynomial ring behavior

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-09-12 23:31:09

Assignee: somebody

{{{      sage: R.<x,y> = PolynomialRing(ZZ, 2)
        sage: S = R/(x^2 + y^2); S
        sage: S.<a,b> = R/(x^2 + y^2)
        sage: a^2 + b^2 == 0
    << -- *should* be true or give an error -- will require macaulay2... >>
}}}


---

Comment by was created at 2007-01-19 09:22:19

Fixed.


```
# HG changeset patch
# User William Stein <wstein`@`gmail.com>
# Date 1169198371 28800
# Node ID cbda6c27c46e6e36c6c192550b172f79189ce974
# Parent  39c4cda2f4c474719648b289148014737a234682
Trac bug #39 -- fix issues with working with quotients of polynomial rings over ZZ and reduce method for their ideals.

diff -r 39c4cda2f4c4 -r cbda6c27c46e sage/rings/multi_polynomial_ideal.py
--- a/sage/rings/multi_polynomial_ideal.py      Fri Jan 19 00:35:22 2007 -0800
+++ b/sage/rings/multi_polynomial_ideal.py      Fri Jan 19 01:19:31 2007 -0800
`@``@` -35,6 +35,20 `@``@` benchmark and test ideal.
     sage: B = I.groebner_basis()
     sage: len(B)
     45
+
+We compute in a quotient of a polynomial ring over Z/17*Z:
+    sage: R.<x,y> = PolynomialRing(ZZ, 2)                             
+    sage: S.<a,b> = R.quotient((x^2 + y^2, 17))                 # optional -- requires Macaulay2
+    sage: S                                                     # optional 
+    Quotient of Polynomial Ring in x, y over Integer Ring by the ideal (17, y^2 + x^2)
+    sage: a^2 + b^2 == 0                                        # optional 
+    True
+    sage: a^3 - b^2                                             # optional
+    -1*b^2 - a*b^2
+    sage: (a+b)^17                                              # optional
+    b^17 + a*b^16
+    sage: S(17) == 0                                            # optional
+    True
 """
 
 #*****************************************************************************
`@``@` -457,7 +471,7 `@``@` class MPolynomialIdeal_singular_repr:
         I.parent().lib('primdec.lib')
         r = I.radical()
         return S.ideal(r)
-    
+
     def reduce(self, f):
         """
         Reduce an element modulo a standard basis for this ideal.
`@``@` -481,21 +495,27 `@``@` class MPolynomialIdeal_singular_repr:
             sage: (y^2 - x)^2
             y^4 - 2*x*y^2 + x^2
         """
-        try:
-            try:
-                S = self.__singular_groebner_basis.parent()
-            except AttributeError:
-                self.groebner_basis()
-                S = self.__singular_groebner_basis.parent()
-            
-            f = self.ring()(f)
-            g = self.__singular_groebner_basis.parent()(f)
-            h = g.reduce(self.__singular_groebner_basis)
-            return self.ring()(h)
-        
-        except TypeError:
-            
-            return f
+        if self.base_ring() == sage.rings.integer_ring.ZZ:
+            return self._reduce_using_macaulay2(f)
+        
+        try:
+            singular = self.__singular_groebner_basis.parent()
+        except AttributeError:
+            self.groebner_basis()
+            singular = self.__singular_groebner_basis.parent()
+
+        f = self.ring()(f)
+        g = singular(f)
+        h = g.reduce(self.__singular_groebner_basis)
+        return self.ring()(h)
+
+    def _reduce_using_macaulay2(self, f):
+        I = self._macaulay2_()
+        M2 = I.parent()
+        R = self.ring()
+        g = M2(R(f))
+        k = M2('%s %% %s'%(g.name(), I.name()))
+        return R(k)
 
     def syzygy_module(self):
         r"""
`@``@` -714,11 +734,6 `@``@` class MPolynomialIdeal( MPolynomialIdeal
             return self._macaulay2_groebner_basis()
         elif algorithm == 'magma:GroebnerBasis':
             return self._magma_groebner_basis()
-        elif algorithm == None:
-            if self.ring() == ZZ:
-                return self._macaulay2_groebner_basis()
-            else:
-                return self._singular_groebner_basis()
         else:
             raise TypeError, "algorithm '%s' unknown"%algorithm
```



---

Comment by was created at 2007-01-19 09:22:19

Resolution: fixed
