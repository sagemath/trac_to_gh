# Issue 3100: coercion errors from SymbolicRing to various fields

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2008-05-03 23:02:13

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



---

Comment by mhansen created at 2009-06-05 01:54:33

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

Comment by mhansen created at 2009-06-05 02:04:10

Err, make that #6144 and #6194.


---

Comment by mhansen created at 2009-06-05 02:04:10

Resolution: fixed


---

Comment by chapoton created at 2016-08-01 19:59:21

bad authors removed
