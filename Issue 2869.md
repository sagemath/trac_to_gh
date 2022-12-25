# Issue 2869: Cell sizing is broken

archive/issues_002869.json:
```json
{
    "body": "Assignee: boothby\n\nCells with funny input (i.e., long lines or long words) don't get sized nicely.  Worse, cells containing the character '<' are totally broken.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2869\n\n",
    "created_at": "2008-04-09T23:50:44Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Cell sizing is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2869",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```
Assignee: boothby

Cells with funny input (i.e., long lines or long words) don't get sized nicely.  Worse, cells containing the character '<' are totally broken.

Issue created by migration from https://trac.sagemath.org/ticket/2869





---

archive/issue_comments_019649.json:
```json
{
    "body": "Attachment [2869-resizer.patch](tarball://root/attachments/some-uuid/ticket2869/2869-resizer.patch) by boothby created at 2008-04-09 23:52:17",
    "created_at": "2008-04-09T23:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2869#issuecomment-19649",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [2869-resizer.patch](tarball://root/attachments/some-uuid/ticket2869/2869-resizer.patch) by boothby created at 2008-04-09 23:52:17



---

archive/issue_comments_019650.json:
```json
{
    "body": "REFEREE REPORT:\n* Very good, simple, etc.  Excellent!\n\n* It's still very slow when the textarea gets full, esp. on Safari.  That's a separate issue though.",
    "created_at": "2008-04-10T16:37:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2869#issuecomment-19650",
    "user": "https://github.com/williamstein"
}
```

REFEREE REPORT:
* Very good, simple, etc.  Excellent!

* It's still very slow when the textarea gets full, esp. on Safari.  That's a separate issue though.



---

archive/issue_comments_019651.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-10T16:46:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2869#issuecomment-19651",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003065.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-04-10T16:46:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2869",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2869#event-3065"
}
```



---

archive/issue_comments_019652.json:
```json
{
    "body": "Merged in Sage 3.0.alpha4",
    "created_at": "2008-04-10T16:46:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2869#issuecomment-19652",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha4



---

archive/issue_comments_019653.json:
```json
{
    "body": "Attachment [2869-resizer_rebase-alpha5.patch](tarball://root/attachments/some-uuid/ticket2869/2869-resizer_rebase-alpha5.patch) by boothby created at 2008-04-17 18:28:39",
    "created_at": "2008-04-17T18:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2869#issuecomment-19653",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [2869-resizer_rebase-alpha5.patch](tarball://root/attachments/some-uuid/ticket2869/2869-resizer_rebase-alpha5.patch) by boothby created at 2008-04-17 18:28:39



---

archive/issue_comments_019654.json:
```json
{
    "body": "Patch was only partially applied to alpha4.  Posted rebase.",
    "created_at": "2008-04-17T18:29:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2869#issuecomment-19654",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Patch was only partially applied to alpha4.  Posted rebase.



---

archive/issue_comments_019655.json:
```json
{
    "body": "Yeah, something went very, very wrong. Applied 2869-resizer_rebase-alpha5.patch - sorry boothby ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-04-17T18:32:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2869#issuecomment-19655",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Yeah, something went very, very wrong. Applied 2869-resizer_rebase-alpha5.patch - sorry boothby ;)

Cheers,

Michael
