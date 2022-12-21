# Issue 2124: [with patch, needs review] minor bug in f.root_field()

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-02-09 05:15:22

Assignee: craigcitro

f.root_field() currently does is_IntegralDomain(f.parent()) instead of f.parent().is_integral_domain(), which is bad. The attached patch fixes it.

Before:

```
sage: R.<x> = PolynomialRing(Integers(31))

sage: h = x+5

sage: h.root_field('a')
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/Users/craigcitro/<ipython console> in <module>()

/Users/craigcitro/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial.root_field()

<type 'exceptions.ValueError'>: the base ring must be a domain

sage: h.base_ring()
 Ring of integers modulo 31
```


After:

```
sage: R.<x> = PolynomialRing(Integers(31))

sage: h = x+5

sage: h.root_field('a')
 Ring of integers modulo 31
```





---

Attachment


---

Comment by AlexGhitza created at 2008-02-09 05:26:07

looks good


---

Comment by mabshoff created at 2008-02-10 00:58:23

Resolution: fixed


---

Comment by mabshoff created at 2008-02-10 00:58:23

Merged in Sage 2.10.2.alpha0
