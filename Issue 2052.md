# Issue 2052: PolyBoRi wrapper incomplete

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-02-05 11:56:20

Assignee: burcin

Keywords: polybori

Try these:

```
sage: P.<x0, x1, x2, x3> = BooleanPolynomialRing(4)
sage: I = P.ideal(x0*x1*x2*x3 + x0*x1*x3 + x0*x1 + x0*x2 + x0)
sage: I
Ideal (x0*x1*x2*x3 + x0*x1*x3 + x0*x1 + x0*x2 + x0) of Boolean PolynomialRing in x0, x1, x2, x3

sage: I.groebner_basis(draw_matrices=True)
*BOOM*
sage: I.groebner_basis(invert=True)
*BOOM*
sage: I.groebner_basis(noro=True)
*BOOM*
sage: I.groebner_basis(preprocess_only=True)
*BOOM*
```



---

Comment by malb created at 2008-02-05 17:35:45

I think this can be closed again, see #2051.


---

Comment by malb created at 2008-02-05 17:35:45

Resolution: fixed
