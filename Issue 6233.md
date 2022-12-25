# Issue 6233: remove the explain_picklejar function, since it is self contained and its test fails on all platforms

archive/issues_006233.json:
```json
{
    "body": "Assignee: tbd\n\nThe doctest for explain_picklejar fails on all platforms.  Thus the choice is to either remove explain_pickle entirely, fix the bug (needs cwitty), or remove that one function.  This ticket removes that one function explain_picklejar until cwitty fixes it. \n\nIssue created by migration from https://trac.sagemath.org/ticket/6233\n\n",
    "created_at": "2009-06-06T16:16:24Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "remove the explain_picklejar function, since it is self contained and its test fails on all platforms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6233",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

The doctest for explain_picklejar fails on all platforms.  Thus the choice is to either remove explain_pickle entirely, fix the bug (needs cwitty), or remove that one function.  This ticket removes that one function explain_picklejar until cwitty fixes it. 

Issue created by migration from https://trac.sagemath.org/ticket/6233





---

archive/issue_comments_049636.json:
```json
{
    "body": "Attachment [trac_6233.patch](tarball://root/attachments/some-uuid/ticket6233/trac_6233.patch) by @williamstein created at 2009-06-06 16:21:05",
    "created_at": "2009-06-06T16:21:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6233#issuecomment-49636",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_6233.patch](tarball://root/attachments/some-uuid/ticket6233/trac_6233.patch) by @williamstein created at 2009-06-06 16:21:05



---

archive/issue_comments_049637.json:
```json
{
    "body": "Note that I think this was merged into 4.0.1 already, over a week ago in order to get that release out.",
    "created_at": "2009-06-15T23:48:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6233#issuecomment-49637",
    "user": "https://github.com/williamstein"
}
```

Note that I think this was merged into 4.0.1 already, over a week ago in order to get that release out.



---

archive/issue_comments_049638.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-20T01:59:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6233#issuecomment-49638",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_049639.json:
```json
{
    "body": "Yep.  I believe this was.",
    "created_at": "2009-06-20T01:59:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6233#issuecomment-49639",
    "user": "https://github.com/mwhansen"
}
```

Yep.  I believe this was.
