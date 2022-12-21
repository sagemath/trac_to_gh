# Issue 8530: affine patches of projective curves should be affine curves

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2010-03-13 22:41:35

Assignee: AlexGhitza

CC:  minz

Let C be a projective curve.  At the moment, the method `affine_patch` is just the generic one for projective schemes.  In particular, this returns a subscheme of the affine plane:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: R.<x, y, z> = QQ[]
sage: C = Curve(x^3 + y^3 - z^3)
sage: C
Projective Curve over Rational Field defined by x^3 + y^3 - z^3
sage: C.affine_patch(2)
Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
  x0^3 + x1^3 - 1
```

| Sage Version 4.3.3, Release Date: 2010-02-21                       |
| Type notebook() for the GUI, and license() for information.        |
Of course, this is actually an affine curve, and it would make more sense for `C.affine_patch()` to return an affine curve, in our example:


```
sage: Curve(C.affine_patch(2).defining_polynomials()[0])
Affine Curve over Rational Field defined by x0^3 + x1^3 - 1
```


