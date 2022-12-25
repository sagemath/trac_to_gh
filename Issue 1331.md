# Issue 1331: [with patch] 2.8.14/Solaris: fix complex_double doctest  - numerical noise

archive/issues_001331.json:
```json
{
    "body": "Assignee: mabshoff\n\nOn Solaris I get the following doctest failures due to numerical noise:\n\n```\nsage -t  devel/sage-main/sage/rings/complex_double.pyx      **********************************************************************\nFile \"complex_double.pyx\", line 1496:\n    sage: z^2 - z + 1\nExpected:\n    2.22044604925e-16 + 1.11022302463e-16*I\nGot:\n    2.22044604925e-16 + 2.22044604925e-16*I\n```\nThe attached patch fixes that.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1331\n\n",
    "created_at": "2007-11-28T23:20:10Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "[with patch] 2.8.14/Solaris: fix complex_double doctest  - numerical noise",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1331",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

On Solaris I get the following doctest failures due to numerical noise:

```
sage -t  devel/sage-main/sage/rings/complex_double.pyx      **********************************************************************
File "complex_double.pyx", line 1496:
    sage: z^2 - z + 1
Expected:
    2.22044604925e-16 + 1.11022302463e-16*I
Got:
    2.22044604925e-16 + 2.22044604925e-16*I
```
The attached patch fixes that.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1331





---

archive/issue_comments_008497.json:
```json
{
    "body": "Attachment [Sage-2.8.14-fix-complex_double-doctest-failure-on-Sparc.patch](tarball://root/attachments/some-uuid/ticket1331/Sage-2.8.14-fix-complex_double-doctest-failure-on-Sparc.patch) by mabshoff created at 2007-11-28 23:20:18",
    "created_at": "2007-11-28T23:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1331#issuecomment-8497",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [Sage-2.8.14-fix-complex_double-doctest-failure-on-Sparc.patch](tarball://root/attachments/some-uuid/ticket1331/Sage-2.8.14-fix-complex_double-doctest-failure-on-Sparc.patch) by mabshoff created at 2007-11-28 23:20:18



---

archive/issue_comments_008498.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-28T23:20:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1331#issuecomment-8498",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008499.json:
```json
{
    "body": "We need another approach for this... what if on another machine, the imaginary component is exactly zero?\n\nBut let's cross that bridge when we come to it.\n\nLooks good to me.",
    "created_at": "2007-12-01T02:23:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1331#issuecomment-8499",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

We need another approach for this... what if on another machine, the imaginary component is exactly zero?

But let's cross that bridge when we come to it.

Looks good to me.



---

archive/issue_comments_008500.json:
```json
{
    "body": "Merged in 2.8.15.alpha0.",
    "created_at": "2007-12-01T11:27:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1331#issuecomment-8500",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.15.alpha0.



---

archive/issue_comments_008501.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-01T11:27:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1331#issuecomment-8501",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003466.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-01T11:27:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1331",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1331#event-3466"
}
```
