# Issue 5113: [with patch, needs review] elliptic curve construction from weierstrass equation

archive/issues_005113.json:
```json
{
    "body": "Assignee: was\n\nCC:  rlm\n\nIt would be nice to be able to do \n\n```\n        sage: x, y = var('x,y')\n        sage: EllipticCurve(y^2 + y ==  x^3 + x - 9)\n        Elliptic Curve defined by y^2 + y = x^3 + x - 9 over Rational Field\n        \n        sage: R.<x,y> = GF(5)[]\n        sage: EllipticCurve(x^3 + x^2 + 2 - y^2 - y*x)\n        Elliptic Curve defined by y^2 + x*y  = x^3 + x^2 + 2 over Finite Field of size 5\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5113\n\n",
    "created_at": "2009-01-27T22:21:12Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] elliptic curve construction from weierstrass equation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5113",
    "user": "robertwb"
}
```
Assignee: was

CC:  rlm

It would be nice to be able to do 

```
        sage: x, y = var('x,y')
        sage: EllipticCurve(y^2 + y ==  x^3 + x - 9)
        Elliptic Curve defined by y^2 + y = x^3 + x - 9 over Rational Field
        
        sage: R.<x,y> = GF(5)[]
        sage: EllipticCurve(x^3 + x^2 + 2 - y^2 - y*x)
        Elliptic Curve defined by y^2 + x*y  = x^3 + x^2 + 2 over Finite Field of size 5
```


Issue created by migration from https://trac.sagemath.org/ticket/5113





---

archive/issue_comments_039083.json:
```json
{
    "body": "Attachment [5113-ec-construction.patch](tarball://root/attachments/some-uuid/ticket5113/5113-ec-construction.patch) by rlm created at 2009-01-28 19:06:01\n\nI'm curious why you don't just do\n\n```\na1 = -1*f.coefficient(x*y)\na2 = f.coefficient(x**2)\n```\n\ninstead of iterating through `f`. I'm sure it doesn't matter.\n\nThe patch looks good though, positive review.\n\nI've also fixed printing of elliptic curves, see #5118.",
    "created_at": "2009-01-28T19:06:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5113#issuecomment-39083",
    "user": "rlm"
}
```

Attachment [5113-ec-construction.patch](tarball://root/attachments/some-uuid/ticket5113/5113-ec-construction.patch) by rlm created at 2009-01-28 19:06:01

I'm curious why you don't just do

```
a1 = -1*f.coefficient(x*y)
a2 = f.coefficient(x**2)
```

instead of iterating through `f`. I'm sure it doesn't matter.

The patch looks good though, positive review.

I've also fixed printing of elliptic curves, see #5118.



---

archive/issue_comments_039084.json:
```json
{
    "body": "I tried that first. The problem is f.coefficient(x) returns everything divisible by one power of x, not the x (alone) term\n\n\n```\nsage: R.<x,y> = QQ[]\nsage: f = x^2 + x*y + y^2*x\nsage: f.coef\nf.coefficient   f.coefficients  \nsage: f.coefficient(x)\ny^2 + y\nsage: f.coefficient(y^2)\nx\n```\n\n\nIt is also harder to exclude bad terms using that method.",
    "created_at": "2009-01-28T23:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5113#issuecomment-39084",
    "user": "robertwb"
}
```

I tried that first. The problem is f.coefficient(x) returns everything divisible by one power of x, not the x (alone) term


```
sage: R.<x,y> = QQ[]
sage: f = x^2 + x*y + y^2*x
sage: f.coef
f.coefficient   f.coefficients  
sage: f.coefficient(x)
y^2 + y
sage: f.coefficient(y^2)
x
```


It is also harder to exclude bad terms using that method.



---

archive/issue_comments_039085.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-29T00:27:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5113#issuecomment-39085",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039086.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-29T00:27:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5113#issuecomment-39086",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael
