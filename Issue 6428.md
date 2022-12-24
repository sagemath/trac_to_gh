# Issue 6428: Large exponents overflow to negative in polydict ring

archive/issues_006428.json:
```json
{
    "body": "Assignee: tbd\n\nLarge exponents overflow to negative in polydict ring:\n\nsage: from sage.rings.polynomial.multi_polynomial_ring import \\\n...       MPolynomialRing_polydict\nsage: ring = MPolynomialRing_polydict(ZZ, 3, ['a','b','c'], \"lex\")\nsage: a = ring.gens()[0]\n\nsage: a<sup>(2</sup>31-1)\na^2147483647\n\nsage: a<sup>(2</sup>31)\na^-2147483648\n\nsage: a<sup>(2</sup>32)\n1\n\nIssue created by migration from https://trac.sagemath.org/ticket/6428\n\n",
    "created_at": "2009-06-26T18:26:31Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Large exponents overflow to negative in polydict ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6428",
    "user": "broune"
}
```
Assignee: tbd

Large exponents overflow to negative in polydict ring:

sage: from sage.rings.polynomial.multi_polynomial_ring import \
...       MPolynomialRing_polydict
sage: ring = MPolynomialRing_polydict(ZZ, 3, ['a','b','c'], "lex")
sage: a = ring.gens()[0]

sage: a<sup>(2</sup>31-1)
a^2147483647

sage: a<sup>(2</sup>31)
a^-2147483648

sage: a<sup>(2</sup>32)
1

Issue created by migration from https://trac.sagemath.org/ticket/6428





---

archive/issue_comments_051619.json:
```json
{
    "body": "Fixed layout.",
    "created_at": "2009-06-26T18:29:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6428#issuecomment-51619",
    "user": "broune"
}
```

Fixed layout.



---

archive/issue_comments_051620.json:
```json
{
    "body": "Changing component from algebra to commutative algebra.",
    "created_at": "2009-11-15T13:14:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6428#issuecomment-51620",
    "user": "@aghitza"
}
```

Changing component from algebra to commutative algebra.



---

archive/issue_comments_051621.json:
```json
{
    "body": "This is still a bug.   Ick!\n\n\n```\nsage: R.<y,z> =Frac(QQ['x'])[]\nsage: y^(2^32)\n1\nsage: y^(2^32-1)\ny^-1\nsage: y^(2^31)\ny^-2147483648\n```\n",
    "created_at": "2010-01-18T01:39:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6428#issuecomment-51621",
    "user": "@williamstein"
}
```

This is still a bug.   Ick!


```
sage: R.<y,z> =Frac(QQ['x'])[]
sage: y^(2^32)
1
sage: y^(2^32-1)
y^-1
sage: y^(2^31)
y^-2147483648
```




---

archive/issue_comments_051622.json:
```json
{
    "body": "Here is better input to replicate what is at the core of the problem:\n\n```\nsage: a = sage.rings.polynomial.polydict.PolyDict({(2147483647r,):1r})\nsage: a*a\nPolyDict with representation {(-2,): 1}\n```\n",
    "created_at": "2010-01-18T09:59:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6428#issuecomment-51622",
    "user": "@williamstein"
}
```

Here is better input to replicate what is at the core of the problem:

```
sage: a = sage.rings.polynomial.polydict.PolyDict({(2147483647r,):1r})
sage: a*a
PolyDict with representation {(-2,): 1}
```




---

archive/issue_comments_051623.json:
```json
{
    "body": "Attachment [trac_6428.patch](tarball://root/attachments/some-uuid/ticket6428/trac_6428.patch) by @williamstein created at 2010-01-18 10:19:17",
    "created_at": "2010-01-18T10:19:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6428#issuecomment-51623",
    "user": "@williamstein"
}
```

Attachment [trac_6428.patch](tarball://root/attachments/some-uuid/ticket6428/trac_6428.patch) by @williamstein created at 2010-01-18 10:19:17



---

archive/issue_comments_051624.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-18T10:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6428#issuecomment-51624",
    "user": "@williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_051625.json:
```json
{
    "body": "This patch simply reports an error if this happens. I thought the polydict ring was supposed to allow arbitrary precision exponents.",
    "created_at": "2010-01-18T18:58:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6428#issuecomment-51625",
    "user": "broune"
}
```

This patch simply reports an error if this happens. I thought the polydict ring was supposed to allow arbitrary precision exponents.



---

archive/issue_comments_051626.json:
```json
{
    "body": "> This patch simply reports an error if this happens. I thought the polydict\n> ring was supposed to allow arbitrary precision exponents. \n\nSince in the entire Cython implementation of polydict, the exponents are represented internally as C ints there is no way it is supposed to represent arbitrary precision exponents.   One could write something that does arbitrary exponents, but that ETuple stuff simply isn't such a thing.",
    "created_at": "2010-01-18T22:35:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6428#issuecomment-51626",
    "user": "@williamstein"
}
```

> This patch simply reports an error if this happens. I thought the polydict
> ring was supposed to allow arbitrary precision exponents. 

Since in the entire Cython implementation of polydict, the exponents are represented internally as C ints there is no way it is supposed to represent arbitrary precision exponents.   One could write something that does arbitrary exponents, but that ETuple stuff simply isn't such a thing.



---

archive/issue_comments_051627.json:
```json
{
    "body": "By the way, for basic arithmetic, the symbolic ring supports arbitrary exponents. \n\n\n```\nsage: var('y')\ny\nsage: y^(2^32)\ny^4294967296\nsage: y^(2^50)\ny^1125899906842624\nsage: y^(2^50+y)\ny^(y + 1125899906842624)\n```\n",
    "created_at": "2010-01-18T22:37:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6428#issuecomment-51627",
    "user": "@williamstein"
}
```

By the way, for basic arithmetic, the symbolic ring supports arbitrary exponents. 


```
sage: var('y')
y
sage: y^(2^32)
y^4294967296
sage: y^(2^50)
y^1125899906842624
sage: y^(2^50+y)
y^(y + 1125899906842624)
```




---

archive/issue_comments_051628.json:
```json
{
    "body": "Attachment [6428_ETuple_overflow.patch](tarball://root/attachments/some-uuid/ticket6428/6428_ETuple_overflow.patch) by @wjp created at 2010-01-21 00:32:37\n\nI added a new patch (to be applied instead of the old one) that also handles negative exponents. (The previous patch broke LaurentPolynomials).",
    "created_at": "2010-01-21T00:32:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6428#issuecomment-51628",
    "user": "@wjp"
}
```

Attachment [6428_ETuple_overflow.patch](tarball://root/attachments/some-uuid/ticket6428/6428_ETuple_overflow.patch) by @wjp created at 2010-01-21 00:32:37

I added a new patch (to be applied instead of the old one) that also handles negative exponents. (The previous patch broke LaurentPolynomials).



---

archive/issue_comments_051629.json:
```json
{
    "body": "This now passes all doctests.",
    "created_at": "2010-01-21T00:57:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6428#issuecomment-51629",
    "user": "spancratz"
}
```

This now passes all doctests.



---

archive/issue_comments_051630.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-21T01:02:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6428#issuecomment-51630",
    "user": "spancratz"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_051631.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-23T09:05:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6428#issuecomment-51631",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_051632.json:
```json
{
    "body": "Merged [6428_ETuple_overflow.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6428/6428_ETuple_overflow.patch).",
    "created_at": "2010-01-23T09:05:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6428#issuecomment-51632",
    "user": "mvngu"
}
```

Merged [6428_ETuple_overflow.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6428/6428_ETuple_overflow.patch).
