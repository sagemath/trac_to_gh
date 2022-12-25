# Issue 6259: [with patch, positive review] Fix spurious file creation in sage/server/support.py

archive/issues_006259.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @mwhansen @ncalexan\n\nThe file above generates a file in the current directory when running doctests on it; the attached patch just moves that to an appropriate temp directory. (That is, it switches the doctest, not the actual code.) \n\nI'm adding two people to the cc in the hopes that someone can give this a three-second glance.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6259\n\n",
    "closed_at": "2009-06-12T07:55:15Z",
    "created_at": "2009-06-11T09:40:40Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "[with patch, positive review] Fix spurious file creation in sage/server/support.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6259",
    "user": "https://github.com/craigcitro"
}
```
Assignee: boothby

CC:  @mwhansen @ncalexan

The file above generates a file in the current directory when running doctests on it; the attached patch just moves that to an appropriate temp directory. (That is, it switches the doctest, not the actual code.) 

I'm adding two people to the cc in the hopes that someone can give this a three-second glance.

Issue created by migration from https://trac.sagemath.org/ticket/6259





---

archive/issue_comments_049890.json:
```json
{
    "body": "When using this on the server, are the temp files properly cleaned up?  But this addresses the problem for now.",
    "created_at": "2009-06-11T16:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6259#issuecomment-49890",
    "user": "https://github.com/ncalexan"
}
```

When using this on the server, are the temp files properly cleaned up?  But this addresses the problem for now.



---

archive/issue_comments_049891.json:
```json
{
    "body": "Attachment [trac-6259.patch](tarball://root/attachments/some-uuid/ticket6259/trac-6259.patch) by @craigcitro created at 2009-06-12 07:54:38",
    "created_at": "2009-06-12T07:54:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6259#issuecomment-49891",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-6259.patch](tarball://root/attachments/some-uuid/ticket6259/trac-6259.patch) by @craigcitro created at 2009-06-12 07:54:38



---

archive/issue_comments_049892.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-12T07:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6259#issuecomment-49892",
    "user": "https://github.com/craigcitro"
}
```

Resolution: fixed



---

archive/issue_events_014655.json:
```json
{
    "actor": "https://github.com/craigcitro",
    "created_at": "2009-06-12T07:55:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6259",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6259#event-14655"
}
```



---

archive/issue_comments_049893.json:
```json
{
    "body": "Somehow this patch got dropped between `alpha0` and `rc3`. I've added it back in `rc3`.",
    "created_at": "2009-06-18T10:25:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6259#issuecomment-49893",
    "user": "https://github.com/craigcitro"
}
```

Somehow this patch got dropped between `alpha0` and `rc3`. I've added it back in `rc3`.
