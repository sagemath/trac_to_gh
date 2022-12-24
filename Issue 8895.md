# Issue 8895: symbolic unit conversion function should ignore non-unit symbolic variables

archive/issues_008895.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @jdemeyer\n\nThis seems wrong to me:\n\n\n```\nsage: (x * units.length.meter).convert(units.length.mile)\nTraceback (most recent call last):\n...\nValueError: Incompatible units\nsage: (10 * units.length.meter).convert(units.length.mile)\n625/100584*mile\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8895\n\n",
    "created_at": "2010-05-05T19:59:18Z",
    "labels": [
        "calculus",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "symbolic unit conversion function should ignore non-unit symbolic variables",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8895",
    "user": "@williamstein"
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

archive/issue_comments_081780.json:
```json
{
    "body": "Ticket #11592 fixes this.",
    "created_at": "2011-07-13T01:56:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8895#issuecomment-81780",
    "user": "@eviatarbach"
}
```

Ticket #11592 fixes this.



---

archive/issue_comments_081781.json:
```json
{
    "body": "Changing component from calculus to symbolics.",
    "created_at": "2011-07-20T17:42:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8895#issuecomment-81781",
    "user": "@burcin"
}
```

Changing component from calculus to symbolics.



---

archive/issue_comments_081782.json:
```json
{
    "body": "This should be closed as a duplicate of #11592. The patch attached to that ticket fixes this and contains doctests covering William's example from the description.",
    "created_at": "2011-07-20T17:42:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8895#issuecomment-81782",
    "user": "@burcin"
}
```

This should be closed as a duplicate of #11592. The patch attached to that ticket fixes this and contains doctests covering William's example from the description.



---

archive/issue_comments_081783.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-03-20T22:59:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8895#issuecomment-81783",
    "user": "@tscrim"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081784.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-03-20T23:06:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8895#issuecomment-81784",
    "user": "@tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081785.json:
```json
{
    "body": "Still fixed in 5.7:\n\n```\nsage: (x*units.length.meter).convert(units.length.mile)\n(125/201168*x)*mile\nsage: (10*units.length.meter).convert(units.length.mile)\n625/100584*mile\n```\n",
    "created_at": "2013-03-20T23:06:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8895#issuecomment-81785",
    "user": "@tscrim"
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

archive/issue_comments_081786.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-03-29T18:55:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8895#issuecomment-81786",
    "user": "@jdemeyer"
}
```

Resolution: worksforme
