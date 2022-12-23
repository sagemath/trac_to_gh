# Issue 392: round() ignores the innate precision of a real number

archive/issues_000392.json:
```json
{
    "body": "Assignee: was\n\nKeywords: round, real, arithmetic\n\nThe function round() seems to ignore precision information slightly beyond the default 53 bits for a real number.  This leads to some incorrect rounding results for close calls.\n\n\n```\nsage: a = 5.499999999999999 \nsage: a.prec()\n56\nsage: round(a)  ## This is ok\n5.0\n\nsage: b = 5.4999999999999999\nsage: b.prec()\n59\nsage: round(b)  ## This isn't ok \n6.0\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/392\n\n",
    "created_at": "2007-06-28T06:03:57Z",
    "labels": [
        "algebraic geometry",
        "minor",
        "bug"
    ],
    "title": "round() ignores the innate precision of a real number",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/392",
    "user": "jonhanke"
}
```
Assignee: was

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

archive/issue_comments_001926.json:
```json
{
    "body": "Changing keywords from \"round, real, arithmetic\" to \"round, real, precision, arithmetic\".",
    "created_at": "2007-06-28T06:04:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/392#issuecomment-1926",
    "user": "jonhanke"
}
```

Changing keywords from "round, real, arithmetic" to "round, real, precision, arithmetic".



---

archive/issue_comments_001927.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-18T22:25:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/392#issuecomment-1927",
    "user": "was"
}
```

Resolution: fixed
