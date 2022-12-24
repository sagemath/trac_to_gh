# Issue 1729: disable password prompt on initial startup

archive/issues_001729.json:
```json
{
    "body": "Assignee: boothby\n\nBecause the user can always do notebook(reset=True) it isn't a security risk to automatically log you in the web page that pops up. \n\nThis patch fixes this issue. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1729\n\n",
    "created_at": "2008-01-09T06:07:20Z",
    "labels": [
        "notebook",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "disable password prompt on initial startup",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1729",
    "user": "@robertwb"
}
```
Assignee: boothby

Because the user can always do notebook(reset=True) it isn't a security risk to automatically log you in the web page that pops up. 

This patch fixes this issue. 


Issue created by migration from https://trac.sagemath.org/ticket/1729





---

archive/issue_comments_010944.json:
```json
{
    "body": "Attachment [1729-notebook-login.patch](tarball://root/attachments/some-uuid/ticket1729/1729-notebook-login.patch) by @robertwb created at 2008-01-09 06:08:26",
    "created_at": "2008-01-09T06:08:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1729#issuecomment-10944",
    "user": "@robertwb"
}
```

Attachment [1729-notebook-login.patch](tarball://root/attachments/some-uuid/ticket1729/1729-notebook-login.patch) by @robertwb created at 2008-01-09 06:08:26



---

archive/issue_comments_010945.json:
```json
{
    "body": "There is no patch attacheD?!",
    "created_at": "2008-01-09T06:08:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1729#issuecomment-10945",
    "user": "@williamstein"
}
```

There is no patch attacheD?!



---

archive/issue_comments_010946.json:
```json
{
    "body": "Sorry, took me more than 18 seconds to attach the patch.",
    "created_at": "2008-01-09T06:09:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1729#issuecomment-10946",
    "user": "@robertwb"
}
```

Sorry, took me more than 18 seconds to attach the patch.



---

archive/issue_comments_010947.json:
```json
{
    "body": "Attachment [1729-notebook-login.2.patch](tarball://root/attachments/some-uuid/ticket1729/1729-notebook-login.2.patch) by boothby created at 2008-01-09 06:30:27\n\nRobert's patch works for me, but adds noise to the log.  Revised patch removes the noise.",
    "created_at": "2008-01-09T06:30:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1729#issuecomment-10947",
    "user": "boothby"
}
```

Attachment [1729-notebook-login.2.patch](tarball://root/attachments/some-uuid/ticket1729/1729-notebook-login.2.patch) by boothby created at 2008-01-09 06:30:27

Robert's patch works for me, but adds noise to the log.  Revised patch removes the noise.



---

archive/issue_comments_010948.json:
```json
{
    "body": "sage: notebook(secure=False)\nis now broken.",
    "created_at": "2008-01-09T06:53:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1729#issuecomment-10948",
    "user": "@williamstein"
}
```

sage: notebook(secure=False)
is now broken.



---

archive/issue_comments_010949.json:
```json
{
    "body": "Attachment [inotebook-fix.patch](tarball://root/attachments/some-uuid/ticket1729/inotebook-fix.patch) by @robertwb created at 2008-01-09 07:21:01",
    "created_at": "2008-01-09T07:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1729#issuecomment-10949",
    "user": "@robertwb"
}
```

Attachment [inotebook-fix.patch](tarball://root/attachments/some-uuid/ticket1729/inotebook-fix.patch) by @robertwb created at 2008-01-09 07:21:01



---

archive/issue_comments_010950.json:
```json
{
    "body": "Changing assignee from boothby to @robertwb.",
    "created_at": "2008-01-09T07:21:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1729#issuecomment-10950",
    "user": "@robertwb"
}
```

Changing assignee from boothby to @robertwb.



---

archive/issue_comments_010951.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-09T07:21:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1729#issuecomment-10951",
    "user": "@robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010952.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-09T14:54:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1729#issuecomment-10952",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010953.json:
```json
{
    "body": "Merged in Sage 2.10.alpha1. Specifically I merged\n\n* 1729-notebook-login.2.patch\n* inotebook-fix.patch\n\nCheers,\n\nMichael",
    "created_at": "2008-01-09T14:54:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1729#issuecomment-10953",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.alpha1. Specifically I merged

* 1729-notebook-login.2.patch
* inotebook-fix.patch

Cheers,

Michael
