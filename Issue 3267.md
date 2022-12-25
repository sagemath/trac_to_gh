# Issue 3267: Sage 3.0.2.alpha1: doctest failure in sage/server/support.py

archive/issues_003267.json:
```json
{
    "body": "Assignee: failure\n\n```\nsage -t -long devel/sage/sage/server/support.py             \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.2.rc0/tmp/support.py\", line 85:\n    sage: sage.server.support.help(numpy.linalg.norm)\nExpected:\n    <html><table notruncate notracebacks bgcolor=\"#386074\" cellpadding=10 cellspacing=10><tr><td bgcolor=\"#f5f5f5\"><font color=\"#37546d\">\n    Help on function norm in module numpy.linalg.linalg:\n    ...\n    For values ord < 0, the result is, strictly speaking, not a\n    mathematical 'norm', but it may still be useful for numerical purposes.\n    </font></tr></td></table></html>\nGot:\n    <html><table notracebacks bgcolor=\"#386074\" cellpadding=10 cellspacing=10><tr><td bgcolor=\"#f5f5f5\"><font color=\"#37546d\">\n    &nbsp;&nbsp;&nbsp;<a target='_new' href='cell://docs-1.html'>Click to open help window</a>&nbsp;&nbsp;&nbsp;\n    <br></font></tr></td></table></html>\n**********************************************************************\n1 items had failures:\n   1 of   3 in __main__.example_2\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.2.rc0/tmp/.doctest_support.py\n         [2.4 s]\nexit code: 1024\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t -long devel/sage/sage/server/support.py\nTotal time for all tests: 2.4 seconds\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3267\n\n",
    "created_at": "2008-05-21T13:55:51Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "Sage 3.0.2.alpha1: doctest failure in sage/server/support.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3267",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: failure

```
sage -t -long devel/sage/sage/server/support.py             
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.2.rc0/tmp/support.py", line 85:
    sage: sage.server.support.help(numpy.linalg.norm)
Expected:
    <html><table notruncate notracebacks bgcolor="#386074" cellpadding=10 cellspacing=10><tr><td bgcolor="#f5f5f5"><font color="#37546d">
    Help on function norm in module numpy.linalg.linalg:
    ...
    For values ord < 0, the result is, strictly speaking, not a
    mathematical 'norm', but it may still be useful for numerical purposes.
    </font></tr></td></table></html>
Got:
    <html><table notracebacks bgcolor="#386074" cellpadding=10 cellspacing=10><tr><td bgcolor="#f5f5f5"><font color="#37546d">
    &nbsp;&nbsp;&nbsp;<a target='_new' href='cell://docs-1.html'>Click to open help window</a>&nbsp;&nbsp;&nbsp;
    <br></font></tr></td></table></html>
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_2
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.2.rc0/tmp/.doctest_support.py
         [2.4 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


        sage -t -long devel/sage/sage/server/support.py
Total time for all tests: 2.4 seconds
```

Issue created by migration from https://trac.sagemath.org/ticket/3267





---

archive/issue_comments_022570.json:
```json
{
    "body": "prototype patch [actually only a diff]",
    "created_at": "2008-05-21T14:12:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3267#issuecomment-22570",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

prototype patch [actually only a diff]



---

archive/issue_comments_022571.json:
```json
{
    "body": "Changing assignee from failure to mabshoff.",
    "created_at": "2008-05-21T14:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3267#issuecomment-22571",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from failure to mabshoff.



---

archive/issue_comments_022572.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-21T14:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3267#issuecomment-22572",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_022573.json:
```json
{
    "body": "Attachment [trac_3267.patch](tarball://root/attachments/some-uuid/ticket3267/trac_3267.patch) by mabshoff created at 2008-05-21 14:14:43\n\nAfter talking to William in IRC I changed the test to the new, expected error message since we now post a link to the error message instead of the error message itself. I add \"...\" since the number depends if other help files have been produced since they are not deleted, i.e. \"sage/server/docs-0.html\" sticks around. See #3265 for that issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-21T14:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3267#issuecomment-22573",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_3267.patch](tarball://root/attachments/some-uuid/ticket3267/trac_3267.patch) by mabshoff created at 2008-05-21 14:14:43

After talking to William in IRC I changed the test to the new, expected error message since we now post a link to the error message instead of the error message itself. I add "..." since the number depends if other help files have been produced since they are not deleted, i.e. "sage/server/docs-0.html" sticks around. See #3265 for that issue.

Cheers,

Michael



---

archive/issue_comments_022574.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-23T06:08:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3267#issuecomment-22574",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022575.json:
```json
{
    "body": "Merged in Sage 3.0.2.rc0",
    "created_at": "2008-05-23T06:08:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3267#issuecomment-22575",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.2.rc0



---

archive/issue_events_007354.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-23T06:08:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3267",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3267#event-7354"
}
```
