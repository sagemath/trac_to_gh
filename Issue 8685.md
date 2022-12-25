# Issue 8685: evaluation of Monsky-Washnitzer objects

archive/issues_008685.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @robertwb @kedlaya @roed314 jpflori\n\nThe following should raise an error since f0 has a singularity at P  (and isn't necessarily 0 at all finite Weierstrass points):\n\n```\nsage: R.<x> = QQ['x']\nsage: H= HyperellipticCurve(x^3-10*x+9)\nsage: K = Qp(5,10)\nsage: HK = H.change_ring(K)\nsage: P = HK(1,0)\nsage: import sage.schemes.elliptic_curves.monsky_washnitzer as mw\nsage: Mfrob,forms=mw.matrix_of_frobenius_hyperelliptic(HK)\nsage: f0 = forms[0]\nsage: f0(P[0],P[1])\n0\nsage: f0(x,K(0))\n0\n\n```\n\nIn fact, Sage seems to knows this...just not when the y-coordinate is 0 in the p-adic field. So, a coercion error?\n\n```\nsage: f0(x,0)\n---------------------------------------------------------------------------\nZeroDivisionError                         Traceback (most recent call last)\n\nZeroDivisionError: Rational division by zero\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8685\n\n",
    "created_at": "2010-04-14T06:20:29Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "evaluation of Monsky-Washnitzer objects",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8685",
    "user": "https://github.com/jbalakrishnan"
}
```
Assignee: @williamstein

CC:  @robertwb @kedlaya @roed314 jpflori

The following should raise an error since f0 has a singularity at P  (and isn't necessarily 0 at all finite Weierstrass points):

```
sage: R.<x> = QQ['x']
sage: H= HyperellipticCurve(x^3-10*x+9)
sage: K = Qp(5,10)
sage: HK = H.change_ring(K)
sage: P = HK(1,0)
sage: import sage.schemes.elliptic_curves.monsky_washnitzer as mw
sage: Mfrob,forms=mw.matrix_of_frobenius_hyperelliptic(HK)
sage: f0 = forms[0]
sage: f0(P[0],P[1])
0
sage: f0(x,K(0))
0

```

In fact, Sage seems to knows this...just not when the y-coordinate is 0 in the p-adic field. So, a coercion error?

```
sage: f0(x,0)
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)

ZeroDivisionError: Rational division by zero
```



Issue created by migration from https://trac.sagemath.org/ticket/8685





---

archive/issue_comments_079012.json:
```json
{
    "body": "This appears to be a problem with (surprise) power series over p-adic fields:\n\n```\nsage: R.<y> = LaurentSeriesRing(Rationals())\nsage: K = Qp(5, 10)\nsage: u = y^(-1)\nsage: u(K(0)) ## Should blow up but doesn't\n0\nsage: u(0) ## Should blow up and does\n---------------------------------------------------------------------------\nZeroDivisionError                         Traceback (most recent call last)\n\nZeroDivisionError: Rational division by zero\n```\n",
    "created_at": "2010-04-15T20:27:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8685#issuecomment-79012",
    "user": "https://github.com/kedlaya"
}
```

This appears to be a problem with (surprise) power series over p-adic fields:

```
sage: R.<y> = LaurentSeriesRing(Rationals())
sage: K = Qp(5, 10)
sage: u = y^(-1)
sage: u(K(0)) ## Should blow up but doesn't
0
sage: u(0) ## Should blow up and does
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)

ZeroDivisionError: Rational division by zero
```




---

archive/issue_comments_079013.json:
```json
{
    "body": "I just tried the test cases and (modulo the fact that monsky_washnitzer moved to hyperelliptic_curves) they no longer return the claimed errors. Probably this is due to some bug in p-adic power series getting fixed (perhaps #9457).\n\nIn light of that, I propose to resolve this ticket as \"fixed\".",
    "created_at": "2016-03-23T22:40:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8685#issuecomment-79013",
    "user": "https://github.com/kedlaya"
}
```

I just tried the test cases and (modulo the fact that monsky_washnitzer moved to hyperelliptic_curves) they no longer return the claimed errors. Probably this is due to some bug in p-adic power series getting fixed (perhaps #9457).

In light of that, I propose to resolve this ticket as "fixed".



---

archive/issue_comments_079014.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-03-24T20:50:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8685#issuecomment-79014",
    "user": "https://github.com/roed314"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079015.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-03-24T20:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8685#issuecomment-79015",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079016.json:
```json
{
    "body": "Works for me.",
    "created_at": "2016-03-24T20:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8685#issuecomment-79016",
    "user": "https://github.com/roed314"
}
```

Works for me.



---

archive/issue_comments_079017.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2016-03-26T12:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8685#issuecomment-79017",
    "user": "https://github.com/vbraun"
}
```

Resolution: worksforme



---

archive/issue_events_008859.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2016-03-26T12:02:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8685",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8685#event-8859"
}
```



---

archive/issue_comments_079018.json:
```json
{
    "body": "Changing keywords from \"\" to \"days71\".",
    "created_at": "2016-03-26T12:47:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8685#issuecomment-79018",
    "user": "https://github.com/jbalakrishnan"
}
```

Changing keywords from "" to "days71".
