# Issue 8822: Bug in Family constructor

archive/issues_008822.json:
```json
{
    "body": "Assignee: @hivert\n\nCC:  sage-combinat\n\nKeywords: combinat, family\n\n```\nsage: f = Family(Zmod(3), lambda i: 2*i, lazy=False)\nsage: f\nLazy family (<lambda>(i))_{i in Ring of integers modulo 3}\n```\n\nShould we really just silently ignore the intent here, or should\n\n`Family(S, f, lazy=False)` always return `Family([i for i in S], f)`\n\n(I guess the default for lazy should then be made 'None' so that 'True',\n'False' and 'None' could all have different behaviors.)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8822\n\n",
    "created_at": "2010-04-29T12:25:31Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.8",
    "title": "Bug in Family constructor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8822",
    "user": "https://github.com/jbandlow"
}
```
Assignee: @hivert

CC:  sage-combinat

Keywords: combinat, family

```
sage: f = Family(Zmod(3), lambda i: 2*i, lazy=False)
sage: f
Lazy family (<lambda>(i))_{i in Ring of integers modulo 3}
```

Should we really just silently ignore the intent here, or should

`Family(S, f, lazy=False)` always return `Family([i for i in S], f)`

(I guess the default for lazy should then be made 'None' so that 'True',
'False' and 'None' could all have different behaviors.)


Issue created by migration from https://trac.sagemath.org/ticket/8822





---

archive/issue_comments_080891.json:
```json
{
    "body": "Changing assignee from sage-combinat to @hivert.",
    "created_at": "2010-05-13T22:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8822#issuecomment-80891",
    "user": "https://github.com/hivert"
}
```

Changing assignee from sage-combinat to @hivert.



---

archive/issue_comments_080892.json:
```json
{
    "body": "I'm working on this one\n\nFlorent",
    "created_at": "2010-05-13T22:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8822#issuecomment-80892",
    "user": "https://github.com/hivert"
}
```

I'm working on this one

Florent



---

archive/issue_events_021511.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8822",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8822#event-21511"
}
```



---

archive/issue_events_021512.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8822",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8822#event-21512"
}
```



---

archive/issue_events_021513.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8822",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8822#event-21513"
}
```



---

archive/issue_events_021514.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8822",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8822#event-21514"
}
```



---

archive/issue_events_021515.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8822",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8822#event-21515"
}
```



---

archive/issue_events_021516.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8822",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8822#event-21516"
}
```



---

archive/issue_events_021517.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8822",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8822#event-21517"
}
```



---

archive/issue_events_021518.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-08-17T16:52:31Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8822",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8822#event-21518"
}
```



---

archive/issue_events_021519.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-08-17T16:52:31Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8822",
    "milestone": "sage-9.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8822#event-21519"
}
```



---

archive/issue_comments_080893.json:
```json
{
    "body": "Setting new milestone based on a cursory review of ticket status, priority, and last modification date.",
    "created_at": "2021-02-13T20:51:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8822#issuecomment-80893",
    "user": "https://github.com/mkoeppe"
}
```

Setting new milestone based on a cursory review of ticket status, priority, and last modification date.



---

archive/issue_events_021520.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-02-13T20:51:01Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8822",
    "milestone": "sage-9.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8822#event-21520"
}
```



---

archive/issue_events_021521.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-02-13T20:51:01Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8822",
    "milestone": "sage-9.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8822#event-21521"
}
```



---

archive/issue_events_021522.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-07-19T01:43:17Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8822",
    "milestone": "sage-9.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8822#event-21522"
}
```



---

archive/issue_events_021523.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-07-19T01:43:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8822",
    "milestone": "sage-9.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8822#event-21523"
}
```



---

archive/issue_events_021524.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-12-18T19:11:26Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8822",
    "milestone": "sage-9.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8822#event-21524"
}
```



---

archive/issue_events_021525.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-12-18T19:11:26Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8822",
    "milestone": "sage-9.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8822#event-21525"
}
```



---

archive/issue_events_021526.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2022-04-01T21:16:35Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8822",
    "milestone": "sage-9.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8822#event-21526"
}
```



---

archive/issue_events_021527.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2022-04-01T21:16:35Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8822",
    "milestone": "sage-9.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8822#event-21527"
}
```



---

archive/issue_events_021528.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2022-08-31T05:25:02Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8822",
    "milestone": "sage-9.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8822#event-21528"
}
```



---

archive/issue_events_021529.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2022-08-31T05:25:02Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8822",
    "milestone": "sage-9.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8822#event-21529"
}
```
