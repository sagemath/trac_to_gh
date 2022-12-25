# Issue 5126: error coercing stacked polynomial rings to relative number fields

archive/issues_005126.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @roed314\n\nKeywords: polynomial ring coercion relative number field\n\nFrom David Roe, reviewing #1367:\n\n\n```\nI'm not completely convinced that the following example is the behavior we want:\n\nsage: K.<a> = NumberField?(ZZx?.05 + 2, 'a') sage: L.<b> = K.extension(ZZx?.02 + 3*a, 'b') sage: u = QQu?.gen() sage: t = u.parent()t?.gen()\n\nsage: L(u*5) 5*b\n\nI guess if we're going to convert at all this makes the most sense, but I want to think about it a bit more. I'm even less convinced of the following:\n\nsage: W.<w> = t.parent()[] sage: L(w*5) 5*b sage: L(W(t)) 5*a sage: L(W(u)) TypeError?\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5126\n\n",
    "created_at": "2009-01-29T05:07:46Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "error coercing stacked polynomial rings to relative number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5126",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @williamstein

CC:  @roed314

Keywords: polynomial ring coercion relative number field

From David Roe, reviewing #1367:


```
I'm not completely convinced that the following example is the behavior we want:

sage: K.<a> = NumberField?(ZZx?.05 + 2, 'a') sage: L.<b> = K.extension(ZZx?.02 + 3*a, 'b') sage: u = QQu?.gen() sage: t = u.parent()t?.gen()

sage: L(u*5) 5*b

I guess if we're going to convert at all this makes the most sense, but I want to think about it a bit more. I'm even less convinced of the following:

sage: W.<w> = t.parent()[] sage: L(w*5) 5*b sage: L(W(t)) 5*a sage: L(W(u)) TypeError?
```


Issue created by migration from https://trac.sagemath.org/ticket/5126





---

archive/issue_events_011860.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-29T07:04:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5126",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5126#event-11860"
}
```



---

archive/issue_comments_039102.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-21T08:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5126#issuecomment-39102",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to number fields.



---

archive/issue_comments_039103.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-21T08:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5126#issuecomment-39103",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_events_011861.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5126",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5126#event-11861"
}
```



---

archive/issue_events_011862.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5126",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5126#event-11862"
}
```



---

archive/issue_events_011863.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5126",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5126#event-11863"
}
```



---

archive/issue_events_011864.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5126",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5126#event-11864"
}
```



---

archive/issue_events_011865.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5126",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5126#event-11865"
}
```



---

archive/issue_events_011866.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5126",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5126#event-11866"
}
```



---

archive/issue_events_011867.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5126",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5126#event-11867"
}
```



---

archive/issue_events_011868.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5126",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5126#event-11868"
}
```
