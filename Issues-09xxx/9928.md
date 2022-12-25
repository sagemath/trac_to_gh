# Issue 9928: polynomial ring over pAdics doesn't respect the sparse argument

archive/issues_009928.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @roed314 @xcaruso\n\nKeywords: padicIMA\n\n```\nsage: R.<x> = PolynomialRing(Zp(17), sparse=True)\nsage: x**(10**10)\nTraceback (most recent call last)\n...\nMemoryError:\n```\n\nThis should work (and be fast). The solution is probably in the file `polynomial_ring_constructor.py` in the function `single_variate`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9929\n\n",
    "closed_at": "2019-02-26T13:58:00Z",
    "created_at": "2010-09-17T07:27:14Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "polynomial ring over pAdics doesn't respect the sparse argument",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9928",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```
Assignee: @aghitza

CC:  @roed314 @xcaruso

Keywords: padicIMA

```
sage: R.<x> = PolynomialRing(Zp(17), sparse=True)
sage: x**(10**10)
Traceback (most recent call last)
...
MemoryError:
```

This should work (and be fast). The solution is probably in the file `polynomial_ring_constructor.py` in the function `single_variate`.

Issue created by migration from https://trac.sagemath.org/ticket/9929





---

archive/issue_events_025038.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9928",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9928#event-25038"
}
```



---

archive/issue_events_025039.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9928",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9928#event-25039"
}
```



---

archive/issue_events_025040.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9928",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9928#event-25040"
}
```



---

archive/issue_events_025041.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9928",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9928#event-25041"
}
```



---

archive/issue_events_025042.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9928",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9928#event-25042"
}
```



---

archive/issue_events_025043.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9928",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9928#event-25043"
}
```



---

archive/issue_events_025044.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9928",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9928#event-25044"
}
```



---

archive/issue_events_025045.json:
```json
{
    "actor": "https://github.com/saraedum",
    "created_at": "2018-07-26T22:23:51Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9928",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9928#event-25045"
}
```



---

archive/issue_events_025046.json:
```json
{
    "actor": "https://github.com/saraedum",
    "created_at": "2018-07-26T22:23:51Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9928",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9928#event-25046"
}
```



---

archive/issue_comments_098705.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2018-07-26T22:23:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9928#issuecomment-98705",
    "user": "https://github.com/saraedum"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098706.json:
```json
{
    "body": "Changing keywords from \"\" to \"padicIMA\".",
    "created_at": "2018-07-26T22:23:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9928#issuecomment-98706",
    "user": "https://github.com/saraedum"
}
```

Changing keywords from "" to "padicIMA".



---

archive/issue_comments_098707.json:
```json
{
    "body": "works for me.",
    "created_at": "2018-07-26T22:23:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9928#issuecomment-98707",
    "user": "https://github.com/saraedum"
}
```

works for me.



---

archive/issue_comments_098708.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-07-26T22:23:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9928#issuecomment-98708",
    "user": "https://github.com/saraedum"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_025047.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2019-02-26T13:58:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9928",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9928#event-25047"
}
```



---

archive/issue_comments_098709.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2019-02-26T13:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9928#issuecomment-98709",
    "user": "https://github.com/embray"
}
```

Resolution: invalid



---

archive/issue_comments_098710.json:
```json
{
    "body": "Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.",
    "created_at": "2019-02-26T13:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9928#issuecomment-98710",
    "user": "https://github.com/embray"
}
```

Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.
