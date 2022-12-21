# Issue 951: evaluating polynomial over Z/nZ produces incorrect type

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2007-10-20 21:21:02

Assignee: somebody

When evaluating a polynomial over Z/nZ at a point, I get a polynomial instead of a constant:


```
sage: R.<x> = PolynomialRing(Integers(10))
sage: f = x^2 + x + 1
sage: f(3)
3
sage: type(f(3))
<type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_modn_ntl_zz'>
```


It should behave more like this:

```
sage: S.<y> = PolynomialRing(ZZ)     
sage: g = y^2 + y + 1
sage: type(g(3))
<type 'sage.rings.integer.Integer'>
```




---

Attachment


---

Comment by was created at 2007-10-21 01:33:40

Resolution: fixed
