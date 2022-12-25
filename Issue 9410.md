# Issue 9410: EC.local_data() can't handle extensions of number fields

archive/issues_009410.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nCC:  @williamstein cturner beankao\n\nKeywords: local_data\n\nIn 4.4.4 the following code produces a ValueError:\n\n\n```\nsage: K.<a> = NumberField(x^2+1)\nsage: L.<b> = K.extension(x^2-17)\nsage: E = EllipticCurve(L, [1,1])\nsage: E.local_data()\n```\n\n\nAs a workaround, one can use absolute_field:\n\n\n```\nL1.<c> = L.absolute_field()\nE1 = EllipticCurve(L1, [1,1])\nE1.local_data()\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9410\n\n",
    "created_at": "2010-07-02T17:40:15Z",
    "labels": [
        "component: elliptic curves",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "EC.local_data() can't handle extensions of number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9410",
    "user": "https://github.com/arminstraub"
}
```
Assignee: @JohnCremona

CC:  @williamstein cturner beankao

Keywords: local_data

In 4.4.4 the following code produces a ValueError:


```
sage: K.<a> = NumberField(x^2+1)
sage: L.<b> = K.extension(x^2-17)
sage: E = EllipticCurve(L, [1,1])
sage: E.local_data()
```


As a workaround, one can use absolute_field:


```
L1.<c> = L.absolute_field()
E1 = EllipticCurve(L1, [1,1])
E1.local_data()
```




Issue created by migration from https://trac.sagemath.org/ticket/9410





---

archive/issue_comments_089537.json:
```json
{
    "body": "This seems to have been fixed since I reported this a couple of years ago, so this ticket can be closed.  Can/should I do something to flag the ticket as such?",
    "created_at": "2016-08-08T12:34:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9410#issuecomment-89537",
    "user": "https://github.com/arminstraub"
}
```

This seems to have been fixed since I reported this a couple of years ago, so this ticket can be closed.  Can/should I do something to flag the ticket as such?



---

archive/issue_comments_089538.json:
```json
{
    "body": "Choose invalid/dontfix from the Milestone menu (under \"Modify Ticket\").  It will the be closed.\n\nI think it has been fixed for ages, but it hardly seems worth looking for when.  Thanks for noticing -- I'll let you follow the above instructions.",
    "created_at": "2016-08-08T12:51:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9410#issuecomment-89538",
    "user": "https://github.com/JohnCremona"
}
```

Choose invalid/dontfix from the Milestone menu (under "Modify Ticket").  It will the be closed.

I think it has been fixed for ages, but it hardly seems worth looking for when.  Thanks for noticing -- I'll let you follow the above instructions.



---

archive/issue_comments_089539.json:
```json
{
    "body": "yes, please set to positive review with milestone \"duplicate invalid wontfix\"",
    "created_at": "2016-08-08T12:53:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9410#issuecomment-89539",
    "user": "https://github.com/fchapoton"
}
```

yes, please set to positive review with milestone "duplicate invalid wontfix"



---

archive/issue_events_023242.json:
```json
{
    "actor": "https://github.com/arminstraub",
    "created_at": "2016-08-08T13:18:10Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9410",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9410#event-23242"
}
```



---

archive/issue_comments_089540.json:
```json
{
    "body": "Thank you both!  I have changed the milestone as instructed.\n\nThere was no option yet to flag this as positively reviewed, so I didn't do that.  My guess is that one has to first set the ticket as \"needs review\" before that option becomes available.  If this should be done, please let me know.",
    "created_at": "2016-08-08T13:18:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9410#issuecomment-89540",
    "user": "https://github.com/arminstraub"
}
```

Thank you both!  I have changed the milestone as instructed.

There was no option yet to flag this as positively reviewed, so I didn't do that.  My guess is that one has to first set the ticket as "needs review" before that option becomes available.  If this should be done, please let me know.



---

archive/issue_comments_089541.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-08-08T13:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9410#issuecomment-89541",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089542.json:
```json
{
    "body": "yes, this is a 2-step job. I did the first step for you, you can now do the second step. You could have done both yourself.",
    "created_at": "2016-08-08T13:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9410#issuecomment-89542",
    "user": "https://github.com/fchapoton"
}
```

yes, this is a 2-step job. I did the first step for you, you can now do the second step. You could have done both yourself.



---

archive/issue_comments_089543.json:
```json
{
    "body": "Thanks!  I was hesitant to do that without understanding what will happen.  It is set to \"positive review\" now (with no reviewer, but I hope that is OK in such a case).",
    "created_at": "2016-08-08T13:35:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9410#issuecomment-89543",
    "user": "https://github.com/arminstraub"
}
```

Thanks!  I was hesitant to do that without understanding what will happen.  It is set to "positive review" now (with no reviewer, but I hope that is OK in such a case).



---

archive/issue_comments_089544.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-08-08T13:35:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9410#issuecomment-89544",
    "user": "https://github.com/arminstraub"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089545.json:
```json
{
    "body": "I am not sure if we need a reviewer here, but you can add your name for safety.",
    "created_at": "2016-08-08T13:37:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9410#issuecomment-89545",
    "user": "https://github.com/fchapoton"
}
```

I am not sure if we need a reviewer here, but you can add your name for safety.



---

archive/issue_comments_089546.json:
```json
{
    "body": "Done!",
    "created_at": "2016-08-08T13:45:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9410#issuecomment-89546",
    "user": "https://github.com/arminstraub"
}
```

Done!



---

archive/issue_events_023243.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2016-08-30T13:32:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9410",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9410#event-23243"
}
```



---

archive/issue_comments_089547.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2016-08-30T13:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9410#issuecomment-89547",
    "user": "https://github.com/embray"
}
```

Resolution: wontfix



---

archive/issue_comments_089548.json:
```json
{
    "body": "Determined to be invalid/duplicate/wontfix (closing as \"wontfix\" as a catch-all resolution).",
    "created_at": "2016-08-30T13:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9410#issuecomment-89548",
    "user": "https://github.com/embray"
}
```

Determined to be invalid/duplicate/wontfix (closing as "wontfix" as a catch-all resolution).
