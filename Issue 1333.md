# Issue 1333: [with trivial patch] fix a major inefficiency in floating point square root computation in Sage

archive/issues_001333.json:
```json
{
    "body": "Assignee: somebody\n\nPaul Zimmerman's benchmarks unveiled a serious slowdown in x.sqrt() for x mpfr.\n\nThis patch fixes the problem. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1333\n\n",
    "created_at": "2007-11-29T06:53:50Z",
    "labels": [
        "component: basic arithmetic"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "[with trivial patch] fix a major inefficiency in floating point square root computation in Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1333",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

Paul Zimmerman's benchmarks unveiled a serious slowdown in x.sqrt() for x mpfr.

This patch fixes the problem. 

Issue created by migration from https://trac.sagemath.org/ticket/1333





---

archive/issue_comments_008503.json:
```json
{
    "body": "Attachment [trac1333.patch](tarball://root/attachments/some-uuid/ticket1333/trac1333.patch) by @williamstein created at 2007-11-29 06:54:49",
    "created_at": "2007-11-29T06:54:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1333#issuecomment-8503",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac1333.patch](tarball://root/attachments/some-uuid/ticket1333/trac1333.patch) by @williamstein created at 2007-11-29 06:54:49



---

archive/issue_comments_008504.json:
```json
{
    "body": "(I didn't actually test it, but...) looks good to me.",
    "created_at": "2007-12-01T03:27:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1333#issuecomment-8504",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

(I didn't actually test it, but...) looks good to me.



---

archive/issue_comments_008505.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-01T18:21:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1333#issuecomment-8505",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_008506.json:
```json
{
    "body": "Merged in 2.8.15.alpha1.",
    "created_at": "2007-12-01T18:21:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1333#issuecomment-8506",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.15.alpha1.
