# Issue 7144: desolve does not use contrib_ode

archive/issues_007144.json:
```json
{
    "body": "Assignee: @burcin\n\nThe following code fails\n\n```\ny=function('y',x)\neqn=x*diff(y,x)^2-(1+x*y)*diff(y,x)+y == 0\ndesolve(eqn,y)\n```\n\nHowever, Maxima is able to produce the solution using contrib_ode command. If ode2 fails, Sage should call contrib_ode\n\nmaxima commands\n\n```\nload('contrib_ode)$\neqn:x*'diff(y,x)^2-(1+x*y)*'diff(y,x)+y=0;\ncontrib_ode(eqn,y,x);\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7144\n\n",
    "created_at": "2009-10-06T20:18:17Z",
    "labels": [
        "component: calculus",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "desolve does not use contrib_ode",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7144",
    "user": "https://github.com/robert-marik"
}
```
Assignee: @burcin

The following code fails

```
y=function('y',x)
eqn=x*diff(y,x)^2-(1+x*y)*diff(y,x)+y == 0
desolve(eqn,y)
```

However, Maxima is able to produce the solution using contrib_ode command. If ode2 fails, Sage should call contrib_ode

maxima commands

```
load('contrib_ode)$
eqn:x*'diff(y,x)^2-(1+x*y)*'diff(y,x)+y=0;
contrib_ode(eqn,y,x);
```


Issue created by migration from https://trac.sagemath.org/ticket/7144





---

archive/issue_comments_059076.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-10-07T11:43:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7144#issuecomment-59076",
    "user": "https://github.com/robert-marik"
}
```

Resolution: duplicate



---

archive/issue_events_007364.json:
```json
{
    "actor": "@robert-marik",
    "created_at": "2009-10-07T11:43:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7144",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7144#event-7364"
}
```



---

archive/issue_comments_059077.json:
```json
{
    "body": "Closed as duplicate of #6479.",
    "created_at": "2009-10-14T17:11:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7144#issuecomment-59077",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Closed as duplicate of #6479.
