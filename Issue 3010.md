# Issue 3010: Numerical noise doctest failure in rings/complex_double.pyx

archive/issues_003010.json:
```json
{
    "body": "Assignee: failure\n\nAndrzej Giniewicz reported:\n\n```\nsage -t  devel/sage-main/sage/rings/complex_double.pyx\n**********************************************************************\nFile \"/opt/sage-3.0.rc1/tmp/complex_double.py\", line 1659:\n    sage: z^2 - z + 1\nExpected:\n    2.22044604925e-16 + ...e-16*I\nGot:\n    2.22044604925e-16\n**********************************************************************\n1 items had failures:\n   1 of   7 in __main__.example_93\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /opt/sage-3.0.rc1/\ntmp/.doctest_complex_double.py\n         [4.1 s]\nexit code: 1024\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3010\n\n",
    "created_at": "2008-04-23T21:07:14Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "Numerical noise doctest failure in rings/complex_double.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3010",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: failure

Andrzej Giniewicz reported:

```
sage -t  devel/sage-main/sage/rings/complex_double.pyx
**********************************************************************
File "/opt/sage-3.0.rc1/tmp/complex_double.py", line 1659:
    sage: z^2 - z + 1
Expected:
    2.22044604925e-16 + ...e-16*I
Got:
    2.22044604925e-16
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_93
***Test Failed*** 1 failures.
For whitespace errors, see the file /opt/sage-3.0.rc1/
tmp/.doctest_complex_double.py
         [4.1 s]
exit code: 1024
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3010





---

archive/issue_comments_020651.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-05-03T15:37:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3010#issuecomment-20651",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_020652.json:
```json
{
    "body": "Attachment [trac_3010.patch](tarball://root/attachments/some-uuid/ticket3010/trac_3010.patch) by mabshoff created at 2008-05-03 15:53:55",
    "created_at": "2008-05-03T15:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3010#issuecomment-20652",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_3010.patch](tarball://root/attachments/some-uuid/ticket3010/trac_3010.patch) by mabshoff created at 2008-05-03 15:53:55



---

archive/issue_comments_020653.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-03T15:54:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3010#issuecomment-20653",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020654.json:
```json
{
    "body": "Changing assignee from failure to mabshoff.",
    "created_at": "2008-05-03T15:54:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3010#issuecomment-20654",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from failure to mabshoff.



---

archive/issue_comments_020655.json:
```json
{
    "body": "After applying that patch, doctest pass without problem",
    "created_at": "2008-05-03T16:29:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3010#issuecomment-20655",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

After applying that patch, doctest pass without problem



---

archive/issue_comments_020656.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-03T16:33:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3010#issuecomment-20656",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020657.json:
```json
{
    "body": "Merged in Sage 3.0.1.final",
    "created_at": "2008-05-03T16:33:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3010#issuecomment-20657",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.1.final



---

archive/issue_events_003215.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-03T16:33:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3010",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3010#event-3215"
}
```
