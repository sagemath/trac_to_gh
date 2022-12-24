# Issue 350: bug in rational_points on hyperelliptic curve

archive/issues_000350.json:
```json
{
    "body": "Assignee: @williamstein\n\n\nHi.\nI am quite happy that rational_points() of a hyperelliptic curve over\na finite field lists the poitn at infinity twice, but I don't\nunderstand why it also lists other points twice.\n\nChris.\n\n\n\n```\nf = x^8+x+1\nft = f.change_ring(GF(7))\nC = HyperellipticCurve(ft)\nC.rational_points()\n///\n[(2 : 0 : 1), (4 : 0 : 1), (2 : 0 : 1), (4 : 0 : 1), (0 : 1 : 1), (6 :\n1 : 1), (0 : 6 : 1), (6 : 6 : 1), (0 : 1 : 0), (0 : 1 : 0)]\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/350\n\n",
    "created_at": "2007-04-11T01:53:05Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.2",
    "title": "bug in rational_points on hyperelliptic curve",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/350",
    "user": "@williamstein"
}
```
Assignee: @williamstein


Hi.
I am quite happy that rational_points() of a hyperelliptic curve over
a finite field lists the poitn at infinity twice, but I don't
understand why it also lists other points twice.

Chris.



```
f = x^8+x+1
ft = f.change_ring(GF(7))
C = HyperellipticCurve(ft)
C.rational_points()
///
[(2 : 0 : 1), (4 : 0 : 1), (2 : 0 : 1), (4 : 0 : 1), (0 : 1 : 1), (6 :
1 : 1), (0 : 6 : 1), (6 : 6 : 1), (0 : 1 : 0), (0 : 1 : 0)]
```



Issue created by migration from https://trac.sagemath.org/ticket/350





---

archive/issue_comments_001697.json:
```json
{
    "body": "The expression `x^8+x+1` is now a symbolic expression, not a polynomial, so the `change_ring` method is no longer valid.\n\nIn any case, the bug appears to be fixed now, so I'm closing this ticket.",
    "created_at": "2007-08-18T17:29:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/350#issuecomment-1697",
    "user": "dmharvey"
}
```

The expression `x^8+x+1` is now a symbolic expression, not a polynomial, so the `change_ring` method is no longer valid.

In any case, the bug appears to be fixed now, so I'm closing this ticket.



---

archive/issue_comments_001698.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-18T17:29:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/350#issuecomment-1698",
    "user": "dmharvey"
}
```

Resolution: fixed
