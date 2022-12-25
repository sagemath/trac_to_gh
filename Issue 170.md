# Issue 170: QQ('1/0')

archive/issues_000170.json:
```json
{
    "body": "Assignee: somebody\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/170\n\n",
    "created_at": "2006-11-28T21:41:04Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "title": "QQ('1/0')",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/170",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody



Issue created by migration from https://trac.sagemath.org/ticket/170





---

archive/issue_comments_000779.json:
```json
{
    "body": "Fixed, along with some other related problems.  Basically it's necessary to program around a bug in GMP. \n\n```\n# HG changeset patch\n# User William Stein <wstein@gmail.com>\n# Date 1168651986 28800\n# Node ID 931f47e34e11519acdd0b2bb8ae0c811c252e13f\n# Parent  4ee645ba1eb61c95dbc383f05e8ea09da8682b7a\nFix trac bug #170 -- QQ('1/0') plus fix some other related issues with rational.pyx\n\ndiff -r 4ee645ba1eb6 -r 931f47e34e11 sage/rings/rational.pyx\n--- a/sage/rings/rational.pyx   Fri Jan 12 16:29:26 2007 -0800\n+++ b/sage/rings/rational.pyx   Fri Jan 12 17:33:06 2007 -0800\n@@ -104,7 +104,26 @@ the_rational_ring = sage.rings.rational_\n the_rational_ring = sage.rings.rational_field.Q\n     \n cdef class Rational(sage.structure.element.FieldElement):\n-\n+    \"\"\"\n+    A Rational number.\n+\n+    Rational numbers are implemented using the GMP C library.\n+\n+    EXAMPLES:\n+        sage: a = -2/3\n+        sage: type(a)\n+        <type 'sage.rings.rational.Rational'>\n+        sage: parent(a)\n+        Rational Field\n+        sage: Rational('1/0')\n+        Traceback (most recent call last):\n+        ...\n+        TypeError: unable to convert 1/0 to a rational        \n+        sage: Rational(1.5)\n+        3/2\n+        sage: Rational('9/6')\n+        3/2\n+    \"\"\"\n     def __new__(self, x=None, int base=0):\n         global the_rational_ring\n         mpq_init(self.value)\n@@ -149,21 +168,25 @@ cdef class Rational(sage.structure.eleme\n \n         elif isinstance(x, long):\n             mpz_set_pylong(mpq_numref(self.value), x)\n-            #s = \"%x\"%x\n-            #mpq_set_str(self.value, s, 16)\n             \n         elif isinstance(x, integer.Integer):\n             set_from_Integer(self, x)\n \n         elif isinstance(x, sage.rings.real_mpfr.RealNumber):\n+            \n             if x == 0:\n                 mpq_set_si(self.value, 0, 1)\n                 return\n             if not base:\n                 v = x._pari_().contfrac().contfracpnqn()\n                 s = '%s/%s'%(hex(v[0,0]), hex(v[1,0]))\n-                if mpq_set_str(self.value, s, 16):\n+                n = mpq_set_str(self.value, s, 16)\n+                # this mpq_denref business is to program around a bug in GMP, where\n+                # it doesn't correctly return an error code in mpq_set_str (or canonicalalize)\n+                # for strings with a 0 in the denominator.   In fact, it crashes horribly.\n+                if n or mpz_cmp_si(mpq_denref(self.value), 0) == 0:\n                     raise TypeError, \"unable to convert %s to a rational\"%x\n+                mpq_canonicalize(self.value)                                    \n             else:\n                 xstr = x.str(base)\n                 if '.' in xstr:\n@@ -171,21 +194,21 @@ cdef class Rational(sage.structure.eleme\n                     p = base**exp\n                     pstr = '1'+'0'*exp\n                     s = xstr.replace('.','') +'/'+pstr\n-                    if mpq_set_str( self.value, s, base):\n+                    n = mpq_set_str( self.value, s, base)\n+                    if n or mpz_cmp_si(mpq_denref(self.value), 0) == 0:\n                         raise TypeError, \"unable to convert %s to a rational\"%x\n                     mpq_canonicalize(self.value)                    \n                 else:\n-                    if mpq_set_str(self.value, xstr, base):\n+                    n = mpq_set_str(self.value, xstr, base)\n+                    if n or mpz_cmp_si(mpq_denref(self.value), 0) == 0:\n                         raise TypeError, \"unable to convert %s to a rational\"%x\n                     mpq_canonicalize(self.value)\n             \n         elif isinstance(x, str):\n-            _sig_on\n-            if mpq_set_str(self.value, x, base):\n-                _sig_off\n+            n = mpq_set_str(self.value, x, base)\n+            if n or mpz_cmp_si(mpq_denref(self.value), 0) == 0:\n                 raise TypeError, \"unable to convert %s to a rational\"%x\n             mpq_canonicalize(self.value)\n-            _sig_off\n             \n         elif hasattr(x, \"_rational_\"):\n             set_from_Rational(self, x._rational_())\n@@ -194,12 +217,10 @@ cdef class Rational(sage.structure.eleme\n             s = \"%s/%s\"%x\n             if x[1] == 0:\n                 raise ValueError, \"denominator must not be 0\"\n-            _sig_on\n             n = mpq_set_str(self.value, s, 0)\n+            if n or mpz_cmp_si(mpq_denref(self.value), 0) == 0:\n+                raise TypeError, \"unable to convert %s to a rational\"%s\n             mpq_canonicalize(self.value)\n-            _sig_off\n-            if i:\n-                raise TypeError, \"unable to convert %s to a rational\"%s\n \n         elif isinstance(x, list) and len(x) == 1:\n             self.__set_value(x[0], base)\n@@ -207,7 +228,8 @@ cdef class Rational(sage.structure.eleme\n         elif isinstance(x, sage.libs.pari.all.pari_gen):\n             # TODO: figure out how to convert to pari integer in base 16\n             s = str(x)\n-            if mpq_set_str(self.value, s, 0):\n+            n = mpq_set_str(self.value, s, 0)\n+            if n or mpz_cmp_si(mpq_denref(self.value), 0) == 0:\n                 raise TypeError, \"Unable to coerce %s (%s) to Rational\"%(x,type(x))\n             \n         else:\n@@ -543,8 +565,10 @@ cdef class Rational(sage.structure.eleme\n \n     def set_str(self, s, base=10):\n         valid = mpq_set_str(self.value, s, base)\n-        if valid != 0:\n-            raise ValueError, \"invalid literal:\" + s\n+        if valid != 0 or mpz_cmp_si(mpq_denref(self.value), 0) == 0:\n+            mpq_set_si(self.value, 0, 1)  # so data is valid -- but don't waste time making backup.\n+            raise ValueError, \"invalid literal (%s); object set to 0\"%s\n+        mpq_canonicalize(self.value)\n \n     ################################################################\n     # Optimized arithmetic\n```\n",
    "created_at": "2007-01-13T01:33:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/170#issuecomment-779",
    "user": "https://github.com/williamstein"
}
```

Fixed, along with some other related problems.  Basically it's necessary to program around a bug in GMP. 

```
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1168651986 28800
# Node ID 931f47e34e11519acdd0b2bb8ae0c811c252e13f
# Parent  4ee645ba1eb61c95dbc383f05e8ea09da8682b7a
Fix trac bug #170 -- QQ('1/0') plus fix some other related issues with rational.pyx

