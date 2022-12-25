# Issue 579: pass additional *args and **kwds for GF to finite field implementations

archive/issues_000579.json:
```json
{
    "body": "Assignee: somebody\n\nFor example, you may print finite field elements as integers via the Givaro implementation. But the constructor parameter to allow this is not passed to the actual implementation so far.\n\nAfter the attached patch is applied, this works:\n\n```\nsage: k.<a> = GF(2^8,repr='int')\nsage: a\n2\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/579\n\n",
    "created_at": "2007-09-03T15:17:47Z",
    "labels": [
        "component: basic arithmetic",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "pass additional *args and **kwds for GF to finite field implementations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/579",
    "user": "https://github.com/malb"
}
```
Assignee: somebody

For example, you may print finite field elements as integers via the Givaro implementation. But the constructor parameter to allow this is not passed to the actual implementation so far.

After the attached patch is applied, this works:

```
sage: k.<a> = GF(2^8,repr='int')
sage: a
2
```

Issue created by migration from https://trac.sagemath.org/ticket/579





---

archive/issue_comments_002986.json:
```json
{
    "body": "Attachment [6078.patch](tarball://root/attachments/some-uuid/ticket579/6078.patch) by @malb created at 2007-09-03 15:18:07",
    "created_at": "2007-09-03T15:18:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/579#issuecomment-2986",
    "user": "https://github.com/malb"
}
```

Attachment [6078.patch](tarball://root/attachments/some-uuid/ticket579/6078.patch) by @malb created at 2007-09-03 15:18:07



---

archive/issue_events_001549.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-05T05:00:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/579",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/579#event-1549"
}
```



---

archive/issue_comments_002987.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-05T05:00:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/579#issuecomment-2987",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
