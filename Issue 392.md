# Issue 392: round() ignores the innate precision of a real number

archive/issues_000392.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: round, real, arithmetic\n\nThe function round() seems to ignore precision information slightly beyond the default 53 bits for a real number.  This leads to some incorrect rounding results for close calls.\n\n\n```\nsage: a = 5.499999999999999 \nsage: a.prec()\n56\nsage: round(a)  ## This is ok\n5.0\n\nsage: b = 5.4999999999999999\nsage: b.prec()\n59\nsage: round(b)  ## This isn't ok \n6.0\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/392\n\n",
    "created_at": "2007-06-28T06:03:57Z",
    "labels": [
        "component: algebraic geometry",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.2",
    "title": "round() ignores the innate precision of a real number",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/392",
    "user": "https://github.com/jonhanke"
}
```
Assignee: @williamstein

Keywords: round, real, arithmetic

The function round() seems to ignore precision information slightly beyond the default 53 bits for a real number.  This leads to some incorrect rounding results for close calls.


```
sage: a = 5.499999999999999 
sage: a.prec()
56
sage: round(a)  ## This is ok
5.0

sage: b = 5.4999999999999999
sage: b.prec()
59
sage: round(b)  ## This isn't ok 
6.0
```


Issue created by migration from https://trac.sagemath.org/ticket/392





---

archive/issue_comments_001918.json:
```json
{
    "body": "Changing keywords from \"round, real, arithmetic\" to \"round, real, precision, arithmetic\".",
    "created_at": "2007-06-28T06:04:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/392#issuecomment-1918",
    "user": "https://github.com/jonhanke"
}
```

Changing keywords from "round, real, arithmetic" to "round, real, precision, arithmetic".



---

archive/issue_events_000414.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-08-18T22:25:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/392",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/392#event-414"
}
```



---

archive/issue_comments_001919.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-18T22:25:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/392#issuecomment-1919",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
