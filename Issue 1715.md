# Issue 1715: [with patch, needs review] PolyBoRi pickling/hasing

archive/issues_001715.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @burcin mabshoff\n\nPickling and hashing of PolyBori rings and polynomials.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1715\n\n",
    "created_at": "2008-01-07T15:41:40Z",
    "labels": [
        "commutative algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with patch, needs review] PolyBoRi pickling/hasing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1715",
    "user": "@malb"
}
```
Assignee: @malb

CC:  @burcin mabshoff

Pickling and hashing of PolyBori rings and polynomials.

Issue created by migration from https://trac.sagemath.org/ticket/1715





---

archive/issue_comments_010871.json:
```json
{
    "body": "I've added a speed-up patch `unpickle_polybori.patch` which should be applied after the first patch `trac_1715.patch`",
    "created_at": "2008-01-09T13:32:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1715#issuecomment-10871",
    "user": "@malb"
}
```

I've added a speed-up patch `unpickle_polybori.patch` which should be applied after the first patch `trac_1715.patch`



---

archive/issue_comments_010872.json:
```json
{
    "body": "Note that doctests will SEGFAULT with these patches until #1712 is resolved.",
    "created_at": "2008-01-09T13:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1715#issuecomment-10872",
    "user": "@malb"
}
```

Note that doctests will SEGFAULT with these patches until #1712 is resolved.



---

archive/issue_comments_010873.json:
```json
{
    "body": "Now that I merged #1668 this needs to be rebased. But I could also edit the patch directly and fix the various names analog to #1668.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-13T17:55:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1715#issuecomment-10873",
    "user": "mabshoff"
}
```

Now that I merged #1668 this needs to be rebased. But I could also edit the patch directly and fix the various names analog to #1668.

Cheers,

Michael



---

archive/issue_comments_010874.json:
```json
{
    "body": "Attachment [trac_1715.patch](tarball://root/attachments/some-uuid/ticket1715/trac_1715.patch) by @malb created at 2008-01-17 13:23:12",
    "created_at": "2008-01-17T13:23:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1715#issuecomment-10874",
    "user": "@malb"
}
```

Attachment [trac_1715.patch](tarball://root/attachments/some-uuid/ticket1715/trac_1715.patch) by @malb created at 2008-01-17 13:23:12



---

archive/issue_comments_010875.json:
```json
{
    "body": "The attached patch `trac_1715.patch` applies cleanly against `2.10.alpha4` and contains all patches posted here earlier, i.e. only this patch needs to be applied.",
    "created_at": "2008-01-17T13:24:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1715#issuecomment-10875",
    "user": "@malb"
}
```

The attached patch `trac_1715.patch` applies cleanly against `2.10.alpha4` and contains all patches posted here earlier, i.e. only this patch needs to be applied.



---

archive/issue_comments_010876.json:
```json
{
    "body": "The patch looks good, should go in for 2.10.",
    "created_at": "2008-01-17T14:06:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1715#issuecomment-10876",
    "user": "@burcin"
}
```

The patch looks good, should go in for 2.10.



---

archive/issue_comments_010877.json:
```json
{
    "body": "Merged in Sage 2.10.alpha5",
    "created_at": "2008-01-17T14:28:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1715#issuecomment-10877",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.alpha5



---

archive/issue_comments_010878.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-17T14:28:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1715#issuecomment-10878",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010879.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha0. Initially this was merged in Sage 2.10.alpha5, but since 2.10.alpha4 become the release it was postponed and finally merged now.",
    "created_at": "2008-01-19T08:40:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1715#issuecomment-10879",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha0. Initially this was merged in Sage 2.10.alpha5, but since 2.10.alpha4 become the release it was postponed and finally merged now.
