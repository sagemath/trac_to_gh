# Issue 484: multivariate polynomial coercion bug

archive/issues_000484.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: x,y=PolynomialRing(QQ,2,\"xy\").gens()\nsage: f = 5*x+y-5\nsage: f(1,1)\n 1\nsage: type(f(1,1))\n <type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>\n```\n\n\nI usually think of the values of a polynomial as belonging to the\nground ring as opposed to the polynomial ring.\n\nIssue created by migration from https://trac.sagemath.org/ticket/484\n\n",
    "created_at": "2007-08-23T16:53:19Z",
    "labels": [
        "algebraic geometry",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.3",
    "title": "multivariate polynomial coercion bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/484",
    "user": "@wdjoyner"
}
```
Assignee: @williamstein


```
sage: x,y=PolynomialRing(QQ,2,"xy").gens()
sage: f = 5*x+y-5
sage: f(1,1)
 1
sage: type(f(1,1))
 <type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
```


I usually think of the values of a polynomial as belonging to the
ground ring as opposed to the polynomial ring.

Issue created by migration from https://trac.sagemath.org/ticket/484





---

archive/issue_comments_002417.json:
```json
{
    "body": "Works for me now:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.8.3.alpha2, Release Date: 2007-08-29                |\n| Type notebook() for the GUI, and license() for information.        |\nsage: x,y=PolynomialRing(QQ,2,\"xy\").gens()\nsage: f = 5*x+y-5\nsage: f(1,1)\n1\nsage: type(f(1,1))\n<type 'sage.rings.rational.Rational'>\n```\n\n\nI guess credit should go to Robert or William.\n\nCheers,\n\nMichael",
    "created_at": "2007-08-30T12:21:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/484#issuecomment-2417",
    "user": "mabshoff"
}
```

Works for me now:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.3.alpha2, Release Date: 2007-08-29                |
| Type notebook() for the GUI, and license() for information.        |
sage: x,y=PolynomialRing(QQ,2,"xy").gens()
sage: f = 5*x+y-5
sage: f(1,1)
1
sage: type(f(1,1))
<type 'sage.rings.rational.Rational'>
```


I guess credit should go to Robert or William.

Cheers,

Michael



---

archive/issue_comments_002418.json:
```json
{
    "body": "Changing component from algebraic geometry to basic arithmetic.",
    "created_at": "2007-08-30T12:21:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/484#issuecomment-2418",
    "user": "mabshoff"
}
```

Changing component from algebraic geometry to basic arithmetic.



---

archive/issue_comments_002419.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-30T12:21:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/484#issuecomment-2419",
    "user": "mabshoff"
}
```

Resolution: fixed
