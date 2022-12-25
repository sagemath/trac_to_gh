# Issue 3579: bug in RandonGNP graph constructor

archive/issues_003579.json:
```json
{
    "body": "Assignee: @rlmill\n\n\n```\n17:32 < itolkov> sage: graphs.RandomGNP(n=4, p=1)\n17:32 < itolkov> Traceback ... OverflowError: math range error\n17:32 < itolkov> bug?\n17:34 < wstein-3576> nt necessarily.\n17:35 < wstein-3576> the line lp=math.log(1.0-p) shows why it doesn't work.\n17:35 < wstein-3576> The docs do not ban probability 1, so yes, it is a bug.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3579\n\n",
    "created_at": "2008-07-07T00:37:28Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.6",
    "title": "bug in RandonGNP graph constructor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3579",
    "user": "https://github.com/williamstein"
}
```
Assignee: @rlmill


```
17:32 < itolkov> sage: graphs.RandomGNP(n=4, p=1)
17:32 < itolkov> Traceback ... OverflowError: math range error
17:32 < itolkov> bug?
17:34 < wstein-3576> nt necessarily.
17:35 < wstein-3576> the line lp=math.log(1.0-p) shows why it doesn't work.
17:35 < wstein-3576> The docs do not ban probability 1, so yes, it is a bug.
```


Issue created by migration from https://trac.sagemath.org/ticket/3579





---

archive/issue_events_008195.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/ekirkman",
    "created_at": "2008-07-10T17:06:56Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3579",
    "milestone": "sage-3.0.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3579#event-8195"
}
```



---

archive/issue_comments_025220.json:
```json
{
    "body": "Attachment [trac3579-random_graph_generator_bug_fix.patch](tarball://root/attachments/some-uuid/ticket3579/trac3579-random_graph_generator_bug_fix.patch) by ekirkman created at 2008-07-10 17:06:56",
    "created_at": "2008-07-10T17:06:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3579#issuecomment-25220",
    "user": "https://trac.sagemath.org/admin/accounts/users/ekirkman"
}
```

Attachment [trac3579-random_graph_generator_bug_fix.patch](tarball://root/attachments/some-uuid/ticket3579/trac3579-random_graph_generator_bug_fix.patch) by ekirkman created at 2008-07-10 17:06:56



---

archive/issue_comments_025221.json:
```json
{
    "body": "+1",
    "created_at": "2008-07-10T17:09:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3579#issuecomment-25221",
    "user": "https://github.com/rlmill"
}
```

+1



---

archive/issue_comments_025222.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-15T01:49:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3579#issuecomment-25222",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025223.json:
```json
{
    "body": "Merged in Sage 3.0.6.alpha0",
    "created_at": "2008-07-15T01:49:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3579#issuecomment-25223",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.6.alpha0



---

archive/issue_events_008196.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-15T01:49:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3579",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3579#event-8196"
}
```
