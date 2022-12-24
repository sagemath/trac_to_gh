# Issue 5795: Improved performance of MPolynomialRing_libsingular.__call__()

archive/issues_005795.json:
```json
{
    "body": "Assignee: @simon-king-jena\n\nCC:  @malb\n\nKeywords: MPolynomialRing_libsingular, coercion, call\n\nOne comment in the `__call__()` method of MPolynomialRing_libsingular states:\n #TODO: We can do this faster without the dict\n\nIn fact, we can!\n\nWithout the patch, we have the following timings on sage.math:\n\n```\nsage: R=PolynomialRing(QQ,5,'x')\nsage: S=PolynomialRing(QQ,6,'x')\nsage: T=PolynomialRing(QQ,5,'y')\nsage: U=PolynomialRing(GF(2),5,'x')\nsage: p=R('x0*x1+2*x4+x3*x1^2')^4\nsage: timeit('q=S(p)')\n625 loops, best of 3: 341 \u00c2\u00b5s per loop\nsage: timeit('q=T(p)')\n625 loops, best of 3: 370 \u00c2\u00b5s per loop\nsage: timeit('q=U(p)')\n625 loops, best of 3: 451 \u00c2\u00b5s per loop\n```\n\n\nWith the patch, we have\n\n```\nsage: timeit('q=S(p)')\n625 loops, best of 3: 328 \u00c2\u00b5s per loop\nsage: timeit('q=T(p)')\n625 loops, best of 3: 292 \u00c2\u00b5s per loop\nsage: timeit('q=U(p)')\n625 loops, best of 3: 396 \u00c2\u00b5s per loop\n```\n\nSo, the improvement is small, but it *is* an improvement.\n\nBackground: \n In the original version, if the input of `__call__` is MPolynomial_libsingular, then the `dict()` method of this polynomial was called in order to get the coefficients and exponent vectors. \n \n In the new version, the underlying libsingular methods are called directly, which is faster. The price to pay is that currRing changes more often. I hope change of currRing is not too expensive (in my examples above, apparently it isn't).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5795\n\n",
    "created_at": "2009-04-16T02:50:47Z",
    "labels": [
        "commutative algebra",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "Improved performance of MPolynomialRing_libsingular.__call__()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5795",
    "user": "@simon-king-jena"
}
```
Assignee: @simon-king-jena

CC:  @malb

Keywords: MPolynomialRing_libsingular, coercion, call

One comment in the `__call__()` method of MPolynomialRing_libsingular states:
 #TODO: We can do this faster without the dict

In fact, we can!

Without the patch, we have the following timings on sage.math:

```
sage: R=PolynomialRing(QQ,5,'x')
sage: S=PolynomialRing(QQ,6,'x')
sage: T=PolynomialRing(QQ,5,'y')
sage: U=PolynomialRing(GF(2),5,'x')
sage: p=R('x0*x1+2*x4+x3*x1^2')^4
sage: timeit('q=S(p)')
625 loops, best of 3: 341 Âµs per loop
sage: timeit('q=T(p)')
625 loops, best of 3: 370 Âµs per loop
sage: timeit('q=U(p)')
625 loops, best of 3: 451 Âµs per loop
```


With the patch, we have

```
sage: timeit('q=S(p)')
625 loops, best of 3: 328 Âµs per loop
sage: timeit('q=T(p)')
625 loops, best of 3: 292 Âµs per loop
sage: timeit('q=U(p)')
625 loops, best of 3: 396 Âµs per loop
```

So, the improvement is small, but it *is* an improvement.

