# Issue 154: gfan -- something wrong

archive/issues_000154.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\nsage: R.<x,y> = PolynomialRing(QQ,2)\nsage: i = ideal([x + y - 1])\nsage: g = i.groebner_fan()\nsage: g.tropical_basis()\nTraceback (most recent call last):\n...\nKeyError: 'Dimension of homogeneity space'\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/154\n\n",
    "created_at": "2006-10-26T20:37:48Z",
    "labels": [
        "component: algebraic geometry",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-1.8",
    "title": "gfan -- something wrong",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/154",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

```
sage: R.<x,y> = PolynomialRing(QQ,2)
sage: i = ideal([x + y - 1])
sage: g = i.groebner_fan()
sage: g.tropical_basis()
Traceback (most recent call last):
...
KeyError: 'Dimension of homogeneity space'
```

Issue created by migration from https://trac.sagemath.org/ticket/154





---

archive/issue_events_000285.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-01-19T09:57:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/154",
    "milestone": "sage-1.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/154#event-285"
}
```



---

archive/issue_comments_000697.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-19T11:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/154#issuecomment-697",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_000698.json:
```json
{
    "body": "This is now fixed.",
    "created_at": "2007-01-19T11:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/154#issuecomment-698",
    "user": "https://github.com/williamstein"
}
```

This is now fixed.



---

archive/issue_events_000286.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-01-19T11:39:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/154",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/154#event-286"
}
```
