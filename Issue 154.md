# Issue 154: gfan -- something wrong

archive/issues_000154.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: R.<x,y> = PolynomialRing(QQ,2)\nsage: i = ideal([x + y - 1])\nsage: g = i.groebner_fan()\nsage: g.tropical_basis()\nTraceback (most recent call last):\n...\nKeyError: 'Dimension of homogeneity space'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/154\n\n",
    "created_at": "2006-10-26T20:37:48Z",
    "labels": [
        "algebraic geometry",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-1.8",
    "title": "gfan -- something wrong",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/154",
    "user": "@williamstein"
}
```
Assignee: @williamstein


```
sage: R.<x,y> = PolynomialRing(QQ,2)
sage: i = ideal([x + y - 1])
sage: g = i.groebner_fan()
sage: g.tropical_basis()
Traceback (most recent call last):
...
KeyError: 'Dimension of homogeneity space'
```


Issue created by migration from https://trac.sagemath.org/ticket/154





---

archive/issue_comments_000700.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-19T11:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/154#issuecomment-700",
    "user": "@williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_000701.json:
```json
{
    "body": "This is now fixed.",
    "created_at": "2007-01-19T11:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/154#issuecomment-701",
    "user": "@williamstein"
}
```

This is now fixed.
