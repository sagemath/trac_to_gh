# Issue 29: implement len for elliptic curve over finite field

archive/issues_000029.json:
```json
{
    "body": "Assignee: somebody\n\n```\nsage: E=EllipticCurve(GF(37),range(5))\n   sage: len(E)\n   Traceback (most recent call last):\n   ...\n   TypeError: len() of unsized object\n```\n\n(also should have trace of frob, charpoly, ap, etc.)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/29\n\n",
    "created_at": "2006-09-12T23:26:11Z",
    "labels": [
        "component: basic arithmetic",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "implement len for elliptic curve over finite field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/29",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

```
sage: E=EllipticCurve(GF(37),range(5))
   sage: len(E)
   Traceback (most recent call last):
   ...
   TypeError: len() of unsized object
```

(also should have trace of frob, charpoly, ap, etc.)


Issue created by migration from https://trac.sagemath.org/ticket/29





---

archive/issue_comments_000201.json:
```json
{
    "body": "Slight problem is that `__len__()` has to return a python int. Even a long is unacceptable. So this will only work if the curve is not too large, otherwise it will necessarily throw a `TypeError`.",
    "created_at": "2006-10-27T02:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/29",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/29#issuecomment-201",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Slight problem is that `__len__()` has to return a python int. Even a long is unacceptable. So this will only work if the curve is not too large, otherwise it will necessarily throw a `TypeError`.



---

archive/issue_comments_000202.json:
```json
{
    "body": "Changing assignee from somebody to dmharvey.",
    "created_at": "2006-10-27T02:51:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/29",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/29#issuecomment-202",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Changing assignee from somebody to dmharvey.



---

archive/issue_events_000053.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-09-11T02:17:33Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/29",
    "milestone": "sage-feature",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/29#event-53"
}
```



---

archive/issue_comments_000203.json:
```json
{
    "body": "Changing component from basic arithmetic to algebraic geometry.",
    "created_at": "2008-01-27T05:08:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/29",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/29#issuecomment-203",
    "user": "https://github.com/aghitza"
}
```

Changing component from basic arithmetic to algebraic geometry.



---

archive/issue_comments_000204.json:
```json
{
    "body": "This is essentially completed by #1130.\n\nI think asking for len(E) is not right, in any case -- len(E.points()) makes some sense, and #1130 makes that work.",
    "created_at": "2008-02-16T21:42:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/29",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/29#issuecomment-204",
    "user": "https://github.com/ncalexan"
}
```

This is essentially completed by #1130.

I think asking for len(E) is not right, in any case -- len(E.points()) makes some sense, and #1130 makes that work.



---

archive/issue_events_000054.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-16T21:50:29Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/29",
    "milestone": "sage-feature",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/29#event-54"
}
```



---

archive/issue_events_000055.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-16T21:50:29Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/29",
    "milestone": "sage-2.10.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/29#event-55"
}
```



---

archive/issue_comments_000205.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-16T21:50:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/29",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/29#issuecomment-205",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_000206.json:
```json
{
    "body": "Closed as fixed since I just merged #1130.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-16T21:50:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/29",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/29#issuecomment-206",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Closed as fixed since I just merged #1130.

Cheers,

Michael



---

archive/issue_events_000056.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-16T21:50:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/29",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/29#event-56"
}
```
