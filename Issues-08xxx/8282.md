# Issue 8282: implement victor_miller_basis over an arbitrary base ring

archive/issues_008282.json:
```json
{
    "body": "Assignee: @craigcitro\n\nThis can now be done as:\n\n```\nsage: time bas = victor_miller_basis(2000, prec=200)\nCPU times: user 8.44 s, sys: 0.08 s, total: 8.52 s\nWall time: 8.55 s\nsage: time bas_mod7 = [ f.change_ring(GF(7)) for f in bas ]\nCPU times: user 2.52 s, sys: 0.00 s, total: 2.52 s\nWall time: 2.61 s\n```\n\nIt would be nice (and presumably much faster and less memory-consuming) to compute the Victor Miller basis *directly over GF(7)*.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8282\n\n",
    "created_at": "2010-02-16T13:11:56Z",
    "labels": [
        "component: modular forms",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "implement victor_miller_basis over an arbitrary base ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8282",
    "user": "https://github.com/aghitza"
}
```
Assignee: @craigcitro

This can now be done as:

```
sage: time bas = victor_miller_basis(2000, prec=200)
CPU times: user 8.44 s, sys: 0.08 s, total: 8.52 s
Wall time: 8.55 s
sage: time bas_mod7 = [ f.change_ring(GF(7)) for f in bas ]
CPU times: user 2.52 s, sys: 0.00 s, total: 2.52 s
Wall time: 2.61 s
```

It would be nice (and presumably much faster and less memory-consuming) to compute the Victor Miller basis *directly over GF(7)*.


Issue created by migration from https://trac.sagemath.org/ticket/8282





---

archive/issue_events_019815.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8282",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8282#event-19815"
}
```



---

archive/issue_events_019816.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8282",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8282#event-19816"
}
```



---

archive/issue_events_019817.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8282",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8282#event-19817"
}
```



---

archive/issue_events_019818.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8282",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8282#event-19818"
}
```



---

archive/issue_events_019819.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8282",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8282#event-19819"
}
```



---

archive/issue_events_019820.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8282",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8282#event-19820"
}
```



---

archive/issue_events_019821.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8282",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8282#event-19821"
}
```
