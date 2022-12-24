# Issue 8924: Comparison between Sage and mpmath numbers is broken

archive/issues_008924.json:
```json
{
    "body": "Assignee: @aghitza\n\nComparison between Sage and mpmath numbers works with mpmath numbers on the left, but not on the right:\n\n\n```\nsage: mpmath.mpf(1) < 3\nTrue\nsage: 1 < mpmath.mpf(3)\nFalse\nsage: 4 == mpmath.mpf(4)\nFalse\n```\n\n\nFound by Harald Schilly (see #8791).\n\nThis appears to be a bug in Sage (or Cython). Sage's numbers do the pure-Python equivalent of not returning NotImplemented when compared to unrecognized types. For a minimal example:\n\n\n```\nsage: class X(object):\n....:         def __init__(self, v): self.v = v\n....:     def __lt__(self, other): return self.v < int(other)\n....:     def __gt__(self, other): return self.v > int(other)\n....:\nsage: X(1) < 3\nTrue\nsage: 1 < X(3)\nFalse\nsage: X(1) < int(3)\nTrue\nsage: int(1) < X(3)\nTrue\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8924\n\n",
    "created_at": "2010-05-07T19:23:24Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Comparison between Sage and mpmath numbers is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8924",
    "user": "@fredrik-johansson"
}
```
Assignee: @aghitza

Comparison between Sage and mpmath numbers works with mpmath numbers on the left, but not on the right:


```
sage: mpmath.mpf(1) < 3
True
sage: 1 < mpmath.mpf(3)
False
sage: 4 == mpmath.mpf(4)
False
```


Found by Harald Schilly (see #8791).

This appears to be a bug in Sage (or Cython). Sage's numbers do the pure-Python equivalent of not returning NotImplemented when compared to unrecognized types. For a minimal example:


```
sage: class X(object):
....:         def __init__(self, v): self.v = v
....:     def __lt__(self, other): return self.v < int(other)
....:     def __gt__(self, other): return self.v > int(other)
....:
sage: X(1) < 3
True
sage: 1 < X(3)
False
sage: X(1) < int(3)
True
sage: int(1) < X(3)
True
```


Issue created by migration from https://trac.sagemath.org/ticket/8924





---

archive/issue_comments_082211.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-08-15T17:54:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8924#issuecomment-82211",
    "user": "@mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082212.json:
```json
{
    "body": "The tests from the description work as of 7.4.beta0.",
    "created_at": "2016-08-15T17:54:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8924#issuecomment-82212",
    "user": "@mkoeppe"
}
```

The tests from the description work as of 7.4.beta0.



---

archive/issue_comments_082213.json:
```json
{
    "body": "I think this is fixed by #21163.",
    "created_at": "2016-08-15T17:59:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8924#issuecomment-82213",
    "user": "@jdemeyer"
}
```

I think this is fixed by #21163.



---

archive/issue_comments_082214.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-08-15T17:59:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8924#issuecomment-82214",
    "user": "@jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082215.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2016-08-30T13:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8924#issuecomment-82215",
    "user": "@embray"
}
```

Resolution: wontfix



---

archive/issue_comments_082216.json:
```json
{
    "body": "Determined to be invalid/duplicate/wontfix (closing as \"wontfix\" as a catch-all resolution).",
    "created_at": "2016-08-30T13:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8924#issuecomment-82216",
    "user": "@embray"
}
```

Determined to be invalid/duplicate/wontfix (closing as "wontfix" as a catch-all resolution).
