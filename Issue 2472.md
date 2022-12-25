# Issue 2472: what parent should floor return?

archive/issues_002472.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @ncalexan\n\nKeywords: floor truncate ceil ceiling parent integer\n\nI think `floor` and `ceil` and `truncate` should return integers.\n\n```\nsage: floor(2).parent()\nInteger Ring\nsage: floor(2.0).parent()\nInteger Ring\nsage: floor(RIF(2.0)).parent()\nReal Interval Field with 53 bits of precision\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2472\n\n",
    "created_at": "2008-03-11T20:58:33Z",
    "labels": [
        "component: basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "what parent should floor return?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2472",
    "user": "https://github.com/ncalexan"
}
```
Assignee: somebody

CC:  @ncalexan

Keywords: floor truncate ceil ceiling parent integer

I think `floor` and `ceil` and `truncate` should return integers.

```
sage: floor(2).parent()
Integer Ring
sage: floor(2.0).parent()
Integer Ring
sage: floor(RIF(2.0)).parent()
Real Interval Field with 53 bits of precision
```

Issue created by migration from https://trac.sagemath.org/ticket/2472





---

archive/issue_comments_016702.json:
```json
{
    "body": "> I think floor and ceil and truncate should return integers.\n\n\nI agree, though this goes against what Python does:\n\n```\nsage: math.floor(float(2.3))\n2.0    \n```\n\nI don't like Python's math.floor behavior, but I bet it agrees with the C library.\nYep:\n\n```\n     double\n     floor(double x);\n\n     long double\n     floorl(long double x);\n```\n\nI still vote for making floor always return Integer.",
    "created_at": "2008-03-11T21:03:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2472#issuecomment-16702",
    "user": "https://github.com/williamstein"
}
```

> I think floor and ceil and truncate should return integers.


I agree, though this goes against what Python does:

```
sage: math.floor(float(2.3))
2.0    
```

I don't like Python's math.floor behavior, but I bet it agrees with the C library.
Yep:

```
     double
     floor(double x);

     long double
     floorl(long double x);
```

I still vote for making floor always return Integer.



---

archive/issue_comments_016703.json:
```json
{
    "body": "But what integer should it return?  In particular, what do you want floor(RIF(1.5, 12345.678)) to return, and why?  \n\nMy vote would be that floor and ceiling should not be implemented for RIF at all, because I don't think they have a sensible meaning.\n\nNote that when William first implemented floor and ceiling for RIF, he had them return integers; but he immediately (38 minutes later, according to Mercurial) changed them to return intervals, calling this a '\"moral\" improvement'.",
    "created_at": "2008-03-12T01:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2472#issuecomment-16703",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

But what integer should it return?  In particular, what do you want floor(RIF(1.5, 12345.678)) to return, and why?  

My vote would be that floor and ceiling should not be implemented for RIF at all, because I don't think they have a sensible meaning.

Note that when William first implemented floor and ceiling for RIF, he had them return integers; but he immediately (38 minutes later, according to Mercurial) changed them to return intervals, calling this a '"moral" improvement'.



---

archive/issue_comments_016704.json:
```json
{
    "body": "Perhaps what we need is an `IntegerInterval` class which represents an interval in ZZ.\n\nI think this might even have come up in the context of valuations of p-adic numbers, and I might have even discussed it with David Roe, but I can't remember if anything came out of it.",
    "created_at": "2008-03-13T18:50:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2472#issuecomment-16704",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Perhaps what we need is an `IntegerInterval` class which represents an interval in ZZ.

I think this might even have come up in the context of valuations of p-adic numbers, and I might have even discussed it with David Roe, but I can't remember if anything came out of it.



---

archive/issue_events_005825.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2472",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2472#event-5825"
}
```



---

archive/issue_events_005826.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2472",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2472#event-5826"
}
```



---

archive/issue_events_005827.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2472",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2472#event-5827"
}
```



---

archive/issue_events_005828.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2472",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2472#event-5828"
}
```



---

archive/issue_events_005829.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2472",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2472#event-5829"
}
```



---

archive/issue_events_005830.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2472",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2472#event-5830"
}
```



---

archive/issue_events_005831.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2472",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2472#event-5831"
}
```



---

archive/issue_events_005832.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2014-09-02T08:57:32Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2472",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2472#event-5832"
}
```



---

archive/issue_events_005833.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2014-09-02T08:57:32Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2472",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2472#event-5833"
}
```



---

archive/issue_comments_016705.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-09-02T08:57:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2472#issuecomment-16705",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_016706.json:
```json
{
    "body": "We now have `unique_floor()` for `RIF` returning an integer, which solves the problem I guess.",
    "created_at": "2014-09-02T08:57:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2472#issuecomment-16706",
    "user": "https://github.com/jdemeyer"
}
```

We now have `unique_floor()` for `RIF` returning an integer, which solves the problem I guess.



---

archive/issue_comments_016707.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-09-02T08:57:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2472#issuecomment-16707",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_005834.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-09-09T14:53:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2472",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2472#event-5834"
}
```



---

archive/issue_comments_016708.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-09-09T14:53:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2472#issuecomment-16708",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
