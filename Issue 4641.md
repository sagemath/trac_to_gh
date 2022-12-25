# Issue 4641: [with patch, needs review] "-notebook" commandline option should take trailing options

archive/issues_004641.json:
```json
{
    "body": "Assignee: @kwankyu\n\nKeywords: commandline option\n\nThe commandline option \"-notebook\" is advertised to take trailing options, but does not yet (as of Sage 3.1.2). A patch is included.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4641\n\n",
    "created_at": "2008-11-28T05:24:45Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "[with patch, needs review] \"-notebook\" commandline option should take trailing options",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4641",
    "user": "https://github.com/kwankyu"
}
```
Assignee: @kwankyu

Keywords: commandline option

The commandline option "-notebook" is advertised to take trailing options, but does not yet (as of Sage 3.1.2). A patch is included.

Issue created by migration from https://trac.sagemath.org/ticket/4641





---

archive/issue_comments_034867.json:
```json
{
    "body": "Attachment [1030.patch](tarball://root/attachments/some-uuid/ticket4641/1030.patch) by @kwankyu created at 2008-11-28 05:25:39",
    "created_at": "2008-11-28T05:25:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4641#issuecomment-34867",
    "user": "https://github.com/kwankyu"
}
```

Attachment [1030.patch](tarball://root/attachments/some-uuid/ticket4641/1030.patch) by @kwankyu created at 2008-11-28 05:25:39



---

archive/issue_comments_034868.json:
```json
{
    "body": "Changing assignee from @kwankyu to somebody.",
    "created_at": "2008-11-28T05:38:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4641#issuecomment-34868",
    "user": "https://github.com/kwankyu"
}
```

Changing assignee from @kwankyu to somebody.



---

archive/issue_comments_034869.json:
```json
{
    "body": "With the patch, the following works:\n\nsage -notebook \"address='10.0.1.199'\" secure=True open_viewer=False",
    "created_at": "2008-11-28T06:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4641#issuecomment-34869",
    "user": "https://github.com/kwankyu"
}
```

With the patch, the following works:

sage -notebook "address='10.0.1.199'" secure=True open_viewer=False



---

archive/issue_comments_034870.json:
```json
{
    "body": "This is *very* nice and a simple solution.  Excellent work!\n\nMabshoff -- apply the patch to the scripts repo.",
    "created_at": "2008-11-28T23:41:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4641#issuecomment-34870",
    "user": "https://github.com/williamstein"
}
```

This is *very* nice and a simple solution.  Excellent work!

Mabshoff -- apply the patch to the scripts repo.



---

archive/issue_comments_034871.json:
```json
{
    "body": "Merged in Sage 3.2.1.rc0",
    "created_at": "2008-11-28T23:49:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4641#issuecomment-34871",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.rc0



---

archive/issue_events_004888.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-11-28T23:49:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4641",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4641#event-4888"
}
```



---

archive/issue_comments_034872.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-28T23:49:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4641#issuecomment-34872",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
