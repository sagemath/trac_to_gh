# Issue 1729: [with patch, positive review] disable password prompt on initial startup

archive/issues_001729.json:
```json
{
    "body": "Assignee: @robertwb\n\nBecause the user can always do notebook(reset=True) it isn't a security risk to automatically log you in the web page that pops up. \n\nThis patch fixes this issue. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1729\n\n",
    "closed_at": "2008-01-09T14:54:06Z",
    "created_at": "2008-01-09T06:07:20Z",
    "labels": [
        "component: notebook",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "[with patch, positive review] disable password prompt on initial startup",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1729",
    "user": "https://github.com/robertwb"
}
```
Assignee: @robertwb

Because the user can always do notebook(reset=True) it isn't a security risk to automatically log you in the web page that pops up. 

This patch fixes this issue. 


Issue created by migration from https://trac.sagemath.org/ticket/1729





---

archive/issue_comments_010917.json:
```json
{
    "body": "Attachment [1729-notebook-login.patch](tarball://root/attachments/some-uuid/ticket1729/1729-notebook-login.patch) by @robertwb created at 2008-01-09 06:08:26",
    "created_at": "2008-01-09T06:08:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1729#issuecomment-10917",
    "user": "https://github.com/robertwb"
}
```

Attachment [1729-notebook-login.patch](tarball://root/attachments/some-uuid/ticket1729/1729-notebook-login.patch) by @robertwb created at 2008-01-09 06:08:26



---

archive/issue_comments_010918.json:
```json
{
    "body": "There is no patch attacheD?!",
    "created_at": "2008-01-09T06:08:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1729#issuecomment-10918",
    "user": "https://github.com/williamstein"
}
```

There is no patch attacheD?!



---

archive/issue_comments_010919.json:
```json
{
    "body": "Sorry, took me more than 18 seconds to attach the patch.",
    "created_at": "2008-01-09T06:09:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1729#issuecomment-10919",
    "user": "https://github.com/robertwb"
}
```

Sorry, took me more than 18 seconds to attach the patch.



---

archive/issue_comments_010920.json:
```json
{
    "body": "Attachment [1729-notebook-login.2.patch](tarball://root/attachments/some-uuid/ticket1729/1729-notebook-login.2.patch) by boothby created at 2008-01-09 06:30:27\n\nRobert's patch works for me, but adds noise to the log.  Revised patch removes the noise.",
    "created_at": "2008-01-09T06:30:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1729#issuecomment-10920",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [1729-notebook-login.2.patch](tarball://root/attachments/some-uuid/ticket1729/1729-notebook-login.2.patch) by boothby created at 2008-01-09 06:30:27

Robert's patch works for me, but adds noise to the log.  Revised patch removes the noise.



---

archive/issue_comments_010921.json:
```json
{
    "body": "sage: notebook(secure=False)\nis now broken.",
    "created_at": "2008-01-09T06:53:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1729#issuecomment-10921",
    "user": "https://github.com/williamstein"
}
```

sage: notebook(secure=False)
is now broken.



---

archive/issue_comments_010922.json:
```json
{
    "body": "Attachment [inotebook-fix.patch](tarball://root/attachments/some-uuid/ticket1729/inotebook-fix.patch) by @robertwb created at 2008-01-09 07:21:01",
    "created_at": "2008-01-09T07:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1729#issuecomment-10922",
    "user": "https://github.com/robertwb"
}
```

Attachment [inotebook-fix.patch](tarball://root/attachments/some-uuid/ticket1729/inotebook-fix.patch) by @robertwb created at 2008-01-09 07:21:01



---

archive/issue_comments_010923.json:
```json
{
    "body": "Changing assignee from boothby to @robertwb.",
    "created_at": "2008-01-09T07:21:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1729#issuecomment-10923",
    "user": "https://github.com/robertwb"
}
```

Changing assignee from boothby to @robertwb.



---

archive/issue_comments_010924.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-09T07:21:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1729#issuecomment-10924",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010925.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-09T14:54:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1729#issuecomment-10925",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010926.json:
```json
{
    "body": "Merged in Sage 2.10.alpha1. Specifically I merged\n\n* 1729-notebook-login.2.patch\n* inotebook-fix.patch\n\nCheers,\n\nMichael",
    "created_at": "2008-01-09T14:54:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1729#issuecomment-10926",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.alpha1. Specifically I merged

* 1729-notebook-login.2.patch
* inotebook-fix.patch

Cheers,

Michael



---

archive/issue_events_004203.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-09T14:54:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1729",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1729#event-4203"
}
```
