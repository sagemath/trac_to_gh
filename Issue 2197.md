# Issue 2197: Elliptic Curve quadratic/quartic/sextic twists: unhelpful error message when D=0

archive/issues_002197.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe code for quadratic, quartic and sextic twists of elliptic curves does not check that the twisting parameter is nonzero, and hence fail when a singular curve tries to be constructed.  Instead we output a helpful message.\n\nNote that in characteristic 2, the quadratic twist by 0 is allowed (but gives back the same curve), just as twisting by 1 in odd characteristic.\n\nThe patch provided also enhances the Hasse_bounds function (which should probably be put somewhere other than ell_generic.py).\n\nIssue created by migration from https://trac.sagemath.org/ticket/2197\n\n",
    "created_at": "2008-02-17T19:10:18Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Elliptic Curve quadratic/quartic/sextic twists: unhelpful error message when D=0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2197",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @williamstein

The code for quadratic, quartic and sextic twists of elliptic curves does not check that the twisting parameter is nonzero, and hence fail when a singular curve tries to be constructed.  Instead we output a helpful message.

Note that in characteristic 2, the quadratic twist by 0 is allowed (but gives back the same curve), just as twisting by 1 in odd characteristic.

The patch provided also enhances the Hasse_bounds function (which should probably be put somewhere other than ell_generic.py).

Issue created by migration from https://trac.sagemath.org/ticket/2197





---

archive/issue_events_005247.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-17T19:45:24Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2197",
    "milestone": "sage-2.10.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2197#event-5247"
}
```



---

archive/issue_comments_014403.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-02-17T21:16:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2197#issuecomment-14403",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: duplicate



---

archive/issue_events_005248.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-17T21:16:23Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2197",
    "milestone": "sage-2.10.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2197#event-5248"
}
```



---

archive/issue_events_005249.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-17T21:16:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2197",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2197#event-5249"
}
```



---

archive/issue_comments_014404.json:
```json
{
    "body": "This is a duplicate of #2196.",
    "created_at": "2008-02-17T21:16:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2197#issuecomment-14404",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is a duplicate of #2196.
