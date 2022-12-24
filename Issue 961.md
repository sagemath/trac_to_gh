# Issue 961: sage -standard fails without write permission to $SAGE_LOCAL/tmp

archive/issues_000961.json:
```json
{
    "body": "Assignee: mabshoff\n\nHello,\n\nI am not sure if this qualifies as a bug, but by storing the list in ~/.sage the following should work even if the user doesn't have write permission below $SAGE_LOCAL:\n\n```\nmabshoff@sage:/tmp/Work-mabshoff/sage-2.8.8$ sage -standard\nUsing SAGE Server http://www.sagemath.org//packages\nhttp://www.sagemath.org//packages/standard/list --> /home/was/s/tmp/list\n[Errno 13] Permission denied: '/home/was/s/tmp/list'\n\n\n\n********************************************************************************\n\n\n\nError contacting http://www.sagemath.org//packages/standard/list. Try using an alternative server.\nFor example, from the bash prompt try typing\n\n   export SAGE_SERVER=http://sage.scipy.org/sage/\n\nthen try again.\n\n\n\n********************************************************************************\n```\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/961\n\n",
    "created_at": "2007-10-21T14:19:24Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sage -standard fails without write permission to $SAGE_LOCAL/tmp",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/961",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Hello,

I am not sure if this qualifies as a bug, but by storing the list in ~/.sage the following should work even if the user doesn't have write permission below $SAGE_LOCAL:

```
mabshoff@sage:/tmp/Work-mabshoff/sage-2.8.8$ sage -standard
Using SAGE Server http://www.sagemath.org//packages
http://www.sagemath.org//packages/standard/list --> /home/was/s/tmp/list
[Errno 13] Permission denied: '/home/was/s/tmp/list'



********************************************************************************



Error contacting http://www.sagemath.org//packages/standard/list. Try using an alternative server.
For example, from the bash prompt try typing

   export SAGE_SERVER=http://sage.scipy.org/sage/

then try again.



********************************************************************************
```

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/961





---

archive/issue_comments_005855.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-21T14:19:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/961#issuecomment-5855",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005856.json:
```json
{
    "body": "The same applies for -optional, -experimental and so on. This ought to be fixed since it has been hit a bunch of times by various people.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-30T06:24:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/961#issuecomment-5856",
    "user": "mabshoff"
}
```

The same applies for -optional, -experimental and so on. This ought to be fixed since it has been hit a bunch of times by various people.

Cheers,

Michael



---

archive/issue_comments_005857.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-05-16T07:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/961#issuecomment-5857",
    "user": "jdemeyer"
}
```

Resolution: worksforme
