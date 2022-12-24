# Issue 895: [with patch] .inverse() method for matrices

archive/issues_000895.json:
```json
{
    "body": "Assignee: mhansen\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/895\n\n",
    "created_at": "2007-10-13T23:47:18Z",
    "labels": [
        "linear algebra",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.9",
    "title": "[with patch] .inverse() method for matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/895",
    "user": "mhansen"
}
```
Assignee: mhansen



Issue created by migration from https://trac.sagemath.org/ticket/895





---

archive/issue_comments_005510.json:
```json
{
    "body": "Attachment [6721.patch](tarball://root/attachments/some-uuid/ticket895/6721.patch) by was created at 2007-10-19 01:12:43\n\nThis patch needs some work:\n\n1. It should be in matrix2.pyx not matrix_dense.pyx, so it will be available to both sparse and dense matrices.\n\n2. It should call m.__invert__() instead of do m**(-1).      Or it could call ~m, which is the Python notation for __invert__.\n\n3. The docstring should also mention doing ~m.\n\nWilliam",
    "created_at": "2007-10-19T01:12:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/895#issuecomment-5510",
    "user": "was"
}
```

Attachment [6721.patch](tarball://root/attachments/some-uuid/ticket895/6721.patch) by was created at 2007-10-19 01:12:43

This patch needs some work:

1. It should be in matrix2.pyx not matrix_dense.pyx, so it will be available to both sparse and dense matrices.

2. It should call m.__invert__() instead of do m**(-1).      Or it could call ~m, which is the Python notation for __invert__.

3. The docstring should also mention doing ~m.

William



---

archive/issue_comments_005511.json:
```json
{
    "body": "Attachment [6971.patch](tarball://root/attachments/some-uuid/ticket895/6971.patch) by mhansen created at 2007-10-19 21:27:26\n\nUpadated patch -- use the last one and ignore the first one.",
    "created_at": "2007-10-19T21:27:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/895#issuecomment-5511",
    "user": "mhansen"
}
```

Attachment [6971.patch](tarball://root/attachments/some-uuid/ticket895/6971.patch) by mhansen created at 2007-10-19 21:27:26

Upadated patch -- use the last one and ignore the first one.



---

archive/issue_comments_005512.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-21T03:34:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/895#issuecomment-5512",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_005513.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-10-21T03:34:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/895#issuecomment-5513",
    "user": "was"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_005514.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-10-21T03:34:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/895#issuecomment-5514",
    "user": "was"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_005515.json:
```json
{
    "body": "applied to 2.8.9.alpha0",
    "created_at": "2007-10-23T19:48:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/895#issuecomment-5515",
    "user": "malb"
}
```

applied to 2.8.9.alpha0



---

archive/issue_comments_005516.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-23T19:48:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/895#issuecomment-5516",
    "user": "malb"
}
```

Resolution: fixed
