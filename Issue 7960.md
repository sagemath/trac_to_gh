# Issue 7960: QQbar should accept number field elements with embeddings

archive/issues_007960.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @videlec\n\nOne should be able to do \n\n\n```\nsage: K.<a> = NumberField(x^3-x+1, embedding=-1.32)\nsage: QQBar(a)\n-1.324717957244746?\n```\n\n\nFollowup to #4621\n\nIssue created by migration from https://trac.sagemath.org/ticket/7960\n\n",
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
sage: QQBar(a)
-1.324717957244746?
```


Followup to #4621

Issue created by migration from https://trac.sagemath.org/ticket/7960





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
    "body": "The requested example now works.  It would be even nicer to also have a coercion map from `K` to `QQbar`, but currently we do not have this:\n\n```\nsage: K.<a> = NumberField(x^3 - x + 1, embedding=-1.32)\nsage: QQbar(a)\n-1.324717957244746?\nsage: QQbar.coerce_map_from(K) is None\nTrue\n```\n",
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
    "body": "Replying to [comment:8 pbruin]:\n> It would be even nicer to also have a coercion map from `K` to `QQbar`\nOK, there is already a ticket for this: #5355.  Positive review for this one.",
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

archive/issue_events_008176.json:
```json
{
    "actor": "@embray",
    "created_at": "2019-02-26T13:58:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7960",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7960#event-8176"
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
