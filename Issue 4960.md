# Issue 4960: issue with user account creation in the notebook

archive/issues_004960.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @williamstein @mwhansen\n\n```\nHello,\n\nI'm running my server with account creation disabled and when I want\nto add a user I restart it briefly with notebook(...,accounts=true)\n\nStage 1:\nI through the \"create a new account\" procedure without trying the\nnewly created user then immediately restarts the server with accounts\ndisabled (as I don't want to run too much with account creation open)\nI try to log in -> the user \"doesn't exist\".\n\nStage 2:\nI restart the server accounts=true, create the user and log in a first\ntime with the newly created account, then logout and restart the\nserver with accounts creation disabled.\nSame error, user doesn't exist anymore.\n\nStage 3:\n- Create account\n- Log in with it\n- Create a new (first) worksheet\n- Logout\n- Restart the server\n- Alleluia the user finally exists and can log in.\n\nApparently existence of the user seems to be linked to the existence\nof a first sheet or at least the user directory under .sage/\nsage_notebook/worksheets/\n\nI would rather expect stage1 to be enough to create a new account,\nmaybe creating the user directory during what is supposed to be the\ninitial user creation would be enough?\n\nPhil\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/4960\n\n",
    "created_at": "2009-01-09T22:50:11Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "issue with user account creation in the notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4960",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

CC:  @williamstein @mwhansen

```
Hello,

I'm running my server with account creation disabled and when I want
to add a user I restart it briefly with notebook(...,accounts=true)

Stage 1:
I through the "create a new account" procedure without trying the
newly created user then immediately restarts the server with accounts
disabled (as I don't want to run too much with account creation open)
I try to log in -> the user "doesn't exist".

Stage 2:
I restart the server accounts=true, create the user and log in a first
time with the newly created account, then logout and restart the
server with accounts creation disabled.
Same error, user doesn't exist anymore.

Stage 3:
- Create account
- Log in with it
- Create a new (first) worksheet
- Logout
- Restart the server
- Alleluia the user finally exists and can log in.

Apparently existence of the user seems to be linked to the existence
of a first sheet or at least the user directory under .sage/
sage_notebook/worksheets/

I would rather expect stage1 to be enough to create a new account,
maybe creating the user directory during what is supposed to be the
initial user creation would be enough?

Phil
```

Issue created by migration from https://trac.sagemath.org/ticket/4960





---

archive/issue_comments_037631.json:
```json
{
    "body": "I cannot replicate this issue anymore. Can someone confirm and close?",
    "created_at": "2010-01-17T09:05:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4960#issuecomment-37631",
    "user": "https://github.com/TimDumol"
}
```

I cannot replicate this issue anymore. Can someone confirm and close?



---

archive/issue_comments_037632.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-17T11:26:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4960#issuecomment-37632",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_011466.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-01-17T11:26:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4960",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4960#event-11466"
}
```



---

archive/issue_comments_037633.json:
```json
{
    "body": "Probably our rewrite fixed this...",
    "created_at": "2010-01-17T11:26:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4960#issuecomment-37633",
    "user": "https://github.com/williamstein"
}
```

Probably our rewrite fixed this...
