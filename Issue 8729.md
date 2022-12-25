# Issue 8729: simple integral using trig functions gives wrong answer

archive/issues_008729.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @kcrisman\n\nSee http://groups.google.com/group/sage-devel/browse_frm/thread/f82e24efdfe23b07/d9e563f086b1136d for a solution\n\n\n```\nsage: a=sqrt((sin(t))^2 + (cos(t))^2)\nsage: integrate(a, t, 0, 2*pi) # WRONG!\npi\nsage: a.simplify_full().simplify_trig()\n1\nsage: integrate(a.simplify_full().simplify_trig(), t, 0, 2*pi)\n2*pi \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8729\n\n",
    "created_at": "2010-04-20T16:52:51Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "simple integral using trig functions gives wrong answer",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8729",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @burcin

CC:  @kcrisman

See http://groups.google.com/group/sage-devel/browse_frm/thread/f82e24efdfe23b07/d9e563f086b1136d for a solution


```
sage: a=sqrt((sin(t))^2 + (cos(t))^2)
sage: integrate(a, t, 0, 2*pi) # WRONG!
pi
sage: a.simplify_full().simplify_trig()
1
sage: integrate(a.simplify_full().simplify_trig(), t, 0, 2*pi)
2*pi 
```


Issue created by migration from https://trac.sagemath.org/ticket/8729





---

archive/issue_comments_079607.json:
```json
{
    "body": "It looks like this is fixed in maxima 5.21.0, so maybe we should just upgrade.",
    "created_at": "2010-04-20T17:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8729#issuecomment-79607",
    "user": "https://github.com/jasongrout"
}
```

It looks like this is fixed in maxima 5.21.0, so maybe we should just upgrade.



---

archive/issue_comments_079608.json:
```json
{
    "body": "This is fixed in the maxima upgrade at #8731",
    "created_at": "2010-05-13T04:33:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8729#issuecomment-79608",
    "user": "https://github.com/jasongrout"
}
```

This is fixed in the maxima upgrade at #8731



---

archive/issue_events_008899.json:
```json
{
    "actor": "@rlmill",
    "created_at": "2010-06-25T11:23:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8729",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8729#event-8899"
}
```



---

archive/issue_comments_079609.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-06-25T11:23:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8729#issuecomment-79609",
    "user": "https://github.com/rlmill"
}
```

Resolution: duplicate



---

archive/issue_comments_079610.json:
```json
{
    "body": "Note put on #8731 to check this with a doctest when that ticket is done.",
    "created_at": "2010-06-25T13:10:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8729#issuecomment-79610",
    "user": "https://github.com/kcrisman"
}
```

Note put on #8731 to check this with a doctest when that ticket is done.
