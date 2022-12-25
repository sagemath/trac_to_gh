# Issue 5123: add univariate polynomial xgcd over GF(p) to sage

archive/issues_005123.json:
```json
{
    "body": "Assignee: somebody\n\nThis caused me trouble when preparing for my class today:\n\n\n```\nsage: k.<X> = GF(2)[]\nsage: xgcd(X^2, X+1)\nTraceback (most recent call last):\n...\nNotImplementedError\nsage: (X^2).xgcd(X+1)\nTraceback (most recent call last):\n...\nNotImplementedError\n```\n\n\nNote that PARI can do this, so that's an easy shortcut to implement *something*:\n\n```\nsage: pari(X^2).xgcd(X+1)\n(Mod(1, 2), Mod(1, 2), Mod(1, 2)*X + Mod(1, 2))\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5123\n\n",
    "created_at": "2009-01-28T20:57:39Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "add univariate polynomial xgcd over GF(p) to sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5123",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

This caused me trouble when preparing for my class today:


```
sage: k.<X> = GF(2)[]
sage: xgcd(X^2, X+1)
Traceback (most recent call last):
...
NotImplementedError
sage: (X^2).xgcd(X+1)
Traceback (most recent call last):
...
NotImplementedError
```


Note that PARI can do this, so that's an easy shortcut to implement *something*:

```
sage: pari(X^2).xgcd(X+1)
(Mod(1, 2), Mod(1, 2), Mod(1, 2)*X + Mod(1, 2))
```


Issue created by migration from https://trac.sagemath.org/ticket/5123





---

archive/issue_events_005372.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-06-05T01:19:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5123",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5123#event-5372"
}
```



---

archive/issue_comments_039088.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-06-05T01:19:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5123#issuecomment-39088",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid



---

archive/issue_comments_039089.json:
```json
{
    "body": "Fixed by #5393",
    "created_at": "2009-06-05T01:19:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5123#issuecomment-39089",
    "user": "https://github.com/mwhansen"
}
```

Fixed by #5393
