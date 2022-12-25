# Issue 3117: bug in quotient polynomial rings when using funny term order

archive/issues_003117.json:
```json
{
    "body": "Assignee: @malb\n\nHi,\n\nWhether or not an element of R/I is zero must not depend on the term order. However, behold:\n\n```\nsage: R.<x,y> = PolynomialRing(QQ, order='neglex')\nsage: Q.<xbar,ybar> = R.quotient(y^2 - x^3 - x -1)\nsage: xbar\n0\n```\n\n\nwhereas\n\n```\nsage: R.<x,y> = PolynomialRing(QQ, order='lex')\nsage: Q.<xbar,ybar> = R.quotient(y^2 - x^3 - x -1)\nsage: xbar\nxbar\nsage: xbar != 0\nTrue\n```\n\n\nNOTE: I don't even know what neglex is (\"negative lex\", whatever that is). \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3117\n\n",
    "created_at": "2008-05-07T03:08:55Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "bug in quotient polynomial rings when using funny term order",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3117",
    "user": "https://github.com/williamstein"
}
```
Assignee: @malb

Hi,

Whether or not an element of R/I is zero must not depend on the term order. However, behold:

```
sage: R.<x,y> = PolynomialRing(QQ, order='neglex')
sage: Q.<xbar,ybar> = R.quotient(y^2 - x^3 - x -1)
sage: xbar
0
```


whereas

```
sage: R.<x,y> = PolynomialRing(QQ, order='lex')
sage: Q.<xbar,ybar> = R.quotient(y^2 - x^3 - x -1)
sage: xbar
xbar
sage: xbar != 0
True
```


NOTE: I don't even know what neglex is ("negative lex", whatever that is). 


Issue created by migration from https://trac.sagemath.org/ticket/3117





---

archive/issue_comments_021534.json:
```json
{
    "body": "neglex is a local ordering (x < 1) and thus I'm not sure what the expected result should be. See\n\n http://www.sagemath.org/doc/html/ref/module-sage.rings.polynomial.term-order.html\n\nfor details on neglex.",
    "created_at": "2008-05-07T07:50:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3117#issuecomment-21534",
    "user": "https://github.com/malb"
}
```

neglex is a local ordering (x < 1) and thus I'm not sure what the expected result should be. See

 http://www.sagemath.org/doc/html/ref/module-sage.rings.polynomial.term-order.html

for details on neglex.



---

archive/issue_comments_021535.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-06-03T14:52:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3117#issuecomment-21535",
    "user": "https://github.com/malb"
}
```

Resolution: invalid



---

archive/issue_comments_021536.json:
```json
{
    "body": "Michael Brickenstein wrote (my translation):\n\n```\ny^2 - x^3 - x -1\nis a unit in Singular if you calculate in 'ls'. If you take a quotient of \nthat zero is the answer.\n\nSingular there works with the localisation of the polynomial ring \nby all polynomials with constant leading term. Check a commutative \nalgebra book about localisation.\n```\n",
    "created_at": "2008-06-03T14:52:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3117#issuecomment-21536",
    "user": "https://github.com/malb"
}
```

Michael Brickenstein wrote (my translation):

```
y^2 - x^3 - x -1
is a unit in Singular if you calculate in 'ls'. If you take a quotient of 
that zero is the answer.

Singular there works with the localisation of the polynomial ring 
by all polynomials with constant leading term. Check a commutative 
algebra book about localisation.
```




---

archive/issue_events_003334.json:
```json
{
    "actor": "@malb",
    "created_at": "2008-06-03T14:52:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3117",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3117#event-3334"
}
```
