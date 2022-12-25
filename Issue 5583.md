# Issue 5583: coercion bug in perm groups

archive/issues_005583.json:
```json
{
    "body": "Assignee: joyner\n\nCC:  @tscrim\n\n\n```\nsage: PermutationGroup([(), (1,3)]).has_coerce_map_from( PermutationGroup([(), (1,2)]) )\nTrue\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5583\n\n",
    "created_at": "2009-03-22T11:36:05Z",
    "labels": [
        "component: group theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.8",
    "title": "coercion bug in perm groups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5583",
    "user": "https://github.com/robertwb"
}
```
Assignee: joyner

CC:  @tscrim


```
sage: PermutationGroup([(), (1,3)]).has_coerce_map_from( PermutationGroup([(), (1,2)]) )
True
```


Issue created by migration from https://trac.sagemath.org/ticket/5583





---

archive/issue_events_013143.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5583",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5583#event-13143"
}
```



---

archive/issue_events_013144.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5583",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5583#event-13144"
}
```



---

archive/issue_events_013145.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5583",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5583#event-13145"
}
```



---

archive/issue_events_013146.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5583",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5583#event-13146"
}
```



---

archive/issue_events_013147.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5583",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5583#event-13147"
}
```



---

archive/issue_events_013148.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5583",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5583#event-13148"
}
```



---

archive/issue_events_013149.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5583",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5583#event-13149"
}
```



---

archive/issue_comments_043435.json:
```json
{
    "body": "works in 8.8.b5:\n\n```\nsage: PermutationGroup([(), (1,3)]).has_coerce_map_from( PermutationGroup([(), (\n....: 1,2)]) )\n\nFalse\n```\n",
    "created_at": "2019-05-17T17:40:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5583#issuecomment-43435",
    "user": "https://github.com/fchapoton"
}
```

works in 8.8.b5:

```
sage: PermutationGroup([(), (1,3)]).has_coerce_map_from( PermutationGroup([(), (
....: 1,2)]) )

False
```




---

archive/issue_events_013150.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2019-05-17T17:40:16Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5583",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5583#event-13150"
}
```



---

archive/issue_events_013151.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2019-05-17T17:40:16Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5583",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5583#event-13151"
}
```



---

archive/issue_comments_043436.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2019-05-17T17:40:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5583#issuecomment-43436",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_043437.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2019-05-17T17:58:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5583#issuecomment-43437",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_043438.json:
```json
{
    "body": "I agree. It works going back to Sage 8.3 (that's the oldest version I have installed), in both Python 2 and Python 3.",
    "created_at": "2019-05-17T17:58:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5583#issuecomment-43438",
    "user": "https://github.com/jhpalmieri"
}
```

I agree. It works going back to Sage 8.3 (that's the oldest version I have installed), in both Python 2 and Python 3.



---

archive/issue_comments_043439.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2019-06-01T07:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5583#issuecomment-43439",
    "user": "https://github.com/fchapoton"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_043440.json:
```json
{
    "body": "I have decided to add a doctest, just to be safe.\n----\nNew commits:",
    "created_at": "2019-06-01T07:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5583#issuecomment-43440",
    "user": "https://github.com/fchapoton"
}
```

I have decided to add a doctest, just to be safe.
----
New commits:



---

archive/issue_events_013152.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2019-06-01T07:20:45Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5583",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5583#event-13152"
}
```



---

archive/issue_events_013153.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2019-06-01T07:20:45Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5583",
    "milestone": "sage-8.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5583#event-13153"
}
```



---

archive/issue_comments_043441.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2019-06-01T07:20:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5583#issuecomment-43441",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_043442.json:
```json
{
    "body": "green bot, please review this easy ticket",
    "created_at": "2019-06-01T10:25:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5583#issuecomment-43442",
    "user": "https://github.com/fchapoton"
}
```

green bot, please review this easy ticket



---

archive/issue_comments_043443.json:
```json
{
    "body": "LGTM.",
    "created_at": "2019-06-01T23:37:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5583#issuecomment-43443",
    "user": "https://github.com/tscrim"
}
```

LGTM.



---

archive/issue_comments_043444.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2019-06-01T23:37:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5583#issuecomment-43444",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_043445.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2019-06-05T18:31:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5583#issuecomment-43445",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_013154.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2019-06-05T18:31:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5583",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5583#event-13154"
}
```
