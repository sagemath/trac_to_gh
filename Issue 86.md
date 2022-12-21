# Issue 86: can't create points of an elliptic curve over p-adics

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2006-09-26 20:38:04

Assignee: was


```
sage: K = pAdicField(5)
sage: E = EllipticCurve([K(1), K(1)])
sage: P = E([K(0), K(1), K(1)])
------------------------------------------------------------------------ 
---
exceptions.NotImplementedError                       Traceback (most  
recent call last)

/home/dmharvey/sage-1.3.7.3.3/<ipython console>

/home/dmharvey/sage-1.3.7.3.3/local/lib/python2.4/site-packages/sage/ 
schemes/elliptic_curves/ell_generic.py in __call__(self, *args)
     299             R = self.base_ring()
     300             return self.point([R(0),R(1),R(0)], check=False)
--> 301         return plane_curve.ProjectiveCurve_generic.__call__ 
(self, *args)
     302
     303     def __getitem__(self, n):

/home/dmharvey/sage-1.3.7.3.3/local/lib/python2.4/site-packages/sage/ 
schemes/generic/scheme.py in __call__(self, *args)
     122             if S.codomain() == self:
     123                 return S
--> 124         return self.point(args)
     125
     126     def point_homset(self, R=None):

/home/dmharvey/sage-1.3.7.3.3/local/lib/python2.4/site-packages/sage/ 
schemes/generic/scheme.py in point(self, v, check)
     138
     139     def point(self, v, check=True):
--> 140         return self._point_class(self, v, check=check)
     141
     142     def _point_class(self):

/home/dmharvey/sage-1.3.7.3.3/local/lib/python2.4/site-packages/sage/ 
schemes/generic/morphism.py in __init__(self, X, v, check)
     341     def __init__(self, X, v, check=True):
     342         if scheme.is_Scheme(X):
--> 343             X = X(X.base_ring())
     344         SchemeMorphism.__init__(self, X)
     345         if check:

/home/dmharvey/sage-1.3.7.3.3/local/lib/python2.4/site-packages/sage/ 
schemes/elliptic_curves/ell_generic.py in __call__(self, *args)
     299             R = self.base_ring()
     300             return self.point([R(0),R(1),R(0)], check=False)
--> 301         return plane_curve.ProjectiveCurve_generic.__call__ 
(self, *args)
     302
     303     def __getitem__(self, n):

/home/dmharvey/sage-1.3.7.3.3/local/lib/python2.4/site-packages/sage/ 
schemes/generic/scheme.py in __call__(self, *args)
     114         S = args[0]
     115         if is_CommutativeRing(S):
--> 116             return self.point_homset(S)
     117         elif is_Scheme(S):
     118             return S.Hom(self)

/home/dmharvey/sage-1.3.7.3.3/local/lib/python2.4/site-packages/sage/ 
schemes/generic/scheme.py in point_homset(self, R)
     133         except KeyError:
     134             pass
--> 135         H = self._homset_class(self,R)
     136         self.__point_homset[R] = H
     137         return H

/home/dmharvey/sage-1.3.7.3.3/local/lib/python2.4/site-packages/sage/ 
schemes/generic/algebraic_scheme.py in _homset_class(self, *args,  
**kwds)
      89
      90     def _homset_class(self, *args, **kwds):
---> 91         return self.__A._homset_class(*args, **kwds)
      92
      93     def _point_class(self, *args, **kwds):

/home/dmharvey/sage-1.3.7.3.3/local/lib/python2.4/site-packages/sage/ 
schemes/generic/projective_space.py in _homset_class(self, *args,  
**kwds)
     304 class ProjectiveSpace_field(ProjectiveSpace_ring):
     305     def _homset_class(self, *args, **kwds):
--> 306         return  
homset.SchemeHomset_projective_coordinates_field(*args, **kwds)
     307
     308     def _point_class(self, *args, **kwds):

/home/dmharvey/sage-1.3.7.3.3/local/lib/python2.4/site-packages/sage/ 
schemes/generic/homset.py in __init__(self, X, S)
     211     def __init__(self, X, S):
     212         R = X.base_ring()
--> 213         SchemeHomset_generic.__init__(self, spec.Spec(S, R), X)
     214
     215     def _repr_(self):

/home/dmharvey/sage-1.3.7.3.3/local/lib/python2.4/site-packages/sage/ 
schemes/generic/spec.py in __init__(self, R, S, check)
      80                 raise TypeError, "S (=%s) must be a  
commutative ring"%S
      81             try:
---> 82                 S.hom(R)
      83             except TypeError:
      84                 raise ValueError, "There must be a natural  
map S --> R, but S = %s and R = %s"%(S,R)

/home/dmharvey/sage-1.3.7.3.3/gens.pyx in gens.Generators.hom()

/home/dmharvey/sage-1.3.7.3.3/local/lib/python2.4/site-packages/sage/ 
rings/homset.py in natural_map(self)
      50
      51     def natural_map(self):
---> 52         return morphism.RingHomomorphism_coercion(self)
      53
      54

/home/dmharvey/sage-1.3.7.3.3/local/lib/python2.4/site-packages/sage/ 
categories/morphism.py in __init__(self, parent)
     113         Morphism.__init__(self, parent)
     114         try:
--> 115             self.codomain()._coerce_(self.domain().gen(0))
     116         except TypeError:
     117             raise TypeError, "Natural coercion morphism from  
%s to %s not defined."%(self.domain(), self.codomain())

/home/dmharvey/sage-1.3.7.3.3/gens.pyx in gens.Generators.gen()

NotImplementedError: i-th generator not known.
```




