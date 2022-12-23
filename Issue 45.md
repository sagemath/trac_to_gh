# Issue 45: NTL modulus not reset correctly

Issue created by migration from https://trac.sagemath.org/ticket/45

Original creator: dmharvey

Original creation time: 2006-09-13 01:34:10

Assignee: somebody


```
 sage: x = PolynomialRing(Integers(100)).gen()
 sage: p = 3*x
 sage: q = 7*x
 sage: y = PolynomialRing(Integers(8)).gen()
 sage: p + q
   2*x
 sage: p + q
   10*x
```


I think what's happening is the following. The first p+q calls Polynomial_dense_mod_n._add_(). This function does *not* reset the NTL modulus correctly before calling ntl_ZZ_pX.__add__(), hence the first bogus answer. Then Polynomial_dense_mod_n._add_() calls PolynomialRing_dense_mod_n.__call__(), which *does* reset the NTL modulus.



---

Comment by was created at 2007-01-12 22:17:53

This is fixed now, interestingly, but maybe the problem is still there?

```
sage: x = PolynomialRing(Integers(100),'x').gen()
 sage: p = 3*x
 sage: q = 7*x
 sage: y = PolynomialRing(Integers(8),'y').gen()
 sage: print p + q
   10*x
 sage: print p + q
   10*x
10*x
10*x

```



---

Comment by was created at 2007-01-22 02:27:33

Resolution: fixed


---

Comment by was created at 2007-01-22 02:27:33

OK, I finally replicated the problem correctly, then tracked it down and fixed it.
NOTE to self -- be sure to not forget about this fix when we transition to sagex polynomials later!!


