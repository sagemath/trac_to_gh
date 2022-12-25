# Issue 6873: *huge* bug in multivariate polynomial substitution

archive/issues_006873.json:
```json
{
    "body": "Assignee: @malb\n\nObserve:\n\n```\nsage: R.<x,y> = QQ[]\nsage: f = x + 2*y\nsage: f.subs(x=y,y=x)\n3*y\nsage: var('x,y')\nsage: f = x + 2*y\nsage: f.subs(x=y,y=x)\n2*x + y\n```\n\n\nThis is really really bad.   Notice in the first and second substitution that the semantics are completely wrong/inconsistent.  The semantics should be as in the second one in both cases. \n\nIf you do `f.subs` in the first case above you'll see at the bottom code using I think libsingular that is really wrong.  Probably the only way to do this right will be to construct a homomorphism and apply it (?), sort of like this:\n\n```\nsage: R.<x,y> = QQ[]\nsage: f = x + 2*y\nsage: R.hom([y,x])(f)\n2*x + y\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/6873\n\n",
    "closed_at": "2009-09-09T20:13:49Z",
    "created_at": "2009-09-03T06:12:27Z",
    "labels": [
        "component: commutative algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "*huge* bug in multivariate polynomial substitution",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6873",
    "user": "https://github.com/williamstein"
}
```
Assignee: @malb

Observe:

```
sage: R.<x,y> = QQ[]
sage: f = x + 2*y
sage: f.subs(x=y,y=x)
3*y
sage: var('x,y')
sage: f = x + 2*y
sage: f.subs(x=y,y=x)
2*x + y
```


This is really really bad.   Notice in the first and second substitution that the semantics are completely wrong/inconsistent.  The semantics should be as in the second one in both cases. 

If you do `f.subs` in the first case above you'll see at the bottom code using I think libsingular that is really wrong.  Probably the only way to do this right will be to construct a homomorphism and apply it (?), sort of like this:

```
sage: R.<x,y> = QQ[]
sage: f = x + 2*y
sage: R.hom([y,x])(f)
2*x + y
```

Issue created by migration from https://trac.sagemath.org/ticket/6873





---

archive/issue_comments_056641.json:
```json
{
    "body": "This is a dupe of #6482.\n\nI think the fix is to not check whether `b` in `a=b` is a monomial but whether it is constant. If it isn't a constant we should just fall back to `fast_map`.",
    "created_at": "2009-09-03T11:24:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6873#issuecomment-56641",
    "user": "https://github.com/malb"
}
```

This is a dupe of #6482.

I think the fix is to not check whether `b` in `a=b` is a monomial but whether it is constant. If it isn't a constant we should just fall back to `fast_map`.



---

archive/issue_comments_056642.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-09-09T20:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6873#issuecomment-56642",
    "user": "https://github.com/malb"
}
```

Resolution: duplicate



---

archive/issue_events_016171.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2009-09-09T20:13:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6873",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6873#event-16171"
}
```



---

archive/issue_comments_056643.json:
```json
{
    "body": "Dupe of #6482",
    "created_at": "2009-09-09T20:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6873#issuecomment-56643",
    "user": "https://github.com/malb"
}
```

Dupe of #6482



---

archive/issue_events_016172.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-20T22:11:26Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6873",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6873#event-16172"
}
```
