# Issue 2879: [with patch, needs review] Bug fix in totallyreal_rel

archive/issues_002879.json:
```json
{
    "body": "Assignee: citro\n\nThere was an bug in the enumeration of relative totally real fields: if the extension was constant (coming from Q), it was ignored by a resultant calculation.  Also, some exceptional cases were unintentionally ignored.  The fix is attached.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2879\n\n",
    "created_at": "2008-04-11T18:09:32Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch, needs review] Bug fix in totallyreal_rel",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2879",
    "user": "https://github.com/jvoight"
}
```
Assignee: citro

There was an bug in the enumeration of relative totally real fields: if the extension was constant (coming from Q), it was ignored by a resultant calculation.  Also, some exceptional cases were unintentionally ignored.  The fix is attached.

Issue created by migration from https://trac.sagemath.org/ticket/2879





---

archive/issue_comments_019764.json:
```json
{
    "body": "Attachment [8681.patch](tarball://root/attachments/some-uuid/ticket2879/8681.patch) by @jvoight created at 2008-04-11 18:10:03",
    "created_at": "2008-04-11T18:10:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2879#issuecomment-19764",
    "user": "https://github.com/jvoight"
}
```

Attachment [8681.patch](tarball://root/attachments/some-uuid/ticket2879/8681.patch) by @jvoight created at 2008-04-11 18:10:03



---

archive/issue_comments_019765.json:
```json
{
    "body": "Attachment [8683.patch](tarball://root/attachments/some-uuid/ticket2879/8683.patch) by @jvoight created at 2008-04-11 18:10:09",
    "created_at": "2008-04-11T18:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2879#issuecomment-19765",
    "user": "https://github.com/jvoight"
}
```

Attachment [8683.patch](tarball://root/attachments/some-uuid/ticket2879/8683.patch) by @jvoight created at 2008-04-11 18:10:09



---

archive/issue_comments_019766.json:
```json
{
    "body": "Patch looks good. I'm attaching a new version of the patch, since I had merge troubles.",
    "created_at": "2008-04-15T10:48:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2879#issuecomment-19766",
    "user": "https://github.com/craigcitro"
}
```

Patch looks good. I'm attaching a new version of the patch, since I had merge troubles.



---

archive/issue_comments_019767.json:
```json
{
    "body": "Attachment [trac-2879.patch](tarball://root/attachments/some-uuid/ticket2879/trac-2879.patch) by @craigcitro created at 2008-04-15 10:49:02",
    "created_at": "2008-04-15T10:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2879#issuecomment-19767",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-2879.patch](tarball://root/attachments/some-uuid/ticket2879/trac-2879.patch) by @craigcitro created at 2008-04-15 10:49:02



---

archive/issue_comments_019768.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-15T10:57:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2879#issuecomment-19768",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019769.json:
```json
{
    "body": "Merged trac-2879.patch in Sage 3.0.alpha5",
    "created_at": "2008-04-15T10:57:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2879#issuecomment-19769",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac-2879.patch in Sage 3.0.alpha5
