# Issue 527: gap -- gap_reset_workspace()

archive/issues_000527.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe gap workspace cache should be invalidated not only when the version of gap changes but when the\nspkg version number changes.  This very important. \n\nIssue created by migration from https://trac.sagemath.org/ticket/527\n\n",
    "created_at": "2007-08-30T06:49:55Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.12",
    "title": "gap -- gap_reset_workspace()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/527",
    "user": "@williamstein"
}
```
Assignee: @williamstein

The gap workspace cache should be invalidated not only when the version of gap changes but when the
spkg version number changes.  This very important. 

Issue created by migration from https://trac.sagemath.org/ticket/527





---

archive/issue_comments_002680.json:
```json
{
    "body": "Actually invalidate it even when SAGE is upgraded at all!",
    "created_at": "2007-09-07T18:30:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/527#issuecomment-2680",
    "user": "@williamstein"
}
```

Actually invalidate it even when SAGE is upgraded at all!



---

archive/issue_comments_002681.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2007-09-07T18:30:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/527#issuecomment-2681",
    "user": "@williamstein"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_002682.json:
```json
{
    "body": "Changing priority from blocker to critical.",
    "created_at": "2007-10-05T06:42:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/527#issuecomment-2682",
    "user": "@williamstein"
}
```

Changing priority from blocker to critical.



---

archive/issue_comments_002683.json:
```json
{
    "body": "This ticket is related to #407.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-19T18:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/527#issuecomment-2683",
    "user": "mabshoff"
}
```

This ticket is related to #407.

Cheers,

Michael



---

archive/issue_comments_002684.json:
```json
{
    "body": "Attachment [trac527.patch](tarball://root/attachments/some-uuid/ticket527/trac527.patch) by @williamstein created at 2007-11-03 19:21:11",
    "created_at": "2007-11-03T19:21:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/527#issuecomment-2684",
    "user": "@williamstein"
}
```

Attachment [trac527.patch](tarball://root/attachments/some-uuid/ticket527/trac527.patch) by @williamstein created at 2007-11-03 19:21:11



---

archive/issue_comments_002685.json:
```json
{
    "body": "It is also a good idea to replace the gap packages by these:\n(I didn't up the version, since forcing an upgrade is pointless.)\n\n  http://sage.math.washington.edu/tmp/gap-4.4.10.spkg\n\nThis is for the next release manager.",
    "created_at": "2007-11-03T19:22:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/527#issuecomment-2685",
    "user": "@williamstein"
}
```

It is also a good idea to replace the gap packages by these:
(I didn't up the version, since forcing an upgrade is pointless.)

  http://sage.math.washington.edu/tmp/gap-4.4.10.spkg

This is for the next release manager.



---

archive/issue_comments_002686.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-03T19:22:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/527#issuecomment-2686",
    "user": "@williamstein"
}
```

Resolution: fixed
