# Issue 844: dsage -- priority queues

archive/issues_000844.json:
```json
{
    "body": "Assignee: yqiang\n\nYi,\n\nSuppose I launch 1000 jobs like you saw me do.  Now I want to do\nsomething else, e.g., compute a bunch of things \"at another level\",\nwhile leaving those 1000 jobs (or what remains) in the queue.\nIs there any way to make a d = DSage() that submits jobs ahead\nof the 1000 jobs I submitted before.  E.g.,\n\n```\n    d.eval('foo', priority=-1)\n```\n\n???\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/844\n\n",
    "created_at": "2007-10-10T02:11:49Z",
    "labels": [
        "component: distribution"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "dsage -- priority queues",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/844",
    "user": "https://github.com/williamstein"
}
```
Assignee: yqiang

Yi,

Suppose I launch 1000 jobs like you saw me do.  Now I want to do
something else, e.g., compute a bunch of things "at another level",
while leaving those 1000 jobs (or what remains) in the queue.
Is there any way to make a d = DSage() that submits jobs ahead
of the 1000 jobs I submitted before.  E.g.,

```
    d.eval('foo', priority=-1)
```

???


Issue created by migration from https://trac.sagemath.org/ticket/844





---

archive/issue_events_000957.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-02-01T03:07:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/844",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/844#event-957"
}
```



---

archive/issue_comments_005205.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-02-01T03:07:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/844#issuecomment-5205",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: wontfix



---

archive/issue_comments_005206.json:
```json
{
    "body": "Close as wontfix. The dsage module has been removed by #7975.",
    "created_at": "2010-02-01T03:07:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/844#issuecomment-5206",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Close as wontfix. The dsage module has been removed by #7975.
