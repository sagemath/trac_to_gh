# Issue 6233: remove the explain_picklejar function, since it is self contained and its test fails on all platforms

archive/issues_006233.json:
```json
{
    "body": "Assignee: tbd\n\nThe doctest for explain_picklejar fails on all platforms.  Thus the choice is to either remove explain_pickle entirely, fix the bug (needs cwitty), or remove that one function.  This ticket removes that one function explain_picklejar until cwitty fixes it. \n\nIssue created by migration from https://trac.sagemath.org/ticket/6233\n\n",
    "created_at": "2009-06-06T16:16:24Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "remove the explain_picklejar function, since it is self contained and its test fails on all platforms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6233",
    "user": "@williamstein"
}
```
Assignee: tbd

The doctest for explain_picklejar fails on all platforms.  Thus the choice is to either remove explain_pickle entirely, fix the bug (needs cwitty), or remove that one function.  This ticket removes that one function explain_picklejar until cwitty fixes it. 

Issue created by migration from https://trac.sagemath.org/ticket/6233





---

archive/issue_comments_049731.json:
```json
{
    "body": "Attachment [trac_6233.patch](tarball://root/attachments/some-uuid/ticket6233/trac_6233.patch) by @williamstein created at 2009-06-06 16:21:05",
    "created_at": "2009-06-06T16:21:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6233#issuecomment-49731",
    "user": "@williamstein"
}
```

Attachment [trac_6233.patch](tarball://root/attachments/some-uuid/ticket6233/trac_6233.patch) by @williamstein created at 2009-06-06 16:21:05



---

archive/issue_comments_049732.json:
```json
{
    "body": "Note that I think this was merged into 4.0.1 already, over a week ago in order to get that release out.",
    "created_at": "2009-06-15T23:48:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6233#issuecomment-49732",
    "user": "@williamstein"
}
```

Note that I think this was merged into 4.0.1 already, over a week ago in order to get that release out.



---

archive/issue_comments_049733.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-20T01:59:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6233#issuecomment-49733",
    "user": "@mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_049734.json:
```json
{
    "body": "Yep.  I believe this was.",
    "created_at": "2009-06-20T01:59:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6233#issuecomment-49734",
    "user": "@mwhansen"
}
```

Yep.  I believe this was.
