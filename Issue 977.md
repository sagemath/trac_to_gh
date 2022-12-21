# Issue 977: Schubert polynomials send 1 -> wrong polynomial ring

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2007-10-23 21:06:30

Assignee: mhansen

CC:  sage-combinat

It seems that this is only happening with the identity element. Here's an example:


```
sage: R = SchubertPolynomialRing(ZZ)
sage: f = R([1])
sage: type(f.expand())
<type 'sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl'>
sage: f = R([1,2])
sage: type(f.expand())
<type 'sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl'>

# But all of the polynomials returned should be multi-polynomials

sage: f = R([1,3,2,4])
sage: type(f.expand())
<class 'sage.rings.polynomial.multi_polynomial_element.MPolynomial_polydict'>
```



---

Comment by mhansen created at 2007-10-23 23:50:56

Changing status from new to assigned.


---

Comment by malb created at 2007-10-24 21:48:49

Resolution: fixed


---

Attachment

this is applied to 2.8.9.alpha1
