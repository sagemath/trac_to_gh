# Issue 109: inconsistent return type for generic powering or something

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2006-10-04 21:25:16

Assignee: somebody


```
sage: R.<x> = PolynomialRing(pAdicField(5))
sage: type(x)
 <class 'sage.rings.polynomial_element.Polynomial_generic_dense_field'>
sage: type(x**int(0))
 <class 'sage.rings.polynomial_element.Polynomial_generic_dense_field'>
sage: type((x**3)**int(0))
 <type 'int'>
```




---

Comment by dmharvey created at 2006-10-04 21:27:24

Sorry that was a misleading example. It has nothing to do with `int(0)`, the same thing happens for SAGE Integer(0).


---

Comment by was created at 2006-10-05 07:56:50

Resolution: fixed


---

Comment by was created at 2006-10-05 07:56:50

Fixed for sage-1.4.
