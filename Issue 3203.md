# Issue 3203: show() smashes multiplied numbers together so the product looks like a number

archive/issues_003203.json:
```json
{
    "body": "Assignee: boothby\n\nTo see this, evaluate the following in a notebook cell:\n\n\n```\nvar('r,z')\na=(r*z^2).integrate(z,0,r).integrate(r,0,sqrt(9/2))*2*pi\na.show()\nprint a\n```\n\n\nFirefox 3 Beta 5; Ubuntu 8.04\n\nIssue created by migration from https://trac.sagemath.org/ticket/3203\n\n",
    "created_at": "2008-05-14T12:13:05Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "show() smashes multiplied numbers together so the product looks like a number",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3203",
    "user": "https://github.com/jasongrout"
}
```
Assignee: boothby

To see this, evaluate the following in a notebook cell:


```
var('r,z')
a=(r*z^2).integrate(z,0,r).integrate(r,0,sqrt(9/2))*2*pi
a.show()
print a
```


Firefox 3 Beta 5; Ubuntu 8.04

Issue created by migration from https://trac.sagemath.org/ticket/3203





---

archive/issue_events_003421.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/dmharvey",
    "created_at": "2008-06-21T17:21:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3203",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3203#event-3421"
}
```



---

archive/issue_comments_022088.json:
```json
{
    "body": "duplicate of #3202",
    "created_at": "2008-06-21T17:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3203#issuecomment-22088",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

duplicate of #3202



---

archive/issue_comments_022089.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-06-21T17:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3203#issuecomment-22089",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Resolution: duplicate
