# Issue 9115: smart summing

archive/issues_009115.json:
```json
{
    "body": "Assignee: jason\n\nCC:  robertwb ncohen\n\nWe should extend the Sage sum function to call a magic method to handle summing things in the case of the python sum calling convention (and we shouldn't use the \"sum()\" method, as that name is probably way too likely to be used, and may be used for something else!)\n\nThis can take care of the performance issues at #9089 and #9061.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9115\n\n",
    "created_at": "2010-06-02T22:23:29Z",
    "labels": [
        "misc",
        "major",
        "enhancement"
    ],
    "title": "smart summing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9115",
    "user": "jason"
}
```
Assignee: jason

CC:  robertwb ncohen

We should extend the Sage sum function to call a magic method to handle summing things in the case of the python sum calling convention (and we shouldn't use the "sum()" method, as that name is probably way too likely to be used, and may be used for something else!)

This can take care of the performance issues at #9089 and #9061.

Issue created by migration from https://trac.sagemath.org/ticket/9115





---

archive/issue_comments_084803.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-06-02T22:25:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9115#issuecomment-84803",
    "user": "jason"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_084804.json:
```json
{
    "body": "Attachment [trac-9115.patch](tarball://root/attachments/some-uuid/ticket9115/trac-9115.patch) by jason created at 2010-06-02 22:25:27\n\nHere is an unfinished rough patch for the feature suggested at #9089.",
    "created_at": "2010-06-02T22:25:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9115#issuecomment-84804",
    "user": "jason"
}
```

Attachment [trac-9115.patch](tarball://root/attachments/some-uuid/ticket9115/trac-9115.patch) by jason created at 2010-06-02 22:25:27

Here is an unfinished rough patch for the feature suggested at #9089.
