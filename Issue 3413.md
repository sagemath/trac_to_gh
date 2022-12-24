# Issue 3413: [with patch; needs review] sage-3.0.3.alpha2 -- endianess issue with time_series doctest

archive/issues_003413.json:
```json
{
    "body": "Assignee: @williamstein\n\nTwo of the doctests for time_series.pyx have endianess issues on osxppc.  I fixed them.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3413\n\n",
    "created_at": "2008-06-13T14:21:32Z",
    "labels": [
        "finance",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "[with patch; needs review] sage-3.0.3.alpha2 -- endianess issue with time_series doctest",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3413",
    "user": "@williamstein"
}
```
Assignee: @williamstein

Two of the doctests for time_series.pyx have endianess issues on osxppc.  I fixed them.

Issue created by migration from https://trac.sagemath.org/ticket/3413





---

archive/issue_comments_023936.json:
```json
{
    "body": "Attachment [sage-3413.patch](tarball://root/attachments/some-uuid/ticket3413/sage-3413.patch) by mabshoff created at 2008-06-15 19:03:58\n\nWe need a review for this patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-15T19:03:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3413#issuecomment-23936",
    "user": "mabshoff"
}
```

Attachment [sage-3413.patch](tarball://root/attachments/some-uuid/ticket3413/sage-3413.patch) by mabshoff created at 2008-06-15 19:03:58

We need a review for this patch.

Cheers,

Michael



---

archive/issue_comments_023937.json:
```json
{
    "body": "William is going to add one more tiny (literally 5 character) patch, and this will be ready to go.",
    "created_at": "2008-06-15T20:33:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3413#issuecomment-23937",
    "user": "@craigcitro"
}
```

William is going to add one more tiny (literally 5 character) patch, and this will be ready to go.



---

archive/issue_comments_023938.json:
```json
{
    "body": "adds \",2\"; and works.",
    "created_at": "2008-06-15T22:38:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3413#issuecomment-23938",
    "user": "@williamstein"
}
```

adds ",2"; and works.



---

archive/issue_comments_023939.json:
```json
{
    "body": "Attachment [9840.patch](tarball://root/attachments/some-uuid/ticket3413/9840.patch) by @craigcitro created at 2008-06-15 22:41:21\n\nLooks good. It's ready to go.",
    "created_at": "2008-06-15T22:41:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3413#issuecomment-23939",
    "user": "@craigcitro"
}
```

Attachment [9840.patch](tarball://root/attachments/some-uuid/ticket3413/9840.patch) by @craigcitro created at 2008-06-15 22:41:21

Looks good. It's ready to go.



---

archive/issue_comments_023940.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-16T04:56:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3413#issuecomment-23940",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_023941.json:
```json
{
    "body": "Merged in Sage 3.0.3.rc0",
    "created_at": "2008-06-16T04:56:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3413#issuecomment-23941",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.3.rc0
