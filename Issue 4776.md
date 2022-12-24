# Issue 4776: random element of multivariate polynomial ring in one variable is totally broken

archive/issues_004776.json:
```json
{
    "body": "Assignee: malb\n\n\n```\nsage: R.<x> = PolynomialRing(Integers(3), 1)\nsage: R.random_element()\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/Users/wstein/sage/build/sage-3.2.2.alpha0/devel/sage-main/sage/rings/<ipython console> in <module>()\n\n/Users/wstein/sage/build/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ring_generic.so in sage.rings.polynomial.multi_polynomial_ring_generic.MPolynomialRing_generic.random_element (sage/rings/polynomial/multi_polynomial_ring_generic.c:7404)()\n\nTypeError: Cannot compute polynomial with more terms than exist.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4776\n\n",
    "created_at": "2008-12-13T02:07:22Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.3",
    "title": "random element of multivariate polynomial ring in one variable is totally broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4776",
    "user": "was"
}
```
Assignee: malb


```
sage: R.<x> = PolynomialRing(Integers(3), 1)
sage: R.random_element()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/wstein/sage/build/sage-3.2.2.alpha0/devel/sage-main/sage/rings/<ipython console> in <module>()

/Users/wstein/sage/build/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ring_generic.so in sage.rings.polynomial.multi_polynomial_ring_generic.MPolynomialRing_generic.random_element (sage/rings/polynomial/multi_polynomial_ring_generic.c:7404)()

TypeError: Cannot compute polynomial with more terms than exist.
```


Issue created by migration from https://trac.sagemath.org/ticket/4776





---

archive/issue_comments_036196.json:
```json
{
    "body": "Attachment [mpoly_random_element.patch](tarball://root/attachments/some-uuid/ticket4776/mpoly_random_element.patch) by malb created at 2008-12-13 15:31:30",
    "created_at": "2008-12-13T15:31:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4776#issuecomment-36196",
    "user": "malb"
}
```

Attachment [mpoly_random_element.patch](tarball://root/attachments/some-uuid/ticket4776/mpoly_random_element.patch) by malb created at 2008-12-13 15:31:30



---

archive/issue_comments_036197.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-12-20T17:01:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4776#issuecomment-36197",
    "user": "AlexGhitza"
}
```

Looks good to me.



---

archive/issue_comments_036198.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-21T12:37:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4776#issuecomment-36198",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036199.json:
```json
{
    "body": "Merged in Sage 3.2.3.alpha0",
    "created_at": "2008-12-21T12:37:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4776#issuecomment-36199",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.3.alpha0
