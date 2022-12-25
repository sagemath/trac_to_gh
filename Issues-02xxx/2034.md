# Issue 2034: __floordiv__ should be part of coercion model

archive/issues_002034.json:
```json
{
    "body": "Assignee: @robertwb\n\nAdd `__floordiv__` to the coercion model for `RingElement` and change `__floordiv__` to `_floordiv_` where applicable.\n\nThis does not change any semantics of floor division, but it does fix floor division in a few cases where coercion is involved. It also fixes various segmentation faults like\n\n```\nsage: R.<x> = QQbar[]\nsage: int(1) // x\n...\n```\n\nFinally, we also implement `__itruediv__`, which was forgotten when adding `__truediv__`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2034\n\n",
    "closed_at": "2016-01-23T20:42:41Z",
    "created_at": "2008-02-02T13:52:56Z",
    "labels": [
        "component: coercion",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-7.1",
    "title": "__floordiv__ should be part of coercion model",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2034",
    "user": "https://github.com/malb"
}
```
Assignee: @robertwb

Add `__floordiv__` to the coercion model for `RingElement` and change `__floordiv__` to `_floordiv_` where applicable.

This does not change any semantics of floor division, but it does fix floor division in a few cases where coercion is involved. It also fixes various segmentation faults like

```
sage: R.<x> = QQbar[]
sage: int(1) // x
...
```

Finally, we also implement `__itruediv__`, which was forgotten when adding `__truediv__`.

Issue created by migration from https://trac.sagemath.org/ticket/2034





---

archive/issue_comments_013128.json:
```json
{
    "body": "Changing assignee from somebody to @robertwb.",
    "created_at": "2009-07-11T13:19:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2034#issuecomment-13128",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from somebody to @robertwb.



---

archive/issue_comments_013129.json:
```json
{
    "body": "Changing component from basic arithmetic to coercion.",
    "created_at": "2009-07-11T13:19:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2034#issuecomment-13129",
    "user": "https://github.com/aghitza"
}
```

Changing component from basic arithmetic to coercion.



---

archive/issue_events_004879.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:34:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2034#event-4879"
}
```



---

archive/issue_events_004880.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2034#event-4880"
}
```



---

archive/issue_events_004881.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2034#event-4881"
}
```



---

archive/issue_events_004882.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:19:32Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2034#event-4882"
}
```



---

archive/issue_events_004883.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:19:32Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2034#event-4883"
}
```



---

archive/issue_events_004884.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2034#event-4884"
}
```



---

archive/issue_events_004885.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2034#event-4885"
}
```



---

archive/issue_events_004886.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2016-01-19T10:35:10Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2034#event-4886"
}
```



---

archive/issue_events_004887.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2016-01-19T10:35:10Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "milestone": "sage-7.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2034#event-4887"
}
```



---

archive/issue_comments_013130.json:
```json
{
    "body": "New commits:",
    "created_at": "2016-01-19T16:41:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2034#issuecomment-13130",
    "user": "https://github.com/jdemeyer"
}
```

New commits:



---

archive/issue_comments_013131.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-01-19T16:41:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2034#issuecomment-13131",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_013132.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-01-20T12:47:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2034#issuecomment-13132",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_013133.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-01-20T13:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2034#issuecomment-13133",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_013134.json:
```json
{
    "body": "According to the \"principle of least surprise\", supporting floordiv for finite fields looks suspicious\n\n```\nsage: ZZ(5) // ZZ(3)\n1\nsage: GF(7)(5) // GF(7)(3)\n4\n```\nIf this is just an alias of division, why do we need it?",
    "created_at": "2016-01-20T14:22:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2034#issuecomment-13134",
    "user": "https://github.com/videlec"
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

archive/issue_comments_013135.json:
```json
{
    "body": "Replying to [comment:16 vdelecroix]:\n> According to the \"principle of least surprise\", supporting floordiv for finite fields looks suspicious\n\n\nThat's outside the scope of this ticket. This ticket only implements coercion for `__floordiv__`, it doesn't otherwise change the semantics of floor division. There shouldn't be anything controversial in this ticket.",
    "created_at": "2016-01-20T14:35:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2034#issuecomment-13135",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:16 vdelecroix]:
> According to the "principle of least surprise", supporting floordiv for finite fields looks suspicious


That's outside the scope of this ticket. This ticket only implements coercion for `__floordiv__`, it doesn't otherwise change the semantics of floor division. There shouldn't be anything controversial in this ticket.



---

archive/issue_comments_013136.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-01-20T15:01:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2034#issuecomment-13136",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_013137.json:
```json
{
    "body": "All right. Hope this will be fixed with #15260.",
    "created_at": "2016-01-20T15:01:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2034#issuecomment-13137",
    "user": "https://github.com/videlec"
}
```

All right. Hope this will be fixed with #15260.



---

archive/issue_events_004888.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2016-01-23T20:42:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2034#event-4888"
}
```



---

archive/issue_comments_013138.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-01-23T20:42:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2034#issuecomment-13138",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
