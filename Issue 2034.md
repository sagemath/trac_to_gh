# Issue 2034: {{{__floordiv__}}} should be part of coercion modell

archive/issues_002034.json:
```json
{
    "body": "Assignee: somebody\n\nbut it isn't\n\nIssue created by migration from https://trac.sagemath.org/ticket/2034\n\n",
    "created_at": "2008-02-02T13:52:56Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-7.1",
    "title": "{{{__floordiv__}}} should be part of coercion modell",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2034",
    "user": "malb"
}
```
Assignee: somebody

but it isn't

Issue created by migration from https://trac.sagemath.org/ticket/2034





---

archive/issue_comments_013159.json:
```json
{
    "body": "Changing assignee from somebody to robertwb.",
    "created_at": "2009-07-11T13:19:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2034#issuecomment-13159",
    "user": "AlexGhitza"
}
```

Changing assignee from somebody to robertwb.



---

archive/issue_comments_013160.json:
```json
{
    "body": "Changing component from basic arithmetic to coercion.",
    "created_at": "2009-07-11T13:19:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2034#issuecomment-13160",
    "user": "AlexGhitza"
}
```

Changing component from basic arithmetic to coercion.



---

archive/issue_comments_013161.json:
```json
{
    "body": "New commits:",
    "created_at": "2016-01-19T16:41:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2034#issuecomment-13161",
    "user": "jdemeyer"
}
```

New commits:



---

archive/issue_comments_013162.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-01-19T16:41:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2034#issuecomment-13162",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_013163.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-01-20T12:47:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2034#issuecomment-13163",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_013164.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-01-20T13:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2034#issuecomment-13164",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_013165.json:
```json
{
    "body": "According to the \"principle of least surprise\", supporting floordiv for finite fields looks suspicious\n\n```\nsage: ZZ(5) // ZZ(3)\n1\nsage: GF(7)(5) // GF(7)(3)\n4\n```\n\nIf this is just an alias of division, why do we need it?",
    "created_at": "2016-01-20T14:22:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2034#issuecomment-13165",
    "user": "vdelecroix"
}
```

According to the "principle of least surprise", supporting floordiv for finite fields looks suspicious

```
sage: ZZ(5) // ZZ(3)
1
sage: GF(7)(5) // GF(7)(3)
4
```

If this is just an alias of division, why do we need it?



---

archive/issue_comments_013166.json:
```json
{
    "body": "Replying to [comment:16 vdelecroix]:\n> According to the \"principle of least surprise\", supporting floordiv for finite fields looks suspicious\n\nThat's outside the scope of this ticket. This ticket only implements coercion for `__floordiv__`, it doesn't otherwise change the semantics of floor division. There shouldn't be anything controversial in this ticket.",
    "created_at": "2016-01-20T14:35:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2034#issuecomment-13166",
    "user": "jdemeyer"
}
```

Replying to [comment:16 vdelecroix]:
> According to the "principle of least surprise", supporting floordiv for finite fields looks suspicious

That's outside the scope of this ticket. This ticket only implements coercion for `__floordiv__`, it doesn't otherwise change the semantics of floor division. There shouldn't be anything controversial in this ticket.



---

archive/issue_comments_013167.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-01-20T15:01:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2034#issuecomment-13167",
    "user": "vdelecroix"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_013168.json:
```json
{
    "body": "All right. Hope this will be fixed with #15260.",
    "created_at": "2016-01-20T15:01:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2034#issuecomment-13168",
    "user": "vdelecroix"
}
```

All right. Hope this will be fixed with #15260.



---

archive/issue_comments_013169.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-01-23T20:42:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2034#issuecomment-13169",
    "user": "vbraun"
}
```

Resolution: fixed
