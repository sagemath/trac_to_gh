# Issue 697: NTL rewrite (splitting ntl.pyx down into each class)

Issue created by migration from https://trac.sagemath.org/ticket/697

Original creator: jbmohler

Original creation time: 2007-09-19 20:56:57

Assignee: was

This is finally the big NTL rewrite.  It would be nice to get this integrated soon since David Harvey is already building on top of this for dense polys over ZZ.  Robert Bradshaw and Craig Citro are also champing at the bit.


---

Comment by jbmohler created at 2007-09-19 20:57:40

bundle with my rewrite and some fixes by R. Bradshaw and D. Harvey


---

Attachment


---

Comment by was created at 2007-09-20 20:25:22

The following must be manually merged in because ntl.pyx was deleted:

```
--- a/sage/libs/ntl/ntl.pyx	Wed Aug 29 19:08:56 2007 -0700
+++ b/sage/libs/ntl/ntl.pyx	Thu Sep 20 00:11:17 2007 -0400
@@ -35,6 +35,9 @@ from sage.rings.integer_ring cimport Int
 
 ZZ_sage = IntegerRing()
 
+from sage.structure.proof.proof import get_flag
+cdef proof_flag(t):
+    return get_flag(t, "polynomial")
 
 ##############################################################################
 # ZZ: Arbitrary precision integers
@@ -726,7 +729,7 @@ cdef class ntl_ZZX:
         g = self.gcd(other)
         return (self*other).quo_rem(g)[0]
 
-    def xgcd(self, ntl_ZZX other, proof=True):
+    def xgcd(self, ntl_ZZX other, proof=None):
         """
         If self and other are coprime over the rationals, return r, s,
         t such that r = s*self + t*other.  Otherwise return 0.  This
@@ -738,7 +741,8 @@ cdef class ntl_ZZX:
         function computes s and t such that: a*s + b*t = r; otherwise
         s and t are both 0.  If proof = False (*not* the default),
         then resultant computation may use a randomized strategy that
-        errs with probability no more than $2^{-80}$.
+        errs with probability no more than $2^{-80}$.  The default is
+        proof=None (see proof.polynomial or sage.structure.proof).
 
         EXAMPLES:
             sage: f = ntl.ZZX([1,2,3]) * ntl.ZZX([4,5])**2
@@ -752,6 +756,7 @@ cdef class ntl_ZZX:
             sage: f.xgcd(g)
             (169, [-13], [13])
         """
+        proof = proof_flag(proof)
         cdef ZZX_c *s, *t
         cdef ZZ_c *r 
         _sig_on
@@ -1012,10 +1017,11 @@ cdef class ntl_ZZX:
         t = ZZX_trace_list(self.x)
         return eval(string(t).replace(' ', ','))
 
-    def resultant(self, ntl_ZZX other, proof=True):
+    def resultant(self, ntl_ZZX other, proof=None):
         """
         Return the resultant of self and other.  If proof = False (the
-        default is proof=True), then this function may use a
+        default is proof=None, see proof.polynomial or sage.structure.proof,
+        but the global default is True), then this function may use a
         randomized strategy that errors with probability no more than
         $2^{-80}$.
 
@@ -1028,15 +1034,18 @@ cdef class ntl_ZZX:
             1345873
         """
         # NOTES: Within a factor of 2 in speed compared to MAGMA.
+        proof = proof_flag(proof)
         _sig_on
         return make_ZZ(ZZX_resultant(self.x, other.x, proof))
 
-    def norm_mod(self, ntl_ZZX modulus, proof=True):
+    def norm_mod(self, ntl_ZZX modulus, proof=None):
         """
         Return the norm of this polynomial modulo the modulus.  The
         modulus must be monic, and of positive degree strictly greater
         than the degree of self.  If proof=False (the default is
-        proof=True) then it may use a randomized strategy that errors
+        proof=None, see proof.polynomial or sage.structure.proof, but
+        the global default is proof=True)
+        then it may use a randomized strategy that errors
         with probability no more than $2^{-80}$.
 
 
@@ -1050,17 +1059,20 @@ cdef class ntl_ZZX:
             sage: f.charpoly_mod(mod)
             [-8846 -594 -60 14 1]
         """
+        proof = proof_flag(proof)
         _sig_on
         return make_ZZ(ZZX_norm_mod(self.x, modulus.x, proof))
 
-    def discriminant(self, proof=True):
+    def discriminant(self, proof=None):
         r"""
         Return the discriminant of self, which is by definition
         $$
                 (-1)^{m(m-1)/2} {\mbox{\tt resultant}}(a, a')/lc(a),
         $$      
         where m = deg(a), and lc(a) is the leading coefficient of a.
-        If proof is False (the default is True), then this function
+        If proof is False (the default is
+        proof=None, see proof.polynomial or sage.structure.proof, but
+        the global default is proof=True), then this function
         may use a randomized strategy that errors with probability no
         more than $2^{-80}$.
         EXAMPLES:
@@ -1070,6 +1082,7 @@ cdef class ntl_ZZX:
             sage: f.discriminant(proof=False)
             -339
         """
+        proof = proof_flag(proof)
         _sig_on
         return make_ZZ(ZZX_discriminant(self.x, proof))
 
@@ -1077,11 +1090,13 @@ cdef class ntl_ZZX:
     #    _sig_on
     #    return make_ZZ(ZZX_polyeval(self.x, a.x))
 
-    def charpoly_mod(self, ntl_ZZX modulus, proof=True):
+    def charpoly_mod(self, ntl_ZZX modulus, proof=None):
         """
         Return the characteristic polynomial of this polynomial modulo
         the modulus.  The modulus must be monic of degree bigger than
-        self. If proof=False (the default is True), then this function
+        self. If proof=False (the default is
+        proof=None, see proof.polynomial or sage.structure.proof, but
+        the global default is proof=True), then this function
         may use a randomized strategy that errors with probability no
         more than $2^{-80}$.
 
@@ -1092,6 +1107,7 @@ cdef class ntl_ZZX:
             [-8846 -594 -60 14 1]
 
         """
+        proof = proof_flag(proof)
         _sig_on
         return make_ZZX(ZZX_charpoly_mod(self.x, modulus.x, proof))
 
```



---

Comment by was created at 2007-09-20 21:18:57

Resolution: fixed