diff -r 4ee645ba1eb6 -r 931f47e34e11 sage/rings/rational.pyx
--- a/sage/rings/rational.pyx   Fri Jan 12 16:29:26 2007 -0800
+++ b/sage/rings/rational.pyx   Fri Jan 12 17:33:06 2007 -0800
@@ -104,7 +104,26 @@ the_rational_ring = sage.rings.rational_
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
@@ -149,21 +168,25 @@ cdef class Rational(sage.structure.eleme
 
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
@@ -171,21 +194,21 @@ cdef class Rational(sage.structure.eleme
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
@@ -194,12 +217,10 @@ cdef class Rational(sage.structure.eleme
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
@@ -207,7 +228,8 @@ cdef class Rational(sage.structure.eleme
         elif isinstance(x, sage.libs.pari.all.pari_gen):
             # TODO: figure out how to convert to pari integer in base 16
             s = str(x)
-            if mpq_set_str(self.value, s, 0):
+            n = mpq_set_str(self.value, s, 0)
+            if n or mpz_cmp_si(mpq_denref(self.value), 0) == 0:
                 raise TypeError, "Unable to coerce %s (%s) to Rational"%(x,type(x))
             
         else:
@@ -543,8 +565,10 @@ cdef class Rational(sage.structure.eleme
 
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

archive/issue_comments_000780.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-13T01:33:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/170#issuecomment-780",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
