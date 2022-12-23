# Issue 3803: prime_range takes WAY WAY too long to convert its data back to PARI

archive/issues_003803.json:
```json
{
    "body": "Assignee: was\n\n\n```\nd142-058-050-205:src was$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading SAGE library. Current Mercurial branch is: review2\nsage: timeit('prime_range(10^6)')\n5 loops, best of 3: 214 ms per loop\nsage: timeit('prime_range(10^6,leave_pari=True)')\n125 loops, best of 3: 4.29 ms per loop\nsage: 214/4.29\n49.8834498834499\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3803\n\n",
    "created_at": "2008-08-11T04:03:23Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "prime_range takes WAY WAY too long to convert its data back to PARI",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3803",
    "user": "was"
}
```
Assignee: was


```
d142-058-050-205:src was$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: review2
sage: timeit('prime_range(10^6)')
5 loops, best of 3: 214 ms per loop
sage: timeit('prime_range(10^6,leave_pari=True)')
125 loops, best of 3: 4.29 ms per loop
sage: 214/4.29
49.8834498834499
```


Issue created by migration from https://trac.sagemath.org/ticket/3803





---

archive/issue_comments_027032.json:
```json
{
    "body": "Since we removed the `leave_pari` option altogether, this ticket is now invalid.",
    "created_at": "2009-01-23T13:21:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3803#issuecomment-27032",
    "user": "craigcitro"
}
```

Since we removed the `leave_pari` option altogether, this ticket is now invalid.



---

archive/issue_comments_027033.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-01-23T13:21:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3803#issuecomment-27033",
    "user": "craigcitro"
}
```

Resolution: invalid
