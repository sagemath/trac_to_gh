# Issue 5179: Delete __getslice__ from matrices

archive/issues_005179.json:
```json
{
    "body": "Assignee: @williamstein\n\n`__getslice__` has been deprecated for a long time in Python.  This patch adds equivalent functionality to `__getitem__`, which is where the functionality should be.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5179\n\n",
    "created_at": "2009-02-04T18:31:44Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Delete __getslice__ from matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5179",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

`__getslice__` has been deprecated for a long time in Python.  This patch adds equivalent functionality to `__getitem__`, which is where the functionality should be.

Issue created by migration from https://trac.sagemath.org/ticket/5179





---

archive/issue_comments_039635.json:
```json
{
    "body": "Attachment [delete-getslice.patch](tarball://root/attachments/some-uuid/ticket5179/delete-getslice.patch) by @jasongrout created at 2009-02-04 18:32:33",
    "created_at": "2009-02-04T18:32:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5179#issuecomment-39635",
    "user": "https://github.com/jasongrout"
}
```

Attachment [delete-getslice.patch](tarball://root/attachments/some-uuid/ticket5179/delete-getslice.patch) by @jasongrout created at 2009-02-04 18:32:33



---

archive/issue_comments_039636.json:
```json
{
    "body": "I thought I opened another ticket for this issue and posted a patch there, but I cannot find it at all.  If there is another ticket open at this time with a patch, this ticket and patch supersedes it.",
    "created_at": "2009-02-04T18:33:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5179#issuecomment-39636",
    "user": "https://github.com/jasongrout"
}
```

I thought I opened another ticket for this issue and posted a patch there, but I cannot find it at all.  If there is another ticket open at this time with a patch, this ticket and patch supersedes it.



---

archive/issue_comments_039637.json:
```json
{
    "body": "Code looks good, all doctests pass.\n\nPositive review.",
    "created_at": "2009-02-05T05:00:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5179#issuecomment-39637",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Code looks good, all doctests pass.

Positive review.



---

archive/issue_events_005433.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-05T10:49:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5179",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5179#event-5433"
}
```



---

archive/issue_comments_039638.json:
```json
{
    "body": "Merged in Sage 3.3.alpha6.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-05T10:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5179#issuecomment-39638",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha6.

Cheers,

Michael



---

archive/issue_comments_039639.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-05T10:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5179#issuecomment-39639",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
