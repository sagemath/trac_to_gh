# Issue 155: bug in factor over RR

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2006-10-27 01:25:32

Assignee: somebody

This is good:

```
sage: x = PolynomialRing(QQ,"x").gen()
sage: f = x^2-1
sage: factor(f)
(x - 1) * (x + 1)
```

This is bad:

```
sage: x = PolynomialRing(RR,"x").gen()
sage: f = x^2-1
sage: factor(f)
---------------------------------------------------------------------------
<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)

...
```

I didn't see this entered in the bug tracker.


---

Comment by was created at 2007-01-13 00:18:04

Fixed.

```

# HG changeset patch
# User William Stein <wstein`@`gmail.com>
# Date 1168647440 28800
# Node ID c7164849d131e768a44b8c02da9bde74bed9f801
# Parent  e7e66d37ff7a6bc0c31efa693c0dcd5be1c6d048
Fix trac #155 and related issues (poly factoring over RR and CC).

diff -r e7e66d37ff7a -r c7164849d131 sage/rings/complex_number.pxd
--- a/sage/rings/complex_number.pxd     Fri Jan 12 14:39:13 2007 -0800
+++ b/sage/rings/complex_number.pxd     Fri Jan 12 16:17:20 2007 -0800
`@``@` -2,10 +2,9 `@``@` include 'mpfr.pxi'
 include 'mpfr.pxi'
 
 cimport sage.structure.element
-cimport sage.libs.pari.gen
 cimport real_mpfr
 
-cdef class ComplexNumber(sage.structure.element.RingElement):
+cdef class ComplexNumber(sage.structure.element.FieldElement):
     cdef mpfr_t __re
     cdef mpfr_t __im
     #cdef sage.rings.real_mpfr.RealNumber __re
diff -r e7e66d37ff7a -r c7164849d131 sage/rings/complex_number.pyx
--- a/sage/rings/complex_number.pyx     Fri Jan 12 14:39:13 2007 -0800
+++ b/sage/rings/complex_number.pyx     Fri Jan 12 16:17:20 2007 -0800
`@``@` -17,7 +17,7 `@``@` import math
 import math
 import operator
 
-from sage.structure.element cimport RingElement, Element, ModuleElement
+from sage.structure.element cimport FieldElement, RingElement, Element, ModuleElement
 
 import complex_field
 import real_field
`@``@` -39,7 +39,7 `@``@` def is_ComplexNumber(x):
 def is_ComplexNumber(x):
     return isinstance(x, ComplexNumber)
 
-cdef class ComplexNumber(sage.structure.element.RingElement):
+cdef class ComplexNumber(sage.structure.element.FieldElement):
     """
     A complex number.
 
`@``@` -65,7 +65,7 `@``@` cdef class ComplexNumber(sage.structure.
     
     def __init__(self, parent, real, imag=None):
         cdef real_mpfr.RealNumber rr, ii
-        sage.rings.ring_element.RingElement.__init__(self, parent)
+        self._parent = parent
         self._prec = self._parent._prec
         self._multiplicative_order = None
 
`@``@` -101,7 +101,7 `@``@` cdef class ComplexNumber(sage.structure.
     
     def  __dealloc__(self):
         mpfr_clear(self.__re)
-        mpfr_clear(self.__im)        
+        mpfr_clear(self.__im)
 
     def _repr_(self):
         return self.str(10)
diff -r e7e66d37ff7a -r c7164849d131 sage/rings/polynomial_element.py
--- a/sage/rings/polynomial_element.py  Fri Jan 12 14:39:13 2007 -0800
+++ b/sage/rings/polynomial_element.py  Fri Jan 12 16:17:20 2007 -0800
`@``@` -952,6 +952,22 `@``@` class Polynomial(commutative_algebra_ele
             sage: f = x^0
             sage: f.factor()
             1
+
+        Factor over the real numbers:
+            sage: x = PolynomialRing(RealField(200),"x").gen()
+            sage: f = x^2-1
+            sage: factor(f)
+            (1.0000000000000000000000000000000000000000000000000000000000*x + 1.0000000000000000000000000000000000000000000000000000000000) * (1.0000000000000000000000000000000000000000000000000000000000*x - 1.0000000000000000000000000000000000000000000000000000000000)
+
+        Factor over the complex numbers:
+            sage: x = PolynomialRing(ComplexField(200),"x").gen()
+            sage: f = x^2+1
+            sage: factor(f)
+            (1.0000000000000000000000000000000000000000000000000000000000*x + -1.0000000000000000000000000000000000000000000000000000000000*I) * (1.0000000000000000000000000000000000000000000000000000000000*x + 1.0000000000000000000000000000000000000000000000000000000000*I)
+            sage: x = PolynomialRing(CC,"x").gen()
+            sage: f = (x^2+1)*CC.0
+            sage: factor(f)
+            (1.00000000000000*I) * (1.00000000000000*x + -1.00000000000000*I) * (1.00000000000000*x + 1.00000000000000*I)
         """
 
         # PERFORMANCE NOTE:
`@``@` -972,10 +988,13 `@``@` class Polynomial(commutative_algebra_ele
         
         from sage.rings.number_field.all import is_NumberField
         
-        if integer_mod_ring.is_IntegerModRing(R) or \
+        if integer_mod_ring.is_IntegerModRing(R) or is_RealField(R) or \
                isinstance(R, (integer_ring.IntegerRing, rational_field.RationalField)):
 
             G = list(self._pari_('x').factor())
+
+        elif complex_field.is_ComplexField(R):
+            G = list((pari(R.gen())*self._pari_('x')).factor())
 
         elif is_NumberField(R) or finite_field.is_FiniteField(R):
 
```



---

Comment by was created at 2007-01-13 00:18:04

Resolution: fixed
