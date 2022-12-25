# Issue 250: strange display of nested rings

archive/issues_000250.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n``` \nsage: R, u = PolynomialRing(GF(p), 'u').objgen()\n \nsage: S, v = PolynomialRing(R, 'v').objgen()\n \nsage: T = S.fraction_field()\n \nsage: F = EllipticCurve(T, [a, b])\n \nsage: F\n Elliptic Curve defined by y^2 + (0)*x*y + (0)*y = x^3 + (0)*x^2 + x\n+1 over Fraction Field of Univariate Polynomial Ring in v over\nUnivariate Polynomial Ring in u over Finite Field of size 29\n \nI'm sure there's a better example of this strange printing, but this\nis how I found it.\n \nNick\n \n }}}\n\nIssue created by migration from https://trac.sagemath.org/ticket/250\n\n",
    "created_at": "2007-02-08T03:39:35Z",
    "labels": [
        "component: user interface",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "strange display of nested rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/250",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


``` 
sage: R, u = PolynomialRing(GF(p), 'u').objgen()
 
sage: S, v = PolynomialRing(R, 'v').objgen()
 
sage: T = S.fraction_field()
 
sage: F = EllipticCurve(T, [a, b])
 
sage: F
 Elliptic Curve defined by y^2 + (0)*x*y + (0)*y = x^3 + (0)*x^2 + x
+1 over Fraction Field of Univariate Polynomial Ring in v over
Univariate Polynomial Ring in u over Finite Field of size 29
 
I'm sure there's a better example of this strange printing, but this
is how I found it.
 
Nick
 
 }}}

Issue created by migration from https://trac.sagemath.org/ticket/250





---

archive/issue_comments_001098.json:
```json
{
    "body": "Attachment [7053.patch](tarball://root/attachments/some-uuid/ticket250/7053.patch) by @williamstein created at 2007-10-21 02:54:20",
    "created_at": "2007-10-21T02:54:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/250#issuecomment-1098",
    "user": "https://github.com/williamstein"
}
```

Attachment [7053.patch](tarball://root/attachments/some-uuid/ticket250/7053.patch) by @williamstein created at 2007-10-21 02:54:20



---

archive/issue_comments_001099.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-21T02:54:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/250#issuecomment-1099",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
