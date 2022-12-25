# Issue 168: Plot bounds ignored when frame=True

archive/issues_000168.json:
```json
{
    "body": "Assignee: boothby\n\nWhen I do:\n\n\n```\n  show(plot(lambda x: 1/x,-1,1),frame=True,ymin=-3,ymax=3)\n```\n\n\nthe ymin and ymax bounds get ignored. Without frame=True, the plot works properly\n\nIssue created by migration from https://trac.sagemath.org/ticket/168\n\n",
    "created_at": "2006-11-08T21:55:30Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-1.8",
    "title": "Plot bounds ignored when frame=True",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/168",
    "user": "https://github.com/nbruin"
}
```
Assignee: boothby

When I do:


```
  show(plot(lambda x: 1/x,-1,1),frame=True,ymin=-3,ymax=3)
```


the ymin and ymax bounds get ignored. Without frame=True, the plot works properly

Issue created by migration from https://trac.sagemath.org/ticket/168





---

archive/issue_events_000174.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-01-17T21:05:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/168",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/168#event-174"
}
```



---

archive/issue_comments_000749.json:
```json
{
    "body": "Alex C sent me a patch that fixes this problem.",
    "created_at": "2007-01-17T21:05:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/168#issuecomment-749",
    "user": "https://github.com/williamstein"
}
```

Alex C sent me a patch that fixes this problem.



---

archive/issue_comments_000750.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-17T21:05:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/168#issuecomment-750",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
