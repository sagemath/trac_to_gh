# Issue 119: Polynomail abstract class

Issue created by migration from https://trac.sagemath.org/ticket/119

Original creator: burhanud

Original creation time: 2006-10-08 00:09:35

Assignee: dmharvey


```
sage: FpX = Polynomial(GF(11))

sage: FpX
---------------------------------------------------------------------------
<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)

/home/burhanud/tor/<ipython console> in <module>()

/home/was/sage-1.4/local/lib/python2.5/site-packages/IPython/Prompts.py in __call__(self, arg)
    514
    515             # and now call a possibly user-defined print mechanism
--> 516             manipulated_val = self.display(arg)
    517
    518             # user display hooks can change the variable to be stored in

/home/was/sage-1.4/local/lib/python2.5/site-packages/IPython/Prompts.py in _display(self, arg)
    538         """
    539
--> 540         return self.shell.hooks.result_display(arg)
    541
    542     # Assign the default display method:

/home/was/sage-1.4/local/lib/python2.5/site-packages/IPython/hooks.py in __call__(self, *args, **kw)
    132             #print "prio",prio,"cmd",cmd #dbg
    133             try:
--> 134                 ret = cmd(*args, **kw)
    135                 return ret
    136             except ipapi.TryNext, exc:

/home/was/sage-1.4/local/lib/python2.5/site-packages/IPython/hooks.py in result_display(self, arg)
    153
    154     if self.rc.pprint:
--> 155         out = pformat(arg)
    156         if '\n' in out:
    157             # So that multi-line strings line up with the left column of

/home/was/sage-1.4/local/lib/python2.5/pprint.py in pformat(self, object)
    109     def pformat(self, object):
    110         sio = _StringIO()
--> 111         self._format(object, sio, 0, 0, {}, 0)
    112         return sio.getvalue()
    113
/home/was/sage-1.4/local/lib/python2.5/pprint.py in _format(self, object, stream, indent, allowance, context, level)
    127             self._readable = False
    128             return
--> 129         rep = self._repr(object, context, level - 1)
    130         typ = _type(object)
    131         sepLines = _len(rep) > (self._width - 1 - indent - allowance)

/home/was/sage-1.4/local/lib/python2.5/pprint.py in _repr(self, object, context, level)
    193     def _repr(self, object, context, level):
    194         repr, readable, recursive = self.format(object, context.copy(),
--> 195                                                 self._depth, level)
    196         if not readable:
    197             self._readable = False

/home/was/sage-1.4/local/lib/python2.5/pprint.py in format(self, object, context, maxlevels, level)
    205         and whether the object represents a recursive construct.
    206         """
--> 207         return _safe_repr(object, context, maxlevels, level)
    208
    209

/home/was/sage-1.4/local/lib/python2.5/pprint.py in _safe_repr(object, context, maxlevels, level)
    290         return format % _commajoin(components), readable, recursive
    291
--> 292     rep = repr(object)
    293     return rep, (rep and not rep.startswith('<')), False
    294

/home/burhanud/tor/sage_object.pyx in sage_object.SageObject.__repr__()

/home/was/sage-1.4/local/lib/python2.5/site-packages/sage/rings/polynomial_element.py in _repr_(self)
    390
    391     def _repr_(self):
--> 392         return self._repr()
    393
    394     def _latex_(self, name=None):

/home/was/sage-1.4/local/lib/python2.5/site-packages/sage/rings/polynomial_element.py in _repr(self, name)
    360     def _repr(self, name=None):
    361         s = " "
--> 362         m = self.degree() + 1
    363         r = reversed(xrange(m))
    364         if name is None:

/home/was/sage-1.4/local/lib/python2.5/site-packages/sage/rings/polynomial_element.py in degree(self)
    791             -- Naqi Jaffery (2006-01-24): examples
    792         """
--> 793         raise NotImplementedError
    794
    795     def denominator(self):

<type 'exceptions.NotImplementedError'>:

sage:

```



---

Comment by dmharvey created at 2006-10-27 03:01:03

The problem seems to be that the `Polynomial.__init__()` method doesn't check that the parent is a `PolynomialRing`. This could be easily fixed, but first I'm wondering what on earth the `construct=False` parameter in the constructor is supposed to mean?...


```
def __init__(self, parent, is_gen = False, construct=False): 
          ring_element.RingElement.__init__(self, parent)
          self._is_gen = is_gen
```



---

Comment by was created at 2007-01-13 02:27:26

Solution: Polynomial should not be called by user code (for efficiency reasons) -- so I de-exported it.