---

Comment by was created at 2007-01-12 22:27:51

Fixed for sage-1.7:

```
# HG changeset patch
# User William Stein <wstein`@`gmail.com>
# Date 1168640804 28800
# Node ID 85b96a510e10e13d5e71aa12afb2a3f1a3564fb8
# Parent  2a6823917a29813a484e00eea7b15f7c697269ab
Fix trac bug # 86: "can't create points of an elliptic curve over p-adics"

diff -r 2a6823917a29 -r 85b96a510e10 sage/categories/morphism.py
--- a/sage/categories/morphism.py       Fri Jan 12 14:11:42 2007 -0800
+++ b/sage/categories/morphism.py       Fri Jan 12 14:26:44 2007 -0800
`@``@` -112,7 +112,7 `@``@` class FormalCoercionMorphism(Morphism):
     def __init__(self, parent):
         Morphism.__init__(self, parent)
         try:
-            self.codomain()._coerce_(self.domain().gen(0))
+            self.codomain().has_coerce_map_from(self.domain())
         except TypeError:
             raise TypeError, "Natural coercion morphism from %s to %s not defined."%(self.domain(), self.codomain())
         
diff -r 2a6823917a29 -r 85b96a510e10 sage/rings/multi_polynomial_element.py
--- a/sage/rings/multi_polynomial_element.py    Fri Jan 12 14:11:42 2007 -0800
+++ b/sage/rings/multi_polynomial_element.py    Fri Jan 12 14:26:44 2007 -0800
`@``@` -105,7 +105,7 `@``@` class MPolynomial(CommutativeRingElement
             K = self.parent().base_ring()
         y = K(0) 
         for (m,c) in self.element().dict().iteritems():  
-            y += c*misc.mul([ x[i]**m[i] for i in range(n) ])      
+            y += c*misc.mul([ x[i]**m[i] for i in range(n) if m[i] > 0])      
         return y 
 
     def __cmp__(self, right):
diff -r 2a6823917a29 -r 85b96a510e10 sage/schemes/elliptic_curves/ell_point.py
--- a/sage/schemes/elliptic_curves/ell_point.py Fri Jan 12 14:11:42 2007 -0800
+++ b/sage/schemes/elliptic_curves/ell_point.py Fri Jan 12 14:26:44 2007 -0800
`@``@` -1,5 +1,14 `@``@`
 """
 Points on elliptic curves
+
+EXAMPLES:
+    sage: sage: K = pAdicField(5)
+    sage: sage: E = EllipticCurve([K(1), K(1)])
+    sage: P = E([K(0), K(1), K(1)])
+    sage: P
+    (0 : 1 : 1)
+    sage: P + P
+    (4 + 3*5 + 3*5^2 + 3*5^3 + 3*5^4 + 3*5^5 + 3*5^6 + 3*5^7 + 3*5^8 + 3*5^9 + 3*5^10 + 3*5^11 + 3*5^12 + 3*5^13 + 3*5^14 + 3*5^15 + 3*5^16 + 3*5^17 + 3*5^18 + 3*5^19 + O(5^20) : 2 + 3*5^2 + 3*5^4 + 3*5^6 + 3*5^8 + 3*5^10 + 3*5^12 + 3*5^14 + 3*5^16 + 3*5^18 + O(5^20) : 1)    
 """
 
 #*****************************************************************************
0
sage: 
Exiting SAGE (CPU time 0m0.04s, Wall time 1m9.81s).
rank4:~/grants was$ cd
rank4:~ was$ cd d/sage/sage
rank4:~/d/sage/sage was$ hg export tip
# HG changeset patch
# User William Stein <wstein`@`gmail.com>
# Date 1168640804 28800
# Node ID 85b96a510e10e13d5e71aa12afb2a3f1a3564fb8
# Parent  2a6823917a29813a484e00eea7b15f7c697269ab
Fix trac bug # 86: "can't create points of an elliptic curve over p-adics"

diff -r 2a6823917a29 -r 85b96a510e10 sage/categories/morphism.py
--- a/sage/categories/morphism.py       Fri Jan 12 14:11:42 2007 -0800
+++ b/sage/categories/morphism.py       Fri Jan 12 14:26:44 2007 -0800
`@``@` -112,7 +112,7 `@``@` class FormalCoercionMorphism(Morphism):
     def __init__(self, parent):
         Morphism.__init__(self, parent)
         try:
-            self.codomain()._coerce_(self.domain().gen(0))
+            self.codomain().has_coerce_map_from(self.domain())
         except TypeError:
             raise TypeError, "Natural coercion morphism from %s to %s not defined."%(self.domain(), self.codomain())
         
diff -r 2a6823917a29 -r 85b96a510e10 sage/rings/multi_polynomial_element.py
--- a/sage/rings/multi_polynomial_element.py    Fri Jan 12 14:11:42 2007 -0800
+++ b/sage/rings/multi_polynomial_element.py    Fri Jan 12 14:26:44 2007 -0800
`@``@` -105,7 +105,7 `@``@` class MPolynomial(CommutativeRingElement
             K = self.parent().base_ring()
         y = K(0) 
         for (m,c) in self.element().dict().iteritems():  
-            y += c*misc.mul([ x[i]**m[i] for i in range(n) ])      
+            y += c*misc.mul([ x[i]**m[i] for i in range(n) if m[i] > 0])      
         return y 
 
     def __cmp__(self, right):
diff -r 2a6823917a29 -r 85b96a510e10 sage/schemes/elliptic_curves/ell_point.py
--- a/sage/schemes/elliptic_curves/ell_point.py Fri Jan 12 14:11:42 2007 -0800
+++ b/sage/schemes/elliptic_curves/ell_point.py Fri Jan 12 14:26:44 2007 -0800
`@``@` -1,5 +1,14 `@``@`
 """
 Points on elliptic curves
+
+EXAMPLES:
+    sage: sage: K = pAdicField(5)
+    sage: sage: E = EllipticCurve([K(1), K(1)])
+    sage: P = E([K(0), K(1), K(1)])
+    sage: P
+    (0 : 1 : 1)
+    sage: P + P
+    (4 + 3*5 + 3*5^2 + 3*5^3 + 3*5^4 + 3*5^5 + 3*5^6 + 3*5^7 + 3*5^8 + 3*5^9 + 3*5^10 + 3*5^11 + 3*5^12 + 3*5^13 + 3*5^14 + 3*5^15 + 3*5^16 + 3*5^17 + 3*5^18 + 3*5^19 + O(5^20) : 2 + 3*5^2 + 3*5^4 + 3*5^6 + 3*5^8 + 3*5^10 + 3*5^12 + 3*5^14 + 3*5^16 + 3*5^18 + O(5^20) : 1)    
 """
 
 #*****************************************************************************
```



---

Comment by was created at 2007-01-12 22:27:51

Resolution: fixed
