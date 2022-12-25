# Issue 6430: Cython problem with hashing Laurent series elements over CDF

archive/issues_006430.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @mwhansen\n\nKeywords: hash Laurent series\n\n```\nsage: hash(1/CDF[['t']].gen())\n-2\nsage: hash(1/CDF[['t']].gen()^2)\n---------------------------------------------------------------------------\nSystemError                               Traceback (most recent call last)\n\n/Users/ncalexan/Documents/School/period_matrix/riemann_surface.py in <module>()\n\nSystemError: error return without exception set\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/6430\n\n",
    "closed_at": "2019-02-26T13:58:00Z",
    "created_at": "2009-06-27T04:37:25Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Cython problem with hashing Laurent series elements over CDF",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6430",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @malb

CC:  @mwhansen

Keywords: hash Laurent series

```
sage: hash(1/CDF[['t']].gen())
-2
sage: hash(1/CDF[['t']].gen()^2)
---------------------------------------------------------------------------
SystemError                               Traceback (most recent call last)

/Users/ncalexan/Documents/School/period_matrix/riemann_surface.py in <module>()

SystemError: error return without exception set
```

Issue created by migration from https://trac.sagemath.org/ticket/6430





---

archive/issue_events_015159.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6430",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6430#event-15159"
}
```



---

archive/issue_events_015160.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6430",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6430#event-15160"
}
```



---

archive/issue_events_015161.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6430",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6430#event-15161"
}
```



---

archive/issue_events_015162.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6430",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6430#event-15162"
}
```



---

archive/issue_events_015163.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6430",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6430#event-15163"
}
```



---

archive/issue_events_015164.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6430",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6430#event-15164"
}
```



---

archive/issue_events_015165.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6430",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6430#event-15165"
}
```



---

archive/issue_comments_051546.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2018-08-22T18:48:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6430#issuecomment-51546",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_051547.json:
```json
{
    "body": "works fine in 8.4.b1",
    "created_at": "2018-08-22T18:48:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6430#issuecomment-51547",
    "user": "https://github.com/fchapoton"
}
```

works fine in 8.4.b1



---

archive/issue_events_015166.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2018-08-22T18:48:02Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6430",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6430#event-15166"
}
```



---

archive/issue_events_015167.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2018-08-22T18:48:02Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6430",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6430#event-15167"
}
```



---

archive/issue_comments_051548.json:
```json
{
    "body": "Confirmed.",
    "created_at": "2018-08-22T22:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6430#issuecomment-51548",
    "user": "https://github.com/tscrim"
}
```

Confirmed.



---

archive/issue_comments_051549.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-08-22T22:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6430#issuecomment-51549",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_051550.json:
```json
{
    "body": "Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.",
    "created_at": "2019-02-26T13:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6430#issuecomment-51550",
    "user": "https://github.com/embray"
}
```

Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.



---

archive/issue_events_015168.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2019-02-26T13:58:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6430",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6430#event-15168"
}
```



---

archive/issue_comments_051551.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2019-02-26T13:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6430#issuecomment-51551",
    "user": "https://github.com/embray"
}
```

Resolution: invalid
