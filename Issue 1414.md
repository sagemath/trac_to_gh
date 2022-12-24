# Issue 1414: wrap MPolynomialRing so inject_on() works.

archive/issues_001414.json:
```json
{
    "body": "Assignee: @malb\n\nThis should work but doesn't\n\n```\nsage: p = 17; q = (p-1)//2\nsage: inject_on()\nRedefining: Frac FreeMonoid GF FractionField FiniteField PolynomialRing quotient NumberField LaurentSeriesRing quo \nsage: R = MPolynomialRing(GF(p),q,\"x\")\nDefining x\nDefining x0, x1, x2, x3, x4, x5, x6, x7\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1414\n\n",
    "created_at": "2007-12-07T02:15:00Z",
    "labels": [
        "commutative algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "wrap MPolynomialRing so inject_on() works.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1414",
    "user": "@williamstein"
}
```
Assignee: @malb

This should work but doesn't

```
sage: p = 17; q = (p-1)//2
sage: inject_on()
Redefining: Frac FreeMonoid GF FractionField FiniteField PolynomialRing quotient NumberField LaurentSeriesRing quo 
sage: R = MPolynomialRing(GF(p),q,"x")
Defining x
Defining x0, x1, x2, x3, x4, x5, x6, x7
```



Issue created by migration from https://trac.sagemath.org/ticket/1414





---

archive/issue_comments_009123.json:
```json
{
    "body": "MPolynomialRing is going to be deprecated, see #2353.",
    "created_at": "2008-05-22T16:38:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1414#issuecomment-9123",
    "user": "@burcin"
}
```

MPolynomialRing is going to be deprecated, see #2353.



---

archive/issue_comments_009124.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-08-23T23:04:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1414#issuecomment-9124",
    "user": "@malb"
}
```

Resolution: wontfix



---

archive/issue_comments_009125.json:
```json
{
    "body": "Since it is deprecated now, I'm closing the ticket as `wontfix`. Mabshoff, do we need to change the milestone?",
    "created_at": "2008-08-23T23:04:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1414#issuecomment-9125",
    "user": "@malb"
}
```

Since it is deprecated now, I'm closing the ticket as `wontfix`. Mabshoff, do we need to change the milestone?