```
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1169432669 28800
# Node ID e4bb5ab8b7beb15adbfe9560ad7d2c015b3e9b5b
# Parent  17021b7f73726bc025d59471aaa49fceaf33d24d
Trac #45 -- ntl modulus not reset correctly

diff -r 17021b7f7372 -r e4bb5ab8b7be sage/rings/polynomial_element.py
--- a/sage/rings/polynomial_element.py  Sun Jan 21 17:23:55 2007 -0800
+++ b/sage/rings/polynomial_element.py  Sun Jan 21 18:24:29 2007 -0800
@@ -2887,11 +2887,29 @@ class Polynomial_dense_mod_n(Polynomial)
     """
     A dense polynomial over the integers modulo n, where n is composite.
 
+    Much of the underlying arithmetic is done using NTL.
+
     EXAMPLES:
+    
         sage: R.<x> = PolynomialRing(Integers(16))
         sage: f = x^3 - x + 17
+        sage: f^2
+        x^6 + 14*x^4 + 2*x^3 + x^2 + 14*x + 1
+        
         sage: loads(f.dumps()) == f
         True
+
+        sage: R.<x> = Integers(100)[]
+        sage: p = 3*x
+        sage: q = 7*x
+        sage: p+q
+        10*x
+        sage: R.<x> = Integers(8)[]
+        sage: parent(p)
+        Univariate Polynomial Ring in x over Ring of integers modulo 100
+        sage: p + q
+        10*x    
+        
     """
     def __init__(self, parent, x=None, check=True,
                  is_gen=False, construct=False):
@@ -2901,7 +2919,6 @@ class Polynomial_dense_mod_n(Polynomial)
             if isinstance(x, ZZ_pX_class):
                 self.__poly = x
                 return
-            parent._ntl_set_modulus()
             self.__poly = ZZ_pX(x)
             return
 
@@ -2952,6 +2969,9 @@ class Polynomial_dense_mod_n(Polynomial)
         parent._ntl_set_modulus()
         self.__poly = ZZ_pX(x)
 
+    def _ntl_set_modulus(self):
+        self.parent()._ntl_set_modulus()
+
     def __reduce__(self):
         return Polynomial_dense_mod_n, \
                (self.parent(), self.list(), False, self.is_gen())
@@ -2973,10 +2993,14 @@ class Polynomial_dense_mod_n(Polynomial)
                pari(1).Mod(self.parent().base_ring().order())
 
     def ntl_ZZ_pX(self):
-        """
+        r"""
         Return underlying NTL representation of this polynomial.
         Additional ``bonus'' functionality is available through this
         function.
+
+        WARNING:
+        You must call \code{ntl.set_modulus(ntl.ZZ(n))} before doing
+        arithmetic with this object!
         """
         return self.__poly
 
@@ -2997,11 +3021,12 @@ class Polynomial_dense_mod_n(Polynomial)
         n = int(n)
         if n < 0:
             raise IndexError, "n must be >= 0"
-        self.parent()._ntl_set_modulus()
+        self._ntl_set_modulus()
         self.__poly[n] = int(value)
 
     def _pow(self, n):
         n = int(n)
+        self._ntl_set_modulus()        
         if self.degree() <= 0:
             return self.parent()(self[0]**n)
         if n < 0:
@@ -3009,7 +3034,8 @@ class Polynomial_dense_mod_n(Polynomial)
         return self.parent()(self.__poly**n, construct=True)
      
     def _add_(self, right):
-        return self.parent()(self.__poly + right.__poly, construct=True)
+        self._ntl_set_modulus()
+        return self.parent()(self.__poly + right.__poly, construct=True)        
 
     def _mul_(self, right):
         """
@@ -3018,7 +3044,8 @@ class Polynomial_dense_mod_n(Polynomial)
             sage: (x - 2)*(x^2 - 8*x + 16)
             x^3 + 90*x^2 + 32*x + 68
         """
-        return self.parent()(self.__poly * right.__poly, construct=True)
+        self._ntl_set_modulus()
+        return self.parent()(self.__poly * right.__poly, construct=True)        
 
     def quo_rem(self, right):
         """
@@ -3029,9 +3056,10 @@ class Polynomial_dense_mod_n(Polynomial)
             right = self.parent()(right)
         elif self.parent() != right.parent():
             raise TypeError
+        self._ntl_set_modulus()
         v = self.__poly.quo_rem(right.__poly)
         P = self.parent()
-        return P(v[0], construct=True), P(v[1], construct=True)
+        return (P(v[0], construct=True), P(v[1], construct=True) )
         
     def shift(self, n):
         r"""
@@ -3055,13 +3083,17 @@ class Polynomial_dense_mod_n(Polynomial)
         """
         if n == 0:
             return self
-        return self.parent()(self.__poly.left_shift(n), construct=True)
+        self._ntl_set_modulus()
+        return self.parent()(self.__poly.left_shift(n),
+                             construct=True)
             
     def _sub_(self, right):
-        return self.parent()(self.__poly - right.__poly, construct=True)
+        self._ntl_set_modulus()
+        return self.parent()(self.__poly - right.__poly, construct=True)        
         
     def __floordiv__(self, right):
-        if is_Polynomial(right) and right.is_constant() and right[0] in self.parent().base_ring():
+        if is_Polynomial(right) and right.is_constant() and \
+                         right[0] in self.parent().base_ring():
             d = right[0]
         elif (right in self.parent().base_ring()):
             d = right
@@ -3135,7 +3167,7 @@ class Polynomial_dense_mod_n(Polynomial)
         """
         if self._is_gen:
             raise TypeError, "Cannot change the value of the generator."
-        self.parent()._ntl_set_modulus()
+        self._ntl_set_modulus()
         self.__poly = ZZ_pX(v)
         try:
             del self.__list
@@ -3146,9 +3178,22 @@ class Polynomial_dense_mod_p(Polynomial_
                              Polynomial_singular_repr,
                              principal_ideal_domain_element.PrincipalIdealDomainElement):
     """
-    A dense polynomial over the integers modulo p, where p is prime. 
+    A dense polynomial over the integers modulo p, where p is prime.
     """
     def __reduce__(self):
+        """
+        This is called when pickling this object.
+        
+        EXAMPLES:
+            sage: R.<x> = PolynomialRing(Integers(17))
+            sage: type(x)
+            <class 'sage.rings.polynomial_element.Polynomial_dense_mod_p'>
+            sage: z = loads(x.dumps())
+            sage: x == z
+            True
+            sage: type(z)
+            <class 'sage.rings.polynomial_element.Polynomial_dense_mod_p'>
+        """
         return Polynomial_dense_mod_p, \
                (self.parent(), self.list(), False, self.is_gen())
 
@@ -3189,7 +3234,7 @@ class Polynomial_dense_mod_p(Polynomial_
         """
         if not isinstance(other, Polynomial) or self.parent() != other.parent():
             other = self.polynomial(other)
-        self.parent()._ntl_set_modulus()
+        self._ntl_set_modulus()
         return self.base_ring()(str(self.ntl_ZZ_pX().resultant(other.ntl_ZZ_pX())))
         
     def discriminant(self):

```

