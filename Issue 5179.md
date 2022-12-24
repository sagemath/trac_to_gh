# Issue 5179: Delete __getslice__ from matrices

archive/issues_005179.json:
```json
{
    "body": "Assignee: was\n\n`__getslice__` has been deprecated for a long time in Python.  This patch adds equivalent functionality to `__getitem__`, which is where the functionality should be.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5179\n\n",
    "created_at": "2009-02-04T18:31:44Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Delete __getslice__ from matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5179",
    "user": "jason"
}
```
Assignee: was

`__getslice__` has been deprecated for a long time in Python.  This patch adds equivalent functionality to `__getitem__`, which is where the functionality should be.

Issue created by migration from https://trac.sagemath.org/ticket/5179





---

archive/issue_comments_039711.json:
```json
{
    "body": "Attachment [delete-getslice.patch](tarball://root/attachments/some-uuid/ticket5179/delete-getslice.patch) by jason created at 2009-02-04 18:32:33",
    "created_at": "2009-02-04T18:32:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5179#issuecomment-39711",
    "user": "jason"
}
```

Attachment [delete-getslice.patch](tarball://root/attachments/some-uuid/ticket5179/delete-getslice.patch) by jason created at 2009-02-04 18:32:33



---

archive/issue_comments_039712.json:
```json
{
    "body": "I thought I opened another ticket for this issue and posted a patch there, but I cannot find it at all.  If there is another ticket open at this time with a patch, this ticket and patch supersedes it.",
    "created_at": "2009-02-04T18:33:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5179#issuecomment-39712",
    "user": "jason"
}
```

I thought I opened another ticket for this issue and posted a patch there, but I cannot find it at all.  If there is another ticket open at this time with a patch, this ticket and patch supersedes it.



---

archive/issue_comments_039713.json:
```json
{
    "body": "Code looks good, all doctests pass.\n\nPositive review.",
    "created_at": "2009-02-05T05:00:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5179#issuecomment-39713",
    "user": "cwitty"
}
```

Code looks good, all doctests pass.

Positive review.



---

archive/issue_comments_039714.json:
```json
{
    "body": "Merged in Sage 3.3.alpha6.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-05T10:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5179#issuecomment-39714",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha6.

Cheers,

Michael



---

archive/issue_comments_039715.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-05T10:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5179#issuecomment-39715",
    "user": "mabshoff"
}
```

Resolution: fixed
