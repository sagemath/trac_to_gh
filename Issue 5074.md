# Issue 5074: singular factorization over GF(p) need not be a complete factorization

archive/issues_005074.json:
```json
{
    "body": "Assignee: @malb\n\n\n```\nsage: k.<a> = GF(9)\nsage: R.<x,y> = PolynomialRing(k)\nsage: h = - (-x^2 - x*y + y^2 - 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (-x^4 - x^3*y - x*y^3 + y^4 - x^3 + x^2*y + x*y^2 - x^2 - x*y - y^2 + x + 1)\n\nsage: h.factor()\n(-1) * (-x^2 - x*y + y^2 - 1) * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^6 - x^5*y + x*y^5 + y^6 + x^5 + x*y^4 - x^4 + x^2*y^2 + x*y^3 + y^4 + x^2*y - y^2 - x - 1)\nsage: h.factor()\n(-1) * (-x^2 - x*y + y^2 - 1)^2 * (-x^6*y^2 - x^5*y^3 - x^4*y^4 + x^3*y^5 + x^2*y^6 - x*y^7 + y^8 - x^6*y - x^4*y^3 + x^3*y^4 + x^2*y^5 + x*y^6 + y^7 + x^6 - x^5*y + x^2*y^4 + x^5 + x^3*y^2 - x^2*y^3 - y^5 - x^4 - x^3*y + x^2*y^2 - y^4 + x^2*y + x*y^2 + y^3 - x*y - y^2 - x - 1)\n```\n\n\nNote that the factors need not even be coprime!\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5074\n\n",
    "created_at": "2009-01-23T14:30:09Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "singular factorization over GF(p) need not be a complete factorization",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5074",
    "user": "https://github.com/williamstein"
}
```
Assignee: @malb


```
sage: k.<a> = GF(9)
sage: R.<x,y> = PolynomialRing(k)
sage: h = - (-x^2 - x*y + y^2 - 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (-x^4 - x^3*y - x*y^3 + y^4 - x^3 + x^2*y + x*y^2 - x^2 - x*y - y^2 + x + 1)

sage: h.factor()
(-1) * (-x^2 - x*y + y^2 - 1) * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^6 - x^5*y + x*y^5 + y^6 + x^5 + x*y^4 - x^4 + x^2*y^2 + x*y^3 + y^4 + x^2*y - y^2 - x - 1)
sage: h.factor()
(-1) * (-x^2 - x*y + y^2 - 1)^2 * (-x^6*y^2 - x^5*y^3 - x^4*y^4 + x^3*y^5 + x^2*y^6 - x*y^7 + y^8 - x^6*y - x^4*y^3 + x^3*y^4 + x^2*y^5 + x*y^6 + y^7 + x^6 - x^5*y + x^2*y^4 + x^5 + x^3*y^2 - x^2*y^3 - y^5 - x^4 - x^3*y + x^2*y^2 - y^4 + x^2*y + x*y^2 + y^3 - x*y - y^2 - x - 1)
```


Note that the factors need not even be coprime!



Issue created by migration from https://trac.sagemath.org/ticket/5074





---

archive/issue_comments_038561.json:
```json
{
    "body": "Code I use to find countexamples:\n\n\n```\nk.<a> = GF(19^2); R.<x,y> = PolynomialRing(k)\nfor i in range(5000):\n    v = [R.random_element() for _ in range(3)]; print i; assert prod(v).factor().prod() == prod(v)\n```\n",
    "created_at": "2009-01-23T14:45:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5074#issuecomment-38561",
    "user": "https://github.com/williamstein"
}
```

Code I use to find countexamples:


```
k.<a> = GF(19^2); R.<x,y> = PolynomialRing(k)
for i in range(5000):
    v = [R.random_element() for _ in range(3)]; print i; assert prod(v).factor().prod() == prod(v)
```




---

