# Issue 3100: coercion errors from SymbolicRing to various fields

archive/issues_003100.json:
```json
{
    "body": "Assignee: malb\n\nCC:  ncalexan\n\nKeywords: CC RR CIF RIF symbolic\n\nThis might need to be split up, but here goes:\n\nThis is just wrong:\n\n```\nsage: exp(2*I*pi*75132146442745860257639161594828134642293652547987666191250)\n1\nsage: CIF(exp(2*I*pi*75132146442745860257639161594828134642293652547987666191250))\n[-1.0000000000000000000000000000000000000000000000 .. 1.0000000000000000000000000000000000000000000000] + [-1.0000000000000000000000000000000000000000000000 .. 1.0000000000000000000000000000000000000000000000]*I\n```\n\n\nThat prompted me to try:\n *\n\n```\nsage: CC(exp(2*I*pi*75132146442745860257639161594828134642293652547987666191250))\n---------------------------------------------------------------------------\n<class 'sage.libs.pari.gen.PariError'>    Traceback (most recent call last)\n\n/Users/ncalexan/<ipython console> in <module>()\n\n/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/rings/complex_field.py in __call__(self, x, im)\n    204 \n    205             try:\n--> 206                 return x._complex_mpfr_field_( self )\n    207             except AttributeError:\n    208                 pass\n\n/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _complex_mpfr_field_(self, field)\n   6007         f = self._operands[0]\n   6008         g = self._operands[1]\n-> 6009         x = f(g._complex_mpfr_field_(field))\n   6010         if isinstance(x, SymbolicExpression):\n   6011             if field.prec() <= 53:\n\n/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in __call__(self, x)\n   7625         if not isinstance(x, (Integer, Rational)):\n   7626             try:\n-> 7627                 return x.exp()\n   7628             except AttributeError:\n   7629                 pass\n\n/Users/ncalexan/complex_number.pyx in sage.rings.complex_number.ComplexNumber.exp()\n\n/Users/ncalexan/gen.pyx in sage.libs.pari.gen._pari_trap()\n\n<class 'sage.libs.pari.gen.PariError'>: precision too low (18)\n```\n\n\nAnd\n\n *\n\n```\nsage: RIF(exp(2*I*pi*75132146442745860257639161594828134642293652547987666191250))\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/Users/ncalexan/<ipython console> in <module>()\n\n/Users/ncalexan/real_mpfi.pyx in sage.rings.real_mpfi.RealIntervalField.__call__()\n\n/Users/ncalexan/real_mpfi.pyx in sage.rings.real_mpfi.RealIntervalFieldElement.__init__()\n\n/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _mpfr_(self, field)\n   5986         f = self._operands[0]\n   5987         g = self._operands[1]\n-> 5988         x = f(g._mpfr_(field))\n   5989         if isinstance(x, SymbolicExpression):\n   5990             if field.prec() <= 53:\n\n/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _mpfr_(self, field)\n   4675             0.00000000000000000000000000000000000000000000000000000000000\n   4676         \"\"\"\n-> 4677         return self._convert(field)\n   4678 \n   4679     def _complex_mpfr_field_(self, field):\n\n/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _convert(self, typ)\n   4629                 raise\n   4630             else:\n-> 4631                 return typ(g)\n   4632         return self._operator(*fops)\n   4633         \n\n/Users/ncalexan/real_mpfi.pyx in sage.rings.real_mpfi.RealIntervalField.__call__()\n\n/Users/ncalexan/real_mpfi.pyx in sage.rings.real_mpfi.RealIntervalFieldElement.__init__()\n\n/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _mpfr_(self, field)\n   4675             0.00000000000000000000000000000000000000000000000000000000000\n   4676         \"\"\"\n-> 4677         return self._convert(field)\n   4678 \n   4679     def _complex_mpfr_field_(self, field):\n\n/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _convert(self, typ)\n   4623         \"\"\"\n   4624         try:\n-> 4625             fops = [typ(op) for op in self._operands]\n   4626         except TypeError:\n   4627             g = self.simplify()\n\n/Users/ncalexan/real_mpfi.pyx in sage.rings.real_mpfi.RealIntervalField.__call__()\n\n/Users/ncalexan/real_mpfi.pyx in sage.rings.real_mpfi.RealIntervalFieldElement.__init__()\n\n/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _mpfr_(self, field)\n   4675             0.00000000000000000000000000000000000000000000000000000000000\n   4676         \"\"\"\n-> 4677         return self._convert(field)\n   4678 \n   4679     def _complex_mpfr_field_(self, field):\n\n/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _convert(self, typ)\n   4623         \"\"\"\n   4624         try:\n-> 4625             fops = [typ(op) for op in self._operands]\n   4626         except TypeError:\n   4627             g = self.simplify()\n\n/Users/ncalexan/real_mpfi.pyx in sage.rings.real_mpfi.RealIntervalField.__call__()\n\n/Users/ncalexan/real_mpfi.pyx in sage.rings.real_mpfi.RealIntervalFieldElement.__init__()\n\n<type 'exceptions.TypeError'>: Unable to convert number to real interval.\n```\n\n\nAnd finally:\n\n *\n\n```\nsage: RR(exp(2*I*pi*75132146442745860257639161594828134642293652547987666191250))\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/Users/ncalexan/<ipython console> in <module>()\n\n/Users/ncalexan/real_mpfr.pyx in sage.rings.real_mpfr.RealField.__call__()\n\n/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _mpfr_(self, field)\n   5986         f = self._operands[0]\n   5987         g = self._operands[1]\n-> 5988         x = f(g._mpfr_(field))\n   5989         if isinstance(x, SymbolicExpression):\n   5990             if field.prec() <= 53:\n\n/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _mpfr_(self, field)\n   4675             0.00000000000000000000000000000000000000000000000000000000000\n   4676         \"\"\"\n-> 4677         return self._convert(field)\n   4678 \n   4679     def _complex_mpfr_field_(self, field):\n\n/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _convert(self, typ)\n   4629                 raise\n   4630             else:\n-> 4631                 return typ(g)\n   4632         return self._operator(*fops)\n   4633         \n\n/Users/ncalexan/real_mpfr.pyx in sage.rings.real_mpfr.RealField.__call__()\n\n/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _mpfr_(self, field)\n   4675             0.00000000000000000000000000000000000000000000000000000000000\n   4676         \"\"\"\n-> 4677         return self._convert(field)\n   4678 \n   4679     def _complex_mpfr_field_(self, field):\n\n/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _convert(self, typ)\n   4623         \"\"\"\n   4624         try:\n-> 4625             fops = [typ(op) for op in self._operands]\n   4626         except TypeError:\n   4627             g = self.simplify()\n\n/Users/ncalexan/real_mpfr.pyx in sage.rings.real_mpfr.RealField.__call__()\n\n/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _mpfr_(self, field)\n   4675             0.00000000000000000000000000000000000000000000000000000000000\n   4676         \"\"\"\n-> 4677         return self._convert(field)\n   4678 \n   4679     def _complex_mpfr_field_(self, field):\n\n/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _convert(self, typ)\n   4623         \"\"\"\n   4624         try:\n-> 4625             fops = [typ(op) for op in self._operands]\n   4626         except TypeError:\n   4627             g = self.simplify()\n\n/Users/ncalexan/real_mpfr.pyx in sage.rings.real_mpfr.RealField.__call__()\n\n/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/functions/constants.py in _mpfr_(self, R)\n    854             TypeError\n    855         \"\"\"\n--> 856         raise TypeError\n    857 \n    858     def _real_rqdf_(self, R):\n\n<type 'exceptions.TypeError'>: \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3100\n\n",
    "created_at": "2008-05-03T23:02:13Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "coercion errors from SymbolicRing to various fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3100",
    "user": "ncalexan"
}
```
Assignee: malb

CC:  ncalexan

Keywords: CC RR CIF RIF symbolic

This might need to be split up, but here goes:

This is just wrong:

```
sage: exp(2*I*pi*75132146442745860257639161594828134642293652547987666191250)
1
sage: CIF(exp(2*I*pi*75132146442745860257639161594828134642293652547987666191250))
[-1.0000000000000000000000000000000000000000000000 .. 1.0000000000000000000000000000000000000000000000] + [-1.0000000000000000000000000000000000000000000000 .. 1.0000000000000000000000000000000000000000000000]*I
```


That prompted me to try:
 *

```
sage: CC(exp(2*I*pi*75132146442745860257639161594828134642293652547987666191250))
---------------------------------------------------------------------------
<class 'sage.libs.pari.gen.PariError'>    Traceback (most recent call last)

