# Issue 3918: notebook -- MAJOR BUG involving uploading file from URL

archive/issues_003918.json:
```json
{
    "body": "Assignee: boothby\n\n1. Go to Data --> Upload File\n2. Select a URL that takes \"forever\" to download.\n3. Now the ENTIRE SERVER hangs \"forever\".  \n\nThis is clearly very much not good. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3918\n\n",
    "created_at": "2008-08-20T23:17:14Z",
    "labels": [
        "component: notebook",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "notebook -- MAJOR BUG involving uploading file from URL",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3918",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

1. Go to Data --> Upload File
2. Select a URL that takes "forever" to download.
3. Now the ENTIRE SERVER hangs "forever".  

This is clearly very much not good. 

Issue created by migration from https://trac.sagemath.org/ticket/3918





---

archive/issue_comments_027969.json:
```json
{
    "body": "Changing assignee from boothby to @mwhansen.",
    "created_at": "2008-09-08T10:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3918#issuecomment-27969",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from boothby to @mwhansen.



---

archive/issue_comments_027970.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-08T10:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3918#issuecomment-27970",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_027971.json:
```json
{
    "body": "Attachment [trac_3918.patch](tarball://root/attachments/some-uuid/ticket3918/trac_3918.patch) by @mwhansen created at 2008-09-08 10:25:03",
    "created_at": "2008-09-08T10:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3918#issuecomment-27971",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3918.patch](tarball://root/attachments/some-uuid/ticket3918/trac_3918.patch) by @mwhansen created at 2008-09-08 10:25:03



---

archive/issue_comments_027972.json:
```json
{
    "body": "For review, I first reproduced the bug using sage-3.1.1 and then tried to reproduce it with the patch applied. The bug seems to be fixed with the patch applied. I also made sure that uploading a file worked in general.",
    "created_at": "2008-09-08T11:12:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3918#issuecomment-27972",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

For review, I first reproduced the bug using sage-3.1.1 and then tried to reproduce it with the patch applied. The bug seems to be fixed with the patch applied. I also made sure that uploading a file worked in general.



---

archive/issue_comments_027973.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-09T00:40:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3918#issuecomment-27973",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027974.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc1",
    "created_at": "2008-09-09T00:40:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3918#issuecomment-27974",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.rc1



---

archive/issue_events_008984.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-09T00:40:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3918",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3918#event-8984"
}
```
