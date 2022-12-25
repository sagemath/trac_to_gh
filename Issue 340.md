# Issue 340: error in sageinspect: ode_solver?

archive/issues_000340.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\n\n\nOn 4/1/07, Joshua Kantor <kantor.jm@gmail.com> wrote:\n> I just installed a new version of sage and \n> ode_solver?  fails with the same errors as in his message. Did something\n> change \n> which would obviously cause this.\n\nThis is probably bug in the misc/sageinspect.py, which Nick Alexander recently rewrote\n(so the bug is either mine or his).  In any case, a temporary work around is to type\node_solver?? which will show the documentation (and source code). \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/340\n\n",
    "created_at": "2007-04-01T14:43:12Z",
    "labels": [
        "component: user interface",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.2",
    "title": "error in sageinspect: ode_solver?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/340",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

```


On 4/1/07, Joshua Kantor <kantor.jm@gmail.com> wrote:
> I just installed a new version of sage and 
> ode_solver?  fails with the same errors as in his message. Did something
> change 
> which would obviously cause this.

This is probably bug in the misc/sageinspect.py, which Nick Alexander recently rewrote
(so the bug is either mine or his).  In any case, a temporary work around is to type
ode_solver?? which will show the documentation (and source code). 
```

Issue created by migration from https://trac.sagemath.org/ticket/340





---

archive/issue_comments_001663.json:
```json
{
    "body": "In my sage, version 2.6, and in the new public notebook, this works as expected.  Please reopen and contact me (ncalexan) if this breaks in the future.",
    "created_at": "2007-06-27T06:01:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/340#issuecomment-1663",
    "user": "https://github.com/ncalexan"
}
```

In my sage, version 2.6, and in the new public notebook, this works as expected.  Please reopen and contact me (ncalexan) if this breaks in the future.



---

archive/issue_comments_001664.json:
```json
{
    "body": "Changing assignee from @williamstein to @ncalexan.",
    "created_at": "2007-06-27T06:01:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/340#issuecomment-1664",
    "user": "https://github.com/ncalexan"
}
```

Changing assignee from @williamstein to @ncalexan.



---

archive/issue_events_000799.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-18T21:24:06Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/340",
    "milestone": "sage-2.8.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/340#event-799"
}
```



---

archive/issue_events_000800.json:
```json
{
    "actor": "https://github.com/ncalexan",
    "created_at": "2007-08-19T01:20:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/340",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/340#event-800"
}
```



---

archive/issue_comments_001665.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2007-08-19T01:20:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/340#issuecomment-1665",
    "user": "https://github.com/ncalexan"
}
```

Resolution: worksforme
