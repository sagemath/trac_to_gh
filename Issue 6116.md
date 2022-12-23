# Issue 6116: error in real literal -> RIF conversion

archive/issues_006116.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: RIF(21/10).diameter()\n2.11471052309554e-16\nsage: RIF(2.1).diameter()\n0.000000000000000\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6116\n\n",
    "created_at": "2009-05-21T20:13:01Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "error in real literal -> RIF conversion",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6116",
    "user": "robertwb"
}
```
Assignee: somebody


```
sage: RIF(21/10).diameter()
2.11471052309554e-16
sage: RIF(2.1).diameter()
0.000000000000000
```


Issue created by migration from https://trac.sagemath.org/ticket/6116





---

archive/issue_comments_048876.json:
```json
{
    "body": "I don't think this is a bug, it's just the way how real literals work...",
    "created_at": "2015-08-21T20:28:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6116#issuecomment-48876",
    "user": "jdemeyer"
}
```

I don't think this is a bug, it's just the way how real literals work...



---

archive/issue_comments_048877.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-08-21T20:28:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6116#issuecomment-48877",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_048878.json:
```json
{
    "body": "And if you really want the real literal `2.1` to behave like `21/10`, there are a lot more bugs than just this one.",
    "created_at": "2015-08-21T20:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6116#issuecomment-48878",
    "user": "jdemeyer"
}
```

And if you really want the real literal `2.1` to behave like `21/10`, there are a lot more bugs than just this one.



---

archive/issue_comments_048879.json:
```json
{
    "body": "This is more about floating point rather than real literal\n\n```\nsage: a = 1.0 * RR(2.1)\nsage: type(a)\n<type 'sage.rings.real_mpfr.RealNumber'>\nsage: RIF(a).lower() == RIF(a).upper() == a\nTrue\n```\n\nAnd the last line would be true given **any** floating point (with 53 bits of precision).\n\nThough, it would be nice to explain the difference between `RIF(2.1)` and `RIF(21/10)` in the documentation of `RIF`. Don't you think?\n\nVincent",
    "created_at": "2015-09-17T02:59:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6116#issuecomment-48879",
    "user": "vdelecroix"
}
```

This is more about floating point rather than real literal

```
sage: a = 1.0 * RR(2.1)
sage: type(a)
<type 'sage.rings.real_mpfr.RealNumber'>
sage: RIF(a).lower() == RIF(a).upper() == a
True
```

And the last line would be true given **any** floating point (with 53 bits of precision).

Though, it would be nice to explain the difference between `RIF(2.1)` and `RIF(21/10)` in the documentation of `RIF`. Don't you think?

Vincent



---

archive/issue_comments_048880.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2015-09-17T02:59:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6116#issuecomment-48880",
    "user": "vdelecroix"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_048881.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2018-08-14T17:00:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6116#issuecomment-48881",
    "user": "embray"
}
```

Resolution: worksforme



---

archive/issue_comments_048882.json:
```json
{
    "body": "The docs for `RIF` currently state:\n\n\n```\n |      Values which can be represented as an exact floating-point number\n |      (of the precision of this ``RealIntervalField``) result in a precise\n |      interval, where the lower bound is equal to the upper bound (even\n |      if they print differently). Other values typically result in an\n |      interval where the lower and upper bounds are adjacent\n |      floating-point numbers.\n```\n\n\nand goes on to provide several examples, e.g. both with rational and floating point arguments.",
    "created_at": "2018-08-14T17:00:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6116#issuecomment-48882",
    "user": "embray"
}
```

The docs for `RIF` currently state:


```
 |      Values which can be represented as an exact floating-point number
 |      (of the precision of this ``RealIntervalField``) result in a precise
 |      interval, where the lower bound is equal to the upper bound (even
 |      if they print differently). Other values typically result in an
 |      interval where the lower and upper bounds are adjacent
 |      floating-point numbers.
```


and goes on to provide several examples, e.g. both with rational and floating point arguments.
