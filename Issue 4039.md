# Issue 4039: choose one name for  partial fraction decompositions

archive/issues_004039.json:
```json
{
    "body": "Assignee: tbd\n\nTwo different ways to do partial fractions should have the same function name:\n\n```\nsage: x=polygen(QQ)\nsage: f=(x - 3)/((x +1)*(x-1))\nsage: f.partial_fraction_decomposition()\n(0, [-1/(x - 1), 2/(x + 1)])\nsage: x=var('x')\nsage: f=(x - 3)/((x +1)*(x-1))\nsage: f.partial_fraction()\n2/(x + 1) - 1/(x - 1)\n```\n\nAn added bonus would be if they gave similar output (currently one gives a list, the other gives an expression).\n\nIssue created by migration from https://trac.sagemath.org/ticket/4039\n\n",
    "created_at": "2008-09-02T15:41:20Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.2",
    "title": "choose one name for  partial fraction decompositions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4039",
    "user": "https://github.com/jasongrout"
}
```
Assignee: tbd

Two different ways to do partial fractions should have the same function name:

```
sage: x=polygen(QQ)
sage: f=(x - 3)/((x +1)*(x-1))
sage: f.partial_fraction_decomposition()
(0, [-1/(x - 1), 2/(x + 1)])
sage: x=var('x')
sage: f=(x - 3)/((x +1)*(x-1))
sage: f.partial_fraction()
2/(x + 1) - 1/(x - 1)
```

An added bonus would be if they gave similar output (currently one gives a list, the other gives an expression).

Issue created by migration from https://trac.sagemath.org/ticket/4039





---

archive/issue_comments_029077.json:
```json
{
    "body": "Note that there's no way to \"symbolically\" unevaluated sums of fraction field elements in Frac(QQ[x])",
    "created_at": "2010-09-18T23:38:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4039#issuecomment-29077",
    "user": "https://github.com/robertwb"
}
```

Note that there's no way to "symbolically" unevaluated sums of fraction field elements in Frac(QQ[x])



---

archive/issue_events_009227.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4039",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4039#event-9227"
}
```



---

archive/issue_events_009228.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4039",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4039#event-9228"
}
```



---

archive/issue_events_009229.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4039",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4039#event-9229"
}
```



---

archive/issue_events_009230.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4039",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4039#event-9230"
}
```



---

archive/issue_events_009231.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4039",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4039#event-9231"
}
```



---

archive/issue_events_009232.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4039",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4039#event-9232"
}
```



---

archive/issue_events_009233.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4039",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4039#event-9233"
}
```



---

archive/issue_comments_029078.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-06-25T18:45:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4039#issuecomment-29078",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_029079.json:
```json
{
    "body": "New commits:",
    "created_at": "2020-06-25T18:45:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4039#issuecomment-29079",
    "user": "https://github.com/fchapoton"
}
```

New commits:



---

archive/issue_events_009234.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-06-25T18:45:46Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4039",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4039#event-9234"
}
```



---

archive/issue_events_009235.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-06-25T18:45:46Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4039",
    "milestone": "sage-9.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4039#event-9235"
}
```



---

archive/issue_comments_029080.json:
```json
{
    "body": "Returning the result as a `FormalSum` could also be nice",
    "created_at": "2020-06-25T18:52:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4039#issuecomment-29080",
    "user": "https://github.com/mkoeppe"
}
```

Returning the result as a `FormalSum` could also be nice



---

archive/issue_comments_029081.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-07-09T01:31:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4039#issuecomment-29081",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_009236.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2020-07-10T19:34:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4039",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4039#event-9236"
}
```



---

archive/issue_comments_029082.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2020-07-10T19:34:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4039#issuecomment-29082",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
