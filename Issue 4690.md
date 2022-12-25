# Issue 4690: [with patch; needs review] Sage hangs on derivative of piecewise function

archive/issues_004690.json:
```json
{
    "body": "Assignee: @burcin\n\nDerivatives of piecewise functions where some piece uses multiplication causes Sage to hang. Example code:\n\n\n```\nPiecewise([[(0,1), x * 2]]).derivative()\n```\n\n\nIt hangs waiting for Maxima to return a result, which is because the expression it sends to Maxima is not formatted properly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4690\n\n",
    "created_at": "2008-12-04T01:22:32Z",
    "labels": [
        "component: calculus",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "[with patch; needs review] Sage hangs on derivative of piecewise function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4690",
    "user": "https://trac.sagemath.org/admin/accounts/users/pbutler"
}
```
Assignee: @burcin

Derivatives of piecewise functions where some piece uses multiplication causes Sage to hang. Example code:


```
Piecewise([[(0,1), x * 2]]).derivative()
```


It hangs waiting for Maxima to return a result, which is because the expression it sends to Maxima is not formatted properly.

Issue created by migration from https://trac.sagemath.org/ticket/4690





---

archive/issue_comments_035284.json:
```json
{
    "body": "Attachment [piecewise_derivative.patch](tarball://root/attachments/some-uuid/ticket4690/piecewise_derivative.patch) by pbutler created at 2008-12-04 01:23:15\n\nPatch file for piecewise derivative",
    "created_at": "2008-12-04T01:23:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4690",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4690#issuecomment-35284",
    "user": "https://trac.sagemath.org/admin/accounts/users/pbutler"
}
```

Attachment [piecewise_derivative.patch](tarball://root/attachments/some-uuid/ticket4690/piecewise_derivative.patch) by pbutler created at 2008-12-04 01:23:15

Patch file for piecewise derivative



---

archive/issue_comments_035285.json:
```json
{
    "body": "Paul,\n\nplease make sure to assign a milestone. Usually that is the next open one.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-04T01:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4690",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4690#issuecomment-35285",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Paul,

please make sure to assign a milestone. Usually that is the next open one.

Cheers,

Michael



---

archive/issue_comments_035286.json:
```json
{
    "body": "Looks good to me.  This can go in.\n\nBut, piecewise.py needs some _MAJOR_ work for which I will open up a new ticket.",
    "created_at": "2008-12-04T08:29:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4690",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4690#issuecomment-35286",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.  This can go in.

But, piecewise.py needs some _MAJOR_ work for which I will open up a new ticket.



---

archive/issue_comments_035287.json:
```json
{
    "body": "Paul,\n\nin the future please post hg patches and not diffs, i.e. check in your changes and then export a patch. In this case I have committed the changes in your name so that the credit in the hg log is properly assigned.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-04T14:12:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4690",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4690#issuecomment-35287",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Paul,

in the future please post hg patches and not diffs, i.e. check in your changes and then export a patch. In this case I have committed the changes in your name so that the credit in the hg log is properly assigned.

Cheers,

Michael



---

archive/issue_comments_035288.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-04T14:13:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4690",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4690#issuecomment-35288",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_035289.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha0",
    "created_at": "2008-12-04T14:13:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4690",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4690#issuecomment-35289",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.2.alpha0
