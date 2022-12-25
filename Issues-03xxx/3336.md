# Issue 3336: [with patch, positive review] DyckWords(n) should use an iterator

archive/issues_003336.json:
```json
{
    "body": "Assignee: @dandrake\n\nCC:  sage-combinat\n\nCurrently, DyckWords(n) creates a list, which uses a lot of memory and is slow. See [this sage-devel thread](http://groups.google.com/group/sage-devel/browse_thread/thread/8b739bb399f2e3d4).\n\nIssue created by migration from https://trac.sagemath.org/ticket/3336\n\n",
    "closed_at": "2008-05-31T05:56:41Z",
    "created_at": "2008-05-30T00:44:34Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "[with patch, positive review] DyckWords(n) should use an iterator",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3336",
    "user": "https://github.com/dandrake"
}
```
Assignee: @dandrake

CC:  sage-combinat

Currently, DyckWords(n) creates a list, which uses a lot of memory and is slow. See [this sage-devel thread](http://groups.google.com/group/sage-devel/browse_thread/thread/8b739bb399f2e3d4).

Issue created by migration from https://trac.sagemath.org/ticket/3336





---

archive/issue_comments_023072.json:
```json
{
    "body": "Patch attached.",
    "created_at": "2008-05-30T06:42:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3336#issuecomment-23072",
    "user": "https://github.com/dandrake"
}
```

Patch attached.



---

archive/issue_comments_023073.json:
```json
{
    "body": "Attachment [dyckword-3336.patch](tarball://root/attachments/some-uuid/ticket3336/dyckword-3336.patch) by @mwhansen created at 2008-05-31 03:53:44\n\nLooks good.  Thanks for this Dan!  I also added it to 2144.",
    "created_at": "2008-05-31T03:53:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3336#issuecomment-23073",
    "user": "https://github.com/mwhansen"
}
```

Attachment [dyckword-3336.patch](tarball://root/attachments/some-uuid/ticket3336/dyckword-3336.patch) by @mwhansen created at 2008-05-31 03:53:44

Looks good.  Thanks for this Dan!  I also added it to 2144.



---

archive/issue_events_007473.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-31T05:56:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3336",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3336#event-7473"
}
```



---

archive/issue_comments_023074.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-31T05:56:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3336#issuecomment-23074",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_023075.json:
```json
{
    "body": "Merged in Sage 3.0.3.alpha1",
    "created_at": "2008-05-31T05:56:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3336#issuecomment-23075",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.3.alpha1
