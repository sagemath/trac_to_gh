# Issue 5253: Make a jacobian function which computes the jacobian matrix

archive/issues_005253.json:
```json
{
    "body": "Assignee: @burcin\n\nAttached patch computes the Jacobian matrix, the matrix of partial derivatives of a multivariable function from R^n to R^m.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5253\n\n",
    "created_at": "2009-02-13T05:08:19Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Make a jacobian function which computes the jacobian matrix",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5253",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @burcin

Attached patch computes the Jacobian matrix, the matrix of partial derivatives of a multivariable function from R^n to R^m.

Issue created by migration from https://trac.sagemath.org/ticket/5253





---

archive/issue_comments_040228.json:
```json
{
    "body": "Attachment [trac_5253-jacobian.patch](tarball://root/attachments/some-uuid/ticket5253/trac_5253-jacobian.patch) by @jasongrout created at 2009-02-13 05:11:24",
    "created_at": "2009-02-13T05:11:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5253#issuecomment-40228",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_5253-jacobian.patch](tarball://root/attachments/some-uuid/ticket5253/trac_5253-jacobian.patch) by @jasongrout created at 2009-02-13 05:11:24



---

archive/issue_comments_040229.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-13T05:49:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5253#issuecomment-40229",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040230.json:
```json
{
    "body": "Changing assignee from @burcin to @jasongrout.",
    "created_at": "2009-02-13T05:49:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5253#issuecomment-40230",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @burcin to @jasongrout.



---

archive/issue_comments_040231.json:
```json
{
    "body": "Does what it says, code looks reasonable, all doctests pass.  (I'm not sure if the set of special cases controlling which types it will handle is \"right\", but that can be fixed later if somebody has specific complaints.)\n\nPositive review.",
    "created_at": "2009-02-13T18:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5253#issuecomment-40231",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Does what it says, code looks reasonable, all doctests pass.  (I'm not sure if the set of special cases controlling which types it will handle is "right", but that can be fixed later if somebody has specific complaints.)

Positive review.



---

archive/issue_comments_040232.json:
```json
{
    "body": "FYI, the special casing is because there is no good way right now to represent a function from R<sup>n</sup> to R<sup>m</sup>.  I think people would naturally use either a list, tuple, or vector of symbolic expressions.  The Matrix special case is so that you can do nested jacobians to compute the hessian matrix, like what is illustrated in the doctests.",
    "created_at": "2009-02-13T19:45:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5253#issuecomment-40232",
    "user": "https://github.com/jasongrout"
}
```

FYI, the special casing is because there is no good way right now to represent a function from R<sup>n</sup> to R<sup>m</sup>.  I think people would naturally use either a list, tuple, or vector of symbolic expressions.  The Matrix special case is so that you can do nested jacobians to compute the hessian matrix, like what is illustrated in the doctests.



---

archive/issue_comments_040233.json:
```json
{
    "body": "Merged in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T09:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5253#issuecomment-40233",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.rc1.

Cheers,

Michael



---

archive/issue_comments_040234.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-14T09:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5253#issuecomment-40234",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005509.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-02-14T09:03:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5253",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5253#event-5509"
}
```
