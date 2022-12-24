# Issue 9425: bug in kernel_on() in "matrix2.pyx"

archive/issues_009425.json:
```json
{
    "body": "Assignee: jason, was\n\n\n```\nsage: V = span([[1/7,0,0] ,[0,1,0]], ZZ); V\nFree module of degree 3 and rank 2 over Integer Ring\nEchelon basis matrix:\n[1/7   0   0]\n[  0   1   0]\nsage: T = matrix(ZZ,3,[1,0,0,0,0,0,0,0,0]); T\n[1 0 0]\n[0 0 0]\n[0 0 0]\nsage: W = T.kernel_on(V); W.basis()\n[\n(0, 1, 0)\n]\nsage: W.is_submodule(V)\nFalse\n```\n\nThis is surprising, isn't it? (Patch comes up in a minute, but I need to create the ticket first.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/9425\n\n",
    "created_at": "2010-07-04T21:31:40Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "bug in kernel_on() in \"matrix2.pyx\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9425",
    "user": "GeorgSWeber"
}
```
Assignee: jason, was


```
sage: V = span([[1/7,0,0] ,[0,1,0]], ZZ); V
Free module of degree 3 and rank 2 over Integer Ring
Echelon basis matrix:
[1/7   0   0]
[  0   1   0]
sage: T = matrix(ZZ,3,[1,0,0,0,0,0,0,0,0]); T
[1 0 0]
[0 0 0]
[0 0 0]
sage: W = T.kernel_on(V); W.basis()
[
(0, 1, 0)
]
sage: W.is_submodule(V)
False
```

This is surprising, isn't it? (Patch comes up in a minute, but I need to create the ticket first.)

Issue created by migration from https://trac.sagemath.org/ticket/9425





---

archive/issue_comments_089915.json:
```json
{
    "body": "Attachment [trac_9425_kernel_on.patch](tarball://root/attachments/some-uuid/ticket9425/trac_9425_kernel_on.patch) by GeorgSWeber created at 2010-07-04 21:45:48\n\ncreated against the older Sage-4.4.2, but that shouldn't matter",
    "created_at": "2010-07-04T21:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9425#issuecomment-89915",
    "user": "GeorgSWeber"
}
```

Attachment [trac_9425_kernel_on.patch](tarball://root/attachments/some-uuid/ticket9425/trac_9425_kernel_on.patch) by GeorgSWeber created at 2010-07-04 21:45:48

created against the older Sage-4.4.2, but that shouldn't matter



---

archive/issue_comments_089916.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-04T21:46:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9425#issuecomment-89916",
    "user": "GeorgSWeber"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089917.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-05T10:53:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9425#issuecomment-89917",
    "user": "@williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089918.json:
```json
{
    "body": "Looks good to me.  Thanks!",
    "created_at": "2010-07-05T10:53:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9425#issuecomment-89918",
    "user": "@williamstein"
}
```

Looks good to me.  Thanks!



---

archive/issue_comments_089919.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T08:21:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9425#issuecomment-89919",
    "user": "@qed777"
}
```

Resolution: fixed
