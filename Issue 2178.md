# Issue 2178: latex2html does not like $+$

archive/issues_002178.json:
```json
{
    "body": "Assignee: cwitty\n\nBill Purvis points out (http://groups.google.com/group/sage-support/browse_thread/thread/9531e60cda199e6d#) a problem in the reference manual that seems to be caused by latex2html doing the wrong thing with $+$.\n\nI'll have a patch for this problem shortly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2178\n\n",
    "created_at": "2008-02-16T15:55:18Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "latex2html does not like $+$",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2178",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: cwitty

Bill Purvis points out (http://groups.google.com/group/sage-support/browse_thread/thread/9531e60cda199e6d#) a problem in the reference manual that seems to be caused by latex2html doing the wrong thing with $+$.

I'll have a patch for this problem shortly.

Issue created by migration from https://trac.sagemath.org/ticket/2178





---

archive/issue_comments_014265.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-16T16:11:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2178#issuecomment-14265",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014266.json:
```json
{
    "body": "Attachment [trac-2178.patch](tarball://root/attachments/some-uuid/ticket2178/trac-2178.patch) by cwitty created at 2008-02-16 17:28:00\n\nThe attached patch avoids the problem.  It also patches docstrings that create TeX errors on my laptop, so that I can actually build the refman.",
    "created_at": "2008-02-16T17:28:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2178#issuecomment-14266",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac-2178.patch](tarball://root/attachments/some-uuid/ticket2178/trac-2178.patch) by cwitty created at 2008-02-16 17:28:00

The attached patch avoids the problem.  It also patches docstrings that create TeX errors on my laptop, so that I can actually build the refman.



---

archive/issue_comments_014267.json:
```json
{
    "body": "We do not use `\\mathbb` since it doesn't work with jsmath. Patch looks good.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-16T18:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2178#issuecomment-14267",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

We do not use `\mathbb` since it doesn't work with jsmath. Patch looks good.

Cheers,

Michael



---

archive/issue_comments_014268.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-16T18:15:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2178#issuecomment-14268",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014269.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-16T18:15:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2178#issuecomment-14269",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha1
