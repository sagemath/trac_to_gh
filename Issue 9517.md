# Issue 9517: PolynomialRing() returns Multivariate polynomial rings when you would expect univariate ones

archive/issues_009517.json:
```json
{
    "body": "Assignee: @malb\n\nBelow is an example of the strange behavior in sage 4.4.4.\n\n\n```\nsage: PR1=PolynomialRing(QQ,'x');PR2=PolynomialRing(QQ,1,'x')\nsage: PR1;PR2\nUnivariate Polynomial Ring in x over Rational Field\nMultivariate Polynomial Ring in x over Rational Field\n```\n\n\nI've searched for similar problems but only #9220 seems vagely related but is a real different problem.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9517\n\n",
    "created_at": "2010-07-16T10:20:32Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "PolynomialRing() returns Multivariate polynomial rings when you would expect univariate ones",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9517",
    "user": "https://github.com/koffie"
}
```
Assignee: @malb

Below is an example of the strange behavior in sage 4.4.4.


```
sage: PR1=PolynomialRing(QQ,'x');PR2=PolynomialRing(QQ,1,'x')
sage: PR1;PR2
Univariate Polynomial Ring in x over Rational Field
Multivariate Polynomial Ring in x over Rational Field
```


I've searched for similar problems but only #9220 seems vagely related but is a real different problem.

Issue created by migration from https://trac.sagemath.org/ticket/9517





---

archive/issue_comments_091345.json:
```json
{
    "body": "It's not a bug it's a feature :)\n\nFrom the documentation of PolynomialRing:\n\n\n```\n``PolynomialRing(base_ring, name, sparse=False)`` returns a univariate polynomial ring; also, PolynomialRing(base_ring, names, sparse=False) yields a univariate polynomial ring, if names is a list or tuple providing exactly one name. All other input formats return a multivariate polynomial ring.\n```\n",
    "created_at": "2010-07-16T10:30:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9517#issuecomment-91345",
    "user": "https://github.com/malb"
}
```

It's not a bug it's a feature :)

From the documentation of PolynomialRing:


```
``PolynomialRing(base_ring, name, sparse=False)`` returns a univariate polynomial ring; also, PolynomialRing(base_ring, names, sparse=False) yields a univariate polynomial ring, if names is a list or tuple providing exactly one name. All other input formats return a multivariate polynomial ring.
```




---

archive/issue_comments_091346.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-07-16T10:30:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9517#issuecomment-91346",
    "user": "https://github.com/malb"
}
```

Resolution: wontfix
