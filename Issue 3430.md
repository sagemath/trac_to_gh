# Issue 3430: 3.0.3.rc0: doctest failure in server/notebook/interact.py

archive/issues_003430.json:
```json
{
    "body": "Assignee: failure\n\n```\nsage -t -long devel/sage/sage/server/notebook/interact.py   \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.3.rc0/tmp/interact.py\", line 526:\n    sage: sage.server.notebook.interact.InputBox('theta', 1).render()\nExpected:\n    '<input type=\\'text\\' value=\\'1\\' width=200px onchange=\\'interact(0, \"sage.server.notebook.interact.update(0, \\\\\"theta\\\\\", ..., sage.server.notebook.interact.standard_b64decode(\\\\\"\"+encode64(this.value)+\"\\\\\"), globals())\")\\'></input>'\nGot:\n    '<input type=\\'text\\' value=\\'1\\' size=80 onchange=\\'interact(0, \"sage.server.notebook.interact.update(0, \\\\\"theta\\\\\", 16, sage.server.notebook.interact.standard_b64decode(\\\\\"\"+encode64(this.value)+\"\\\\\"), globals())\")\\'></input>'\n**********************************************************************\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3430\n\n",
    "created_at": "2008-06-15T21:34:06Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "3.0.3.rc0: doctest failure in server/notebook/interact.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3430",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: failure

```
sage -t -long devel/sage/sage/server/notebook/interact.py   
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.3.rc0/tmp/interact.py", line 526:
    sage: sage.server.notebook.interact.InputBox('theta', 1).render()
Expected:
    '<input type=\'text\' value=\'1\' width=200px onchange=\'interact(0, "sage.server.notebook.interact.update(0, \\"theta\\", ..., sage.server.notebook.interact.standard_b64decode(\\""+encode64(this.value)+"\\"), globals())")\'></input>'
Got:
    '<input type=\'text\' value=\'1\' size=80 onchange=\'interact(0, "sage.server.notebook.interact.update(0, \\"theta\\", 16, sage.server.notebook.interact.standard_b64decode(\\""+encode64(this.value)+"\\"), globals())")\'></input>'
**********************************************************************
```

Issue created by migration from https://trac.sagemath.org/ticket/3430





---

archive/issue_comments_024130.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-06-15T21:34:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3430#issuecomment-24130",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_024131.json:
```json
{
    "body": "Changing assignee from failure to mabshoff.",
    "created_at": "2008-06-15T21:34:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3430#issuecomment-24131",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from failure to mabshoff.



---

archive/issue_comments_024132.json:
```json
{
    "body": "Attachment [3430-doctest-update.patch](tarball://root/attachments/some-uuid/ticket3430/3430-doctest-update.patch) by boothby created at 2008-06-16 03:50:27",
    "created_at": "2008-06-16T03:50:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3430#issuecomment-24132",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [3430-doctest-update.patch](tarball://root/attachments/some-uuid/ticket3430/3430-doctest-update.patch) by boothby created at 2008-06-16 03:50:27



---

archive/issue_comments_024133.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-16T04:51:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3430#issuecomment-24133",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_024134.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-16T04:52:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3430#issuecomment-24134",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_024135.json:
```json
{
    "body": "Merged in Sage 3.0.3.rc0",
    "created_at": "2008-06-16T04:52:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3430#issuecomment-24135",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.3.rc0



---

archive/issue_events_007749.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-16T04:52:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3430",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3430#event-7749"
}
```
