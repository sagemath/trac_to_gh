# Issue 7984: QQbar doesn't use canonical coercion for comparison

archive/issues_007984.json:
```json
{
    "body": "Assignee: AlexGhitza\n\n\n```\nsage: QQbar(2) == GF(7)(2)\nBOOM\n```\n\n\nShould be False. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7984\n\n",
    "created_at": "2010-01-18T20:29:47Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "QQbar doesn't use canonical coercion for comparison",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7984",
    "user": "robertwb"
}
```
Assignee: AlexGhitza


```
sage: QQbar(2) == GF(7)(2)
BOOM
```


Should be False. 

Issue created by migration from https://trac.sagemath.org/ticket/7984





---

archive/issue_comments_069729.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-01-18T20:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7984#issuecomment-69729",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_069730.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-01-18T21:11:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7984#issuecomment-69730",
    "user": "wjp"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_069731.json:
```json
{
    "body": "This patch depends on #4621 but seems to break the doctest added by that patch.",
    "created_at": "2010-01-18T21:11:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7984#issuecomment-69731",
    "user": "wjp"
}
```

This patch depends on #4621 but seems to break the doctest added by that patch.



---

archive/issue_comments_069732.json:
```json
{
    "body": "This patch is correct, the one at #4621 is wrong.",
    "created_at": "2010-01-20T08:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7984#issuecomment-69732",
    "user": "robertwb"
}
```

This patch is correct, the one at #4621 is wrong.



---

archive/issue_comments_069733.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-20T08:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7984#issuecomment-69733",
    "user": "robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069734.json:
```json
{
    "body": "This one looks good to me.  However, when testing #4621 I noticed that this:\n\n```\nF.<a>= NumberField(x^2-2)\nRR(a)\n```\n\ncauses an infinite recursion, which is not good, but not caused by this patch.\n\nI am giving this a positive review, and letting #4621 be sorted out after, also the issue above.  Perhaps rwb would like to open a ticket for that unless it is already covered by one?",
    "created_at": "2010-02-21T16:04:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7984#issuecomment-69734",
    "user": "cremona"
}
```

This one looks good to me.  However, when testing #4621 I noticed that this:

```
F.<a>= NumberField(x^2-2)
RR(a)
```

causes an infinite recursion, which is not good, but not caused by this patch.

I am giving this a positive review, and letting #4621 be sorted out after, also the issue above.  Perhaps rwb would like to open a ticket for that unless it is already covered by one?



---

archive/issue_comments_069735.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-21T16:04:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7984#issuecomment-69735",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069736.json:
```json
{
    "body": "Changing keywords from \"\" to \"QQbar comparison\".",
    "created_at": "2010-02-21T16:04:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7984#issuecomment-69736",
    "user": "cremona"
}
```

Changing keywords from "" to "QQbar comparison".



---

archive/issue_comments_069737.json:
```json
{
    "body": "Robert: I have merged [7984-qqbar-cmp.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7984/7984-qqbar-cmp.patch) in your name with a sensible commit message.",
    "created_at": "2010-03-02T21:06:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7984#issuecomment-69737",
    "user": "mvngu"
}
```

Robert: I have merged [7984-qqbar-cmp.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7984/7984-qqbar-cmp.patch) in your name with a sensible commit message.



---

archive/issue_comments_069738.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-02T21:06:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7984#issuecomment-69738",
    "user": "mvngu"
}
```

Resolution: fixed
