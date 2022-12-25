# Issue 990: no support for asinh/acosh etc. in symbolic expressions

archive/issues_000990.json:
```json
{
    "body": "Assignee: @williamstein\n\nAdd support for inverse hyperbolic functions in Sage\n\nIssue created by migration from https://trac.sagemath.org/ticket/990\n\n",
    "created_at": "2007-10-25T01:17:12Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "no support for asinh/acosh etc. in symbolic expressions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/990",
    "user": "https://github.com/bobmoretti"
}
```
Assignee: @williamstein

Add support for inverse hyperbolic functions in Sage

Issue created by migration from https://trac.sagemath.org/ticket/990





---

archive/issue_comments_006020.json:
```json
{
    "body": "This was fixed in an earlier patch.\n\n\n```\nsage: asinh(I)\nI*pi/2\nsage: asinh(2.0)\n1.44363547517881\nsage: acosh(2.0)\n1.31695789692482\nsage: atanh(1.0)\n+infinity\nsage: atanh(0.2)\n0.202732554054082\n```\n",
    "created_at": "2007-11-30T23:32:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/990#issuecomment-6020",
    "user": "https://github.com/mwhansen"
}
```

This was fixed in an earlier patch.


```
sage: asinh(I)
I*pi/2
sage: asinh(2.0)
1.44363547517881
sage: acosh(2.0)
1.31695789692482
sage: atanh(1.0)
+infinity
sage: atanh(0.2)
0.202732554054082
```




---

archive/issue_comments_006021.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2007-11-30T23:32:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/990#issuecomment-6021",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_006022.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-30T23:32:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/990#issuecomment-6022",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006023.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-30T23:34:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/990#issuecomment-6023",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_001113.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2007-11-30T23:34:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/990",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/990#event-1113"
}
```
