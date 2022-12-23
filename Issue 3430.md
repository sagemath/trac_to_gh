# Issue 3430: 3.0.3.rc0: doctest failure in server/notebook/interact.py

archive/issues_003430.json:
```json
{
    "body": "Assignee: failure\n\n\n```\nsage -t -long devel/sage/sage/server/notebook/interact.py   \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.3.rc0/tmp/interact.py\", line 526:\n    sage: sage.server.notebook.interact.InputBox('theta', 1).render()\nExpected:\n    '<input type=\\'text\\' value=\\'1\\' width=200px onchange=\\'interact(0, \"sage.server.notebook.interact.update(0, \\\\\"theta\\\\\", ..., sage.server.notebook.interact.standard_b64decode(\\\\\"\"+encode64(this.value)+\"\\\\\"), globals())\")\\'></input>'\nGot:\n    '<input type=\\'text\\' value=\\'1\\' size=80 onchange=\\'interact(0, \"sage.server.notebook.interact.update(0, \\\\\"theta\\\\\", 16, sage.server.notebook.interact.standard_b64decode(\\\\\"\"+encode64(this.value)+\"\\\\\"), globals())\")\\'></input>'\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3430\n\n",
    "created_at": "2008-06-15T21:34:06Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "3.0.3.rc0: doctest failure in server/notebook/interact.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3430",
    "user": "mabshoff"
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

archive/issue_comments_024179.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-06-15T21:34:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3430#issuecomment-24179",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_024180.json:
```json
{
    "body": "Changing assignee from failure to mabshoff.",
    "created_at": "2008-06-15T21:34:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3430#issuecomment-24180",
    "user": "mabshoff"
}
```

Changing assignee from failure to mabshoff.



---

archive/issue_comments_024181.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-06-16T03:50:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3430#issuecomment-24181",
    "user": "boothby"
}
```

Attachment



---

archive/issue_comments_024182.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-16T04:51:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3430#issuecomment-24182",
    "user": "mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_024183.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-16T04:52:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3430#issuecomment-24183",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_024184.json:
```json
{
    "body": "Merged in Sage 3.0.3.rc0",
    "created_at": "2008-06-16T04:52:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3430#issuecomment-24184",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.3.rc0
