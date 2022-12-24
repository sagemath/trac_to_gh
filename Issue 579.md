# Issue 579: pass additional *args and **kwds for GF to finite field implementations

archive/issues_000579.json:
```json
{
    "body": "Assignee: somebody\n\nFor example, you may print finite field elements as integers via the Givaro implementation. But the constructor parameter to allow this is not passed to the actual implementation so far.\n\nAfter the attached patch is applied, this works:\n\n```\nsage: k.<a> = GF(2^8,repr='int')\nsage: a\n2\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/579\n\n",
    "created_at": "2007-09-03T15:17:47Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "pass additional *args and **kwds for GF to finite field implementations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/579",
    "user": "malb"
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

archive/issue_comments_002998.json:
```json
{
    "body": "Attachment [6078.patch](tarball://root/attachments/some-uuid/ticket579/6078.patch) by malb created at 2007-09-03 15:18:07",
    "created_at": "2007-09-03T15:18:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/579#issuecomment-2998",
    "user": "malb"
}
```

Attachment [6078.patch](tarball://root/attachments/some-uuid/ticket579/6078.patch) by malb created at 2007-09-03 15:18:07



---

archive/issue_comments_002999.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-05T05:00:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/579#issuecomment-2999",
    "user": "was"
}
```

Resolution: fixed
