# Issue 9306: round incoherent with ceil/floor on rational numbers

archive/issues_009306.json:
```json
{
    "body": "Assignee: @aghitza\n\nConsider the following:\n\n```\nsage: q=2^200/3^50\nsage: q.floor()\n2238393297946874000179418290327143433\nsage: q.ceil()\n2238393297946874000179418290327143434\nsage: q.round()\n2238393297946874000179418290327143433\n```\n\nThis is fine so far. However:\n\n```\nsage: floor(q)\n2238393297946874000179418290327143433\nsage: ceil(q)\n2238393297946874000179418290327143434\nsage: round(q)\n2.23839329795e+36\n```\n\nWe would expect `round(q)` to behave like `q.round()`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9306\n\n",
    "created_at": "2010-06-22T09:20:05Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7",
    "title": "round incoherent with ceil/floor on rational numbers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9306",
    "user": "@zimmermann6"
}
```
Assignee: @aghitza

Consider the following:

```
sage: q=2^200/3^50
sage: q.floor()
2238393297946874000179418290327143433
sage: q.ceil()
2238393297946874000179418290327143434
sage: q.round()
2238393297946874000179418290327143433
```

This is fine so far. However:

```
sage: floor(q)
2238393297946874000179418290327143433
sage: ceil(q)
2238393297946874000179418290327143434
sage: round(q)
2.23839329795e+36
```

We would expect `round(q)` to behave like `q.round()`.

Issue created by migration from https://trac.sagemath.org/ticket/9306





---

archive/issue_comments_087645.json:
```json
{
    "body": "Attachment [trac_9306_round_on_rationals.patch](tarball://root/attachments/some-uuid/ticket9306/trac_9306_round_on_rationals.patch) by @haikona created at 2011-03-22 21:14:52\n\nChanges the round() command to defer to an element's .round() method if no precision is specified.",
    "created_at": "2011-03-22T21:14:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9306#issuecomment-87645",
    "user": "@haikona"
}
```

Attachment [trac_9306_round_on_rationals.patch](tarball://root/attachments/some-uuid/ticket9306/trac_9306_round_on_rationals.patch) by @haikona created at 2011-03-22 21:14:52

Changes the round() command to defer to an element's .round() method if no precision is specified.



---

archive/issue_comments_087646.json:
```json
{
    "body": "The above change alters the behaviour of sage's round() command. Before it *always* returned a real double field element; now it defers to an element's .round() method if no precision is specified, i.e. a sage Integer is returned in these cases. This makes round(x) and x.round() agree whenever x has a .round() method.",
    "created_at": "2011-03-22T21:20:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9306#issuecomment-87646",
    "user": "@haikona"
}
```

The above change alters the behaviour of sage's round() command. Before it *always* returned a real double field element; now it defers to an element's .round() method if no precision is specified, i.e. a sage Integer is returned in these cases. This makes round(x) and x.round() agree whenever x has a .round() method.



---

archive/issue_comments_087647.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-03-22T21:20:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9306#issuecomment-87647",
    "user": "@haikona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087648.json:
```json
{
    "body": "Changing keywords from \"\" to \"round\".",
    "created_at": "2011-03-22T21:20:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9306#issuecomment-87648",
    "user": "@haikona"
}
```

Changing keywords from "" to "round".



---

archive/issue_comments_087649.json:
```json
{
    "body": "Five doctests failed, then failed to fail when I retested them, including devel/sage/sage/tests/startup.py . Code is easy to read and clearly does what it is intended to do, which intent I agree with. Everything looks good!",
    "created_at": "2011-03-23T01:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9306#issuecomment-87649",
    "user": "@kini"
}
```

Five doctests failed, then failed to fail when I retested them, including devel/sage/sage/tests/startup.py . Code is easy to read and clearly does what it is intended to do, which intent I agree with. Everything looks good!



---

archive/issue_comments_087650.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-23T01:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9306#issuecomment-87650",
    "user": "@kini"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087651.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-04-07T13:48:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9306#issuecomment-87651",
    "user": "@jdemeyer"
}
```

Resolution: fixed
