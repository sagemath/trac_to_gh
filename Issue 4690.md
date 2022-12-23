# Issue 4690: [with patch; needs review] Sage hangs on derivative of piecewise function

archive/issues_004690.json:
```json
{
    "body": "Assignee: burcin\n\nDerivatives of piecewise functions where some piece uses multiplication causes Sage to hang. Example code:\n\n\n```\nPiecewise([[(0,1), x * 2]]).derivative()\n```\n\n\nIt hangs waiting for Maxima to return a result, which is because the expression it sends to Maxima is not formatted properly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4690\n\n",
    "created_at": "2008-12-04T01:22:32Z",
    "labels": [
        "calculus",
        "minor",
        "bug"
    ],
    "title": "[with patch; needs review] Sage hangs on derivative of piecewise function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4690",
    "user": "pbutler"
}
```
Assignee: burcin

Derivatives of piecewise functions where some piece uses multiplication causes Sage to hang. Example code:


```
Piecewise([[(0,1), x * 2]]).derivative()
```


It hangs waiting for Maxima to return a result, which is because the expression it sends to Maxima is not formatted properly.

Issue created by migration from https://trac.sagemath.org/ticket/4690





---

archive/issue_comments_035353.json:
```json
{
    "body": "Attachment\n\nPatch file for piecewise derivative",
    "created_at": "2008-12-04T01:23:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4690",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4690#issuecomment-35353",
    "user": "pbutler"
}
```

Attachment

Patch file for piecewise derivative



---

archive/issue_comments_035354.json:
```json
{
    "body": "Paul,\n\nplease make sure to assign a milestone. Usually that is the next open one.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-04T01:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4690",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4690#issuecomment-35354",
    "user": "mabshoff"
}
```

Paul,

please make sure to assign a milestone. Usually that is the next open one.

Cheers,

Michael



---

archive/issue_comments_035355.json:
```json
{
    "body": "Looks good to me.  This can go in.\n\nBut, piecewise.py needs some _MAJOR_ work for which I will open up a new ticket.",
    "created_at": "2008-12-04T08:29:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4690",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4690#issuecomment-35355",
    "user": "mhansen"
}
```

Looks good to me.  This can go in.

But, piecewise.py needs some _MAJOR_ work for which I will open up a new ticket.



---

archive/issue_comments_035356.json:
```json
{
    "body": "Paul,\n\nin the future please post hg patches and not diffs, i.e. check in your changes and then export a patch. In this case I have committed the changes in your name so that the credit in the hg log is properly assigned.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-04T14:12:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4690",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4690#issuecomment-35356",
    "user": "mabshoff"
}
```

Paul,

in the future please post hg patches and not diffs, i.e. check in your changes and then export a patch. In this case I have committed the changes in your name so that the credit in the hg log is properly assigned.

Cheers,

Michael



---

archive/issue_comments_035357.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-04T14:13:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4690",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4690#issuecomment-35357",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_035358.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha0",
    "created_at": "2008-12-04T14:13:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4690",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4690#issuecomment-35358",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.2.alpha0
