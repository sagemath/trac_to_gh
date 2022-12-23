# Issue 177: pari interface -- transition to new arithmetic model

Issue created by migration from https://trac.sagemath.org/ticket/177

Original creator: was

Original creation time: 2006-12-04 13:52:37

Assignee: somebody


```
On Mon, 04 Dec 2006 05:37:02 -0800, Luislang <dpl@sun.ac.za> wrote:

>
>
>
> sage: a=pari('a')
> sage: a+1
>  _4 = a + 1
> sage: 1+a
> ------------------------------------------------------------
> Traceback (most recent call last):
>   File "<console>", line 1, in ?
>   File "integer.pyx", line 471, in integer.Integer.__add__
>   File "coerce.pyx", line 123, in coerce.bin_op
> TypeError: unable to find a common parent for 1 (parent: Integer Ring)
> and a (parent: Interface to the PARI C library)

Thanks for the bug report.  This is because in SAGE-1.5, I evidently forgot
to transition the PARI interface to the new arithmetic model (in libs/pari/gen.pyx):

    def __add__(self, other):
        if isinstance(self, gen) and isinstance(other, gen):
            return self._add(other)
        return sage.structure.coerce.bin_op(self, other, operator.add)

but it should be _add_c_impl, etc.  Thanks.

By the way, in the future a+1 and 1+a will both be defined and be
elements of "the PARI C library ring", since there is a canonical map
from Z to PARI. 

This currently works currently for the GP interface:

sage: a=gp('a')
sage: 1+a
a + 1
sage: a+1
a + 1
sage: parent(a+1)
GP/PARI interpreter
```



---

Comment by was created at 2007-01-25 18:36:24

Resolution: fixed


---

Comment by was created at 2007-01-25 18:36:24

done for sage > 1.8.2.1


