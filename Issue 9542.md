# Issue 9542: optimize znpoly arithmetic -- it's way, way too slow because of the polynomial template thingy

archive/issues_009542.json:
```json
{
    "body": "Assignee: @aghitza\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9542\n\n",
    "created_at": "2010-07-18T19:18:03Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.2",
    "title": "optimize znpoly arithmetic -- it's way, way too slow because of the polynomial template thingy",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9542",
    "user": "@williamstein"
}
```
Assignee: @aghitza



Issue created by migration from https://trac.sagemath.org/ticket/9542





---

archive/issue_comments_091949.json:
```json
{
    "body": "Attachment [trac_9542-znpoly_timing.patch](tarball://root/attachments/some-uuid/ticket9542/trac_9542-znpoly_timing.patch) by @williamstein created at 2010-07-18 19:20:10\n\nspeeds up multiplication by a factor of *20* for many benchmarks... but causes a segfault when doctesting rings/arith.py",
    "created_at": "2010-07-18T19:20:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9542#issuecomment-91949",
    "user": "@williamstein"
}
```

Attachment [trac_9542-znpoly_timing.patch](tarball://root/attachments/some-uuid/ticket9542/trac_9542-znpoly_timing.patch) by @williamstein created at 2010-07-18 19:20:10

speeds up multiplication by a factor of *20* for many benchmarks... but causes a segfault when doctesting rings/arith.py



---

archive/issue_comments_091950.json:
```json
{
    "body": "Maybe this can be closed now...\nI'll run basic test laters.",
    "created_at": "2014-02-26T21:53:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9542#issuecomment-91950",
    "user": "jpflori"
}
```

Maybe this can be closed now...
I'll run basic test laters.



---

archive/issue_comments_091951.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-02-26T23:30:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9542#issuecomment-91951",
    "user": "jpflori"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091952.json:
```json
{
    "body": "Based on the same idea (`_mul_no_template_`):\n\n```\nsage: K = Integers(2**6)\nsage: R.<x> = K[]\nsage: f = R([1,2,5,-9]); g = R([1,2,3,4])\nsage: %timeit f._mul_zn_poly(g)\n100000 loops, best of 3: 5.32 us per loop\nsage: %timeit f._mul_(g)\n1000000 loops, best of 3: 1 us per loop\nsage: %timeit f._mul_no_template(g)\n1000000 loops, best of 3: 790 ns per loop\nsage: %timeit f*g\n1000000 loops, best of 3: 845 ns per loop\n```\n\nSo it seems the templating overhead is not so terrible.\nIt also varies a little bit depending on the finite field.\nAnd it does not seem the templating code can be really trimmed down and further optimized.\n\nSo I suggest to close this ticket as won't fix.",
    "created_at": "2014-02-26T23:30:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9542#issuecomment-91952",
    "user": "jpflori"
}
```

Based on the same idea (`_mul_no_template_`):

```
sage: K = Integers(2**6)
sage: R.<x> = K[]
sage: f = R([1,2,5,-9]); g = R([1,2,3,4])
sage: %timeit f._mul_zn_poly(g)
100000 loops, best of 3: 5.32 us per loop
sage: %timeit f._mul_(g)
1000000 loops, best of 3: 1 us per loop
sage: %timeit f._mul_no_template(g)
1000000 loops, best of 3: 790 ns per loop
sage: %timeit f*g
1000000 loops, best of 3: 845 ns per loop
```

So it seems the templating overhead is not so terrible.
It also varies a little bit depending on the finite field.
And it does not seem the templating code can be really trimmed down and further optimized.

So I suggest to close this ticket as won't fix.



---

archive/issue_comments_091953.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-02-26T23:30:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9542#issuecomment-91953",
    "user": "jpflori"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091954.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2014-02-27T22:11:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9542#issuecomment-91954",
    "user": "@vbraun"
}
```

Resolution: wontfix
