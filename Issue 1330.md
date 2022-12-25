# Issue 1330: [with patch] 2.8.14/Solaris: fix sympy doctest - numerical noise

archive/issues_001330.json:
```json
{
    "body": "Assignee: failure\n\nOn Solaris I get the following doctest failures due to numerical noise:\n\n```\nsage -t  devel/sage-main/sage/calculus/test_sympy.py        **********************************************************************\nFile \"test_sympy.py\", line 23:\n    : float(pi + exp(1))\nExpected:\n    5.8598744820488378\nGot:\n    5.8598744820488387\n```\n\n\nThe attached patch fixes that.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1330\n\n",
    "created_at": "2007-11-28T23:17:59Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "[with patch] 2.8.14/Solaris: fix sympy doctest - numerical noise",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1330",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: failure

On Solaris I get the following doctest failures due to numerical noise:

```
sage -t  devel/sage-main/sage/calculus/test_sympy.py        **********************************************************************
File "test_sympy.py", line 23:
    : float(pi + exp(1))
Expected:
    5.8598744820488378
Got:
    5.8598744820488387
```


The attached patch fixes that.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1330





---

archive/issue_comments_008491.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-28T23:18:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1330#issuecomment-8491",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008492.json:
```json
{
    "body": "Changing assignee from failure to mabshoff.",
    "created_at": "2007-11-28T23:18:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1330#issuecomment-8492",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from failure to mabshoff.



---

archive/issue_comments_008493.json:
```json
{
    "body": "Attachment [Sage-2.8.14-fix-sympy-doctest-failure-on-Sparc.patch](tarball://root/attachments/some-uuid/ticket1330/Sage-2.8.14-fix-sympy-doctest-failure-on-Sparc.patch) by mabshoff created at 2007-11-28 23:18:26",
    "created_at": "2007-11-28T23:18:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1330#issuecomment-8493",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [Sage-2.8.14-fix-sympy-doctest-failure-on-Sparc.patch](tarball://root/attachments/some-uuid/ticket1330/Sage-2.8.14-fix-sympy-doctest-failure-on-Sparc.patch) by mabshoff created at 2007-11-28 23:18:26



---

archive/issue_comments_008494.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2007-12-01T02:20:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1330#issuecomment-8494",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Looks good to me.



---

archive/issue_comments_008495.json:
```json
{
    "body": "Merged in 2.8.15.alpha0.",
    "created_at": "2007-12-01T11:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1330#issuecomment-8495",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.15.alpha0.



---

archive/issue_comments_008496.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-01T11:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1330#issuecomment-8496",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001470.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-01T11:27:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1330",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1330#event-1470"
}
```
