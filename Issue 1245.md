# Issue 1245: Error coercing multivariate polynomial rings with one variable into composite integer rings

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2007-11-22 23:57:05

Assignee: was

CC:  robertwb

Keywords: coercion coerce multivariate univariate composite

This works:


```
sage: PolynomialRing(ZZ, 2, 'x').gen() * Mod(1, 9)
x0
sage: PolynomialRing(ZZ, 2, 'x').gen() * Mod(1, 3)
x0
```


This doesn't:


```
sage: PolynomialRing(ZZ, 1, 'x').gen() * Mod(1, 3)
x
sage: PolynomialRing(ZZ, 1, 'x').gen() * Mod(1, 9)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/ncalexan/<ipython console> in <module>()

/Users/ncalexan/element.pyx in sage.structure.element.RingElement.__mul__()

/Users/ncalexan/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c()

<type 'exceptions.TypeError'>: unsupported operand parent(s) for '*': 'Multivariate Polynomial Ring in x over Integer Ring' and 'Ring of integers modulo 9'
```



---

Comment by mabshoff created at 2007-12-20 03:03:04

Changing assignee from was to malb.


---

Comment by mabshoff created at 2008-01-20 03:03:34

This is still a problem with Sage 2.10.

Cheers,

Michael


---

Comment by AlexGhitza created at 2008-01-24 09:00:22

Changing component from algebraic geometry to commutative algebra.


---

Comment by mabshoff created at 2008-02-15 23:02:49

Changing priority from major to critical.


---

Comment by mabshoff created at 2008-02-15 23:02:49

Still an issue with Sage 2.10.2.alpha0.

Cheers,

Michael


---

Comment by malb created at 2008-08-18 11:13:49

I'm stuck with this bug, I don't know where to look. Robert, can you take a look?


---

Comment by mhansen created at 2008-11-14 09:41:04

This has been fixed in at least Sage 3.1.4


```
sage: sage: PolynomialRing(ZZ, 1, 'x').gen() * Mod(1, 3)
x
sage: sage: PolynomialRing(ZZ, 1, 'x').gen() * Mod(1, 9)
x
sage: _.parent()
Univariate Polynomial Ring in x over Ring of integers modulo 9
```



---

Comment by mhansen created at 2008-11-14 09:41:04

Resolution: fixed
