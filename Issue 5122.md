# Issue 5122: point -- plotting bug for point(Elliptic curve point)

archive/issues_005122.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis should draw a point at the origin in 2d:\n\n```\nE = EllipticCurve('37a')\nP = E([0,0])\npoint(P)\n```\n\nIt used to work but is now broken.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5122\n\n",
    "created_at": "2009-01-28T20:09:46Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "point -- plotting bug for point(Elliptic curve point)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5122",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

This should draw a point at the origin in 2d:

```
E = EllipticCurve('37a')
P = E([0,0])
point(P)
```

It used to work but is now broken.

Issue created by migration from https://trac.sagemath.org/ticket/5122





---

archive/issue_comments_039083.json:
```json
{
    "body": "Can you point out a Sage version that this worked in?  That'll make it easier to see what change broke it.",
    "created_at": "2009-01-28T21:41:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5122#issuecomment-39083",
    "user": "https://github.com/jasongrout"
}
```

Can you point out a Sage version that this worked in?  That'll make it easier to see what change broke it.



---

archive/issue_comments_039084.json:
```json
{
    "body": "Duh, from the mailing list, 3.1.1 apparently had a working version.",
    "created_at": "2009-01-28T21:41:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5122#issuecomment-39084",
    "user": "https://github.com/jasongrout"
}
```

Duh, from the mailing list, 3.1.1 apparently had a working version.



---

archive/issue_comments_039085.json:
```json
{
    "body": "I would say that this is correct behavior, since point() is very specifically documented to plot 2d or 3d points (i.e., lists of coordinates) and not more esoteric objects like points on elliptic curves.\n\nA long time ago (5 months ago?), point() would call P.plot(), which is funny since then you could do point(anything) and it would plot correctly.\n\nFor now, the correct thing to do would be to call P.plot() or plot(P), which correctly calls the plot method of P (especially after #5121 is applied).",
    "created_at": "2009-01-28T22:01:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5122#issuecomment-39085",
    "user": "https://github.com/jasongrout"
}
```

I would say that this is correct behavior, since point() is very specifically documented to plot 2d or 3d points (i.e., lists of coordinates) and not more esoteric objects like points on elliptic curves.

A long time ago (5 months ago?), point() would call P.plot(), which is funny since then you could do point(anything) and it would plot correctly.

For now, the correct thing to do would be to call P.plot() or plot(P), which correctly calls the plot method of P (especially after #5121 is applied).



---

archive/issue_comments_039086.json:
```json
{
    "body": "As near as I can tell, the above stopped working in http://www.sagemath.org/hg/sage-main/rev/a54786a80034\n\nThis was about 5 months ago.",
    "created_at": "2009-01-28T22:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5122#issuecomment-39086",
    "user": "https://github.com/jasongrout"
}
```

As near as I can tell, the above stopped working in http://www.sagemath.org/hg/sage-main/rev/a54786a80034

This was about 5 months ago.



---

archive/issue_events_011849.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-01-29T00:55:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5122",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5122#event-11849"
}
```



---

archive/issue_comments_039087.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2009-01-29T00:55:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5122#issuecomment-39087",
    "user": "https://github.com/williamstein"
}
```

Resolution: wontfix



---

archive/issue_events_011850.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-29T00:59:19Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5122",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5122#event-11850"
}
```
