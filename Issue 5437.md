# Issue 5437: [with patch; needs review] pickle jar -- make it run through in order

archive/issues_005437.json:
```json
{
    "body": "Assignee: mabshoff\n\nCurrent when unpickling the pickle jar the files are run through in whatever order os.listdir gives them.  This patch instead unpickles in order.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5437\n\n",
    "created_at": "2009-03-04T05:32:31Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "[with patch; needs review] pickle jar -- make it run through in order",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5437",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

Current when unpickling the pickle jar the files are run through in whatever order os.listdir gives them.  This patch instead unpickles in order.

Issue created by migration from https://trac.sagemath.org/ticket/5437





---

archive/issue_comments_041973.json:
```json
{
    "body": "Attachment [trac_5437.patch](tarball://root/attachments/some-uuid/ticket5437/trac_5437.patch) by @williamstein created at 2009-03-04 05:33:26",
    "created_at": "2009-03-04T05:33:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5437#issuecomment-41973",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5437.patch](tarball://root/attachments/some-uuid/ticket5437/trac_5437.patch) by @williamstein created at 2009-03-04 05:33:26



---

archive/issue_comments_041974.json:
```json
{
    "body": "Positive reiview.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-04T19:50:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5437#issuecomment-41974",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive reiview.

Cheers,

Michael



---

archive/issue_comments_041975.json:
```json
{
    "body": "Merged in Sage 3.4.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-04T19:51:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5437#issuecomment-41975",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.rc1.

Cheers,

Michael



---

archive/issue_events_005689.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-04T19:51:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5437",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5437#event-5689"
}
```



---

archive/issue_comments_041976.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-04T19:51:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5437#issuecomment-41976",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
