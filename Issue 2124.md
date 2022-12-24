# Issue 2124: [with patch, needs review] minor bug in f.root_field()

archive/issues_002124.json:
```json
{
    "body": "Assignee: craigcitro\n\nf.root_field() currently does is_IntegralDomain(f.parent()) instead of f.parent().is_integral_domain(), which is bad. The attached patch fixes it.\n\nBefore:\n\n```\nsage: R.<x> = PolynomialRing(Integers(31))\n\nsage: h = x+5\n\nsage: h.root_field('a')\n---------------------------------------------------------------------------\n<type 'exceptions.ValueError'>            Traceback (most recent call last)\n\n/Users/craigcitro/<ipython console> in <module>()\n\n/Users/craigcitro/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial.root_field()\n\n<type 'exceptions.ValueError'>: the base ring must be a domain\n\nsage: h.base_ring()\n Ring of integers modulo 31\n```\n\n\nAfter:\n\n```\nsage: R.<x> = PolynomialRing(Integers(31))\n\nsage: h = x+5\n\nsage: h.root_field('a')\n Ring of integers modulo 31\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2124\n\n",
    "created_at": "2008-02-09T05:15:22Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "[with patch, needs review] minor bug in f.root_field()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2124",
    "user": "craigcitro"
}
```
Assignee: craigcitro

f.root_field() currently does is_IntegralDomain(f.parent()) instead of f.parent().is_integral_domain(), which is bad. The attached patch fixes it.

Before:

```
sage: R.<x> = PolynomialRing(Integers(31))

sage: h = x+5

sage: h.root_field('a')
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/Users/craigcitro/<ipython console> in <module>()

/Users/craigcitro/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial.root_field()

<type 'exceptions.ValueError'>: the base ring must be a domain

sage: h.base_ring()
 Ring of integers modulo 31
```


After:

```
sage: R.<x> = PolynomialRing(Integers(31))

sage: h = x+5

sage: h.root_field('a')
 Ring of integers modulo 31
```




Issue created by migration from https://trac.sagemath.org/ticket/2124





---

archive/issue_comments_013935.json:
```json
{
    "body": "Attachment [trac-2124.patch](tarball://root/attachments/some-uuid/ticket2124/trac-2124.patch) by craigcitro created at 2008-02-09 05:17:48",
    "created_at": "2008-02-09T05:17:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2124#issuecomment-13935",
    "user": "craigcitro"
}
```

Attachment [trac-2124.patch](tarball://root/attachments/some-uuid/ticket2124/trac-2124.patch) by craigcitro created at 2008-02-09 05:17:48



---

archive/issue_comments_013936.json:
```json
{
    "body": "looks good",
    "created_at": "2008-02-09T05:26:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2124#issuecomment-13936",
    "user": "AlexGhitza"
}
```

looks good



---

archive/issue_comments_013937.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-10T00:58:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2124#issuecomment-13937",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013938.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0",
    "created_at": "2008-02-10T00:58:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2124#issuecomment-13938",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha0
