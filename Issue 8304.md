# Issue 8304: Remove stray factors of 2 in Coleman integration

archive/issues_008304.json:
```json
{
    "body": "Assignee: was\n\nCC:  jen robertwb\n\nKeywords: Coleman integration, hyperelliptic curves\n\nJen discovered some stray factors of 2 buried in the Coleman integration code. (Apply patches at #7927 before trying these examples.)\n\nOn one hand, the invariant differential sometimes thinks it's dx/2y (as it should):\n\n```\nsage: R.<x> = QQ['x']\nsage: H = HyperellipticCurve(x^3+1)\nsage: K = Qp(5,8)\nsage: HK = H.change_ring(K)\nsage: w = HK.invariant_differential()\nsage: P = HK(0,1)\nsage: Q = HK.lift_x(5)\nsage: x,y = HK.monsky_washnitzer_gens()\nsage: (2*y*w).coleman_integral(P,Q)\n5 + O(5^9)\n```\n\nbut on the other hand, it sometimes behaves as if it were dx/y (as it shouldn't):\n\n```\nsage: x,y,z = HK.local_analytic_interpolation(P,Q)\nsage: I1 = (x.derivative()/y).integral()\nsage: I2 = (x.derivative()/(2*y)).integral()\nsage: I1(1)-I1(0)\n5 + 3*5^4 + 3*5^6 + 3*5^7 + O(5^9)\nsage: I2(1)-I2(0)\n3*5 + 2*5^2 + 2*5^3 + 5^4 + 4*5^6 + 5^7 + O(5^9)\nsage: HK.coleman_integral(w,P,Q)\n5 + 3*5^4 + 3*5^6 + 3*5^7 + O(5^9)\n```\n\nThe apparent fix is to insert an extra division by two in tiny_integrals (which then needs a corrected docstring and some doctests, and similarly for tiny_integrals_on_basis) and then remove the multiplication by 2 in coleman_integrals_on_basis. Then correct all the doctests which currently give answers which are off by a factor of 2.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8304\n\n",
    "created_at": "2010-02-19T02:56:02Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "Remove stray factors of 2 in Coleman integration",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8304",
    "user": "kedlaya"
}
```
Assignee: was

CC:  jen robertwb

Keywords: Coleman integration, hyperelliptic curves

Jen discovered some stray factors of 2 buried in the Coleman integration code. (Apply patches at #7927 before trying these examples.)

On one hand, the invariant differential sometimes thinks it's dx/2y (as it should):

```
sage: R.<x> = QQ['x']
sage: H = HyperellipticCurve(x^3+1)
sage: K = Qp(5,8)
sage: HK = H.change_ring(K)
sage: w = HK.invariant_differential()
sage: P = HK(0,1)
sage: Q = HK.lift_x(5)
sage: x,y = HK.monsky_washnitzer_gens()
sage: (2*y*w).coleman_integral(P,Q)
5 + O(5^9)
```

but on the other hand, it sometimes behaves as if it were dx/y (as it shouldn't):

```
sage: x,y,z = HK.local_analytic_interpolation(P,Q)
sage: I1 = (x.derivative()/y).integral()
sage: I2 = (x.derivative()/(2*y)).integral()
sage: I1(1)-I1(0)
5 + 3*5^4 + 3*5^6 + 3*5^7 + O(5^9)
sage: I2(1)-I2(0)
3*5 + 2*5^2 + 2*5^3 + 5^4 + 4*5^6 + 5^7 + O(5^9)
sage: HK.coleman_integral(w,P,Q)
5 + 3*5^4 + 3*5^6 + 3*5^7 + O(5^9)
```

The apparent fix is to insert an extra division by two in tiny_integrals (which then needs a corrected docstring and some doctests, and similarly for tiny_integrals_on_basis) and then remove the multiplication by 2 in coleman_integrals_on_basis. Then correct all the doctests which currently give answers which are off by a factor of 2.

Issue created by migration from https://trac.sagemath.org/ticket/8304





---

archive/issue_comments_073577.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-19T20:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8304#issuecomment-73577",
    "user": "jen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073578.json:
```json
{
    "body": "Attachment\n\nThe attached patch should fix these issues (+doctests), so that invariant differential always behaves as dx/2y:\n\n\n```\nsage: R.<x> = QQ['x']\nsage: H = HyperellipticCurve(x^3+1)\nsage: K = Qp(5,8)\nsage: HK = H.change_ring(K)\nsage: w = HK.invariant_differential()\nsage: P = HK(0,1)\nsage: Q = HK.lift_x(5)\nsage: x,y = HK.monsky_washnitzer_gens()\nsage: (2*y*w).coleman_integral(P,Q)\n5 + O(5^9)\nsage: x,y,z = HK.local_analytic_interpolation(P,Q)\nsage: I2 = (x.derivative()/(2*y)).integral()\nsage: I2(1)-I2(0)\n3*5 + 2*5^2 + 2*5^3 + 5^4 + 4*5^6 + 5^7 + O(5^9)\nsage: HK.coleman_integral(w,P,Q)\n3*5 + 2*5^2 + 2*5^3 + 5^4 + 4*5^6 + 5^7 + O(5^9)\n```\n",
    "created_at": "2010-02-19T20:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8304#issuecomment-73578",
    "user": "jen"
}
```

Attachment

The attached patch should fix these issues (+doctests), so that invariant differential always behaves as dx/2y:


```
sage: R.<x> = QQ['x']
sage: H = HyperellipticCurve(x^3+1)
sage: K = Qp(5,8)
sage: HK = H.change_ring(K)
sage: w = HK.invariant_differential()
sage: P = HK(0,1)
sage: Q = HK.lift_x(5)
sage: x,y = HK.monsky_washnitzer_gens()
sage: (2*y*w).coleman_integral(P,Q)
5 + O(5^9)
sage: x,y,z = HK.local_analytic_interpolation(P,Q)
sage: I2 = (x.derivative()/(2*y)).integral()
sage: I2(1)-I2(0)
3*5 + 2*5^2 + 2*5^3 + 5^4 + 4*5^6 + 5^7 + O(5^9)
sage: HK.coleman_integral(w,P,Q)
3*5 + 2*5^2 + 2*5^3 + 5^4 + 4*5^6 + 5^7 + O(5^9)
```




---

archive/issue_comments_073579.json:
```json
{
    "body": "Attachment\n\nadded doctests for tiny_integrals",
    "created_at": "2010-02-20T05:29:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8304#issuecomment-73579",
    "user": "jen"
}
```

Attachment

added doctests for tiny_integrals



---

archive/issue_comments_073580.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-20T14:53:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8304#issuecomment-73580",
    "user": "kedlaya"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073581.json:
```json
{
    "body": "Looks good, passes long doctests in sage/schemes/ (after applying patches at #7927). Positive review.",
    "created_at": "2010-02-20T14:53:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8304#issuecomment-73581",
    "user": "kedlaya"
}
```

Looks good, passes long doctests in sage/schemes/ (after applying patches at #7927). Positive review.



---

archive/issue_comments_073582.json:
```json
{
    "body": "Merged in this order:\n\n1. [13542.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8304/13542.patch)\n2. [13543.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8304/13543.patch)",
    "created_at": "2010-03-03T15:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8304#issuecomment-73582",
    "user": "mvngu"
}
```

Merged in this order:

1. [13542.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8304/13542.patch)
2. [13543.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8304/13543.patch)



---

archive/issue_comments_073583.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-03T15:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8304#issuecomment-73583",
    "user": "mvngu"
}
```

Resolution: fixed
