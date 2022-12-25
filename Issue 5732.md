# Issue 5732: [with patch, positive review] digits,exact_log,ndigits speed overhaul

archive/issues_005732.json:
```json
{
    "body": "Assignee: somebody\n\nThe Integer.exact_log method is very slow for small input simply because it has never been optimized for this usage.  The attached patch provides a specialized case for small input to exact log.  It also adds a super-fast path for cases when the exact_log can conveniently be computed by log 2 estimation.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5732\n\n",
    "closed_at": "2009-06-03T20:19:32Z",
    "created_at": "2009-04-10T09:55:10Z",
    "labels": [
        "component: basic arithmetic"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "[with patch, positive review] digits,exact_log,ndigits speed overhaul",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5732",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```
Assignee: somebody

The Integer.exact_log method is very slow for small input simply because it has never been optimized for this usage.  The attached patch provides a specialized case for small input to exact log.  It also adds a super-fast path for cases when the exact_log can conveniently be computed by log 2 estimation.

Issue created by migration from https://trac.sagemath.org/ticket/5732





---

archive/issue_comments_044708.json:
```json
{
    "body": "Some timings:\n\n```\nnew patch\nsage: n=5^1000\nsage: m=2975982357823879528793587928793592\nsage: timeit(\"n.exact_log(m)\")\n625 loops, best of 3: 714 ns per loop\nsage: n=5^50\nsage: m=33\nsage: timeit(\"n.exact_log(m)\")\n625 loops, best of 3: 2.49 \u00c2\u00b5s per loop\n```\n\n```\nVanilla sage 3.4\nsage: n=5^1000\nsage: m=2975982357823879528793587928793592\nsage: timeit(\"n.exact_log(m)\")\n625 loops, best of 3: 620 \u00c2\u00b5s per loop\nsage: n=5^50\nsage: m=33\nsage: timeit(\"n.exact_log(m)\")\n625 loops, best of 3: 92.2 \u00c2\u00b5s per loop\n```\n\nI really like the first example :), but it's a bit of a pathology.  There's a relatively narrow band of cases where the log base 2 estimate is quickly provable and exactly correct.",
    "created_at": "2009-04-10T10:07:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5732#issuecomment-44708",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Some timings:

```
new patch
sage: n=5^1000
sage: m=2975982357823879528793587928793592
sage: timeit("n.exact_log(m)")
625 loops, best of 3: 714 ns per loop
sage: n=5^50
sage: m=33
sage: timeit("n.exact_log(m)")
625 loops, best of 3: 2.49 Âµs per loop
```

```
Vanilla sage 3.4
sage: n=5^1000
sage: m=2975982357823879528793587928793592
sage: timeit("n.exact_log(m)")
625 loops, best of 3: 620 Âµs per loop
sage: n=5^50
sage: m=33
sage: timeit("n.exact_log(m)")
625 loops, best of 3: 92.2 Âµs per loop
```

I really like the first example :), but it's a bit of a pathology.  There's a relatively narrow band of cases where the log base 2 estimate is quickly provable and exactly correct.



---

