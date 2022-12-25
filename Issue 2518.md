# Issue 2518: improve the SAGE_ROOT/local/bin/sage-cleaner script so that it kills those damn lisp.run processes

archive/issues_002518.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @williamstein @mwhansen @robertwb\n\nFact is, several people have observed lisp.run's getting left running.\n\nIf *anybody* can find a 100% reliable way to replicate this problem, PLEASE LET US KNOW!\n\nIssue created by migration from https://trac.sagemath.org/ticket/2518\n\n",
    "created_at": "2008-03-14T19:25:20Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "improve the SAGE_ROOT/local/bin/sage-cleaner script so that it kills those damn lisp.run processes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2518",
    "user": "https://github.com/williamstein"
}
```
Assignee: cwitty

CC:  @williamstein @mwhansen @robertwb

Fact is, several people have observed lisp.run's getting left running.

If *anybody* can find a 100% reliable way to replicate this problem, PLEASE LET US KNOW!

Issue created by migration from https://trac.sagemath.org/ticket/2518





---

archive/issue_comments_017139.json:
```json
{
    "body": "Changing assignee from cwitty to mabshoff.",
    "created_at": "2008-07-29T17:23:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2518#issuecomment-17139",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from cwitty to mabshoff.



---

archive/issue_comments_017140.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-07-29T17:23:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2518#issuecomment-17140",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_017141.json:
```json
{
    "body": "The issue here is likely that we use\n\n```\nos.kill(int(pid),0)\n```\n\nIt is likely that using \"kill -9 $PID\" via os.system() ought to fix the issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-29T17:23:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2518#issuecomment-17141",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The issue here is likely that we use

```
os.kill(int(pid),0)
```

It is likely that using "kill -9 $PID" via os.system() ought to fix the issue.

Cheers,

Michael



---

archive/issue_comments_017142.json:
```json
{
    "body": "I believe the problem was that if clisp crashed and restarted those processes could get stuck at 99% and not be killed at exit.\n\nThis hasn't been reported in a while, so I would prefer to close this as fixed. Thoughts?\n\nCheers,\n\nMichael",
    "created_at": "2009-05-13T18:41:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2518#issuecomment-17142",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I believe the problem was that if clisp crashed and restarted those processes could get stuck at 99% and not be killed at exit.

This hasn't been reported in a while, so I would prefer to close this as fixed. Thoughts?

Cheers,

Michael



---

archive/issue_comments_017143.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T07:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2518#issuecomment-17143",
    "user": "https://github.com/TimDumol"
}
```

Resolution: fixed



---

archive/issue_comments_017144.json:
```json
{
    "body": "Since this hasn't been reported in around 8 months, I think this should be closed.",
    "created_at": "2010-01-19T07:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2518#issuecomment-17144",
    "user": "https://github.com/TimDumol"
}
```

Since this hasn't been reported in around 8 months, I think this should be closed.



---

archive/issue_events_002699.json:
```json
{
    "actor": "https://github.com/TimDumol",
    "created_at": "2010-01-19T07:15:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2518",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2518#event-2699"
}
```



---

archive/issue_comments_017145.json:
```json
{
    "body": "Resolution changed from fixed to invalid",
    "created_at": "2010-01-19T07:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2518#issuecomment-17145",
    "user": "https://github.com/mwhansen"
}
```

Resolution changed from fixed to invalid



---

archive/issue_comments_017146.json:
```json
{
    "body": "Seems reasonable to me.",
    "created_at": "2010-01-19T07:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2518#issuecomment-17146",
    "user": "https://github.com/mwhansen"
}
```

Seems reasonable to me.
