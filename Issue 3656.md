# Issue 3656: log_repr and log on finite field with prime order fails,

archive/issues_003656.json:
```json
{
    "body": "Assignee: tbd\n\nThe following code fails in sage,\n\n```\nF=GF(5)\nr=F.multiplicative_generator()\nr.log_repr() \nlog(r,r)\n```\n\nThe error seems to be because SAGE is treating GF(p) as integer mod ring, rather than a field.\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3656\n\n",
    "created_at": "2008-07-15T04:22:58Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "title": "log_repr and log on finite field with prime order fails,",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3656",
    "user": "https://github.com/syazdani77"
}
```
Assignee: tbd

The following code fails in sage,

```
F=GF(5)
r=F.multiplicative_generator()
r.log_repr() 
log(r,r)
```

The error seems to be because SAGE is treating GF(p) as integer mod ring, rather than a field.




Issue created by migration from https://trac.sagemath.org/ticket/3656





---

archive/issue_comments_025794.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-07-15T04:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3656#issuecomment-25794",
    "user": "https://github.com/syazdani77"
}
```

Resolution: invalid



---

archive/issue_events_003875.json:
```json
{
    "actor": "@syazdani77",
    "created_at": "2008-07-15T04:27:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3656",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3656#event-3875"
}
```



---

archive/issue_comments_025795.json:
```json
{
    "body": "I was an idiot. The base was wrong.",
    "created_at": "2008-07-15T04:27:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3656#issuecomment-25795",
    "user": "https://github.com/syazdani77"
}
```

I was an idiot. The base was wrong.
