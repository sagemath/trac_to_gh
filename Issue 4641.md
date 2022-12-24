# Issue 4641: [with patch, needs review] "-notebook" commandline option should take trailing options

archive/issues_004641.json:
```json
{
    "body": "Assignee: klee\n\nKeywords: commandline option\n\nThe commandline option \"-notebook\" is advertised to take trailing options, but does not yet (as of Sage 3.1.2). A patch is included.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4641\n\n",
    "created_at": "2008-11-28T05:24:45Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "[with patch, needs review] \"-notebook\" commandline option should take trailing options",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4641",
    "user": "klee"
}
```
Assignee: klee

Keywords: commandline option

The commandline option "-notebook" is advertised to take trailing options, but does not yet (as of Sage 3.1.2). A patch is included.

Issue created by migration from https://trac.sagemath.org/ticket/4641





---

archive/issue_comments_034935.json:
```json
{
    "body": "Attachment [1030.patch](tarball://root/attachments/some-uuid/ticket4641/1030.patch) by klee created at 2008-11-28 05:25:39",
    "created_at": "2008-11-28T05:25:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4641#issuecomment-34935",
    "user": "klee"
}
```

Attachment [1030.patch](tarball://root/attachments/some-uuid/ticket4641/1030.patch) by klee created at 2008-11-28 05:25:39



---

archive/issue_comments_034936.json:
```json
{
    "body": "Changing assignee from klee to somebody.",
    "created_at": "2008-11-28T05:38:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4641#issuecomment-34936",
    "user": "klee"
}
```

Changing assignee from klee to somebody.



---

archive/issue_comments_034937.json:
```json
{
    "body": "With the patch, the following works:\n\nsage -notebook \"address='10.0.1.199'\" secure=True open_viewer=False",
    "created_at": "2008-11-28T06:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4641#issuecomment-34937",
    "user": "klee"
}
```

With the patch, the following works:

sage -notebook "address='10.0.1.199'" secure=True open_viewer=False



---

archive/issue_comments_034938.json:
```json
{
    "body": "This is *very* nice and a simple solution.  Excellent work!\n\nMabshoff -- apply the patch to the scripts repo.",
    "created_at": "2008-11-28T23:41:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4641#issuecomment-34938",
    "user": "was"
}
```

This is *very* nice and a simple solution.  Excellent work!

Mabshoff -- apply the patch to the scripts repo.



---

archive/issue_comments_034939.json:
```json
{
    "body": "Merged in Sage 3.2.1.rc0",
    "created_at": "2008-11-28T23:49:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4641#issuecomment-34939",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.rc0



---

archive/issue_comments_034940.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-28T23:49:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4641#issuecomment-34940",
    "user": "mabshoff"
}
```

Resolution: fixed
