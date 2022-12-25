# Issue 2714: [with patch, needs review] many interfaces have gp-specific code

archive/issues_002714.json:
```json
{
    "body": "Assignee: @williamstein\n\nIt looks like template.py was created based on gp.py, but kept some vestiges of code that was only useful for gp.  Then, in an excellent display of cargo-cult programming, this useless code was copied to many other interfaces.\n\nThe attached patch cleans up this useless code.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2714\n\n",
    "created_at": "2008-03-29T02:20:37Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "[with patch, needs review] many interfaces have gp-specific code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2714",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @williamstein

It looks like template.py was created based on gp.py, but kept some vestiges of code that was only useful for gp.  Then, in an excellent display of cargo-cult programming, this useless code was copied to many other interfaces.

The attached patch cleans up this useless code.


Issue created by migration from https://trac.sagemath.org/ticket/2714





---

archive/issue_comments_018668.json:
```json
{
    "body": "Attachment [trac2714-interface-cleanup.patch](tarball://root/attachments/some-uuid/ticket2714/trac2714-interface-cleanup.patch) by cwitty created at 2008-03-29 02:21:35",
    "created_at": "2008-03-29T02:21:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2714#issuecomment-18668",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac2714-interface-cleanup.patch](tarball://root/attachments/some-uuid/ticket2714/trac2714-interface-cleanup.patch) by cwitty created at 2008-03-29 02:21:35



---

archive/issue_comments_018669.json:
```json
{
    "body": "Looks good.",
    "created_at": "2008-03-29T13:25:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2714#issuecomment-18669",
    "user": "https://github.com/aghitza"
}
```

Looks good.



---

archive/issue_comments_018670.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-29T14:24:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2714#issuecomment-18670",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018671.json:
```json
{
    "body": "Merged in Sage 2.11.rc0",
    "created_at": "2008-03-29T14:24:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2714#issuecomment-18671",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.rc0



---

archive/issue_events_002902.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-03-29T14:24:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2714",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2714#event-2902"
}
```
