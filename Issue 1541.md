# Issue 1541: [with patch] improve PolyBoRi integration

archive/issues_001541.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @burcin\n\nThe attached patch provides:\n* `mq.SR` can now construct PolyBoRi polynomial systems \n* some comments added to `pbori.pyx`\n* `BooleanPolynomial.__hash__`\n* `BooleanPolynomial.variables`\n* coercion of GF(2) elements to `BooleanPolynomialRing`\n* `BooleanPolynomialRing.__call__` accepts strings\n* `_sig_on`/`_sig_off` around `groebner_basis` call\n\nIssue created by migration from https://trac.sagemath.org/ticket/1541\n\n",
    "created_at": "2007-12-16T21:38:51Z",
    "labels": [
        "commutative algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "[with patch] improve PolyBoRi integration",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1541",
    "user": "@malb"
}
```
Assignee: @malb

CC:  @burcin

The attached patch provides:
* `mq.SR` can now construct PolyBoRi polynomial systems 
* some comments added to `pbori.pyx`
* `BooleanPolynomial.__hash__`
* `BooleanPolynomial.variables`
* coercion of GF(2) elements to `BooleanPolynomialRing`
* `BooleanPolynomialRing.__call__` accepts strings
* `_sig_on`/`_sig_off` around `groebner_basis` call

Issue created by migration from https://trac.sagemath.org/ticket/1541





---

archive/issue_comments_009835.json:
```json
{
    "body": "On sage.math, applied to alpha2:\n\n```\nsage -t  devel/sage-main/sage/crypto/mq/sr.py               sh: line 1: 31648 Segmentation fault      /home/rlmill/release/sage-2.9.1.alpha3/local/bin/python .doctest_sr.py >.doctest/out 2>.doctest/err\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n```\n",
    "created_at": "2007-12-21T22:24:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1541#issuecomment-9835",
    "user": "@rlmill"
}
```

On sage.math, applied to alpha2:

```
sage -t  devel/sage-main/sage/crypto/mq/sr.py               sh: line 1: 31648 Segmentation fault      /home/rlmill/release/sage-2.9.1.alpha3/local/bin/python .doctest_sr.py >.doctest/out 2>.doctest/err

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.
```




---

archive/issue_comments_009836.json:
```json
{
    "body": "results of \n`./sage -t -valgrind devel/sage-main/sage/crypto/mq/sr.py`\nare at\nhttp://sage.math.washington.edu/home/rlmill/.sage/sage-memcheck.850",
    "created_at": "2007-12-21T23:20:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1541#issuecomment-9836",
    "user": "@rlmill"
}
```

results of 
`./sage -t -valgrind devel/sage-main/sage/crypto/mq/sr.py`
are at
http://sage.math.washington.edu/home/rlmill/.sage/sage-memcheck.850



---

archive/issue_comments_009837.json:
```json
{
    "body": "Disregard those valgrind results- they are useless.",
    "created_at": "2007-12-22T00:50:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1541#issuecomment-9837",
    "user": "@rlmill"
}
```

Disregard those valgrind results- they are useless.



---

archive/issue_comments_009838.json:
```json
{
    "body": "I think the negative review has been resolved, and the currRing patch attached to this ticket should be applied (given a positive review) soon.",
    "created_at": "2007-12-25T15:57:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1541#issuecomment-9838",
    "user": "@malb"
}
```

I think the negative review has been resolved, and the currRing patch attached to this ticket should be applied (given a positive review) soon.



---

archive/issue_comments_009839.json:
```json
{
    "body": "Make the methods of BooleanPolynomial in __getattr__ directly available.",
    "created_at": "2007-12-27T13:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1541#issuecomment-9839",
    "user": "@burcin"
}
```

Make the methods of BooleanPolynomial in __getattr__ directly available.



---

archive/issue_comments_009840.json:
```json
{
    "body": "Attachment [polybori_booleanpolynomial_getattr.patch](tarball://root/attachments/some-uuid/ticket1541/polybori_booleanpolynomial_getattr.patch) by @burcin created at 2007-12-27 13:52:29\n\nFollowing Martin's comments on the slowdown caused by using `__getattr__` in `BooleanPolynomial`, attached patch with file name `polybori_booleanpolynomial_getattr.patch` makes the methods directly available.\n\nSome timings (using random polynomials in each case might not be a good idea, but it still demonstrates the point):\n\nWithout the patch:\n\n\n```\nsage: P = BooleanPolynomialRing(100,'x')\nsage: from polybori.randompoly import gen_random_poly\nsage: p = gen_random_poly(int(100))\nsage: %timeit s = p.set()\n100000 loops, best of 3: 2.85 \u00b5s per loop\nsage: %timeit d = p.deg()\n100000 loops, best of 3: 2.26 \u00b5s per loop\nsage: %timeit m = p.lead()\n100000 loops, best of 3: 6.7 \u00b5s per loop\nsage: %timeit n = p.navigation()\n100000 loops, best of 3: 2.82 \u00b5s per loop\nsage: %timeit c = p.constant()\n100000 loops, best of 3: 2.02 \u00b5s per loop\n```\n\n\nWith the patch:\n\n\n```\nsage: %timeit s = p.set()\n1000000 loops, best of 3: 540 ns per loop\nsage: %timeit d = p.deg()\n1000000 loops, best of 3: 382 ns per loop\nsage: %timeit m = p.lead()\n100000 loops, best of 3: 3.76 \u00b5s per loop\nsage: %timeit n = p.navigation()\n1000000 loops, best of 3: 453 ns per loop\nsage: %timeit c = p.constant()\n1000000 loops, best of 3: 305 ns per loop\n```\n",
    "created_at": "2007-12-27T13:52:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1541#issuecomment-9840",
    "user": "@burcin"
}
```

Attachment [polybori_booleanpolynomial_getattr.patch](tarball://root/attachments/some-uuid/ticket1541/polybori_booleanpolynomial_getattr.patch) by @burcin created at 2007-12-27 13:52:29

Following Martin's comments on the slowdown caused by using `__getattr__` in `BooleanPolynomial`, attached patch with file name `polybori_booleanpolynomial_getattr.patch` makes the methods directly available.

Some timings (using random polynomials in each case might not be a good idea, but it still demonstrates the point):

Without the patch:


```
sage: P = BooleanPolynomialRing(100,'x')
sage: from polybori.randompoly import gen_random_poly
sage: p = gen_random_poly(int(100))
sage: %timeit s = p.set()
100000 loops, best of 3: 2.85 µs per loop
sage: %timeit d = p.deg()
100000 loops, best of 3: 2.26 µs per loop
sage: %timeit m = p.lead()
100000 loops, best of 3: 6.7 µs per loop
sage: %timeit n = p.navigation()
100000 loops, best of 3: 2.82 µs per loop
sage: %timeit c = p.constant()
100000 loops, best of 3: 2.02 µs per loop
```


With the patch:


```
sage: %timeit s = p.set()
1000000 loops, best of 3: 540 ns per loop
sage: %timeit d = p.deg()
1000000 loops, best of 3: 382 ns per loop
sage: %timeit m = p.lead()
100000 loops, best of 3: 3.76 µs per loop
sage: %timeit n = p.navigation()
1000000 loops, best of 3: 453 ns per loop
sage: %timeit c = p.constant()
1000000 loops, best of 3: 305 ns per loop
```




---

archive/issue_comments_009841.json:
```json
{
    "body": "attachment:polybori-coercion.patch provides coercion enhancements and small fixes to `pbori.pyx`. It should be applied after attachment:polybori_booleanpolynomial_getattr.patch.\n\nThis patch adds coercion from `ZZ`, and `GF(2)` to `BooleanPolynomialRing`, so Martin's patch needs to be revised.",
    "created_at": "2007-12-30T16:09:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1541#issuecomment-9841",
    "user": "@burcin"
}
```

attachment:polybori-coercion.patch provides coercion enhancements and small fixes to `pbori.pyx`. It should be applied after attachment:polybori_booleanpolynomial_getattr.patch.

This patch adds coercion from `ZZ`, and `GF(2)` to `BooleanPolynomialRing`, so Martin's patch needs to be revised.



---

archive/issue_comments_009842.json:
```json
{
    "body": "attachment:polybori-coercion.patch is now ticket #1667.",
    "created_at": "2008-01-03T15:05:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1541#issuecomment-9842",
    "user": "@burcin"
}
```

attachment:polybori-coercion.patch is now ticket #1667.



---

archive/issue_comments_009843.json:
```json
{
    "body": "Replying to [comment:6 burcin]:\n> This patch adds coercion from `ZZ`, and `GF(2)` to `BooleanPolynomialRing`, so Martin's patch needs to be revised.\n\nIn the sense that the comments are outdated?",
    "created_at": "2008-01-06T13:20:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1541#issuecomment-9843",
    "user": "@malb"
}
```

Replying to [comment:6 burcin]:
> This patch adds coercion from `ZZ`, and `GF(2)` to `BooleanPolynomialRing`, so Martin's patch needs to be revised.

In the sense that the comments are outdated?



---

archive/issue_comments_009844.json:
```json
{
    "body": "The `currRing.patch` is now #1701 because it doesn't logically belong here.",
    "created_at": "2008-01-06T13:23:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1541#issuecomment-9844",
    "user": "@malb"
}
```

The `currRing.patch` is now #1701 because it doesn't logically belong here.



---

archive/issue_comments_009845.json:
```json
{
    "body": "Deleted original patch, just use burcin's getattr patch.",
    "created_at": "2008-01-07T15:40:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1541#issuecomment-9845",
    "user": "@malb"
}
```

Deleted original patch, just use burcin's getattr patch.



---

archive/issue_comments_009846.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-07T17:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1541#issuecomment-9846",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009847.json:
```json
{
    "body": "Merged in Sage 2.10.alpha0. \n\nCaution: when patching the offset was very large: `Hunk #1 succeeded at 1372 (offset 284 lines).` I did verify that indeed the section was moved that far down in the current sources.  \n\nCheers,\n\nMichael",
    "created_at": "2008-01-07T17:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1541#issuecomment-9847",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.alpha0. 

Caution: when patching the offset was very large: `Hunk #1 succeeded at 1372 (offset 284 lines).` I did verify that indeed the section was moved that far down in the current sources.  

Cheers,

Michael