archive/issue_comments_038562.json:
```json
{
    "body": "Attachment [trac_5074.patch](tarball://root/attachments/some-uuid/ticket5074/trac_5074.patch) by @malb created at 2010-07-12 15:11:14",
    "created_at": "2010-07-12T15:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5074#issuecomment-38562",
    "user": "https://github.com/malb"
}
```

Attachment [trac_5074.patch](tarball://root/attachments/some-uuid/ticket5074/trac_5074.patch) by @malb created at 2010-07-12 15:11:14



---

archive/issue_comments_038563.json:
```json
{
    "body": "The original problem seems to be fixed by now. I ran the above snipped and everything was fine. However, for GF(9) I do get an error:\n\n```\nsage: k.<a> = GF(9)\nsage: R.<x,y> = PolynomialRing(k)\nsage: h = - (-x^2 - x*y + y^2 - 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (-x^4 - x^3*y - x*y^3 + y^4 - x^3 + x^2*y + x*y^2 - x^2 - x*y - y^2 + x + 1)\nsage: factor(h)\n---------------------------------------------------------------------------\nAssertionError                            Traceback (most recent call last)\n\nsage.rings.polynomial.multi_polynomial.MPolynomial._factor_over_nonprime_finite_field()\nAssertionError: bug in Singular factoring an auxiliary polynomial over GF(p): bad multiplicity (1, 2)\n```\n",
    "created_at": "2010-07-12T15:13:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5074#issuecomment-38563",
    "user": "https://github.com/malb"
}
```

The original problem seems to be fixed by now. I ran the above snipped and everything was fine. However, for GF(9) I do get an error:

```
sage: k.<a> = GF(9)
sage: R.<x,y> = PolynomialRing(k)
sage: h = - (-x^2 - x*y + y^2 - 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (-x^4 - x^3*y - x*y^3 + y^4 - x^3 + x^2*y + x*y^2 - x^2 - x*y - y^2 + x + 1)
sage: factor(h)
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)

sage.rings.polynomial.multi_polynomial.MPolynomial._factor_over_nonprime_finite_field()
AssertionError: bug in Singular factoring an auxiliary polynomial over GF(p): bad multiplicity (1, 2)
```




---

archive/issue_comments_038564.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-07-12T15:13:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5074#issuecomment-38564",
    "user": "https://github.com/malb"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_038565.json:
```json
{
    "body": "It's definitely still broken.  Note that it isn't broken every single time :-):\n\n```\n\nsage: sage: k.<a> = GF(9)sage: sage: R.<x,y> = PolynomialRing(k)\nsage: sage: h = - (-x^2 - x*y + y^2 - 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (-x^4 - x^3*y - x*y^3 + y^4 - x^3 + x^2*y + x*y^2 - x^2 - x*y - y^2 + x + 1)\nsage: h.factor()\n(-1) * (-x^2 - x*y + y^2 - 1) * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^6 - x^5*y + x*y^5 + y^6 + x^5 + x*y^4 - x^4 + x^2*y^2 + x*y^3 + y^4 + x^2*y - y^2 - x - 1)\nsage: h.factor()\n(-1) * (-x^2 - x*y + y^2 - 1)^2 * (-x^6*y^2 - x^5*y^3 - x^4*y^4 + x^3*y^5 + x^2*y^6 - x*y^7 + y^8 - x^6*y - x^4*y^3 + x^3*y^4 + x^2*y^5 + x*y^6 + y^7 + x^6 - x^5*y + x^2*y^4 + x^5 + x^3*y^2 - x^2*y^3 - y^5 - x^4 - x^3*y + x^2*y^2 - y^4 + x^2*y + x*y^2 + y^3 - x*y - y^2 - x - 1)\nsage: h.factor()\n(-1) * (-x^2 - x*y + y^2 - 1) * (x^8*y^2 - x^7*y^3 + x^6*y^4 - x^5*y^5 + x^3*y^7 + x^2*y^8 + x*y^9 + y^10 + x^8*y + x^7*y^2 - x^3*y^6 - x^2*y^7 + y^9 - x^8 + x^3*y^5 + x*y^7 - y^8 - x^7 + x^4*y^3 + x^3*y^4 - x^2*y^5 + y^7 - x^4*y^2 + x^3*y^3 + x^2*y^4 + x*y^5 - y^6 - x^5 - x^4*y - y^5 + x^4 - x^3*y + x^2*y^2 + x^3 + x*y^2 - y^3 + x^2 - x*y + x + 1)\nsage: h.factor()\n(-1) * (-x^2 - x*y + y^2 - 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (-x^4 - x^3*y - x*y^3 + y^4 - x^3 + x^2*y + x*y^2 - x^2 - x*y - y^2 + x + 1)\n```\n",
    "created_at": "2010-07-14T22:07:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5074#issuecomment-38565",
    "user": "https://github.com/williamstein"
}
```

It's definitely still broken.  Note that it isn't broken every single time :-):

```

sage: sage: k.<a> = GF(9)sage: sage: R.<x,y> = PolynomialRing(k)
sage: sage: h = - (-x^2 - x*y + y^2 - 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (-x^4 - x^3*y - x*y^3 + y^4 - x^3 + x^2*y + x*y^2 - x^2 - x*y - y^2 + x + 1)
sage: h.factor()
(-1) * (-x^2 - x*y + y^2 - 1) * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^6 - x^5*y + x*y^5 + y^6 + x^5 + x*y^4 - x^4 + x^2*y^2 + x*y^3 + y^4 + x^2*y - y^2 - x - 1)
sage: h.factor()
(-1) * (-x^2 - x*y + y^2 - 1)^2 * (-x^6*y^2 - x^5*y^3 - x^4*y^4 + x^3*y^5 + x^2*y^6 - x*y^7 + y^8 - x^6*y - x^4*y^3 + x^3*y^4 + x^2*y^5 + x*y^6 + y^7 + x^6 - x^5*y + x^2*y^4 + x^5 + x^3*y^2 - x^2*y^3 - y^5 - x^4 - x^3*y + x^2*y^2 - y^4 + x^2*y + x*y^2 + y^3 - x*y - y^2 - x - 1)
sage: h.factor()
(-1) * (-x^2 - x*y + y^2 - 1) * (x^8*y^2 - x^7*y^3 + x^6*y^4 - x^5*y^5 + x^3*y^7 + x^2*y^8 + x*y^9 + y^10 + x^8*y + x^7*y^2 - x^3*y^6 - x^2*y^7 + y^9 - x^8 + x^3*y^5 + x*y^7 - y^8 - x^7 + x^4*y^3 + x^3*y^4 - x^2*y^5 + y^7 - x^4*y^2 + x^3*y^3 + x^2*y^4 + x*y^5 - y^6 - x^5 - x^4*y - y^5 + x^4 - x^3*y + x^2*y^2 + x^3 + x*y^2 - y^3 + x^2 - x*y + x + 1)
sage: h.factor()
(-1) * (-x^2 - x*y + y^2 - 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (-x^4 - x^3*y - x*y^3 + y^4 - x^3 + x^2*y + x*y^2 - x^2 - x*y - y^2 + x + 1)
```




---

archive/issue_comments_038566.json:
```json
{
    "body": "See also #9498.",
    "created_at": "2010-07-14T22:10:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5074#issuecomment-38566",
    "user": "https://github.com/williamstein"
}
```

See also #9498.



---

archive/issue_comments_038567.json:
```json
{
    "body": "I just tried it again with 3-1-1-3 which does have some new factorisation code over GF(p)\n\n\n```\nsage: k.<a> = GF(9)sage: sage: R.<x,y> = PolynomialRing(k)\nsage: h = - (-x^2 - x*y + y^2 - 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (-x^4 - x^3*y - x*y^3 + y^4 - x^3 + x^2*y + x*y^2 - x^2 - x*y - y^2 + x + 1)\nsage: for i in range(10): h.factor(proof=False)\n....: \n(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)\n(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)\n(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)\n(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)\n(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)\n(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)\n(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)\n(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)\n(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)\n(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)\n\n\n```\n",
    "created_at": "2010-07-15T09:08:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5074#issuecomment-38567",
    "user": "https://github.com/malb"
}
```

I just tried it again with 3-1-1-3 which does have some new factorisation code over GF(p)


```
sage: k.<a> = GF(9)sage: sage: R.<x,y> = PolynomialRing(k)
sage: h = - (-x^2 - x*y + y^2 - 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (-x^4 - x^3*y - x*y^3 + y^4 - x^3 + x^2*y + x*y^2 - x^2 - x*y - y^2 + x + 1)
sage: for i in range(10): h.factor(proof=False)
....: 
(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)
(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)
(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)
(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)
(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)
(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)
(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)
(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)
(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)
(x^2 + x*y - y^2 + 1)^2 * (x^2*y^2 + y^4 + x^2*y + x*y^2 + y^3 - x^2 + x*y + y^2 - 1) * (x^4 + x^3*y + x*y^3 - y^4 + x^3 - x^2*y - x*y^2 + x^2 + x*y + y^2 - x - 1)


```




---

archive/issue_comments_038568.json:
```json
{
    "body": "Attachment [review_5313.sage](tarball://root/attachments/some-uuid/ticket5074/review_5313.sage) by @malb created at 2010-11-03 13:17:51\n\ntest quality of factorisation for many random examples",
    "created_at": "2010-11-03T13:17:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5074#issuecomment-38568",
    "user": "https://github.com/malb"
}
```

Attachment [review_5313.sage](tarball://root/attachments/some-uuid/ticket5074/review_5313.sage) by @malb created at 2010-11-03 13:17:51

test quality of factorisation for many random examples



---

archive/issue_comments_038569.json:
```json
{
    "body": "I've written a little script to check the quality of factorisation. While I didn't get any wrong answer so far, factorisation sometimes takes ages. This is ticket #291 in the Singular bug tracker: http://www.singular.uni-kl.de:8002/trac/ticket/291\n\nStrictly speaking, this ticket could be closed (modulo review of the patch etc) since there are no known examples where the wrong factorisation is returned. Alternatively, we could wait for the performance issue to be resolved in Singular.",
    "created_at": "2010-11-03T13:20:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5074#issuecomment-38569",
    "user": "https://github.com/malb"
}
```

I've written a little script to check the quality of factorisation. While I didn't get any wrong answer so far, factorisation sometimes takes ages. This is ticket #291 in the Singular bug tracker: http://www.singular.uni-kl.de:8002/trac/ticket/291

Strictly speaking, this ticket could be closed (modulo review of the patch etc) since there are no known examples where the wrong factorisation is returned. Alternatively, we could wait for the performance issue to be resolved in Singular.



---

archive/issue_comments_038570.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-11-03T13:20:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5074#issuecomment-38570",
    "user": "https://github.com/malb"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_038571.json:
```json
{
    "body": "Changing keywords from \"\" to \"factorisation\".",
    "created_at": "2010-11-03T13:20:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5074#issuecomment-38571",
    "user": "https://github.com/malb"
}
```

Changing keywords from "" to "factorisation".



---

archive/issue_comments_038572.json:
```json
{
    "body": "Changing status from needs_info to positive_review.",
    "created_at": "2013-08-13T15:57:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5074#issuecomment-38572",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_info to positive_review.



---

archive/issue_comments_038573.json:
```json
{
    "body": "Totally fixed upstream.",
    "created_at": "2013-08-13T15:57:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5074#issuecomment-38573",
    "user": "https://github.com/jdemeyer"
}
```

Totally fixed upstream.



---

archive/issue_comments_038574.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-08-16T11:10:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5074#issuecomment-38574",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme



---

archive/issue_events_005319.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-16T11:10:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5074",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5074#event-5319"
}
```
