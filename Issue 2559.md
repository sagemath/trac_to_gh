# Issue 2559: issue with roots() over Algebraic Real field

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2008-03-16 22:08:38

Assignee: malb

CC:  ncalexan

Keywords: algebraic real roots

I can't say much about this one:


```
sage: M

[[-1.2859513130484710 .. -1.2859513130484707] [0.48604391035188904 .. 0.48604391035188910]]
[  [2.8742392060133346 .. 2.8742392060133351] [0.18370733043549580 .. 0.18370733043549584]]
sage: M.parent()
Full MatrixSpace of 2 by 2 dense matrices over Algebraic Real Field
sage: M.charpoly()
x^2 + [1.1022439826129748 .. 1.1022439826129751]*x + [-1.6332451457675854 .. -1.6332451457675851]
sage: M.charpoly().parent()
Univariate Polynomial Ring in x over Algebraic Real Field
sage: M.charpoly().roots()
Exception exceptions.AttributeError: "'sage.rings.complex_interval.ComplexIntervalFieldEl' object has no attribute 'lower'" in 'sage.rings.polynomial.polynomial_element.Polynomial_generic_dense.__normalize' ignored
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/Users/ncalexan/Documents/School/MATH235/genus2cm/<ipython console> in <module>()

/Users/ncalexan/Documents/School/MATH235/genus2cm/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial.roots()

/Users/ncalexan/Documents/School/MATH235/genus2cm/real_roots.pyx in sage.rings.polynomial.real_roots.real_roots()

/Users/ncalexan/Documents/School/MATH235/genus2cm/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial.squarefree_decomposition()

/Users/ncalexan/Documents/School/MATH235/genus2cm/element.pyx in sage.structure.element.PrincipalIdealDomainElement.gcd()

/Users/ncalexan/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_element_generic.py in _gcd(self, other)
    542         Return the GCD of self and other, as a monic polynomial.
    543         """
--> 544         g = EuclideanDomainElement._gcd(self, other)
    545         c = g.leading_coefficient()
    546         if c.is_unit():

/Users/ncalexan/Documents/School/MATH235/genus2cm/element.pyx in sage.structure.element.EuclideanDomainElement._gcd()

/Users/ncalexan/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_element_generic.py in quo_rem(self, other)
    533             aaa = (R.leading_coefficient()/B.leading_coefficient())
    534             bbb = X**(R.degree()-B.degree())
--> 535             S = aaa * bbb
    536             Q += S
    537             R -= S*B            

/Users/ncalexan/Documents/School/MATH235/genus2cm/element.pyx in sage.structure.element.RingElement.__mul__()

/Users/ncalexan/Documents/School/MATH235/genus2cm/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c()

/Users/ncalexan/Documents/School/MATH235/genus2cm/action.pyx in sage.categories.action.Action._call_c()

/Users/ncalexan/Documents/School/MATH235/genus2cm/coerce.pyx in sage.structure.coerce.LeftModuleAction._call_c_impl()

/Users/ncalexan/Documents/School/MATH235/genus2cm/coerce.pxi in sage.structure.coerce._rmul_c()

/Users/ncalexan/Documents/School/MATH235/genus2cm/element.pyx in sage.structure.element.ModuleElement._rmul_()

/Users/ncalexan/Documents/School/MATH235/genus2cm/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial_generic_dense._rmul_c_impl()

/Users/ncalexan/Documents/School/MATH235/genus2cm/element.pyx in sage.structure.element.Element.__nonzero__()

/Users/ncalexan/Documents/School/MATH235/genus2cm/element.pyx in sage.structure.element.Element.__richcmp__()

/Users/ncalexan/Documents/School/MATH235/genus2cm/element.pyx in sage.structure.element.Element._richcmp()

/Users/ncalexan/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/rings/qqbar.py in __cmp__(self, other)
   2752         if self is other: return 0
   2753         if other._descr.is_rational() and other._descr.rational_value() == 0:
-> 2754             return self.sign()
   2755         elif self._descr.is_rational() and self._descr.rational_value() == 0:
   2756             return -other.sign()

/Users/ncalexan/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/rings/qqbar.py in sign(self)
   2855             0
   2856         """
-> 2857         if self._value.lower() > 0:
   2858             return 1
   2859         elif self._value.upper() < 0:

<type 'exceptions.AttributeError'>: 'sage.rings.complex_interval.ComplexIntervalFieldEl' object has no attribute 'lower'
```



---

Comment by malb created at 2008-06-03 14:20:45

Remove assignee malb.


---

Comment by cwitty created at 2009-01-23 20:41:03

Nick doesn't remember how to reproduce this, so he said to invalidate it.


---

Comment by cwitty created at 2009-01-23 20:43:56

Resolution: invalid


---

Comment by bascorp2 created at 2010-05-26 08:40:32

[picture of jesus](http://like-search.info/)