/Users/ncalexan/<ipython console> in <module>()

/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/rings/complex_field.py in __call__(self, x, im)
    204 
    205             try:
--> 206                 return x._complex_mpfr_field_( self )
    207             except AttributeError:
    208                 pass

/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _complex_mpfr_field_(self, field)
   6007         f = self._operands[0]
   6008         g = self._operands[1]
-> 6009         x = f(g._complex_mpfr_field_(field))
   6010         if isinstance(x, SymbolicExpression):
   6011             if field.prec() <= 53:

/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in __call__(self, x)
   7625         if not isinstance(x, (Integer, Rational)):
   7626             try:
-> 7627                 return x.exp()
   7628             except AttributeError:
   7629                 pass

/Users/ncalexan/complex_number.pyx in sage.rings.complex_number.ComplexNumber.exp()

/Users/ncalexan/gen.pyx in sage.libs.pari.gen._pari_trap()

<class 'sage.libs.pari.gen.PariError'>: precision too low (18)
```


And

 *

```
sage: RIF(exp(2*I*pi*75132146442745860257639161594828134642293652547987666191250))
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/ncalexan/<ipython console> in <module>()

/Users/ncalexan/real_mpfi.pyx in sage.rings.real_mpfi.RealIntervalField.__call__()

/Users/ncalexan/real_mpfi.pyx in sage.rings.real_mpfi.RealIntervalFieldElement.__init__()

