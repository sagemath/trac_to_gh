# Issue 7960: QQbar should accept number field elements with embeddings

archive/issues_007960.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @videlec\n\nOne should be able to do \n\n```\nsage: K.<a> = NumberField(x^3-x+1, embedding=-1.32)\nsage: QQbar(a)\n-1.324717957244746?\n```\n\nFollowup to #4621\n\nIssue created by migration from https://trac.sagemath.org/ticket/7960\n\n",
    "closed_at": "2019-02-26T13:58:00Z",
    "created_at": "2010-01-17T00:26:12Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "QQbar should accept number field elements with embeddings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7960",
    "user": "https://github.com/robertwb"
}
```
Assignee: @williamstein

CC:  @videlec

One should be able to do 

```
sage: K.<a> = NumberField(x^3-x+1, embedding=-1.32)
sage: QQbar(a)
-1.324717957244746?
```

Followup to #4621

Issue created by migration from https://trac.sagemath.org/ticket/7960





---

archive/issue_events_019048.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7960",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7960#event-19048"
}
```



---

archive/issue_events_019049.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7960",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7960#event-19049"
}
```



---

archive/issue_events_019050.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7960",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7960#event-19050"
}
```



---

archive/issue_events_019051.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7960",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7960#event-19051"
}
```



---

archive/issue_events_019052.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7960",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7960#event-19052"
}
```



---

archive/issue_events_019053.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7960",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7960#event-19053"
}
```



---

archive/issue_events_019054.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7960",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7960#event-19054"
}
```



---

archive/issue_comments_069341.json:
```json
{
    "body": "cc'ing me.\n\nThe function `sage.rings.number_field.number_field_morphisms.create_embedding_from_approx` should really be smarter. This is related to what I am currently doing in #17830.",
    "created_at": "2015-02-26T10:06:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7960#issuecomment-69341",
    "user": "https://github.com/videlec"
}
```

cc'ing me.

The function `sage.rings.number_field.number_field_morphisms.create_embedding_from_approx` should really be smarter. This is related to what I am currently doing in #17830.



---

archive/issue_events_019055.json:
```json
{
    "actor": "https://github.com/mezzarobba",
    "created_at": "2018-09-22T14:31:45Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7960",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7960#event-19055"
}
```



---

archive/issue_events_019056.json:
```json
{
    "actor": "https://github.com/mezzarobba",
    "created_at": "2018-09-22T14:31:45Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7960",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7960#event-19056"
}
```



---

archive/issue_comments_069342.json:
```json
{
    "body": "Fixed in #13041.",
    "created_at": "2018-09-22T14:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7960#issuecomment-69342",
    "user": "https://github.com/mezzarobba"
}
```

Fixed in #13041.



---

archive/issue_comments_069343.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2018-10-02T00:59:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7960#issuecomment-69343",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069344.json:
```json
{
    "body": "The requested example now works.  It would be even nicer to also have a coercion map from `K` to `QQbar`, but currently we do not have this:\n\n```\nsage: K.<a> = NumberField(x^3 - x + 1, embedding=-1.32)\nsage: QQbar(a)\n-1.324717957244746?\nsage: QQbar.coerce_map_from(K) is None\nTrue\n```",
    "created_at": "2018-11-09T13:41:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7960#issuecomment-69344",
    "user": "https://github.com/pjbruin"
}
```

The requested example now works.  It would be even nicer to also have a coercion map from `K` to `QQbar`, but currently we do not have this:

```
sage: K.<a> = NumberField(x^3 - x + 1, embedding=-1.32)
sage: QQbar(a)
-1.324717957244746?
sage: QQbar.coerce_map_from(K) is None
True
```



---

archive/issue_comments_069345.json:
```json
{
    "body": "Replying to [comment:8 pbruin]:\n> It would be even nicer to also have a coercion map from `K` to `QQbar`\n\nOK, there is already a ticket for this: #5355.  Positive review for this one.",
    "created_at": "2018-11-09T13:44:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7960#issuecomment-69345",
    "user": "https://github.com/pjbruin"
}
```

Replying to [comment:8 pbruin]:
> It would be even nicer to also have a coercion map from `K` to `QQbar`

OK, there is already a ticket for this: #5355.  Positive review for this one.



---

archive/issue_comments_069346.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-11-09T13:44:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7960#issuecomment-69346",
    "user": "https://github.com/pjbruin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069347.json:
```json
{
    "body": "Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.",
    "created_at": "2019-02-26T13:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7960#issuecomment-69347",
    "user": "https://github.com/embray"
}
```

Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.



---

archive/issue_comments_069348.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2019-02-26T13:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7960#issuecomment-69348",
    "user": "https://github.com/embray"
}
```

Resolution: invalid



---

archive/issue_events_019057.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2019-02-26T13:58:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7960",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7960#event-19057"
}
```



---

archive/issue_comments_069349.json:
```json
{
    "body": "Just fixing the example in the ticket description so anyone can check this now works.",
    "created_at": "2019-02-26T14:23:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7960#issuecomment-69349",
    "user": "https://github.com/slel"
}
```

Just fixing the example in the ticket description so anyone can check this now works.
