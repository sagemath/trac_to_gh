# Issue 1445: [with patch] symmetrica's longints need to be converted

archive/issues_001445.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\n\n```\nsage: time a = f^8\n---------------------------------------------------------------------------\n<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)\n\n/opt/sage-2.9.alpha1/devel/sage-main/sage/rings/polynomial/<ipython console> in <module>()\n\n/opt/sage-2.9.alpha1/local/lib/python2.5/site-packages/IPython/iplib.py in ipmagic(self, arg_s)\n    962         else:\n    963             magic_args = self.var_expand(magic_args,1)\n--> 964             return fn(magic_args)\n    965 \n    966     def ipalias(self,arg_s):\n\n/opt/sage-2.9.alpha1/local/lib/python2.5/site-packages/IPython/Magic.py in magic_time(self, parameter_s)\n   1855         else:\n   1856             st = clk()\n-> 1857             exec code in glob\n   1858             end = clk()\n   1859             out = None\n\n/opt/sage-2.9.alpha1/devel/sage-main/sage/rings/polynomial/<timed exec> in <module>()\n\n/opt/sage-2.9.alpha1/local/lib/python2.5/site-packages/sage/combinat/sf/classical.py in __pow__(self, n)\n    586         z = A(Integer(1))\n    587         for i in range(n):\n--> 588             z *= self\n    589         return z\n    590 \n\n/opt/sage-2.9.alpha1/devel/sage-main/sage/rings/polynomial/element.pyx in sage.structure.element.RingElement.__imul__()\n\n/opt/sage-2.9.alpha1/devel/sage-main/sage/rings/polynomial/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c()\n\n/opt/sage-2.9.alpha1/devel/sage-main/sage/rings/polynomial/element.pyx in sage.structure.element.RingElement.__imul__()\n\n/opt/sage-2.9.alpha1/devel/sage-main/sage/rings/polynomial/coerce.pxi in sage.structure.element._mul_c()\n\n/opt/sage-2.9.alpha1/local/lib/python2.5/site-packages/sage/combinat/combinatorial_algebra.py in _mul_(self, y)\n    152                         \n    153     def _mul_(self, y):\n--> 154         return self.parent().multiply(self, y)\n    155 \n    156     def _div_(self, y):\n\n/opt/sage-2.9.alpha1/local/lib/python2.5/site-packages/sage/combinat/combinatorial_algebra.py in multiply(self, left, right)\n    475         #coefficients as values\n    476         else:\n--> 477             m = self._multiply(left, right)\n    478             if isinstance(m, self._element_class):\n    479                 return m\n\n/opt/sage-2.9.alpha1/local/lib/python2.5/site-packages/sage/combinat/sf/schur.py in _multiply(self, left, right)\n     80 \n     81         if  R is ZZ or R is QQ:\n---> 82             return symmetrica.mult_schur_schur(left, right)\n     83 \n     84         z_elt = {}\n\n/opt/sage-2.9.alpha1/devel/sage-main/sage/rings/polynomial/schur.pxi in sage.libs.symmetrica.symmetrica.mult_schur_schur_symmetrica()\n\n/opt/sage-2.9.alpha1/devel/sage-main/sage/rings/polynomial/symmetrica.pxi in sage.libs.symmetrica.symmetrica._py()\n\n/opt/sage-2.9.alpha1/devel/sage-main/sage/rings/polynomial/symmetrica.pxi in sage.libs.symmetrica.symmetrica._py_schur()\n\n/opt/sage-2.9.alpha1/devel/sage-main/sage/rings/polynomial/symmetrica.pxi in sage.libs.symmetrica.symmetrica._py_schur_general()\n\n/opt/sage-2.9.alpha1/devel/sage-main/sage/rings/polynomial/symmetrica.pxi in sage.libs.symmetrica.symmetrica._py()\n\n<type 'exceptions.NotImplementedError'>: 22\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1445\n\n",
    "created_at": "2007-12-10T04:31:49Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "[with patch] symmetrica's longints need to be converted",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1445",
    "user": "mhansen"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/1445





---

archive/issue_comments_009319.json:
```json
{
    "body": "Attachment [symmetrica-longint.patch](tarball://root/attachments/some-uuid/ticket1445/symmetrica-longint.patch) by mhansen created at 2007-12-10 04:32:18",
    "created_at": "2007-12-10T04:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1445#issuecomment-9319",
    "user": "mhansen"
}
```

Attachment [symmetrica-longint.patch](tarball://root/attachments/some-uuid/ticket1445/symmetrica-longint.patch) by mhansen created at 2007-12-10 04:32:18



---

archive/issue_comments_009320.json:
```json
{
    "body": "Attachment [1445-doctest.patch](tarball://root/attachments/some-uuid/ticket1445/1445-doctest.patch) by mabshoff created at 2007-12-10 05:26:58\n\nMerged in 2.9.alpha3.",
    "created_at": "2007-12-10T05:26:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1445#issuecomment-9320",
    "user": "mabshoff"
}
```

Attachment [1445-doctest.patch](tarball://root/attachments/some-uuid/ticket1445/1445-doctest.patch) by mabshoff created at 2007-12-10 05:26:58

Merged in 2.9.alpha3.



---

archive/issue_comments_009321.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-10T05:26:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1445#issuecomment-9321",
    "user": "mabshoff"
}
```

Resolution: fixed