/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _mpfr_(self, field)
   5986         f = self._operands[0]
   5987         g = self._operands[1]
-> 5988         x = f(g._mpfr_(field))
   5989         if isinstance(x, SymbolicExpression):
   5990             if field.prec() <= 53:

/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _mpfr_(self, field)
   4675             0.00000000000000000000000000000000000000000000000000000000000
   4676         """
-> 4677         return self._convert(field)
   4678 
   4679     def _complex_mpfr_field_(self, field):

/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _convert(self, typ)
   4629                 raise
   4630             else:
-> 4631                 return typ(g)
   4632         return self._operator(*fops)
   4633         

/Users/ncalexan/real_mpfi.pyx in sage.rings.real_mpfi.RealIntervalField.__call__()

/Users/ncalexan/real_mpfi.pyx in sage.rings.real_mpfi.RealIntervalFieldElement.__init__()

/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _mpfr_(self, field)
   4675             0.00000000000000000000000000000000000000000000000000000000000
   4676         """
-> 4677         return self._convert(field)
   4678 
   4679     def _complex_mpfr_field_(self, field):

/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _convert(self, typ)
   4623         """
   4624         try:
-> 4625             fops = [typ(op) for op in self._operands]
   4626         except TypeError:
   4627             g = self.simplify()

/Users/ncalexan/real_mpfi.pyx in sage.rings.real_mpfi.RealIntervalField.__call__()

/Users/ncalexan/real_mpfi.pyx in sage.rings.real_mpfi.RealIntervalFieldElement.__init__()

/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _mpfr_(self, field)
   4675             0.00000000000000000000000000000000000000000000000000000000000
   4676         """
-> 4677         return self._convert(field)
   4678 
   4679     def _complex_mpfr_field_(self, field):

