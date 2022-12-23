# Issue 4869: make element of relative number field from polynomial

Issue created by migration from https://trac.sagemath.org/ticket/4869

Original creator: AlexGhitza

Original creation time: 2008-12-24 12:41:46

Assignee: was

CC:  cremona

Keywords: relative number field polynomial

John Cremona remarked at #4837:

for an absolute extension we can create an element from a polynomial over the base field, but not for a relative extension:


```
sage: K.<z>=CyclotomicField(7)
sage: Ky.<y>=PolynomialRing(K)
sage: L.<a>=K.extension(y^2+1)
sage: K(K.polynomial_ring().random_element())
z + 1
sage: L(L.polynomial_ring().random_element())
---------------------------------------------------------------------------
TypeError           
...
TypeError: Unable to coerce 7/2*z^5 + 1/2*z^4 + z^3 - 37/2*z to a rational
```




---

Comment by ncalexan created at 2009-01-24 09:34:37

This is fixed by the patches for #1367.  This should be closed as a dupe after #1367 is merged.


---

Comment by mabshoff created at 2009-01-29 05:45:02

Fixed via #1367 in Sage 3.3.alpha3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-29 05:45:02

Resolution: fixed
