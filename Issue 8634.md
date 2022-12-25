# Issue 8634: Broken conversion of sage variable h1 to Maxima

archive/issues_008634.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @kcrisman @burcin\n\nh1, h2, h9 (and perhaps some others) are converted into binomial coefficients. This disallows to solve an equation involving variable h1.\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: h1=var('h1'); h1._maxima_()\nbinomial(n,k)*x^k\nsage: h2=var('h2'); h2._maxima_()\nbinomial(a,k)*binomial(b,n-k)\nsage: h=var('h'); h._maxima_()\nh\nsage: h_1=var('h_1'); h_1._maxima_()\nh_1\nsage: h23=var('h23'); h23._maxima_()\nh23\nsage: ch1=var('ch1'); ch1._maxima_()\nch1\nsage: h9=var('h9'); h9._maxima_()\nn!/(k!*(m+k)!*(n-m-2*k)!)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8634\n\n",
    "created_at": "2010-03-31T09:23:12Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Broken conversion of sage variable h1 to Maxima",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8634",
    "user": "https://github.com/robert-marik"
}
```
Assignee: @burcin

CC:  @kcrisman @burcin

h1, h2, h9 (and perhaps some others) are converted into binomial coefficients. This disallows to solve an equation involving variable h1.

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: h1=var('h1'); h1._maxima_()
binomial(n,k)*x^k
sage: h2=var('h2'); h2._maxima_()
binomial(a,k)*binomial(b,n-k)
sage: h=var('h'); h._maxima_()
h
sage: h_1=var('h_1'); h_1._maxima_()
h_1
sage: h23=var('h23'); h23._maxima_()
h23
sage: ch1=var('ch1'); ch1._maxima_()
ch1
sage: h9=var('h9'); h9._maxima_()
n!/(k!*(m+k)!*(n-m-2*k)!)
```


Issue created by migration from https://trac.sagemath.org/ticket/8634





---

archive/issue_comments_078177.json:
```json
{
    "body": "Changing assignee from @burcin to @robert-marik.",
    "created_at": "2010-03-31T11:02:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8634#issuecomment-78177",
    "user": "https://github.com/robert-marik"
}
```

Changing assignee from @burcin to @robert-marik.



---

archive/issue_comments_078178.json:
```json
{
    "body": "The discussion at [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/67f0a63d00b8d835?pli=1)",
    "created_at": "2010-03-31T11:02:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8634#issuecomment-78178",
    "user": "https://github.com/robert-marik"
}
```

The discussion at [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/67f0a63d00b8d835?pli=1)



---

archive/issue_events_020902.json:
```json
{
    "actor": "https://github.com/robert-marik",
    "created_at": "2010-04-21T13:25:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8634",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8634#event-20902"
}
```



---

archive/issue_comments_078179.json:
```json
{
    "body": "Duplicate of #8734 which already has first draft for the patch.",
    "created_at": "2010-04-21T13:25:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8634#issuecomment-78179",
    "user": "https://github.com/robert-marik"
}
```

Duplicate of #8734 which already has first draft for the patch.



---

archive/issue_comments_078180.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-04-21T13:25:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8634#issuecomment-78180",
    "user": "https://github.com/robert-marik"
}
```

Resolution: duplicate



---

archive/issue_comments_078181.json:
```json
{
    "body": "Oops, I wanted to mark this ticket as duplicate and the ticket has been closed automatically. Sorry for this, I know that only the release manager should close tickets :).",
    "created_at": "2010-04-21T13:28:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8634#issuecomment-78181",
    "user": "https://github.com/robert-marik"
}
```

Oops, I wanted to mark this ticket as duplicate and the ticket has been closed automatically. Sorry for this, I know that only the release manager should close tickets :).



---

archive/issue_events_020903.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-04-22T00:04:18Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8634",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8634#event-20903"
}
```



---

archive/issue_comments_078182.json:
```json
{
    "body": "Close as duplicate of #8734.",
    "created_at": "2010-04-22T00:04:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8634#issuecomment-78182",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Close as duplicate of #8734.
