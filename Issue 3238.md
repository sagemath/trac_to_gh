# Issue 3238: [with patch; needs review] libfpll spkg -- update to work with cygwin

archive/issues_003238.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis was completely straightforward\n\n   http://sage.math.washington.edu/home/was/cygwin/libfplll-2.1.6-20071129.p4.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/3238\n\n",
    "created_at": "2008-05-17T16:00:30Z",
    "labels": [
        "component: porting: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "[with patch; needs review] libfpll spkg -- update to work with cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3238",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

This was completely straightforward

   http://sage.math.washington.edu/home/was/cygwin/libfplll-2.1.6-20071129.p4.spkg

Issue created by migration from https://trac.sagemath.org/ticket/3238





---

archive/issue_comments_022376.json:
```json
{
    "body": "Spkg looks good. I updated the fplll.h.patch to reflect the latest diff. In addition I send the fix upstream so that we do not have to patch this once the new upstream libfplll is released.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-18T13:19:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3238#issuecomment-22376",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Spkg looks good. I updated the fplll.h.patch to reflect the latest diff. In addition I send the fix upstream so that we do not have to patch this once the new upstream libfplll is released.

Cheers,

Michael



---

archive/issue_comments_022377.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha1",
    "created_at": "2008-05-18T13:19:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3238#issuecomment-22377",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.2.alpha1



---

archive/issue_comments_022378.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-18T13:19:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3238#issuecomment-22378",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
