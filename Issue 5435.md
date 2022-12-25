# Issue 5435: [with patch, needs review] sage-ptest "Using cached timings." message could be better

archive/issues_005435.json:
```json
{
    "body": "Assignee: cwitty\n\nThe attached patch changes the message from\n\n```\nUsing cached timings.\n```\n\nto\n\n```\nUsing cached timings to run slower doctests first.\n```\n\n\nHopefully this is enough to explain the otherwise surprising long pause at the beginning of parallel testing runs.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5435\n\n",
    "created_at": "2009-03-04T04:07:39Z",
    "labels": [
        "component: doctest coverage",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "[with patch, needs review] sage-ptest \"Using cached timings.\" message could be better",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5435",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: cwitty

The attached patch changes the message from

```
Using cached timings.
```

to

```
Using cached timings to run slower doctests first.
```


Hopefully this is enough to explain the otherwise surprising long pause at the beginning of parallel testing runs.

Issue created by migration from https://trac.sagemath.org/ticket/5435





---

archive/issue_comments_041963.json:
```json
{
    "body": "Attachment [verbose-cached-timings.patch](tarball://root/attachments/some-uuid/ticket5435/verbose-cached-timings.patch) by cwitty created at 2009-03-04 04:07:49",
    "created_at": "2009-03-04T04:07:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5435#issuecomment-41963",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [verbose-cached-timings.patch](tarball://root/attachments/some-uuid/ticket5435/verbose-cached-timings.patch) by cwitty created at 2009-03-04 04:07:49



---

archive/issue_comments_041964.json:
```json
{
    "body": "Looks good to me.  It took me a second to figure out what this meant when I first encountered it.",
    "created_at": "2009-03-04T04:39:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5435#issuecomment-41964",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.  It took me a second to figure out what this meant when I first encountered it.



---

archive/issue_comments_041965.json:
```json
{
    "body": "Mhh, I think this needs fixing, but I think `slower` is the wrong term here. Maybe `longer` is better? Either way I want this patch to go in, but if there is a consensus I would be happy to change the patch.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-04T05:44:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5435#issuecomment-41965",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Mhh, I think this needs fixing, but I think `slower` is the wrong term here. Maybe `longer` is better? Either way I want this patch to go in, but if there is a consensus I would be happy to change the patch.

Cheers,

Michael



---

archive/issue_comments_041966.json:
```json
{
    "body": "Merged in Sage 3.4.final.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-10T23:13:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5435#issuecomment-41966",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.final.

Cheers,

Michael



---

archive/issue_comments_041967.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-10T23:13:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5435#issuecomment-41967",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
