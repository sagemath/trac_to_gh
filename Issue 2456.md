# Issue 2456: matrix_symbolic_dense doctest failures

archive/issues_002456.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nFile \"matrix_symbolic_dense.pyx\", line 873:\n    sage: list(a.fcp())\nExpected:\n    [(x^2 - 65*x - 250, 1), (x, 3)]\nGot:\n    [(x, 3), (x^2 - 65*x - 250, 1)]\n```\n\nBut inside sage:\n\n```\nsage: a = matrix(SR, 5, [1..5^2]) \nsage: a.fcp()\n(x^2 - 65*x - 250) * x^3\nsage: list(a.fcp())\n[(x^2 - 65*x - 250, 1), (x, 3)]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2456\n\n",
    "created_at": "2008-03-10T13:53:55Z",
    "labels": [
        "component: linear algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "matrix_symbolic_dense doctest failures",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2456",
    "user": "https://github.com/garyfurnish"
}
```
Assignee: @williamstein


```
File "matrix_symbolic_dense.pyx", line 873:
    sage: list(a.fcp())
Expected:
    [(x^2 - 65*x - 250, 1), (x, 3)]
Got:
    [(x, 3), (x^2 - 65*x - 250, 1)]
```

But inside sage:

```
sage: a = matrix(SR, 5, [1..5^2]) 
sage: a.fcp()
(x^2 - 65*x - 250) * x^3
sage: list(a.fcp())
[(x^2 - 65*x - 250, 1), (x, 3)]
```


Issue created by migration from https://trac.sagemath.org/ticket/2456





---

archive/issue_comments_016595.json:
```json
{
    "body": "This patch is correct because of changes in #2206",
    "created_at": "2008-03-10T14:01:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2456#issuecomment-16595",
    "user": "https://github.com/garyfurnish"
}
```

This patch is correct because of changes in #2206



---

archive/issue_comments_016596.json:
```json
{
    "body": "Changing assignee from @williamstein to @garyfurnish.",
    "created_at": "2008-03-10T14:01:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2456#issuecomment-16596",
    "user": "https://github.com/garyfurnish"
}
```

Changing assignee from @williamstein to @garyfurnish.



---

archive/issue_comments_016597.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-10T14:01:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2456#issuecomment-16597",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_016598.json:
```json
{
    "body": "This patch fixes problems in factorization that cause problems here.",
    "created_at": "2008-03-10T15:59:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2456#issuecomment-16598",
    "user": "https://github.com/garyfurnish"
}
```

This patch fixes problems in factorization that cause problems here.



---

archive/issue_comments_016599.json:
```json
{
    "body": "REFEREE REPORT:\n\n* The second chunk in trac_2456.patch, which swaps the order of sort and simplify, breaks things.  This is because simplify assumes its input is sorted, as it combines adjacent pairs.\n\n* The rest of the patch looks fine.",
    "created_at": "2008-03-10T16:06:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2456#issuecomment-16599",
    "user": "https://github.com/williamstein"
}
```

REFEREE REPORT:

* The second chunk in trac_2456.patch, which swaps the order of sort and simplify, breaks things.  This is because simplify assumes its input is sorted, as it combines adjacent pairs.

* The rest of the patch looks fine.



---

archive/issue_comments_016600.json:
```json
{
    "body": "Attachment [trac_2456.patch](tarball://root/attachments/some-uuid/ticket2456/trac_2456.patch) by @williamstein created at 2008-03-10 16:09:58\n\nreplaced patch addresses my concern.",
    "created_at": "2008-03-10T16:09:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2456#issuecomment-16600",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_2456.patch](tarball://root/attachments/some-uuid/ticket2456/trac_2456.patch) by @williamstein created at 2008-03-10 16:09:58

replaced patch addresses my concern.



---

archive/issue_events_002633.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-03-10T17:19:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2456",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2456#event-2633"
}
```



---

archive/issue_comments_016601.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-10T17:19:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2456#issuecomment-16601",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016602.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc4",
    "created_at": "2008-03-10T17:19:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2456#issuecomment-16602",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.rc4
