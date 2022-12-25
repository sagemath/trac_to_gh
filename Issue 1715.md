# Issue 1715: [with patch, needs review] PolyBoRi pickling/hasing

archive/issues_001715.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @burcin mabshoff\n\nPickling and hashing of PolyBori rings and polynomials.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1715\n\n",
    "created_at": "2008-01-07T15:41:40Z",
    "labels": [
        "component: commutative algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with patch, needs review] PolyBoRi pickling/hasing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1715",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  @burcin mabshoff

Pickling and hashing of PolyBori rings and polynomials.

Issue created by migration from https://trac.sagemath.org/ticket/1715





---

archive/issue_comments_010844.json:
```json
{
    "body": "I've added a speed-up patch `unpickle_polybori.patch` which should be applied after the first patch `trac_1715.patch`",
    "created_at": "2008-01-09T13:32:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1715#issuecomment-10844",
    "user": "https://github.com/malb"
}
```

I've added a speed-up patch `unpickle_polybori.patch` which should be applied after the first patch `trac_1715.patch`



---

archive/issue_comments_010845.json:
```json
{
    "body": "Note that doctests will SEGFAULT with these patches until #1712 is resolved.",
    "created_at": "2008-01-09T13:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1715#issuecomment-10845",
    "user": "https://github.com/malb"
}
```

Note that doctests will SEGFAULT with these patches until #1712 is resolved.



---

archive/issue_comments_010846.json:
```json
{
    "body": "Now that I merged #1668 this needs to be rebased. But I could also edit the patch directly and fix the various names analog to #1668.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-13T17:55:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1715#issuecomment-10846",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Now that I merged #1668 this needs to be rebased. But I could also edit the patch directly and fix the various names analog to #1668.

Cheers,

Michael



---

archive/issue_comments_010847.json:
```json
{
    "body": "Attachment [trac_1715.patch](tarball://root/attachments/some-uuid/ticket1715/trac_1715.patch) by @malb created at 2008-01-17 13:23:12",
    "created_at": "2008-01-17T13:23:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1715#issuecomment-10847",
    "user": "https://github.com/malb"
}
```

Attachment [trac_1715.patch](tarball://root/attachments/some-uuid/ticket1715/trac_1715.patch) by @malb created at 2008-01-17 13:23:12



---

archive/issue_comments_010848.json:
```json
{
    "body": "The attached patch `trac_1715.patch` applies cleanly against `2.10.alpha4` and contains all patches posted here earlier, i.e. only this patch needs to be applied.",
    "created_at": "2008-01-17T13:24:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1715#issuecomment-10848",
    "user": "https://github.com/malb"
}
```

The attached patch `trac_1715.patch` applies cleanly against `2.10.alpha4` and contains all patches posted here earlier, i.e. only this patch needs to be applied.



---

archive/issue_comments_010849.json:
```json
{
    "body": "The patch looks good, should go in for 2.10.",
    "created_at": "2008-01-17T14:06:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1715#issuecomment-10849",
    "user": "https://github.com/burcin"
}
```

The patch looks good, should go in for 2.10.



---

archive/issue_comments_010850.json:
```json
{
    "body": "Merged in Sage 2.10.alpha5",
    "created_at": "2008-01-17T14:28:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1715#issuecomment-10850",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.alpha5



---

archive/issue_events_001874.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-17T14:28:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1715",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1715#event-1874"
}
```



---

archive/issue_comments_010851.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-17T14:28:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1715#issuecomment-10851",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010852.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha0. Initially this was merged in Sage 2.10.alpha5, but since 2.10.alpha4 become the release it was postponed and finally merged now.",
    "created_at": "2008-01-19T08:40:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1715#issuecomment-10852",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha0. Initially this was merged in Sage 2.10.alpha5, but since 2.10.alpha4 become the release it was postponed and finally merged now.
