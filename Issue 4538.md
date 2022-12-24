# Issue 4538: write a python script that runs a subprocess and kills it after a while

archive/issues_004538.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  gfurnish\n\nCreate a script `sage-walltimekill` SAGE_ROOT/local/bin/ that would run\na subprocess, wait a certain amount of time, then killing it.  \n\n```\nsage-walltimekill 3600 sage\n```\n\nwould kill the process it starts after 3600 wall seconds.\n\nThis will be useful both for doctesting and the notebook.  It's the sort of\nthing ulimit \"should\" do, but doesn't. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4538\n\n",
    "created_at": "2008-11-17T15:13:40Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "write a python script that runs a subprocess and kills it after a while",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4538",
    "user": "was"
}
```
Assignee: cwitty

CC:  gfurnish

Create a script `sage-walltimekill` SAGE_ROOT/local/bin/ that would run
a subprocess, wait a certain amount of time, then killing it.  

```
sage-walltimekill 3600 sage
```

would kill the process it starts after 3600 wall seconds.

This will be useful both for doctesting and the notebook.  It's the sort of
thing ulimit "should" do, but doesn't. 

Issue created by migration from https://trac.sagemath.org/ticket/4538





---

archive/issue_comments_033826.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-11-17T15:13:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4538#issuecomment-33826",
    "user": "was"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_033827.json:
```json
{
    "body": "Gary,\n\nthis is very interesting and would help to make -tp more robust.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-05T05:18:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4538#issuecomment-33827",
    "user": "mabshoff"
}
```

Gary,

this is very interesting and would help to make -tp more robust.

Cheers,

Michael



---

archive/issue_comments_033828.json:
```json
{
    "body": "With #717 can we close this as invalid?  Or do you want me to encapsulate the #717 code for some other purpose?",
    "created_at": "2008-12-05T07:11:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4538#issuecomment-33828",
    "user": "gfurnish"
}
```

With #717 can we close this as invalid?  Or do you want me to encapsulate the #717 code for some other purpose?



---

archive/issue_comments_033829.json:
```json
{
    "body": "Replying to [comment:3 gfurnish]:\n> With #717 can we close this as invalid?  Or do you want me to encapsulate the #717 code for some other purpose?  \n\nThis could still come in useful for example for the notebook, so I would leave it open.\n\nWilliam: any thoughts here?\n\nCheers,\n\nMichael",
    "created_at": "2008-12-05T07:21:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4538#issuecomment-33829",
    "user": "mabshoff"
}
```

Replying to [comment:3 gfurnish]:
> With #717 can we close this as invalid?  Or do you want me to encapsulate the #717 code for some other purpose?  

This could still come in useful for example for the notebook, so I would leave it open.

William: any thoughts here?

Cheers,

Michael
