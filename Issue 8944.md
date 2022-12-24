# Issue 8944: 32 vs. 64 bit issues in matrix1.pyx

archive/issues_008944.json:
```json
{
    "body": "Assignee: tbd\n\nFrom this [sage-devel](http://groups.google.com/group/sage-devel/msg/dbe5b953a06d1f39) report:\n\n\n```\nThe first on seems to be a trivial 32-bit vs. 64-bit\nissue (probably occurs on any 32-bit machine, even without the \"long\"\noption):\n\nsage -t -long \"devel/sage/sage/matrix/matrix1.pyx\"\n**********************************************************************\nFile \"/Users/Shared/sage/test/sage-4.4.2.alpha0/devel/sage/sage/matrix/\nmatrix1.pyx\", line 460:\n    sage: b.dtype\nExpected:\n    dtype('int64')\nGot:\n    dtype('int32')\n********************************************************************** \n```\n\n\nThis also happens on the Skynet machine cicero, a 32-bit Fedora 12 machine.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8944\n\n",
    "created_at": "2010-05-10T11:01:12Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "32 vs. 64 bit issues in matrix1.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8944",
    "user": "mvngu"
}
```
Assignee: tbd

From this [sage-devel](http://groups.google.com/group/sage-devel/msg/dbe5b953a06d1f39) report:


```
The first on seems to be a trivial 32-bit vs. 64-bit
issue (probably occurs on any 32-bit machine, even without the "long"
option):

sage -t -long "devel/sage/sage/matrix/matrix1.pyx"
**********************************************************************
File "/Users/Shared/sage/test/sage-4.4.2.alpha0/devel/sage/sage/matrix/
matrix1.pyx", line 460:
    sage: b.dtype
Expected:
    dtype('int64')
Got:
    dtype('int32')
********************************************************************** 
```


This also happens on the Skynet machine cicero, a 32-bit Fedora 12 machine.

Issue created by migration from https://trac.sagemath.org/ticket/8944





---

archive/issue_comments_082352.json:
```json
{
    "body": "Attachment [trac_8944.patch](tarball://root/attachments/some-uuid/ticket8944/trac_8944.patch) by mvngu created at 2010-05-10 11:19:59\n\nbased on Sage 4.4.2.alpha0",
    "created_at": "2010-05-10T11:19:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8944#issuecomment-82352",
    "user": "mvngu"
}
```

Attachment [trac_8944.patch](tarball://root/attachments/some-uuid/ticket8944/trac_8944.patch) by mvngu created at 2010-05-10 11:19:59

based on Sage 4.4.2.alpha0



---

archive/issue_comments_082353.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-10T11:20:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8944#issuecomment-82353",
    "user": "mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082354.json:
```json
{
    "body": "Works fine on both 32 and 64 bit machines.",
    "created_at": "2010-05-11T13:06:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8944#issuecomment-82354",
    "user": "@JohnCremona"
}
```

Works fine on both 32 and 64 bit machines.



---

archive/issue_comments_082355.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-11T13:06:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8944#issuecomment-82355",
    "user": "@JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082356.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-12T22:43:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8944#issuecomment-82356",
    "user": "mvngu"
}
```

Resolution: fixed
