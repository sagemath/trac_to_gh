# Issue 2518: improve the SAGE_ROOT/local/bin/sage-cleaner script so that it kills those damn lisp.run processes

archive/issues_002518.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  was mhansen robertwb\n\nFact is, several people have observed lisp.run's getting left running.\n\nIf *anybody* can find a 100% reliable way to replicate this problem, PLEASE LET US KNOW!\n\nIssue created by migration from https://trac.sagemath.org/ticket/2518\n\n",
    "created_at": "2008-03-14T19:25:20Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "improve the SAGE_ROOT/local/bin/sage-cleaner script so that it kills those damn lisp.run processes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2518",
    "user": "was"
}
```
Assignee: cwitty

CC:  was mhansen robertwb

Fact is, several people have observed lisp.run's getting left running.

If *anybody* can find a 100% reliable way to replicate this problem, PLEASE LET US KNOW!

Issue created by migration from https://trac.sagemath.org/ticket/2518





---

archive/issue_comments_017176.json:
```json
{
    "body": "Changing assignee from cwitty to mabshoff.",
    "created_at": "2008-07-29T17:23:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2518#issuecomment-17176",
    "user": "mabshoff"
}
```

Changing assignee from cwitty to mabshoff.



---

archive/issue_comments_017177.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-07-29T17:23:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2518#issuecomment-17177",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_017178.json:
```json
{
    "body": "The issue here is likely that we use\n\n```\nos.kill(int(pid),0)\n```\n\nIt is likely that using \"kill -9 $PID\" via os.system() ought to fix the issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-29T17:23:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2518#issuecomment-17178",
    "user": "mabshoff"
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

archive/issue_comments_017179.json:
```json
{
    "body": "I believe the problem was that if clisp crashed and restarted those processes could get stuck at 99% and not be killed at exit.\n\nThis hasn't been reported in a while, so I would prefer to close this as fixed. Thoughts?\n\nCheers,\n\nMichael",
    "created_at": "2009-05-13T18:41:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2518#issuecomment-17179",
    "user": "mabshoff"
}
```

I believe the problem was that if clisp crashed and restarted those processes could get stuck at 99% and not be killed at exit.

This hasn't been reported in a while, so I would prefer to close this as fixed. Thoughts?

Cheers,

Michael



---

archive/issue_comments_017180.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T07:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2518#issuecomment-17180",
    "user": "timdumol"
}
```

Resolution: fixed



---

archive/issue_comments_017181.json:
```json
{
    "body": "Since this hasn't been reported in around 8 months, I think this should be closed.",
    "created_at": "2010-01-19T07:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2518#issuecomment-17181",
    "user": "timdumol"
}
```

Since this hasn't been reported in around 8 months, I think this should be closed.



---

archive/issue_comments_017182.json:
```json
{
    "body": "Resolution changed from fixed to invalid",
    "created_at": "2010-01-19T07:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2518#issuecomment-17182",
    "user": "mhansen"
}
```

Resolution changed from fixed to invalid



---

archive/issue_comments_017183.json:
```json
{
    "body": "Seems reasonable to me.",
    "created_at": "2010-01-19T07:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2518#issuecomment-17183",
    "user": "mhansen"
}
```

Seems reasonable to me.
