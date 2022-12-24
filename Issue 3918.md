# Issue 3918: notebook -- MAJOR BUG involving uploading file from URL

archive/issues_003918.json:
```json
{
    "body": "Assignee: boothby\n\n1. Go to Data --> Upload File\n2. Select a URL that takes \"forever\" to download.\n3. Now the ENTIRE SERVER hangs \"forever\".  \n\nThis is clearly very much not good. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3918\n\n",
    "created_at": "2008-08-20T23:17:14Z",
    "labels": [
        "notebook",
        "critical",
        "bug"
    ],
    "title": "notebook -- MAJOR BUG involving uploading file from URL",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3918",
    "user": "was"
}
```
Assignee: boothby

1. Go to Data --> Upload File
2. Select a URL that takes "forever" to download.
3. Now the ENTIRE SERVER hangs "forever".  

This is clearly very much not good. 

Issue created by migration from https://trac.sagemath.org/ticket/3918





---

archive/issue_comments_028027.json:
```json
{
    "body": "Changing assignee from boothby to mhansen.",
    "created_at": "2008-09-08T10:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3918#issuecomment-28027",
    "user": "mhansen"
}
```

Changing assignee from boothby to mhansen.



---

archive/issue_comments_028028.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-08T10:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3918#issuecomment-28028",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_028029.json:
```json
{
    "body": "Attachment [trac_3918.patch](tarball://root/attachments/some-uuid/ticket3918/trac_3918.patch) by mhansen created at 2008-09-08 10:25:03",
    "created_at": "2008-09-08T10:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3918#issuecomment-28029",
    "user": "mhansen"
}
```

Attachment [trac_3918.patch](tarball://root/attachments/some-uuid/ticket3918/trac_3918.patch) by mhansen created at 2008-09-08 10:25:03



---

archive/issue_comments_028030.json:
```json
{
    "body": "For review, I first reproduced the bug using sage-3.1.1 and then tried to reproduce it with the patch applied. The bug seems to be fixed with the patch applied. I also made sure that uploading a file worked in general.",
    "created_at": "2008-09-08T11:12:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3918#issuecomment-28030",
    "user": "TimothyClemans"
}
```

For review, I first reproduced the bug using sage-3.1.1 and then tried to reproduce it with the patch applied. The bug seems to be fixed with the patch applied. I also made sure that uploading a file worked in general.



---

archive/issue_comments_028031.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-09T00:40:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3918#issuecomment-28031",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_028032.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc1",
    "created_at": "2008-09-09T00:40:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3918#issuecomment-28032",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc1
