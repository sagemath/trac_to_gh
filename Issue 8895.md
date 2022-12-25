# Issue 8895: symbolic unit conversion function should ignore non-unit symbolic variables

archive/issues_008895.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @jdemeyer\n\nThis seems wrong to me:\n\n\n```\nsage: (x * units.length.meter).convert(units.length.mile)\nTraceback (most recent call last):\n...\nValueError: Incompatible units\nsage: (10 * units.length.meter).convert(units.length.mile)\n625/100584*mile\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8895\n\n",
    "created_at": "2010-05-05T19:59:18Z",
    "labels": [
        "component: calculus",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "symbolic unit conversion function should ignore non-unit symbolic variables",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8895",
    "user": "https://github.com/williamstein"
}
```
Assignee: @burcin

CC:  @jdemeyer

This seems wrong to me:


```
sage: (x * units.length.meter).convert(units.length.mile)
Traceback (most recent call last):
...
ValueError: Incompatible units
sage: (10 * units.length.meter).convert(units.length.mile)
625/100584*mile
```


Issue created by migration from https://trac.sagemath.org/ticket/8895





---

archive/issue_comments_081646.json:
```json
{
    "body": "Ticket #11592 fixes this.",
    "created_at": "2011-07-13T01:56:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8895#issuecomment-81646",
    "user": "https://github.com/eviatarbach"
}
```

Ticket #11592 fixes this.



---

archive/issue_comments_081647.json:
```json
{
    "body": "Changing component from calculus to symbolics.",
    "created_at": "2011-07-20T17:42:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8895#issuecomment-81647",
    "user": "https://github.com/burcin"
}
```

Changing component from calculus to symbolics.



---

archive/issue_comments_081648.json:
```json
{
    "body": "This should be closed as a duplicate of #11592. The patch attached to that ticket fixes this and contains doctests covering William's example from the description.",
    "created_at": "2011-07-20T17:42:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8895#issuecomment-81648",
    "user": "https://github.com/burcin"
}
```

This should be closed as a duplicate of #11592. The patch attached to that ticket fixes this and contains doctests covering William's example from the description.



---

archive/issue_events_021704.json:
```json
{
    "actor": "https://github.com/burcin",
    "created_at": "2011-07-20T17:42:42Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8895",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8895#event-21704"
}
```



---

archive/issue_comments_081649.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-03-20T22:59:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8895#issuecomment-81649",
    "user": "https://github.com/tscrim"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081650.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-03-20T23:06:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8895#issuecomment-81650",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081651.json:
```json
{
    "body": "Still fixed in 5.7:\n\n```\nsage: (x*units.length.meter).convert(units.length.mile)\n(125/201168*x)*mile\nsage: (10*units.length.meter).convert(units.length.mile)\n625/100584*mile\n```\n",
    "created_at": "2013-03-20T23:06:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8895#issuecomment-81651",
    "user": "https://github.com/tscrim"
}
```

Still fixed in 5.7:

```
sage: (x*units.length.meter).convert(units.length.mile)
(125/201168*x)*mile
sage: (10*units.length.meter).convert(units.length.mile)
625/100584*mile
```




---

archive/issue_comments_081652.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-03-29T18:55:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8895#issuecomment-81652",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme



---

archive/issue_events_021705.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-03-29T18:55:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8895",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8895#event-21705"
}
```