archive/issue_events_013456.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-11T00:32:26Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5732",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5732#event-13456"
}
```



---

archive/issue_comments_044709.json:
```json
{
    "body": "This is quote a nice speedup, but unless it gets reviewed soon it will not be in 3.4.1. Since I do not consider this a blocker I am reassigning this to 3.4.2 until it gets a review.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-11T00:32:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5732#issuecomment-44709",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is quote a nice speedup, but unless it gets reviewed soon it will not be in 3.4.1. Since I do not consider this a blocker I am reassigning this to 3.4.2 until it gets a review.

Cheers,

Michael



---

archive/issue_comments_044710.json:
```json
{
    "body": "Attachment [digits_exact_log_comprehensive.patch](tarball://root/attachments/some-uuid/ticket5732/digits_exact_log_comprehensive.patch) by jbmohler created at 2009-06-01 17:24:06\n\nrebased against 4.0",
    "created_at": "2009-06-01T17:24:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5732#issuecomment-44710",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Attachment [digits_exact_log_comprehensive.patch](tarball://root/attachments/some-uuid/ticket5732/digits_exact_log_comprehensive.patch) by jbmohler created at 2009-06-01 17:24:06

rebased against 4.0



---

archive/issue_comments_044711.json:
```json
{
    "body": "I've tested the code using:\n\n```\ndef random(n):\n    a = ZZ.random_element(n)\n    return a\n\ndef z_exact_log_test(m, n, k):\n    for i in range(0, m) :\n        a = random(n) + 2\n        b = random(k)\n        c = a^b\n        d = c.exact_log(a)\n        if b != d:\n            print \"Error\", b, \"!=\", d\n```\n\nfor all sorts of values m, n, k, small large, etc. Everything passes.\n\nThe documentation is sufficient, the code reads well and appears correct. There are doctests.\n\nIt is also fast as advertised:\n\n```\ndef zlog(m, n, k):\n    for i in range(0, m/1000):\n        a = ZZ.random_element(n)+2\n        b = ZZ.random_element(k)\n        c = a^b\n        for i in range (0, 1000):\n            c.exact_log(a)\n```\n\nOld sage 4.0:\n\n```\nsage: time zlog(100000, 2^100, 100)\nCPU times: user 23.19 s, sys: 0.19 s, total: 23.38 s\nWall time: 23.40 s\n\nsage: time zlog(100000, 100, 100)\nCPU times: user 3.46 s, sys: 0.02 s, total: 3.48 s\nWall time: 3.48 s\n```\n\nnew times with patch:\n\n```\nsage: time zlog(100000, 2^100, 100)\nCPU times: user 1.90 s, sys: 0.03 s, total: 1.93 s\nWall time: 1.93 s\n\nsage: time zlog(1000000, 100, 100)\nCPU times: user 0.49 s, sys: 0.06 s, total: 0.55 s\nWall time: 0.55 s\n```",
    "created_at": "2009-06-03T14:51:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5732#issuecomment-44711",
    "user": "https://trac.sagemath.org/admin/accounts/users/wbhart"
}
```

I've tested the code using:

```
def random(n):
    a = ZZ.random_element(n)
    return a

def z_exact_log_test(m, n, k):
    for i in range(0, m) :
        a = random(n) + 2
        b = random(k)
        c = a^b
        d = c.exact_log(a)
        if b != d:
            print "Error", b, "!=", d
```

for all sorts of values m, n, k, small large, etc. Everything passes.

The documentation is sufficient, the code reads well and appears correct. There are doctests.

It is also fast as advertised:

```
def zlog(m, n, k):
    for i in range(0, m/1000):
        a = ZZ.random_element(n)+2
        b = ZZ.random_element(k)
        c = a^b
        for i in range (0, 1000):
            c.exact_log(a)
```

Old sage 4.0:

```
sage: time zlog(100000, 2^100, 100)
CPU times: user 23.19 s, sys: 0.19 s, total: 23.38 s
Wall time: 23.40 s

sage: time zlog(100000, 100, 100)
CPU times: user 3.46 s, sys: 0.02 s, total: 3.48 s
Wall time: 3.48 s
```

new times with patch:

```
sage: time zlog(100000, 2^100, 100)
CPU times: user 1.90 s, sys: 0.03 s, total: 1.93 s
Wall time: 1.93 s

sage: time zlog(1000000, 100, 100)
CPU times: user 0.49 s, sys: 0.06 s, total: 0.55 s
Wall time: 0.55 s
```



---

archive/issue_events_013457.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-06-03T20:19:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5732",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5732#event-13457"
}
```



---

archive/issue_comments_044712.json:
```json
{
    "body": "Merged in 4.0.1.rc0.",
    "created_at": "2009-06-03T20:19:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5732#issuecomment-44712",
    "user": "https://github.com/mwhansen"
}
```

Merged in 4.0.1.rc0.



---

archive/issue_comments_044713.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-03T20:19:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5732#issuecomment-44713",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
