# Issue 2052: PolyBoRi wrapper incomplete

archive/issues_002052.json:
```json
{
    "body": "Assignee: burcin\n\nKeywords: polybori\n\nTry these:\n\n```\nsage: P.<x0, x1, x2, x3> = BooleanPolynomialRing(4)\nsage: I = P.ideal(x0*x1*x2*x3 + x0*x1*x3 + x0*x1 + x0*x2 + x0)\nsage: I\nIdeal (x0*x1*x2*x3 + x0*x1*x3 + x0*x1 + x0*x2 + x0) of Boolean PolynomialRing in x0, x1, x2, x3\n\nsage: I.groebner_basis(draw_matrices=True)\n*BOOM*\nsage: I.groebner_basis(invert=True)\n*BOOM*\nsage: I.groebner_basis(noro=True)\n*BOOM*\nsage: I.groebner_basis(preprocess_only=True)\n*BOOM*\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2052\n\n",
    "created_at": "2008-02-05T11:56:20Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "PolyBoRi wrapper incomplete",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2052",
    "user": "malb"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/2052





---

archive/issue_comments_013287.json:
```json
{
    "body": "I think this can be closed again, see #2051.",
    "created_at": "2008-02-05T17:35:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2052#issuecomment-13287",
    "user": "malb"
}
```

I think this can be closed again, see #2051.



---

archive/issue_comments_013288.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-05T17:35:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2052#issuecomment-13288",
    "user": "malb"
}
```

Resolution: fixed