/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _convert(self, typ)
   4623         """
   4624         try:
-> 4625             fops = [typ(op) for op in self._operands]
   4626         except TypeError:
   4627             g = self.simplify()

/Users/ncalexan/real_mpfi.pyx in sage.rings.real_mpfi.RealIntervalField.__call__()

/Users/ncalexan/real_mpfi.pyx in sage.rings.real_mpfi.RealIntervalFieldElement.__init__()

<type 'exceptions.TypeError'>: Unable to convert number to real interval.
```


And finally:

 *

```
sage: RR(exp(2*I*pi*75132146442745860257639161594828134642293652547987666191250))
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/ncalexan/<ipython console> in <module>()

/Users/ncalexan/real_mpfr.pyx in sage.rings.real_mpfr.RealField.__call__()

/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _mpfr_(self, field)
   5986         f = self._operands[0]
   5987         g = self._operands[1]
-> 5988         x = f(g._mpfr_(field))
   5989         if isinstance(x, SymbolicExpression):
   5990             if field.prec() <= 53:

/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _mpfr_(self, field)
   4675             0.00000000000000000000000000000000000000000000000000000000000
   4676         """
-> 4677         return self._convert(field)
   4678 
   4679     def _complex_mpfr_field_(self, field):

/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _convert(self, typ)
   4629                 raise
   4630             else:
-> 4631                 return typ(g)
   4632         return self._operator(*fops)
   4633         

/Users/ncalexan/real_mpfr.pyx in sage.rings.real_mpfr.RealField.__call__()

/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _mpfr_(self, field)
   4675             0.00000000000000000000000000000000000000000000000000000000000
   4676         """
-> 4677         return self._convert(field)
   4678 
   4679     def _complex_mpfr_field_(self, field):

/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _convert(self, typ)
   4623         """
   4624         try:
-> 4625             fops = [typ(op) for op in self._operands]
   4626         except TypeError:
   4627             g = self.simplify()

/Users/ncalexan/real_mpfr.pyx in sage.rings.real_mpfr.RealField.__call__()

/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _mpfr_(self, field)
   4675             0.00000000000000000000000000000000000000000000000000000000000
   4676         """
-> 4677         return self._convert(field)
   4678 
   4679     def _complex_mpfr_field_(self, field):

/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/calculus/calculus.py in _convert(self, typ)
   4623         """
   4624         try:
-> 4625             fops = [typ(op) for op in self._operands]
   4626         except TypeError:
   4627             g = self.simplify()

/Users/ncalexan/real_mpfr.pyx in sage.rings.real_mpfr.RealField.__call__()

/Users/ncalexan/sage-2.11/local/lib/python/site-packages/sage/functions/constants.py in _mpfr_(self, R)
    854             TypeError
    855         """
--> 856         raise TypeError
    857 
    858     def _real_rqdf_(self, R):

<type 'exceptions.TypeError'>: 
```


Issue created by migration from https://trac.sagemath.org/ticket/3100





---

archive/issue_comments_021412.json:
```json
{
    "body": "This is fixed by #5144:\n\n\n```\nsage: a = exp(2*I*pi*75132146442745860257639161594828134642293652547987666191250)\nsage: RR(a)\n1.00000000000000\nsage: CC(a)\n1.00000000000000\nsage: RIF(a)\n1\nsage: CIF(a)\n1\n```\n",
    "created_at": "2009-06-05T01:54:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3100#issuecomment-21412",
    "user": "mhansen"
}
```

This is fixed by #5144:


```
sage: a = exp(2*I*pi*75132146442745860257639161594828134642293652547987666191250)
sage: RR(a)
1.00000000000000
sage: CC(a)
1.00000000000000
sage: RIF(a)
1
sage: CIF(a)
1
```




---

archive/issue_comments_021413.json:
```json
{
    "body": "Err, make that #6144 and #6194.",
    "created_at": "2009-06-05T02:04:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3100#issuecomment-21413",
    "user": "mhansen"
}
```

Err, make that #6144 and #6194.



---

archive/issue_comments_021414.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-05T02:04:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3100#issuecomment-21414",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_021415.json:
```json
{
    "body": "bad authors removed",
    "created_at": "2016-08-01T19:59:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3100#issuecomment-21415",
    "user": "chapoton"
}
```

bad authors removed
