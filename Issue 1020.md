# Issue 1020: squash warning from decl.pxi emitted by cython

archive/issues_001020.json:
```json
{
    "body": "Assignee: mabshoff\n\nWith 2.8.10.alpha1 every file that includes decl.pxi cython emits the following warnings:\n\n```\nwarning: /tmp/Work-mabshoff/sage-2.8.10.alpha1/devel/sage-main/sage/libs/ntl/decl.pxi:33:18: Function signature does not match previous declaration\nwarning: /tmp/Work-mabshoff/sage-2.8.10.alpha1/devel/sage-main/sage/libs/ntl/decl.pxi:34:18: Function signature does not match previous declaration\nwarning: /tmp/Work-mabshoff/sage-2.8.10.alpha1/devel/sage-main/sage/libs/ntl/decl.pxi:244:27: Function signature does not match previous declaration\n```\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1020\n\n",
    "created_at": "2007-10-28T09:52:05Z",
    "labels": [
        "component: distribution",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.10",
    "title": "squash warning from decl.pxi emitted by cython",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1020",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

With 2.8.10.alpha1 every file that includes decl.pxi cython emits the following warnings:

```
warning: /tmp/Work-mabshoff/sage-2.8.10.alpha1/devel/sage-main/sage/libs/ntl/decl.pxi:33:18: Function signature does not match previous declaration
warning: /tmp/Work-mabshoff/sage-2.8.10.alpha1/devel/sage-main/sage/libs/ntl/decl.pxi:34:18: Function signature does not match previous declaration
warning: /tmp/Work-mabshoff/sage-2.8.10.alpha1/devel/sage-main/sage/libs/ntl/decl.pxi:244:27: Function signature does not match previous declaration
```

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1020





---

archive/issue_events_002794.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/cwitty",
    "created_at": "2007-10-28T16:54:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1020",
    "milestone": "sage-2.8.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1020#event-2794"
}
```



---

archive/issue_comments_006236.json:
```json
{
    "body": "Changing assignee from mabshoff to cwitty.",
    "created_at": "2007-10-28T16:54:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1020#issuecomment-6236",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Changing assignee from mabshoff to cwitty.



---

archive/issue_comments_006237.json:
```json
{
    "body": "Attachment [1020.patch](tarball://root/attachments/some-uuid/ticket1020/1020.patch) by cwitty created at 2007-10-28 17:45:55",
    "created_at": "2007-10-28T17:45:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1020#issuecomment-6237",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [1020.patch](tarball://root/attachments/some-uuid/ticket1020/1020.patch) by cwitty created at 2007-10-28 17:45:55



---

archive/issue_comments_006238.json:
```json
{
    "body": "The attached patches fix these warnings, as well as several others.",
    "created_at": "2007-10-28T17:46:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1020#issuecomment-6238",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

The attached patches fix these warnings, as well as several others.



---

archive/issue_events_002795.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/cwitty",
    "created_at": "2007-10-28T17:46:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1020",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1020#event-2795"
}
```



---

archive/issue_comments_006239.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-28T17:46:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1020#issuecomment-6239",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Resolution: fixed
