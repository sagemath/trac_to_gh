# Issue 7984: QQbar doesn't use canonical coercion for comparison

archive/issues_007984.json:
```json
{
    "body": "Assignee: @aghitza\n\n\n```\nsage: QQbar(2) == GF(7)(2)\nBOOM\n```\n\n\nShould be False. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7984\n\n",
    "created_at": "2010-01-18T20:29:47Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "QQbar doesn't use canonical coercion for comparison",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7984",
    "user": "https://github.com/robertwb"
}
```
Assignee: @aghitza


```
sage: QQbar(2) == GF(7)(2)
BOOM
```


Should be False. 

Issue created by migration from https://trac.sagemath.org/ticket/7984





---

archive/issue_comments_069609.json:
```json
{
    "body": "Attachment [7984-qqbar-cmp.patch](tarball://root/attachments/some-uuid/ticket7984/7984-qqbar-cmp.patch) by @robertwb created at 2010-01-18 20:31:34",
    "created_at": "2010-01-18T20:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7984#issuecomment-69609",
    "user": "https://github.com/robertwb"
}
```

Attachment [7984-qqbar-cmp.patch](tarball://root/attachments/some-uuid/ticket7984/7984-qqbar-cmp.patch) by @robertwb created at 2010-01-18 20:31:34



---

archive/issue_comments_069610.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-01-18T21:11:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7984#issuecomment-69610",
    "user": "https://github.com/wjp"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_069611.json:
```json
{
    "body": "This patch depends on #4621 but seems to break the doctest added by that patch.",
    "created_at": "2010-01-18T21:11:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7984#issuecomment-69611",
    "user": "https://github.com/wjp"
}
```

This patch depends on #4621 but seems to break the doctest added by that patch.



---

archive/issue_comments_069612.json:
```json
{
    "body": "This patch is correct, the one at #4621 is wrong.",
    "created_at": "2010-01-20T08:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7984#issuecomment-69612",
    "user": "https://github.com/robertwb"
}
```

This patch is correct, the one at #4621 is wrong.



---

archive/issue_comments_069613.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-20T08:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7984#issuecomment-69613",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069614.json:
```json
{
    "body": "This one looks good to me.  However, when testing #4621 I noticed that this:\n\n```\nF.<a>= NumberField(x^2-2)\nRR(a)\n```\n\ncauses an infinite recursion, which is not good, but not caused by this patch.\n\nI am giving this a positive review, and letting #4621 be sorted out after, also the issue above.  Perhaps rwb would like to open a ticket for that unless it is already covered by one?",
    "created_at": "2010-02-21T16:04:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7984#issuecomment-69614",
    "user": "https://github.com/JohnCremona"
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

archive/issue_comments_069615.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-21T16:04:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7984#issuecomment-69615",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069616.json:
```json
{
    "body": "Changing keywords from \"\" to \"QQbar comparison\".",
    "created_at": "2010-02-21T16:04:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7984#issuecomment-69616",
    "user": "https://github.com/JohnCremona"
}
```

Changing keywords from "" to "QQbar comparison".



---

archive/issue_comments_069617.json:
```json
{
    "body": "Robert: I have merged [7984-qqbar-cmp.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7984/7984-qqbar-cmp.patch) in your name with a sensible commit message.",
    "created_at": "2010-03-02T21:06:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7984#issuecomment-69617",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Robert: I have merged [7984-qqbar-cmp.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7984/7984-qqbar-cmp.patch) in your name with a sensible commit message.



---

archive/issue_comments_069618.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-02T21:06:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7984#issuecomment-69618",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