```
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1169749924 28800
# Node ID 8faeaa5cc7cbc2f90c980a2011c354ba5479f615
# Parent  77fad05c682bd6d4d76524f689941195f82778e6
Transition pari interface to new arithmetic architecture.

diff -r 77fad05c682b -r 8faeaa5cc7cb sage/libs/pari/gen.pxd
--- a/sage/libs/pari/gen.pxd    Thu Jan 25 07:12:49 2007 -0800
+++ b/sage/libs/pari/gen.pxd    Thu Jan 25 10:32:04 2007 -0800
@@ -1,6 +1,8 @@ include 'decl.pxi'
 include 'decl.pxi'
 
-cdef class gen:
+cimport sage.structure.element 
+
+cdef class gen(sage.structure.element.RingElement):
     cdef GEN g
     cdef object refers_to
     cdef pari_sp b
@@ -12,7 +14,9 @@ cdef class gen:
     cdef GEN _deepcopy_to_python_heap(self, GEN x, pari_sp* address)
     cdef int get_var(self, v)    
 
-cdef class PariInstance:
+cimport sage.structure.parent_base
+
+cdef class PariInstance(sage.structure.parent_base.ParentWithBase):
     cdef gen ZERO, ONE, TWO
     cdef gen new_gen(self, GEN x)
     cdef gen new_gen_noclear(self, GEN x)
diff -r 77fad05c682b -r 8faeaa5cc7cb sage/libs/pari/gen.pyx
--- a/sage/libs/pari/gen.pyx    Thu Jan 25 07:12:49 2007 -0800
+++ b/sage/libs/pari/gen.pyx    Thu Jan 25 10:32:04 2007 -0800
@@ -8,7 +8,26 @@ AUTHORS:
              from any version to the next...).
     -- William Stein (2006-03-06): added newtonpoly
     -- Justin Walker: contributed some of the function definitions
-    -- Gonzalo Tornari: improvements to conversions; much better error handling. 
+    -- Gonzalo Tornari: improvements to conversions; much better error handling.
+
+EXAMPLES:
+    sage: pari('5! + 10/x')
+    (120*x + 10)/x
+    sage: pari('intnum(x=0,13,sin(x)+sin(x^2) + x)')
+    85.18856819515268446242866615
+    sage: f = pari('x^3-1')
+    sage: v = f.factor(); v
+    [x - 1, 1; x^2 + x + 1, 1]
+    sage: v[0]   # indexing is 0-based unlike in GP.
+    [x - 1, x^2 + x + 1]~
+    sage: v[1]
+    [1, 1]~    
+    
+Arithmetic obeys the usual coercion rules.
+    sage: type(pari(1) + 1)
+    <type 'sage.libs.pari.gen.gen'>
+    sage: type(1 + pari(1))
+    <type 'sage.libs.pari.gen.gen'>    
 """
 
 import math
@@ -16,7 +35,10 @@ from sage.misc.misc import xsrange
 from sage.misc.misc import xsrange
 import sage.structure.coerce
 import operator
-
+from sage.structure.element cimport ModuleElement, RingElement, Element
+from sage.structure.parent cimport Parent
+
+#include '../../ext/interrupt.pxi'
 include 'pari_err.pxi'
 include 'setlvalue.pxi'
 include '../../ext/stdsage.pxi'
@@ -33,6 +55,8 @@ P = pari_instance   # shorthand notation
 # See the polgalois section of the PARI users manual.
 new_galois_format = 1   
 
+cdef pari_sp mytop
+
 # keep track of the stack
 cdef pari_sp stack_avma
 
@@ -66,13 +90,13 @@ cdef t4GEN(x):
     global t4
     t4 = P.toGEN(x)
 
-cdef class gen:
+cdef class gen(sage.structure.element.RingElement):
     """
     Python extension class that models the PARI GEN type.
     """
     def __init__(self):
         self.b = 0
-        self.refers_to = {}
+        self._parent = P
 
     def parent(self):
         return pari_instance
@@ -86,6 +110,7 @@ cdef class gen:
         """
         self.g = g
         self.b = b
+        self._parent = P
 
     def __dealloc__(self):
         if self.b:
@@ -117,49 +142,129 @@ cdef class gen:
         return list(self.Vec())
         
     def __reduce__(self):
+        """
+        EXAMPLES:
+            sage: f = pari('x^3 - 3')
+            sage: loads(dumps(f)) == f
+            True
+        """
         s = str(self)
         import sage.libs.pari.gen_py
         return sage.libs.pari.gen_py.pari, (s,)
 
-    def _add(gen self, gen other):
-        _sig_on
-        return P.new_gen(gadd(self.g, other.g))
-
-    def _sub(gen self, gen other):
-        _sig_on
-        return P.new_gen(gsub(self.g, other.g))
-
-    def _mul(gen self, gen other):
-        _sig_on
-        return P.new_gen(gmul(self.g, other.g))
+    cdef ModuleElement _add_c_impl(self, ModuleElement right):
+        _sig_on
+        return P.new_gen(gadd(self.g, (<gen>right).g))
+
+    def _add_unsafe(gen self, gen right):
+        """
+        VERY FAST addition of self and right on stack (and leave on
+        stack) without any type checking.
+
+        Basically, this is often about 10 times faster than just typing "self + right".
+        The drawback is that (1) if self + right would give an error in PARI, it will
+        totally crash SAGE, and (2) the memory used by self + right is *never*
+        returned -- it gets allocated on the PARI stack and will never be freed.
+
+        EXAMPLES:
+            sage: pari(2)._add_unsafe(pari(3))
+            5
+        """
+        global mytop
+        cdef GEN z
+        cdef gen w
+        z = gadd(self.g, right.g)
+        w = PY_NEW(gen)
+        w.init(z,0)
+        mytop = avma
+        return w
+    
+    cdef ModuleElement _sub_c_impl(self, ModuleElement right):
+        _sig_on
+        return P.new_gen(gsub(self.g, (<gen> right).g))
+
+    def _sub_unsafe(gen self, gen right):
+        """
+        VERY FAST subtraction of self and right on stack (and leave on
+        stack) without any type checking.
+
+        Basically, this is often about 10 times faster than just typing "self - right".
+        The drawback is that (1) if self - right would give an error in PARI, it will
+        totally crash SAGE, and (2) the memory used by self + right is *never*
+        returned -- it gets allocated on the PARI stack and will never be freed.
+
+        EXAMPLES:
+            sage: pari(2)._sub_unsafe(pari(3))
+            -1
+        """
+        global mytop
+        cdef GEN z
+        cdef gen w
+        z = gsub(self.g, right.g)
+        w = PY_NEW(gen)
+        w.init(z, 0)
+        mytop = avma
+        return w
+
+    cdef RingElement _mul_c_impl(self, RingElement right):    
+        _sig_on
+        return P.new_gen(gmul(self.g, (<gen>right).g))
+
+    def _mul_unsafe(gen self, gen right):
+        """
+        VERY FAST multiplication of self and right on stack (and leave on
+        stack) without any type checking.
+
+        Basically, this is often about 10 times faster than just typing "self * right".
+        The drawback is that (1) if self - right would give an error in PARI, it will
+        totally crash SAGE, and (2) the memory used by self + right is *never*
+        returned -- it gets allocated on the PARI stack and will never be freed.
+        
+        EXAMPLES:
+            sage: pari(2)._mul_unsafe(pari(3))
+            6
+        """
+        global mytop
+        cdef GEN z
+        cdef gen w
+        z = gmul(self.g, right.g)
+        w = PY_NEW(gen)
+        w.init(z, 0)
+        mytop = avma
+        return w
+
+    cdef RingElement _div_c_impl(self, RingElement right):    
+        _sig_on
+        return P.new_gen(gdiv(self.g, (<gen>right).g))
+
+    def _div_unsafe(gen self, gen right):
+        """
+        VERY FAST division of self and right on stack (and leave on
+        stack) without any type checking.
+
+        Basically, this is often about 10 times faster than just typing "self / right".
+        The drawback is that (1) if self - right would give an error in PARI, it will
+        totally crash SAGE, and (2) the memory used by self + right is *never*
+        returned -- it gets allocated on the PARI stack and will never be freed.
+
+        EXAMPLES:
+            sage: pari(2)._div_unsafe(pari(3))
+            2/3                    
+        """
+        global mytop
+        cdef GEN z
+        cdef gen w
+        z = gdiv(self.g, right.g)
+        w = PY_NEW(gen)
+        w.init(z, 0)
+        mytop = avma
+        return w
+
+    #################################################################
 
     def _mod(gen self, gen other):
         _sig_on
         return P.new_gen(gmod(self.g, other.g))
-
-    def _div(gen self, gen other):
-        _sig_on
-        return P.new_gen(gdiv(self.g, other.g))
-
-    def __add__(self, other):
-        if isinstance(self, gen) and isinstance(other, gen):
-            return self._add(other)
-        return sage.structure.coerce.bin_op(self, other, operator.add)
-
-    def __sub__(self, other):
-        if isinstance(self, gen) and isinstance(other, gen):
-            return self._sub(other)
-        return sage.structure.coerce.bin_op(self, other, operator.sub)
-
-    def __mul__(self, other):
-        if isinstance(self, gen) and isinstance(other, gen):
-            return self._mul(other)
-        return sage.structure.coerce.bin_op(self, other, operator.mul)
-
-    def __div__(self, other):
-        if isinstance(self, gen) and isinstance(other, gen):
-            return self._div(other)
-        return sage.structure.coerce.bin_op(self, other, operator.div)
 
     def __mod__(self, other):
         if isinstance(self, gen) and isinstance(other, gen):
@@ -424,7 +529,10 @@ cdef class gen:
         _sig_on
         x = pari(y)
         if isinstance(n, tuple):
-            self.refers_to[n] = x
+            try:
+                self.refers_to[n] = x
+            except TypeError:
+                self.refers_to = {n:x}
             i = n[0]
             j = n[1]
             if i < 0 or i >= self.nrows():
@@ -436,10 +544,14 @@ cdef class gen:
 
         if n < 0 or n >= glength(self.g):
             raise IndexError, "index (%s) must be between 0 and %s"%(n,glength(self.g)-1)
-        
-        self.refers_to[n] = x       # so python memory manager will work correctly
-                                    # and not free x if PARI part of self is the
-                                    # only thing pointing to it.
+
+        # so python memory manager will work correctly
+        # and not free x if PARI part of self is the
+        # only thing pointing to it.        
+        try:
+            self.refers_to[n] = x
+        except TypeError:
+            self.refers_to = {n:x}
 
         if typ(self.g) == t_POL:
             n = n + 1
@@ -466,8 +578,11 @@ cdef class gen:
         result = gcmp(self.g, other.g)
         _sig_off
         return result
-    
-    def __cmp__(gen self, gen other):
+
+    def __richcmp__(left, right, int op):
+        return (<Element>left)._richcmp(right, op)
+    
+    cdef int _cmp_c_impl(left, Element right) except -2:
         """
         Comparisons
 
@@ -475,24 +590,6 @@ cdef class gen:
         not comparable, it then compares the underlying strings (since
         in Python all objects are supposed to be comparable).
 
-        EXAMPLES:
-            sage: pari(2.5) > None
-            False
-            sage: pari(3) == pari(3)
-            True
-            sage: pari('x^2 + 1') == pari('I-1')
-            False
-            sage: pari(I) == pari(I)
-            True           
-        """
-        try:
-            return self._cmp(other)
-        except PariError:
-            pass
-        return cmp(str(self),str(other))
-
-    def __richcmp__(gen self, other, int op):
-        """
         EXAMPLES:
             sage: a = pari(5)
             sage: b = 10
@@ -512,23 +609,21 @@ cdef class gen:
             True
             sage: a is 5
             False
-        """
-        cdef int n
-        cdef gen x
-        x = P.adapt(other)
-        n = self.__cmp__(x)
-        if op == 0:
-            return bool(n < 0)
-        elif op == 1:
-            return bool(n <= 0)
-        elif op == 2:
-            return bool(n == 0)
-        elif op == 3:
-            return bool(n != 0)
-        elif op == 4:
-            return bool(n > 0)
-        elif op == 5:
-            return bool(n >= 0)
+
+            sage: pari(2.5) > None
+            False
+            sage: pari(3) == pari(3)
+            True
+            sage: pari('x^2 + 1') == pari('I-1')
+            False
+            sage: pari(I) == pari(I)
+            True           
+        """
+        try:
+            return left._cmp(right)
+        except PariError:
+            pass
+        return cmp(str(left),str(right))
 
     def copy(gen self):
         return P.new_gen(forcecopy(self.g))
@@ -5019,7 +5114,7 @@ cdef class gen:
 
 cdef unsigned long num_primes
 
-cdef class PariInstance:
+cdef class PariInstance(sage.structure.parent_base.ParentWithBase):
     def __init__(self, long size=16000000, unsigned long maxprime=500000):
         """
         Initialize the PARI system.
@@ -5087,6 +5182,24 @@ cdef class PariInstance:
     def __repr__(self):
         return "Interface to the PARI C library"
 
+    def __hash__(self):
+        return 907629390   # hash('pari')
+
+    cdef has_coerce_map_from_c_impl(self, x):
+        return True
+
+    def __richcmp__(left, right, int op):
+        """
+        EXAMPLES:
+            sage: pari == pari
+            True
+            sage: pari == gp
+            False
+            sage: pari == 5
+            False
+        """
+        return (<Parent>left)._richcmp(right, op)
+
     def default(self, variable, value=None):
         if not value is None:
             return self('default(%s, %s)'%(variable, value))
@@ -5161,8 +5274,8 @@ cdef class PariInstance:
         cdef gen g
         g = _new_gen(x)
         
-        global top, avma
-        avma = top
+        global mytop, avma
+        avma = mytop
         _sig_off
         return g
 
@@ -5181,8 +5294,11 @@ cdef class PariInstance:
         cdef gen p
         p = gen()
         p.init(x, 0)
-        p.refers_to[-1] = g  # so underlying memory won't get deleted
-                             # out from under us.
+        try:
+            p.refers_to[-1] = g  # so underlying memory won't get deleted
+                                 # out from under us.
+        except TypeError:
+            p.refers_to = {-1:g}
         return p
 
     cdef gen adapt(self, s):
@@ -5223,7 +5339,7 @@ cdef class PariInstance:
         _sig_off
         return self.new_gen(g)
         
-    def _coerce_(self, x):
+    cdef _coerce_c_impl(self, x):
         """
         Implicit canonical coercion into a PARI object.
         """
@@ -5234,6 +5350,9 @@ cdef class PariInstance:
         if isinstance(x, gen):
             return x
         raise TypeError, "x must be a PARI object"
+
+    cdef _an_element_c_impl(self):  # override this in SageX
+        return self.ZERO
 
     def new_with_prec(self, s, long precision=0):
         r"""
@@ -5628,7 +5747,7 @@ cdef int init_stack(size_t size) except 
 cdef int init_stack(size_t size) except -1:
     cdef size_t s
 
-    global top, bot, avma, stack_avma
+    global top, bot, avma, stack_avma, mytop
 
     # delete this if get core dumps and change the 2* to a 1* below.
     if bot:
@@ -5656,8 +5775,8 @@ cdef int init_stack(size_t size) except 
         if not bot:
             raise MemoryError, "Unable to allocate %s bytes memory for PARI."%(<long>size)
     #endif
-
     top = bot + s
+    mytop = top
     avma = top
     stack_avma = avma
 
@@ -5676,7 +5795,7 @@ cdef GEN deepcopy_to_python_heap(GEN x, 
 cdef GEN deepcopy_to_python_heap(GEN x, pari_sp* address):
     cdef size_t s
     cdef pari_sp tmp_bot, tmp_top, tmp_avma
-    global avma, bot, top
+    global avma, bot, top, mytop
     cdef GEN h
 
     tmp_top = top
@@ -5699,14 +5818,23 @@ cdef GEN deepcopy_to_python_heap(GEN x, 
     avma = tmp_avma
     return h
 
+# The first one makes a separate copy on the heap, so the stack
+# won't overflow -- but this costs more time...
 cdef gen _new_gen(GEN x):
     cdef GEN h
     cdef pari_sp address
     cdef gen y
     _sig_on
     h = deepcopy_to_python_heap(x, &address)
-    y = gen()    
+    y = PY_NEW(gen)
     y.init(h, address)
+    _sig_off
+    return y
+
+cdef gen xxx_new_gen(GEN x):
+    cdef gen y
+    y = PY_NEW(gen)
+    y.init(x, 0)
     _sig_off
     return y
 
@@ -5733,8 +5861,8 @@ cdef int _read_script(char* s) except -1
 
     # We set top to avma, so the script's affects won't be undone
     # when we call new_gen again.
-    global top, avma
-    top = avma
+    global mytop, top, avma
+    mytop = avma
     return 0
 
 
diff -r 77fad05c682b -r 8faeaa5cc7cb sage/modules/complex_double_vector.pxd
--- a/sage/modules/complex_double_vector.pxd    Thu Jan 25 07:12:49 2007 -0800
+++ b/sage/modules/complex_double_vector.pxd    Thu Jan 25 10:32:04 2007 -0800
@@ -1,6 +1,8 @@ include '../ext/cdefs.pxi'
 include '../ext/cdefs.pxi'
 include '../ext/interrupt.pxi'
 include '../gsl/gsl.pxi'
+
+cimport sage.structure.element
 
 cimport free_module_element
 import  free_module_element
diff -r 77fad05c682b -r 8faeaa5cc7cb sage/modules/complex_double_vector.pyx
--- a/sage/modules/complex_double_vector.pyx    Thu Jan 25 07:12:49 2007 -0800
+++ b/sage/modules/complex_double_vector.pyx    Thu Jan 25 10:32:04 2007 -0800
@@ -35,8 +35,8 @@ import  free_module_element
 
 from sage.structure.element cimport Element, ModuleElement, RingElement
 
+from sage.rings.complex_double import CDF, new_ComplexDoubleElement
 from sage.rings.complex_double cimport ComplexDoubleElement
-from sage.rings.complex_double import CDF, new_ComplexDoubleElement
 
 include '../ext/stdsage.pxi'
 
diff -r 77fad05c682b -r 8faeaa5cc7cb sage/rings/number_field/number_field.py
--- a/sage/rings/number_field/number_field.py   Thu Jan 25 07:12:49 2007 -0800
+++ b/sage/rings/number_field/number_field.py   Thu Jan 25 10:32:04 2007 -0800
@@ -489,7 +489,7 @@ class NumberField_generic(field.Field):
             
         Here are the factors:
            
-           sage: fi, fj = K.factor_integer(13);fi,fj
+           sage: fi, fj = K.factor_integer(13); fi,fj
             ((Fractional ideal (3*I - 2) of Number Field in I with defining polynomial x^2 + 1, 1),
             (Fractional ideal (-3*I - 2) of Number Field in I with defining polynomial x^2 + 1, 1))
             
diff -r 77fad05c682b -r 8faeaa5cc7cb sage/rings/number_field/number_field_ideal.py
--- a/sage/rings/number_field/number_field_ideal.py     Thu Jan 25 07:12:49 2007 -0800
+++ b/sage/rings/number_field/number_field_ideal.py     Thu Jan 25 10:32:04 2007 -0800
@@ -363,7 +363,7 @@ class NumberFieldIdeal(Ideal_fractional)
                 return self.__is_principal
             bnf = self.number_field().pari_bnf(certify)
             v = bnf.bnfisprincipal(self.pari_hnf())
-            self.__is_principal = (v[0] == 0) ## i.e., v[0] is the zero vector
+            self.__is_principal = (len(v[0]) == 0) ## i.e., v[0] is the zero vector
             if self.__is_principal:
                 K = self.number_field()
                 R = K.polynomial().parent()
@@ -542,7 +542,7 @@ class NumberFieldIdeal_rel(NumberFieldId
             sage: K.<a> = NumberField(x^2+6)
             sage: L.<b> = K.extension(K['x'].gen()^4 + a)
             sage: L.ideal(b).norm()
-            Fractional ideal (-a) of Number Field in a with defining polynomial x^2 + 6
+            Fractional ideal (a) of Number Field in a with defining polynomial x^2 + 6
         """
         L = self.number_field()
         K = L.base_field()
diff -r 77fad05c682b -r 8faeaa5cc7cb sage/structure/element.pyx
--- a/sage/structure/element.pyx        Thu Jan 25 07:12:49 2007 -0800
+++ b/sage/structure/element.pyx        Thu Jan 25 10:32:04 2007 -0800
@@ -1832,6 +1832,7 @@ cdef bin_op_c(x, y, op):
         x1, y1 = canonical_coercion_c(x, y)
         return op(x1,y1)        
     except TypeError, msg:
+        # print msg  # this can be useful for debugging.
         if not op is operator.mul:
             raise TypeError, arith_error_message(x,y,op)
 
diff -r 77fad05c682b -r 8faeaa5cc7cb setup.py
--- a/setup.py  Thu Jan 25 07:12:49 2007 -0800
+++ b/setup.py  Thu Jan 25 10:32:04 2007 -0800
@@ -549,7 +549,7 @@ def need_to_pyrex(filename, outfile):
         # Check to see if a/b/c/d.pxd exists and is newer than filename.
         # If so, we have to regenerate outfile.  If not, we're safe.
         if os.path.exists(A) and is_older(A, outfile):
-            print "\nBuilding %s because it depends on %s."%(outfile, A)
+            print "\nRegenerating %s because it depends on %s."%(outfile, A)
             return True # yep we must rebuild
 
     # OK, next we move on to include pxi files.
```

