# Issue 5253: Make a jacobian function which computes the jacobian matrix

archive/issues_005253.json:
```json
{
    "body": "Assignee: burcin\n\nAttached patch computes the Jacobian matrix, the matrix of partial derivatives of a multivariable function from R^n to R^m.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5253\n\n",
    "created_at": "2009-02-13T05:08:19Z",
    "labels": [
        "calculus",
        "major",
        "enhancement"
    ],
    "title": "Make a jacobian function which computes the jacobian matrix",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5253",
    "user": "jason"
}
```
Assignee: burcin

Attached patch computes the Jacobian matrix, the matrix of partial derivatives of a multivariable function from R^n to R^m.

Issue created by migration from https://trac.sagemath.org/ticket/5253





---

archive/issue_comments_040307.json:
```json
{
    "body": "Attachment [trac_5253-jacobian.patch](tarball://root/attachments/some-uuid/ticket5253/trac_5253-jacobian.patch) by jason created at 2009-02-13 05:11:24",
    "created_at": "2009-02-13T05:11:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5253#issuecomment-40307",
    "user": "jason"
}
```

Attachment [trac_5253-jacobian.patch](tarball://root/attachments/some-uuid/ticket5253/trac_5253-jacobian.patch) by jason created at 2009-02-13 05:11:24



---

archive/issue_comments_040308.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-13T05:49:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5253#issuecomment-40308",
    "user": "jason"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040309.json:
```json
{
    "body": "Changing assignee from burcin to jason.",
    "created_at": "2009-02-13T05:49:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5253#issuecomment-40309",
    "user": "jason"
}
```

Changing assignee from burcin to jason.



---

archive/issue_comments_040310.json:
```json
{
    "body": "Does what it says, code looks reasonable, all doctests pass.  (I'm not sure if the set of special cases controlling which types it will handle is \"right\", but that can be fixed later if somebody has specific complaints.)\n\nPositive review.",
    "created_at": "2009-02-13T18:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5253#issuecomment-40310",
    "user": "cwitty"
}
```

Does what it says, code looks reasonable, all doctests pass.  (I'm not sure if the set of special cases controlling which types it will handle is "right", but that can be fixed later if somebody has specific complaints.)

Positive review.



---

archive/issue_comments_040311.json:
```json
{
    "body": "FYI, the special casing is because there is no good way right now to represent a function from R<sup>n</sup> to R<sup>m</sup>.  I think people would naturally use either a list, tuple, or vector of symbolic expressions.  The Matrix special case is so that you can do nested jacobians to compute the hessian matrix, like what is illustrated in the doctests.",
    "created_at": "2009-02-13T19:45:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5253#issuecomment-40311",
    "user": "jason"
}
```

FYI, the special casing is because there is no good way right now to represent a function from R<sup>n</sup> to R<sup>m</sup>.  I think people would naturally use either a list, tuple, or vector of symbolic expressions.  The Matrix special case is so that you can do nested jacobians to compute the hessian matrix, like what is illustrated in the doctests.



---

archive/issue_comments_040312.json:
```json
{
    "body": "Merged in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T09:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5253#issuecomment-40312",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.rc1.

Cheers,

Michael



---

archive/issue_comments_040313.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-14T09:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5253#issuecomment-40313",
    "user": "mabshoff"
}
```

Resolution: fixed
