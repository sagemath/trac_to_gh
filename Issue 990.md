# Issue 990: no support for asinh/acosh etc. in symbolic expressions

archive/issues_000990.json:
```json
{
    "body": "Assignee: was\n\nAdd support for inverse hyperbolic functions in Sage\n\nIssue created by migration from https://trac.sagemath.org/ticket/990\n\n",
    "created_at": "2007-10-25T01:17:12Z",
    "labels": [
        "calculus",
        "major",
        "enhancement"
    ],
    "title": "no support for asinh/acosh etc. in symbolic expressions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/990",
    "user": "moretti"
}
```
Assignee: was

Add support for inverse hyperbolic functions in Sage

Issue created by migration from https://trac.sagemath.org/ticket/990





---

archive/issue_comments_006040.json:
```json
{
    "body": "This was fixed in an earlier patch.\n\n\n```\nsage: asinh(I)\nI*pi/2\nsage: asinh(2.0)\n1.44363547517881\nsage: acosh(2.0)\n1.31695789692482\nsage: atanh(1.0)\n+infinity\nsage: atanh(0.2)\n0.202732554054082\n```\n",
    "created_at": "2007-11-30T23:32:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/990#issuecomment-6040",
    "user": "mhansen"
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

archive/issue_comments_006041.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2007-11-30T23:32:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/990#issuecomment-6041",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_006042.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-30T23:32:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/990#issuecomment-6042",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006043.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-30T23:34:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/990#issuecomment-6043",
    "user": "mhansen"
}
```

Resolution: fixed
