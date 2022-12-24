# Issue 3433: notebook -- change it so worksheet text is *not* stored in the notebook/worksheet objects when pickling and unpickling

archive/issues_003433.json:
```json
{
    "body": "Assignee: boothby\n\nThis is a major efficiency problem with large notebooks.  The fix is to write custom worksheet __reduce__ and load methods that do not store the actual worksheet text in the object, but instead store it to disk and read it from disk.  That reading from disk should only happen when the worksheet is actually \"activated\", i.e., not when unpickling!\n\nIssue created by migration from https://trac.sagemath.org/ticket/3433\n\n",
    "created_at": "2008-06-15T22:51:57Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "notebook -- change it so worksheet text is *not* stored in the notebook/worksheet objects when pickling and unpickling",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3433",
    "user": "@williamstein"
}
```
Assignee: boothby

This is a major efficiency problem with large notebooks.  The fix is to write custom worksheet __reduce__ and load methods that do not store the actual worksheet text in the object, but instead store it to disk and read it from disk.  That reading from disk should only happen when the worksheet is actually "activated", i.e., not when unpickling!

Issue created by migration from https://trac.sagemath.org/ticket/3433





---

archive/issue_comments_024198.json:
```json
{
    "body": "Mhh, did William not fix this already when speeding up the notebook saving?\n\nCheers,\n\nMichael",
    "created_at": "2008-07-31T02:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3433#issuecomment-24198",
    "user": "mabshoff"
}
```

Mhh, did William not fix this already when speeding up the notebook saving?

Cheers,

Michael



---

archive/issue_comments_024199.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T02:50:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3433#issuecomment-24199",
    "user": "@aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_024200.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-11-14T08:21:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3433#issuecomment-24200",
    "user": "@mwhansen"
}
```

Resolution: invalid
