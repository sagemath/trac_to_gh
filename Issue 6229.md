# Issue 6229: efficiency in Lagrange polynomial interpolation (easy fix...)

archive/issues_006229.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  mvngu\n\nThis is a follow-up to #6043.\n\nThis nested loop is useless:\n{{\n        P = 0 \n        for i in xrange(n): \n            prod = 1 \n            for j in xrange(i): \n                prod *= (x - points[j][0]) \n            P += (F[i] * prod) \n        return P\n\n}}\n\nand should be replaced with (something like)\n\n{{\n        P = F[n-1]\n        for i in xrange(n-2,-1,-1): \n            P *= (x - points[i][0])\n            P += F[i]\n        return P\n}}\n\nIssue created by migration from https://trac.sagemath.org/ticket/6229\n\n",
    "created_at": "2009-06-05T22:15:54Z",
    "labels": [
        "algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "efficiency in Lagrange polynomial interpolation (easy fix...)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6229",
    "user": "ylchapuy"
}
```
Assignee: tbd

CC:  mvngu

This is a follow-up to #6043.

This nested loop is useless:
{{
        P = 0 
        for i in xrange(n): 
            prod = 1 
            for j in xrange(i): 
                prod *= (x - points[j][0]) 
            P += (F[i] * prod) 
        return P

}}

and should be replaced with (something like)

{{
        P = F[n-1]
        for i in xrange(n-2,-1,-1): 
            P *= (x - points[i][0])
            P += F[i]
        return P
}}

Issue created by migration from https://trac.sagemath.org/ticket/6229





---

archive/issue_comments_049711.json:
```json
{
    "body": "I have no clean install yet to produce the patch myself...",
    "created_at": "2009-06-05T22:18:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6229#issuecomment-49711",
    "user": "ylchapuy"
}
```

I have no clean install yet to produce the patch myself...



---

archive/issue_comments_049712.json:
```json
{
    "body": "You mean like evaluating it in nested form, similar to Horner's method? Do'h, I missed that.",
    "created_at": "2009-06-05T23:42:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6229#issuecomment-49712",
    "user": "mvngu"
}
```

You mean like evaluating it in nested form, similar to Horner's method? Do'h, I missed that.



---

archive/issue_comments_049713.json:
```json
{
    "body": "The patch contains the suggested fix by ylchapuy. It's ylchapuy's code, not mine, so authorship credit goes to ylchapuy. I'm just reviewing the code. Here are some timing statistics on sage.math:\n\n```\n# BEFORE\n\nsage: R = PolynomialRing(QQ, 'x')\nsage: %timeit R.lagrange_polynomial([(0,1),(2,2),(3,-2),(-4,9)])\n1000 loops, best of 3: 830 \u00b5s per loop\nsage: R.lagrange_polynomial([(0,1),(2,2),(3,-2),(-4,9)])\n-23/84*x^3 - 11/84*x^2 + 13/7*x + 1\nsage: R = PolynomialRing(GF(2**3,'a'), 'x')\nsage: a = R.base_ring().gen()\nsage: timeit(\"R.lagrange_polynomial([(a^2+a,a),(a,1),(a^2,a^2+a+1)])\")\n625 loops, best of 3: 112 \u00b5s per loop\nsage: R.lagrange_polynomial([(a^2+a,a),(a,1),(a^2,a^2+a+1)])\na^2*x^2 + a^2*x + a^2\n\n\n# AFTER\n\nsage: R = PolynomialRing(QQ, 'x')\nsage: %timeit R.lagrange_polynomial([(0,1),(2,2),(3,-2),(-4,9)])\n1000 loops, best of 3: 416 \u00b5s per loop\nsage: R.lagrange_polynomial([(0,1),(2,2),(3,-2),(-4,9)])\n-23/84*x^3 - 11/84*x^2 + 13/7*x + 1\nsage: R = PolynomialRing(GF(2**3,'a'), 'x')\nsage: a = R.base_ring().gen()\nsage: timeit(\"R.lagrange_polynomial([(a^2+a,a),(a,1),(a^2,a^2+a+1)])\")\n625 loops, best of 3: 86.2 \u00b5s per loop\nsage: R.lagrange_polynomial([(a^2+a,a),(a,1),(a^2,a^2+a+1)])\na^2*x^2 + a^2*x + a^2\n```\n\nSo efficiency gain of up to 50%. Positive review.",
    "created_at": "2009-06-06T00:31:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6229#issuecomment-49713",
    "user": "mvngu"
}
```

The patch contains the suggested fix by ylchapuy. It's ylchapuy's code, not mine, so authorship credit goes to ylchapuy. I'm just reviewing the code. Here are some timing statistics on sage.math:

```
# BEFORE

sage: R = PolynomialRing(QQ, 'x')
sage: %timeit R.lagrange_polynomial([(0,1),(2,2),(3,-2),(-4,9)])
1000 loops, best of 3: 830 µs per loop
sage: R.lagrange_polynomial([(0,1),(2,2),(3,-2),(-4,9)])
-23/84*x^3 - 11/84*x^2 + 13/7*x + 1
sage: R = PolynomialRing(GF(2**3,'a'), 'x')
sage: a = R.base_ring().gen()
sage: timeit("R.lagrange_polynomial([(a^2+a,a),(a,1),(a^2,a^2+a+1)])")
625 loops, best of 3: 112 µs per loop
sage: R.lagrange_polynomial([(a^2+a,a),(a,1),(a^2,a^2+a+1)])
a^2*x^2 + a^2*x + a^2


# AFTER

sage: R = PolynomialRing(QQ, 'x')
sage: %timeit R.lagrange_polynomial([(0,1),(2,2),(3,-2),(-4,9)])
1000 loops, best of 3: 416 µs per loop
sage: R.lagrange_polynomial([(0,1),(2,2),(3,-2),(-4,9)])
-23/84*x^3 - 11/84*x^2 + 13/7*x + 1
sage: R = PolynomialRing(GF(2**3,'a'), 'x')
sage: a = R.base_ring().gen()
sage: timeit("R.lagrange_polynomial([(a^2+a,a),(a,1),(a^2,a^2+a+1)])")
625 loops, best of 3: 86.2 µs per loop
sage: R.lagrange_polynomial([(a^2+a,a),(a,1),(a^2,a^2+a+1)])
a^2*x^2 + a^2*x + a^2
```

So efficiency gain of up to 50%. Positive review.



---

archive/issue_comments_049714.json:
```json
{
    "body": "Attachment [trac_6229.patch](tarball://root/attachments/some-uuid/ticket6229/trac_6229.patch) by mvngu created at 2009-06-06 00:33:32\n\nbased on Sage 4.0.1.rc2",
    "created_at": "2009-06-06T00:33:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6229#issuecomment-49714",
    "user": "mvngu"
}
```

Attachment [trac_6229.patch](tarball://root/attachments/some-uuid/ticket6229/trac_6229.patch) by mvngu created at 2009-06-06 00:33:32

based on Sage 4.0.1.rc2



---

archive/issue_comments_049715.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T21:18:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6229#issuecomment-49715",
    "user": "@ncalexan"
}
```

Resolution: fixed