```
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1168655204 28800
# Node ID e02fb8a03726a1143fbe6a3919c38b8f55d7389e
# Parent  86ad31ae2e4abe1ce83b5f6cb0ee9a2dc263a1c8
Address trac #119 -- Polynomial(blah)

diff -r 86ad31ae2e4a -r e02fb8a03726 sage/groups/perm_gps/permgroup_element.py
--- a/sage/groups/perm_gps/permgroup_element.py Fri Jan 12 17:43:31 2007 -0800
+++ b/sage/groups/perm_gps/permgroup_element.py Fri Jan 12 18:26:44 2007 -0800
@@ -47,7 +47,7 @@ import sage.structure.element as element
 import sage.structure.element as element
 import sage.groups.group as group
 
-from sage.rings.all      import ZZ, Integer, is_MPolynomial, MPolynomialRing, Polynomial
+from sage.rings.all      import ZZ, Integer, is_MPolynomial, MPolynomialRing, is_Polynomial
 from sage.matrix.all     import MatrixSpace
 from sage.interfaces.all import gap, is_GapElement, is_ExpectElement
 
@@ -353,7 +353,7 @@ class PermutationGroupElement(element.Mu
             sage: (f*sigma)*tau
             u^2 + z^2 - y^2 + 2*x^2            
         """
-        if isinstance(left, Polynomial):
+        if is_Polynomial(left):
             if self != 1:
                 raise ValueError, "%s does not act on %s"%(self, left.parent())
             return left
diff -r 86ad31ae2e4a -r e02fb8a03726 sage/rings/all.py
--- a/sage/rings/all.py Fri Jan 12 17:43:31 2007 -0800
+++ b/sage/rings/all.py Fri Jan 12 18:26:44 2007 -0800
@@ -92,7 +92,7 @@ from complex_double import ComplexDouble
 
 # Univariate Polynomial Rings
 from polynomial_ring import PolynomialRing, polygen, polygens, is_PolynomialRing
-from polynomial_element import Polynomial, is_Polynomial
+from polynomial_element import is_Polynomial
 
 # Multivariate Polynomial Rings
 from multi_polynomial_ring import MPolynomialRing, is_MPolynomialRing, TermOrder
diff -r 86ad31ae2e4a -r e02fb8a03726 sage/rings/number_field/number_field.py
--- a/sage/rings/number_field/number_field.py   Fri Jan 12 17:43:31 2007 -0800
+++ b/sage/rings/number_field/number_field.py   Fri Jan 12 18:26:44 2007 -0800
@@ -216,7 +216,7 @@ class NumberField_generic(field.Field):
             sage: k.<a> = NumberField(f)
             sage: v = k.complex_embeddings()
             sage: [phi(k.0^2) for phi in v]
-            [2.97572074037667, 0.921039066973046 - 3.07553311884577*I, 0.921039066973046 + 3.07553311884577*I, -2.40889943716138 + 1.90254105303505*I, -2.40889943716138 - 1.90254105303505*I]
+            [2.97572074037667, 0.921039066973046 - 3.07553311884577*I, 0.921039066973046 + 3.07553311884577*I, -2.40889943716138 + 1.90254105303505*I, -2.40889943716138 - 1.90254105303505*I]            
         """
         try:
             return self.__complex_embeddings[prec]
diff -r 86ad31ae2e4a -r e02fb8a03726 sage/schemes/elliptic_curves/monsky_washnitzer.py
--- a/sage/schemes/elliptic_curves/monsky_washnitzer.py Fri Jan 12 17:43:31 2007 -0800
+++ b/sage/schemes/elliptic_curves/monsky_washnitzer.py Fri Jan 12 18:26:44 2007 -0800
@@ -33,7 +33,7 @@ AUTHORS:
 #*****************************************************************************
 
 
-from sage.rings.all import Integers, Integer, PolynomialRing, Polynomial
+from sage.rings.all import Integers, Integer, PolynomialRing, is_Polynomial
 from sage.matrix.all import matrix
 from sage.rings.ring import CommutativeAlgebra
 from sage.structure.element import CommutativeAlgebraElement
@@ -111,7 +111,7 @@ class SpecialCubicQuotientRing(Commutati
         Q -- a polynomial of the form Q(x) = x^3 + ax + b, where a, b
              belong to a ring in which 2, 3 are invertible.
     """
-    if not isinstance(Q, Polynomial):
+    if is_Polynomial(Q):
       raise TypeError, "Q (=%s) must be a polynomial" % Q
 
     if Q.degree() != 3 or not Q[2].is_zero():
diff -r 86ad31ae2e4a -r e02fb8a03726 sage/schemes/hyperelliptic_curves/constructor.py
--- a/sage/schemes/hyperelliptic_curves/constructor.py  Fri Jan 12 17:43:31 2007 -0800
+++ b/sage/schemes/hyperelliptic_curves/constructor.py  Fri Jan 12 18:26:44 2007 -0800
@@ -17,14 +17,14 @@ from hyperelliptic_g2_finite_field impor
 from hyperelliptic_g2_finite_field import HyperellipticCurve_g2_finite_field
 from hyperelliptic_g2_rational_field import HyperellipticCurve_g2_rational_field
 
-from sage.rings.all import is_FiniteField, is_RationalField, Polynomial
+from sage.rings.all import is_FiniteField, is_RationalField, is_Polynomial
 
 def HyperellipticCurve(f,h=None,names=None,PP=None):
     r"""
     Returns the hyperelliptic curve $y^2 + h y = f$, for univariate
     polynomials $h$ and $f$.
     """
-    if not isinstance(f, Polynomial):
+    if not is_Polynomial(f):
         raise TypeError, "Arguments f (=%s) and h (= %s) must be polynomials"%(f,h)
     P = f.parent()
     if h is None:
```



---

Comment by was created at 2007-01-13 02:27:26

Resolution: fixed
