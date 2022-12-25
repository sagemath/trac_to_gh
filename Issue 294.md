# Issue 294: [with patch] slowness in mpfr_root

archive/issues_000294.json:
```json
{
    "body": "Assignee: somebody\n\nThe `RealNumber.nth_root()` function (new patch, not yet committed) is very slow when the index is large, e.g.\n\n```\nsage: x = RealNumber(8)\n\nsage: time x.nth_root(100000)\nCPU times: user 1.97 s, sys: 0.14 s, total: 2.11 s\nWall time: 2.11\n 1.00002079463162\n```\n\nSeems to be caused by `mpfr_root()` itself; probably needs to be discussed upstream with the mpfr developers.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/294\n\n",
    "closed_at": "2007-10-13T05:23:44Z",
    "created_at": "2007-02-24T17:15:26Z",
    "labels": [
        "component: basic arithmetic",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "[with patch] slowness in mpfr_root",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/294",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: somebody

The `RealNumber.nth_root()` function (new patch, not yet committed) is very slow when the index is large, e.g.

```
sage: x = RealNumber(8)

sage: time x.nth_root(100000)
CPU times: user 1.97 s, sys: 0.14 s, total: 2.11 s
Wall time: 2.11
 1.00002079463162
```

Seems to be caused by `mpfr_root()` itself; probably needs to be discussed upstream with the mpfr developers.


Issue created by migration from https://trac.sagemath.org/ticket/294





---

archive/issue_comments_001387.json:
```json
{
    "body": "Any volunteers for this? Maybe it should be checked out if mpfr 2.3.0 still has the problem.\n\nCheers,\n\nMichael",
    "created_at": "2007-09-10T02:52:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/294#issuecomment-1387",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Any volunteers for this? Maybe it should be checked out if mpfr 2.3.0 still has the problem.

Cheers,

Michael



---

archive/issue_comments_001388.json:
```json
{
    "body": "This is still a problem with Sage 2.8.4.2 + mpfr 2.3:\n\n```\nsage: x = RealNumber(8)\nsage: time x.nth_root(100)\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00\n1.02101212570719\nsage: time x.nth_root(1000)\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00\n1.00208160507963\nsage: time x.nth_root(10000)\nCPU times: user 0.10 s, sys: 0.00 s, total: 0.10 s\nWall time: 0.11\n1.00020796577605\nsage: time x.nth_root(100000)\nCPU times: user 1.97 s, sys: 0.15 s, total: 2.12 s\nWall time: 2.12\n1.00002079463162\nsage: time x.nth_root(1000000)\nCPU times: user 32.92 s, sys: 2.14 s, total: 35.07 s\nWall time: 35.07\n1.00000207944370\n```\n\nCheers,\n\nMichael",
    "created_at": "2007-09-15T09:41:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/294#issuecomment-1388",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is still a problem with Sage 2.8.4.2 + mpfr 2.3:

```
sage: x = RealNumber(8)
sage: time x.nth_root(100)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
1.02101212570719
sage: time x.nth_root(1000)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
1.00208160507963
sage: time x.nth_root(10000)
CPU times: user 0.10 s, sys: 0.00 s, total: 0.10 s
Wall time: 0.11
1.00020796577605
sage: time x.nth_root(100000)
CPU times: user 1.97 s, sys: 0.15 s, total: 2.12 s
Wall time: 2.12
1.00002079463162
sage: time x.nth_root(1000000)
CPU times: user 32.92 s, sys: 2.14 s, total: 35.07 s
Wall time: 35.07
1.00000207944370
```

Cheers,

Michael



---

archive/issue_comments_001389.json:
```json
{
    "body": "Attachment [6718.patch](tarball://root/attachments/some-uuid/ticket294/6718.patch) by cwitty created at 2007-10-08 05:19:58",
    "created_at": "2007-10-08T05:19:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/294#issuecomment-1389",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [6718.patch](tarball://root/attachments/some-uuid/ticket294/6718.patch) by cwitty created at 2007-10-08 05:19:58



---

archive/issue_comments_001390.json:
```json
{
    "body": "I've attached a patch for nth_root that uses a different algorithm for the cases that were slow before.  Now we get:\n\n```\nsage: x = RR(8)\nsage: timeit x.nth_root(10)\n100000 loops, best of 3: 10.3 \u00b5s per loop\nsage: timeit x.nth_root(100)\n1000 loops, best of 3: 207 \u00b5s per loop\nsage: timeit x.nth_root(1000)\n1000 loops, best of 3: 461 \u00b5s per loop\nsage: timeit x.nth_root(10000)\n1000 loops, best of 3: 461 \u00b5s per loop\nsage: timeit x.nth_root(100000)\n1000 loops, best of 3: 462 \u00b5s per loop\nsage: timeit x.nth_root(1000000)\n1000 loops, best of 3: 456 \u00b5s per loop\nsage: timeit x.nth_root(10000000)\n1000 loops, best of 3: 455 \u00b5s per loop\n```",
    "created_at": "2007-10-08T05:24:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/294#issuecomment-1390",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

I've attached a patch for nth_root that uses a different algorithm for the cases that were slow before.  Now we get:

```
sage: x = RR(8)
sage: timeit x.nth_root(10)
100000 loops, best of 3: 10.3 µs per loop
sage: timeit x.nth_root(100)
1000 loops, best of 3: 207 µs per loop
sage: timeit x.nth_root(1000)
1000 loops, best of 3: 461 µs per loop
sage: timeit x.nth_root(10000)
1000 loops, best of 3: 461 µs per loop
sage: timeit x.nth_root(100000)
1000 loops, best of 3: 462 µs per loop
sage: timeit x.nth_root(1000000)
1000 loops, best of 3: 456 µs per loop
sage: timeit x.nth_root(10000000)
1000 loops, best of 3: 455 µs per loop
```



---

archive/issue_events_000670.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/cwitty",
    "created_at": "2007-10-08T05:24:12Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/294",
    "milestone": "sage-2.8.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/294#event-670"
}
```



---

archive/issue_events_000671.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-13T05:23:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/294",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/294#event-671"
}
```



---

archive/issue_comments_001391.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-13T05:23:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/294#issuecomment-1391",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
