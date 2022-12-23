# Issue 7839: Failure to coerce q^(-1) into its own LaurentPolynomialRing

archive/issues_007839.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  sage-combinat\n\nConsider:\n\n\n```\nsage: P.<q> = LaurentPolynomialRing(QQ)\nsage: q in P\nTrue\nsage: P(q)\nq\nsage: q^(-1) in P\nTrue\nsage: P(q^(-1))\n```\n\n\nThe last statement raises an exception.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7839\n\n",
    "created_at": "2010-01-04T04:47:29Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "Failure to coerce q^(-1) into its own LaurentPolynomialRing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7839",
    "user": "bump"
}
```
Assignee: AlexGhitza

CC:  sage-combinat

Consider:


```
sage: P.<q> = LaurentPolynomialRing(QQ)
sage: q in P
True
sage: P(q)
q
sage: q^(-1) in P
True
sage: P(q^(-1))
```


The last statement raises an exception.

Issue created by migration from https://trac.sagemath.org/ticket/7839





---

archive/issue_comments_067907.json:
```json
{
    "body": "This is a duplicate of #3617 which should be fixed soon.",
    "created_at": "2010-01-19T21:55:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7839#issuecomment-67907",
    "user": "mhansen"
}
```

This is a duplicate of #3617 which should be fixed soon.



---

archive/issue_comments_067908.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-01-19T21:55:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7839#issuecomment-67908",
    "user": "mhansen"
}
```

Resolution: duplicate
