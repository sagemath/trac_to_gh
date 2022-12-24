# Issue 3833: [with patch; needs review] calculus -- fix bug in hashing of symbolic expressions

archive/issues_003833.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nThis is stupid\n\n```\nsage: uniq([x-x, -x+x])\n[0, 0]\n```\n\n\nThis patch fixes this idiocy.\n\nThis was persisently reported by Rolandb.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3833\n\n",
    "created_at": "2008-08-13T05:15:04Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "[with patch; needs review] calculus -- fix bug in hashing of symbolic expressions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3833",
    "user": "@williamstein"
}
```
Assignee: @garyfurnish

This is stupid

```
sage: uniq([x-x, -x+x])
[0, 0]
```


This patch fixes this idiocy.

This was persisently reported by Rolandb.

Issue created by migration from https://trac.sagemath.org/ticket/3833





---

archive/issue_comments_027259.json:
```json
{
    "body": "Attachment [sage-3833.patch](tarball://root/attachments/some-uuid/ticket3833/sage-3833.patch) by @williamstein created at 2008-08-13 05:15:56",
    "created_at": "2008-08-13T05:15:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3833#issuecomment-27259",
    "user": "@williamstein"
}
```

Attachment [sage-3833.patch](tarball://root/attachments/some-uuid/ticket3833/sage-3833.patch) by @williamstein created at 2008-08-13 05:15:56



---

archive/issue_comments_027260.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-13T06:29:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3833#issuecomment-27260",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027261.json:
```json
{
    "body": "Merged in Sage 3.1.alpha2",
    "created_at": "2008-08-13T06:29:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3833#issuecomment-27261",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.alpha2
