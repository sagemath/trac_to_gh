# Issue 1445: [with patch] symmetrica's longints need to be converted

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2007-12-10 04:31:49

Assignee: mhansen

CC:  sage-combinat


```
sage: time a = f^8
---------------------------------------------------------------------------
<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)

/opt/sage-2.9.alpha1/devel/sage-main/sage/rings/polynomial/<ipython console> in <module>()

/opt/sage-2.9.alpha1/local/lib/python2.5/site-packages/IPython/iplib.py in ipmagic(self, arg_s)
    962         else:
    963             magic_args = self.var_expand(magic_args,1)
--> 964             return fn(magic_args)
    965 
    966     def ipalias(self,arg_s):

/opt/sage-2.9.alpha1/local/lib/python2.5/site-packages/IPython/Magic.py in magic_time(self, parameter_s)
   1855         else:
   1856             st = clk()
-> 1857             exec code in glob
   1858             end = clk()
   1859             out = None

/opt/sage-2.9.alpha1/devel/sage-main/sage/rings/polynomial/<timed exec> in <module>()

/opt/sage-2.9.alpha1/local/lib/python2.5/site-packages/sage/combinat/sf/classical.py in __pow__(self, n)
    586         z = A(Integer(1))
    587         for i in range(n):
--> 588             z *= self
    589         return z
    590 

/opt/sage-2.9.alpha1/devel/sage-main/sage/rings/polynomial/element.pyx in sage.structure.element.RingElement.__imul__()

/opt/sage-2.9.alpha1/devel/sage-main/sage/rings/polynomial/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c()

/opt/sage-2.9.alpha1/devel/sage-main/sage/rings/polynomial/element.pyx in sage.structure.element.RingElement.__imul__()

/opt/sage-2.9.alpha1/devel/sage-main/sage/rings/polynomial/coerce.pxi in sage.structure.element._mul_c()

/opt/sage-2.9.alpha1/local/lib/python2.5/site-packages/sage/combinat/combinatorial_algebra.py in _mul_(self, y)
    152                         
    153     def _mul_(self, y):
--> 154         return self.parent().multiply(self, y)
    155 
    156     def _div_(self, y):

/opt/sage-2.9.alpha1/local/lib/python2.5/site-packages/sage/combinat/combinatorial_algebra.py in multiply(self, left, right)
    475         #coefficients as values
    476         else:
--> 477             m = self._multiply(left, right)
    478             if isinstance(m, self._element_class):
    479                 return m

/opt/sage-2.9.alpha1/local/lib/python2.5/site-packages/sage/combinat/sf/schur.py in _multiply(self, left, right)
     80 
     81         if  R is ZZ or R is QQ:
---> 82             return symmetrica.mult_schur_schur(left, right)
     83 
     84         z_elt = {}

/opt/sage-2.9.alpha1/devel/sage-main/sage/rings/polynomial/schur.pxi in sage.libs.symmetrica.symmetrica.mult_schur_schur_symmetrica()

/opt/sage-2.9.alpha1/devel/sage-main/sage/rings/polynomial/symmetrica.pxi in sage.libs.symmetrica.symmetrica._py()

/opt/sage-2.9.alpha1/devel/sage-main/sage/rings/polynomial/symmetrica.pxi in sage.libs.symmetrica.symmetrica._py_schur()

/opt/sage-2.9.alpha1/devel/sage-main/sage/rings/polynomial/symmetrica.pxi in sage.libs.symmetrica.symmetrica._py_schur_general()

/opt/sage-2.9.alpha1/devel/sage-main/sage/rings/polynomial/symmetrica.pxi in sage.libs.symmetrica.symmetrica._py()

<type 'exceptions.NotImplementedError'>: 22
```



---

Attachment


---

Attachment

Merged in 2.9.alpha3.


---

Comment by mabshoff created at 2007-12-10 05:26:58

Resolution: fixed
