# Issue 2869: Cell sizing is broken

archive/issues_002869.json:
```json
{
    "body": "Assignee: boothby\n\nCells with funny input (i.e., long lines or long words) don't get sized nicely.  Worse, cells containing the character '<' are totally broken.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2869\n\n",
    "created_at": "2008-04-09T23:50:44Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Cell sizing is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2869",
    "user": "boothby"
}
```
Assignee: boothby

Cells with funny input (i.e., long lines or long words) don't get sized nicely.  Worse, cells containing the character '<' are totally broken.

Issue created by migration from https://trac.sagemath.org/ticket/2869





---

archive/issue_comments_019690.json:
```json
{
    "body": "Attachment [2869-resizer.patch](tarball://root/attachments/some-uuid/ticket2869/2869-resizer.patch) by boothby created at 2008-04-09 23:52:17",
    "created_at": "2008-04-09T23:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2869#issuecomment-19690",
    "user": "boothby"
}
```

Attachment [2869-resizer.patch](tarball://root/attachments/some-uuid/ticket2869/2869-resizer.patch) by boothby created at 2008-04-09 23:52:17



---

archive/issue_comments_019691.json:
```json
{
    "body": "REFEREE REPORT:\n* Very good, simple, etc.  Excellent!\n\n* It's still very slow when the textarea gets full, esp. on Safari.  That's a separate issue though.",
    "created_at": "2008-04-10T16:37:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2869#issuecomment-19691",
    "user": "@williamstein"
}
```

REFEREE REPORT:
* Very good, simple, etc.  Excellent!

* It's still very slow when the textarea gets full, esp. on Safari.  That's a separate issue though.



---

archive/issue_comments_019692.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-10T16:46:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2869#issuecomment-19692",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019693.json:
```json
{
    "body": "Merged in Sage 3.0.alpha4",
    "created_at": "2008-04-10T16:46:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2869#issuecomment-19693",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha4



---

archive/issue_comments_019694.json:
```json
{
    "body": "Attachment [2869-resizer_rebase-alpha5.patch](tarball://root/attachments/some-uuid/ticket2869/2869-resizer_rebase-alpha5.patch) by boothby created at 2008-04-17 18:28:39",
    "created_at": "2008-04-17T18:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2869#issuecomment-19694",
    "user": "boothby"
}
```

Attachment [2869-resizer_rebase-alpha5.patch](tarball://root/attachments/some-uuid/ticket2869/2869-resizer_rebase-alpha5.patch) by boothby created at 2008-04-17 18:28:39



---

archive/issue_comments_019695.json:
```json
{
    "body": "Patch was only partially applied to alpha4.  Posted rebase.",
    "created_at": "2008-04-17T18:29:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2869#issuecomment-19695",
    "user": "boothby"
}
```

Patch was only partially applied to alpha4.  Posted rebase.



---

archive/issue_comments_019696.json:
```json
{
    "body": "Yeah, something went very, very wrong. Applied 2869-resizer_rebase-alpha5.patch - sorry boothby ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-04-17T18:32:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2869#issuecomment-19696",
    "user": "mabshoff"
}
```

Yeah, something went very, very wrong. Applied 2869-resizer_rebase-alpha5.patch - sorry boothby ;)

Cheers,

Michael
