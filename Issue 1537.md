# Issue 1537: jmol triangulation/shadow weirdness

archive/issues_001537.json:
```json
{
    "body": "Assignee: @williamstein\n\nFor example \n\n```\nsage: from sage.plot.plot3d.all import *\nsage: S = plot3d(lambda x, y: 1/(1+x^2+y^2), (-5,5), (-5,5), 'yellow')\nsage: S.show(viewer='jmol')\n```\n\nor even\n\n```\nsage: S = plot3d(lambda x, y: 0, (-5,5), (-5,5), 'yellow')\nsage: S.show(viewer='jmol')\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1537\n\n",
    "created_at": "2007-12-16T10:34:55Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "jmol triangulation/shadow weirdness",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1537",
    "user": "https://github.com/robertwb"
}
```
Assignee: @williamstein

For example 

```
sage: from sage.plot.plot3d.all import *
sage: S = plot3d(lambda x, y: 1/(1+x^2+y^2), (-5,5), (-5,5), 'yellow')
sage: S.show(viewer='jmol')
```

or even

```
sage: S = plot3d(lambda x, y: 0, (-5,5), (-5,5), 'yellow')
sage: S.show(viewer='jmol')
```


Issue created by migration from https://trac.sagemath.org/ticket/1537





---

archive/issue_comments_009786.json:
```json
{
    "body": "Changing assignee from @williamstein to @robertwb.",
    "created_at": "2007-12-16T10:35:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1537#issuecomment-9786",
    "user": "https://github.com/robertwb"
}
```

Changing assignee from @williamstein to @robertwb.



---

archive/issue_comments_009787.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-16T10:35:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1537#issuecomment-9787",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009788.json:
```json
{
    "body": "What is the status of this? It has been four months and a lot of work has gone into fixing various jmol related issues?\n\nCheers,\n\nMichael",
    "created_at": "2008-04-09T01:04:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1537#issuecomment-9788",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

What is the status of this? It has been four months and a lot of work has gone into fixing various jmol related issues?

Cheers,

Michael



---

archive/issue_comments_009789.json:
```json
{
    "body": "I believe this issue was fixed upstream, and I'm no longer seeing these issues so it is safe to close this patch.",
    "created_at": "2008-04-09T02:59:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1537#issuecomment-9789",
    "user": "https://github.com/robertwb"
}
```

I believe this issue was fixed upstream, and I'm no longer seeing these issues so it is safe to close this patch.



---

archive/issue_comments_009790.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-09T03:43:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1537#issuecomment-9790",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009791.json:
```json
{
    "body": "Closed as fixed upstream as per Robert's recommendation.",
    "created_at": "2008-04-09T03:43:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1537#issuecomment-9791",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Closed as fixed upstream as per Robert's recommendation.



---

archive/issue_events_001691.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-09T03:43:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1537",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1537#event-1691"
}
```
