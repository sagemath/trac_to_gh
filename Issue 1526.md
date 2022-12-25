# Issue 1526: conversion from gap matrix over finite field to sage matrix is VERY VERY VERY slow -- but robust.

archive/issues_001526.json:
```json
{
    "body": "Assignee: @williamstein\n\nE.g., in linear_code.py line 780 (in extended_code()), this line dominates:\n\n\n```\n        Gxs = Gx._matrix_(F)           # this is the killer\n```\n\n\nThat is dumb.  Optimize this a lot.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1526\n\n",
    "created_at": "2007-12-15T23:10:22Z",
    "labels": [
        "component: interfaces"
    ],
    "title": "conversion from gap matrix over finite field to sage matrix is VERY VERY VERY slow -- but robust.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1526",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

E.g., in linear_code.py line 780 (in extended_code()), this line dominates:


```
        Gxs = Gx._matrix_(F)           # this is the killer
```


That is dumb.  Optimize this a lot.

Issue created by migration from https://trac.sagemath.org/ticket/1526





---

archive/issue_events_003848.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:34:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1526",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1526#event-3848"
}
```



---

archive/issue_events_003849.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1526",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1526#event-3849"
}
```



---

archive/issue_events_003850.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1526",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1526#event-3850"
}
```



---

archive/issue_events_003851.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:19:32Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1526",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1526#event-3851"
}
```



---

archive/issue_events_003852.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:19:32Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1526",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1526#event-3852"
}
```



---

archive/issue_events_003853.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1526",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1526#event-3853"
}
```



---

archive/issue_events_003854.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1526",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1526#event-3854"
}
```



---

archive/issue_events_003855.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2019-01-15T18:01:47Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1526",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1526#event-3855"
}
```



---

archive/issue_events_003856.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2019-01-15T18:01:47Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1526",
    "milestone": "sage-8.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1526#event-3856"
}
```



---

archive/issue_comments_009738.json:
```json
{
    "body": "The exact code in question no longer exists in that module, though this issue might still be relevant, and would probably be resolved by #26902.\n\nIndeed, this is (unsurprisingly) much faster using the libgap interface.\n\nI wasn't sure exactly how to construct a matrix over a finite field in GAP, so I made it first in Sage, and the passed it to both GAP interfaces, and then back to Sage again:\n\n\n```\nsage: F = GF(2)\nsage: M = matrix(F, [[1,0,0],[1,1,0]])\nsage: M_gap = gap(M); M_gap\n[ [ Z(2)^0, 0*Z(2), 0*Z(2) ], [ Z(2)^0, Z(2)^0, 0*Z(2) ] ]\nsage: M_libgap = libgap(M); M_libgap\n[ [ Z(2)^0, 0*Z(2), 0*Z(2) ], [ Z(2)^0, Z(2)^0, 0*Z(2) ] ]\nsage: %timeit M_gap._matrix_(F)\n10 loops, best of 3: 22.3 ms per loop\nsage: %timeit M_libgap._matrix_(F)\n1000 loops, best of 3: 902 \u00b5s per loop\n```\n\n\nI think that about speaks for itself.  Repeated experiments showed similar results.",
    "created_at": "2019-01-15T18:01:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1526#issuecomment-9738",
    "user": "https://github.com/embray"
}
```

The exact code in question no longer exists in that module, though this issue might still be relevant, and would probably be resolved by #26902.

Indeed, this is (unsurprisingly) much faster using the libgap interface.

I wasn't sure exactly how to construct a matrix over a finite field in GAP, so I made it first in Sage, and the passed it to both GAP interfaces, and then back to Sage again:


```
sage: F = GF(2)
sage: M = matrix(F, [[1,0,0],[1,1,0]])
sage: M_gap = gap(M); M_gap
[ [ Z(2)^0, 0*Z(2), 0*Z(2) ], [ Z(2)^0, Z(2)^0, 0*Z(2) ] ]
sage: M_libgap = libgap(M); M_libgap
[ [ Z(2)^0, 0*Z(2), 0*Z(2) ], [ Z(2)^0, Z(2)^0, 0*Z(2) ] ]
sage: %timeit M_gap._matrix_(F)
10 loops, best of 3: 22.3 ms per loop
sage: %timeit M_libgap._matrix_(F)
1000 loops, best of 3: 902 µs per loop
```


I think that about speaks for itself.  Repeated experiments showed similar results.



---

archive/issue_events_003857.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2019-03-25T10:56:15Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1526",
    "milestone": "sage-8.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1526#event-3857"
}
```



---

archive/issue_events_003858.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2019-03-25T10:56:15Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1526",
    "milestone": "sage-8.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1526#event-3858"
}
```



---

archive/issue_comments_009739.json:
```json
{
    "body": "Ticket retargeted after milestone closed (if you don't believe this ticket is appropriate for the Sage 8.8 release please retarget manually)",
    "created_at": "2019-03-25T10:56:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1526#issuecomment-9739",
    "user": "https://github.com/embray"
}
```

Ticket retargeted after milestone closed (if you don't believe this ticket is appropriate for the Sage 8.8 release please retarget manually)



---

archive/issue_comments_009740.json:
```json
{
    "body": "As the Sage-8.8 release milestone is pending, we should delete the sage-8.8 milestone for tickets that are not actively being worked on or that still require significant work to move forward.  If you feel that this ticket should be included in the next Sage release at the soonest please set its milestone to the next release milestone (sage-8.9).",
    "created_at": "2019-06-14T14:54:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1526#issuecomment-9740",
    "user": "https://github.com/embray"
}
```

As the Sage-8.8 release milestone is pending, we should delete the sage-8.8 milestone for tickets that are not actively being worked on or that still require significant work to move forward.  If you feel that this ticket should be included in the next Sage release at the soonest please set its milestone to the next release milestone (sage-8.9).



---

archive/issue_events_003859.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2019-06-14T14:54:19Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1526",
    "milestone": "sage-8.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1526#event-3859"
}
```