Background: 
 In the original version, if the input of `__call__` is MPolynomial_libsingular, then the `dict()` method of this polynomial was called in order to get the coefficients and exponent vectors. 
 
 In the new version, the underlying libsingular methods are called directly, which is faster. The price to pay is that currRing changes more often. I hope change of currRing is not too expensive (in my examples above, apparently it isn't).


Issue created by migration from https://trac.sagemath.org/ticket/5795





---

archive/issue_comments_045443.json:
```json
{
    "body": "Attachment [MPolyRingCall.patch](tarball://root/attachments/some-uuid/ticket5795/MPolyRingCall.patch) by @simon-king-jena created at 2009-04-16 02:51:35\n\nImproved performance for polynomial conversion",
    "created_at": "2009-04-16T02:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5795#issuecomment-45443",
    "user": "@simon-king-jena"
}
```

Attachment [MPolyRingCall.patch](tarball://root/attachments/some-uuid/ticket5795/MPolyRingCall.patch) by @simon-king-jena created at 2009-04-16 02:51:35

Improved performance for polynomial conversion



---

archive/issue_comments_045444.json:
```json
{
    "body": "Hi Simon, are you sure that you need all the rChangeCurrRing() business? All functions you are calling *should* be safe without it. This might save a few cycles.\n\nBtw. you improved \"conversion\" not \"coercion\". IIRC this is how we call stuff happening in `__call__`.\n\nOther than that the patch looks goog, which version shall I apply the patch agains?",
    "created_at": "2009-04-16T08:51:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5795#issuecomment-45444",
    "user": "@malb"
}
```

Hi Simon, are you sure that you need all the rChangeCurrRing() business? All functions you are calling *should* be safe without it. This might save a few cycles.

Btw. you improved "conversion" not "coercion". IIRC this is how we call stuff happening in `__call__`.

Other than that the patch looks goog, which version shall I apply the patch agains?



---

archive/issue_comments_045445.json:
```json
{
    "body": "Replying to [comment:2 malb]:\n> Hi Simon, are you sure that you need all the rChangeCurrRing() business? All functions you are calling *should* be safe without it. This might save a few cycles.\n\nFirst, I tried it without. But then there was a problem when converting a polynomial over QQ into a polynomial over GF(2) (or the other way around, I don't remember). I found that the line\n\n```\nc = co.si2sa(p_GetCoeff(_element, El_ring), El_ring, El_base) \n```\n\ndid not work properly (always returning zero when it should return 1). \n\nThen, in 'coefficients()', I found that 'rChangeCurrRing()' is used. I thought that it might be for a reason, and indeed the conversion works if 'El_ring' is 'currRing'.\n\nBut I do agree that it would be nice if it were possible to avoid the ring change.\n \n> Btw. you improved \"conversion\" not \"coercion\". IIRC this is how we call stuff happening in `__call__`.\n\nOk, I changed the key word...\n\n> Other than that the patch looks goog, which version shall I apply the patch agains?\n\n3.4.1.rc3\n\nCheers,\n     Simon",
    "created_at": "2009-04-16T11:52:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5795#issuecomment-45445",
    "user": "@simon-king-jena"
}
```

Replying to [comment:2 malb]:
> Hi Simon, are you sure that you need all the rChangeCurrRing() business? All functions you are calling *should* be safe without it. This might save a few cycles.

First, I tried it without. But then there was a problem when converting a polynomial over QQ into a polynomial over GF(2) (or the other way around, I don't remember). I found that the line

```
c = co.si2sa(p_GetCoeff(_element, El_ring), El_ring, El_base) 
```

did not work properly (always returning zero when it should return 1). 

Then, in 'coefficients()', I found that 'rChangeCurrRing()' is used. I thought that it might be for a reason, and indeed the conversion works if 'El_ring' is 'currRing'.

But I do agree that it would be nice if it were possible to avoid the ring change.
 
> Btw. you improved "conversion" not "coercion". IIRC this is how we call stuff happening in `__call__`.

Ok, I changed the key word...

> Other than that the patch looks goog, which version shall I apply the patch agains?

3.4.1.rc3

Cheers,
     Simon



---

archive/issue_comments_045446.json:
```json
{
    "body": "Replying to [comment:3 SimonKing]:\n> Replying to [comment:2 malb]:\n> > Other than that the patch looks goog, which version shall I apply the patch agains?\n> \n> 3.4.1.rc3\n\nOoops, it should be 3.4.1.rc2, I think.",
    "created_at": "2009-04-16T14:19:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5795#issuecomment-45446",
    "user": "@simon-king-jena"
}
```

Replying to [comment:3 SimonKing]:
> Replying to [comment:2 malb]:
> > Other than that the patch looks goog, which version shall I apply the patch agains?
> 
> 3.4.1.rc3

Ooops, it should be 3.4.1.rc2, I think.



---

archive/issue_comments_045447.json:
```json
{
    "body": "Doctests pass, good to go.",
    "created_at": "2009-04-17T11:48:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5795#issuecomment-45447",
    "user": "@malb"
}
```

Doctests pass, good to go.



---

archive/issue_comments_045448.json:
```json
{
    "body": "Merged in Sage 3.4.2.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-22T18:48:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5795#issuecomment-45448",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael



---

archive/issue_comments_045449.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-22T18:48:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5795#issuecomment-45449",
    "user": "mabshoff"
}
```

Resolution: fixed
