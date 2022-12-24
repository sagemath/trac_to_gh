# Issue 494: local/bin/sage-env uses 'bashism'

archive/issues_000494.json:
```json
{
    "body": "Assignee: @williamstein\n\nHello,\n\nlocal/bin/sage-env shipped with Sage 2.8.2 is officially a sh shell script. So it should run flawlessly with a tcsh. But\n\n```\n[mabshoff@m940 sage-2.8.2]# /bin/tcsh local/bin/sage-env\nSAVEDIR=/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2: Command not found.\nif: Expression Syntax.\n```\n\n\nThis was originally mentioned to me \"dropdrive\" in #sage-devel\n\nWhile we are at it: all spkg-install seem to use /bin/bash as shebang. While it is very uncommen to find a Unixy system these days without a bash it might still happen. We should consider fixing those scripts, too, or make it a requirement that users have a bash installed.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/494\n\n",
    "created_at": "2007-08-26T19:54:51Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "local/bin/sage-env uses 'bashism'",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/494",
    "user": "mabshoff"
}
```
Assignee: @williamstein

Hello,

local/bin/sage-env shipped with Sage 2.8.2 is officially a sh shell script. So it should run flawlessly with a tcsh. But

```
[mabshoff@m940 sage-2.8.2]# /bin/tcsh local/bin/sage-env
SAVEDIR=/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2: Command not found.
if: Expression Syntax.
```


This was originally mentioned to me "dropdrive" in #sage-devel

While we are at it: all spkg-install seem to use /bin/bash as shebang. While it is very uncommen to find a Unixy system these days without a bash it might still happen. We should consider fixing those scripts, too, or make it a requirement that users have a bash installed.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/494





---

archive/issue_comments_002468.json:
```json
{
    "body": "The first half of this bug is invalid as stated.  tcsh is not supposed to be sh-compatible, so it's not surprising that it can't source sage-env.",
    "created_at": "2007-10-07T19:11:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/494#issuecomment-2468",
    "user": "cwitty"
}
```

The first half of this bug is invalid as stated.  tcsh is not supposed to be sh-compatible, so it's not surprising that it can't source sage-env.



---

archive/issue_comments_002469.json:
```json
{
    "body": "The second part of the ticket, i.e. to use `/use/bin/env bash` is now #1638, so I am closing this ticket as invalid shortly.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-17T19:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/494#issuecomment-2469",
    "user": "mabshoff"
}
```

The second part of the ticket, i.e. to use `/use/bin/env bash` is now #1638, so I am closing this ticket as invalid shortly.

Cheers,

Michael



---

archive/issue_comments_002470.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-02-17T19:54:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/494#issuecomment-2470",
    "user": "mabshoff"
}
```

Resolution: invalid
