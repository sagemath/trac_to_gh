# Issue 5269: coordinate ring of an affine patch on a hyperelliptic curve is broken

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2009-02-14 11:52:33

Assignee: was

When taking an affine patch of a hyperelliptic curve, the defining polynomial (sometimes?) has the wrong parent:


```
sage: P.<x> = QQ[]
sage: f = 4*x^5 - 30*x^3 + 45*x - 22
sage: C = HyperellipticCurve(f)
sage: D = C.affine_patch(0); D
Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
  x0^2*x1^3 + 22*x1^5 - 45*x1^4 + 30*x1^2 - 4
sage: f = D.defining_polynomials()[0]; f
x0^2*x1^3 + 22*x1^5 - 45*x1^4 + 30*x1^2 - 4
sage: f.parent()
Multivariate Polynomial Ring in x0, x1, x2 over Rational Field
```


Everything is fine except the last line: the parent of f should be a multivariate polynomial ring in two variables, not three.

This might be a more generic problem and not necessarily related to hyperelliptic curves.



---

Comment by AlexGhitza created at 2009-02-14 11:53:33

Changing assignee from was to AlexGhitza.


---

Comment by AlexGhitza created at 2009-02-14 11:53:40

Changing status from new to assigned.


---

Comment by AlexGhitza created at 2009-02-14 13:24:17

The attached patch fixes the issue by making sure that the defining polynomials for a subscheme are elements of the coordinate ring of the ambient space.


---

Attachment

Patch looks good and doctests pass.


---

Comment by mabshoff created at 2009-02-15 07:56:16

Resolution: fixed


---

Comment by mabshoff created at 2009-02-15 07:56:16

Merged in Sage 3.3.rc1.

Cheers,

Michael
