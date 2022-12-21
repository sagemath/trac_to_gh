# Issue 1097: p-adic polynomials don't have discriminant

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2007-11-04 02:00:08

Assignee: somebody


```
sage: R.<x> = PolynomialRing(ZZ)
sage: x.discriminant()
1

sage: R.<x> = PolynomialRing(Zp(5))
sage: x.discriminant()
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/Users/david/temp/<ipython console> in <module>()

<type 'exceptions.AttributeError'>: 'Polynomial_padic_capped_relative_dense' object has no attribute 'discriminant'
```




---

Comment by mabshoff created at 2007-12-26 02:59:25

This is still a problem with 2.9.1.1. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-06 21:50:21

Alex Ghitza and Mike Hansen have confirmed that this is now fixed:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0.alpha1, Release Date: 2008-04-04                  |
| Type notebook() for the GUI, and license() for information.        |
sage: sage: R.<x> = PolynomialRing(Zp(5))
sage: sage: x.discriminant()
1 + O(5^20)
sage:
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-04-06 21:50:21

Resolution: fixed
