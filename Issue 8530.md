# Issue 8530: affine patches of projective curves should be affine curves

archive/issues_008530.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  minz\n\nLet C be a projective curve.  At the moment, the method `affine_patch` is just the generic one for projective schemes.  In particular, this returns a subscheme of the affine plane:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: R.<x, y, z> = QQ[]\nsage: C = Curve(x^3 + y^3 - z^3)\nsage: C\nProjective Curve over Rational Field defined by x^3 + y^3 - z^3\nsage: C.affine_patch(2)\nClosed subscheme of Affine Space of dimension 2 over Rational Field defined by:\n  x0^3 + x1^3 - 1\n```\n\n| Sage Version 4.3.3, Release Date: 2010-02-21                       |\n| Type notebook() for the GUI, and license() for information.        |\nOf course, this is actually an affine curve, and it would make more sense for `C.affine_patch()` to return an affine curve, in our example:\n\n\n```\nsage: Curve(C.affine_patch(2).defining_polynomials()[0])\nAffine Curve over Rational Field defined by x0^3 + x1^3 - 1\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8530\n\n",
    "created_at": "2010-03-13T22:41:35Z",
    "labels": [
        "algebraic geometry",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "affine patches of projective curves should be affine curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8530",
    "user": "AlexGhitza"
}
```
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



Issue created by migration from https://trac.sagemath.org/ticket/8530


