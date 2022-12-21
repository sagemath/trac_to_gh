# Issue 170: QQ('1/0')

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-11-28 21:41:04

Assignee: somebody




---

Comment by was created at 2007-01-13 01:33:51

Fixed, along with some other related problems.  Basically it's necessary to program around a bug in GMP. 

```
# HG changeset patch
# User William Stein <wstein`@`gmail.com>
# Date 1168651986 28800
# Node ID 931f47e34e11519acdd0b2bb8ae0c811c252e13f
# Parent  4ee645ba1eb61c95dbc383f05e8ea09da8682b7a
Fix trac bug #170 -- QQ('1/0') plus fix some other related issues with rational.pyx

diff -r 4ee645ba1eb6 -r 931f47e34e11 sage/rings/rational.pyx
--- a/sage/rings/rational.pyx   Fri Jan 12 16:29:26 2007 -0800
+++ b/sage/rings/rational.pyx   Fri Jan 12 17:33:06 2007 -0800
`@``@` -104,7 +104,26 `@``@` the_rational_ring = sage.rings.rational_
 the_rational_ring = sage.rings.rational_field.Q
     
 cdef class Rational(sage.structure.element.FieldElement):
-
+    """
+    A Rational number.
+
+    Rational numbers are implemented using the GMP C library.
+
+    EXAMPLES:
+        sage: a = -2/3
+        sage: type(a)
+        <type 'sage.rings.rational.Rational'>
+        sage: parent(a)
+        Rational Field
+        sage: Rational('1/0')
+        Traceback (most recent call last):
+        ...
+        TypeError: unable to convert 1/0 to a rational        
+        sage: Rational(1.5)
+        3/2
+        sage: Rational('9/6')
+        3/2
+    """
     def __new__(self, x=None, int base=0):
         global the_rational_ring
         mpq_init(self.value)
`@``@` -149,21 +168,25 `@``@` cdef class Rational(sage.structure.eleme
 
         elif isinstance(x, long):
             mpz_set_pylong(mpq_numref(self.value), x)
-            #s = "%x"%x
-            #mpq_set_str(self.value, s, 16)
             
         elif isinstance(x, integer.Integer):
             set_from_Integer(self, x)
 
         elif isinstance(x, sage.rings.real_mpfr.RealNumber):
+            
             if x == 0:
                 mpq_set_si(self.value, 0, 1)
                 return
             if not base:
                 v = x._pari_().contfrac().contfracpnqn()
                 s = '%s/%s'%(hex(v[0,0]), hex(v[1,0]))
-                if mpq_set_str(self.value, s, 16):
+                n = mpq_set_str(self.value, s, 16)
+                # this mpq_denref business is to program around a bug in GMP, where
+                # it doesn't correctly return an error code in mpq_set_str (or canonicalalize)
+                # for strings with a 0 in the denominator.   In fact, it crashes horribly.
+                if n or mpz_cmp_si(mpq_denref(self.value), 0) == 0:
                     raise TypeError, "unable to convert %s to a rational"%x
+                mpq_canonicalize(self.value)                                    
             else:
                 xstr = x.str(base)
                 if '.' in xstr:
`@``@` -171,21 +194,21 `@``@` cdef class Rational(sage.structure.eleme
                     p = base**exp
                     pstr = '1'+'0'*exp
                     s = xstr.replace('.','') +'/'+pstr
-                    if mpq_set_str( self.value, s, base):
+                    n = mpq_set_str( self.value, s, base)
+                    if n or mpz_cmp_si(mpq_denref(self.value), 0) == 0:
                         raise TypeError, "unable to convert %s to a rational"%x
                     mpq_canonicalize(self.value)                    
                 else:
-                    if mpq_set_str(self.value, xstr, base):
+                    n = mpq_set_str(self.value, xstr, base)
+                    if n or mpz_cmp_si(mpq_denref(self.value), 0) == 0:
                         raise TypeError, "unable to convert %s to a rational"%x
                     mpq_canonicalize(self.value)
             
         elif isinstance(x, str):
-            _sig_on
-            if mpq_set_str(self.value, x, base):
-                _sig_off
+            n = mpq_set_str(self.value, x, base)
+            if n or mpz_cmp_si(mpq_denref(self.value), 0) == 0:
                 raise TypeError, "unable to convert %s to a rational"%x
             mpq_canonicalize(self.value)
-            _sig_off
             
         elif hasattr(x, "_rational_"):
             set_from_Rational(self, x._rational_())
`@``@` -194,12 +217,10 `@``@` cdef class Rational(sage.structure.eleme
             s = "%s/%s"%x
             if x[1] == 0:
                 raise ValueError, "denominator must not be 0"
-            _sig_on
             n = mpq_set_str(self.value, s, 0)
+            if n or mpz_cmp_si(mpq_denref(self.value), 0) == 0:
+                raise TypeError, "unable to convert %s to a rational"%s
             mpq_canonicalize(self.value)
-            _sig_off
-            if i:
-                raise TypeError, "unable to convert %s to a rational"%s
 
         elif isinstance(x, list) and len(x) == 1:
             self.__set_value(x[0], base)
`@``@` -207,7 +228,8 `@``@` cdef class Rational(sage.structure.eleme
         elif isinstance(x, sage.libs.pari.all.pari_gen):
             # TODO: figure out how to convert to pari integer in base 16
             s = str(x)
-            if mpq_set_str(self.value, s, 0):
+            n = mpq_set_str(self.value, s, 0)
+            if n or mpz_cmp_si(mpq_denref(self.value), 0) == 0:
                 raise TypeError, "Unable to coerce %s (%s) to Rational"%(x,type(x))
             
         else:
`@``@` -543,8 +565,10 `@``@` cdef class Rational(sage.structure.eleme
 
     def set_str(self, s, base=10):
         valid = mpq_set_str(self.value, s, base)
-        if valid != 0:
-            raise ValueError, "invalid literal:" + s
+        if valid != 0 or mpz_cmp_si(mpq_denref(self.value), 0) == 0:
+            mpq_set_si(self.value, 0, 1)  # so data is valid -- but don't waste time making backup.
+            raise ValueError, "invalid literal (%s); object set to 0"%s
+        mpq_canonicalize(self.value)
 
     ################################################################
     # Optimized arithmetic
```



---

Comment by was created at 2007-01-13 01:33:51

Resolution: fixed
