# Issue 2515: ExtendedRationalField not so extended

archive/issues_002515.json:
```json
{
    "body": "Assignee: joyner\n\n\n```\nExtendedRationalField(1)/ExtendedRationalField(0)\n```\n\nyields\n\n```\nZeroDivisionError: Rational division by zero\n```\n\nSame for ExtendedIntegerRing(1)/ExtendedIntegerRing(0)\n\nPresumably these should both yield +Infinity?\n\nIssue created by migration from https://trac.sagemath.org/ticket/2515\n\n",
    "created_at": "2008-03-14T08:10:23Z",
    "labels": [
        "component: group_theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "ExtendedRationalField not so extended",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2515",
    "user": "https://trac.sagemath.org/admin/accounts/users/edrex"
}
```
Assignee: joyner


```
ExtendedRationalField(1)/ExtendedRationalField(0)
```

yields

```
ZeroDivisionError: Rational division by zero
```

Same for ExtendedIntegerRing(1)/ExtendedIntegerRing(0)

Presumably these should both yield +Infinity?

Issue created by migration from https://trac.sagemath.org/ticket/2515





---

archive/issue_comments_017045.json:
```json
{
    "body": "Changing assignee from joyner to cwitty.",
    "created_at": "2008-03-14T10:48:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2515#issuecomment-17045",
    "user": "https://github.com/burcin"
}
```

Changing assignee from joyner to cwitty.



---

archive/issue_comments_017046.json:
```json
{
    "body": "The way Sage handles infinity should be revised in general. I say `ExtendedRationalRing` (and `ExtendedIntegerRing`) should go away altogether, since the signed and unsigned infinity rings in `sage/rings/infinity.py` handle the situations when infinity is encountered adequately, at least after #1915 is fixed.",
    "created_at": "2008-03-14T10:48:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2515#issuecomment-17046",
    "user": "https://github.com/burcin"
}
```

The way Sage handles infinity should be revised in general. I say `ExtendedRationalRing` (and `ExtendedIntegerRing`) should go away altogether, since the signed and unsigned infinity rings in `sage/rings/infinity.py` handle the situations when infinity is encountered adequately, at least after #1915 is fixed.



---

archive/issue_comments_017047.json:
```json
{
    "body": "Changing component from group_theory to misc.",
    "created_at": "2008-03-14T10:48:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2515#issuecomment-17047",
    "user": "https://github.com/burcin"
}
```

Changing component from group_theory to misc.



---

archive/issue_comments_017048.json:
```json
{
    "body": "This ticket should be closed once #5735 is merged since the functionality will be removed from Sage - for details see that ticket.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-10T21:00:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2515#issuecomment-17048",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This ticket should be closed once #5735 is merged since the functionality will be removed from Sage - for details see that ticket.

Cheers,

Michael



---

archive/issue_comments_017049.json:
```json
{
    "body": "Fixed in Sage 3.4.1.rc3 via #5735.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T04:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2515#issuecomment-17049",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed in Sage 3.4.1.rc3 via #5735.

Cheers,

Michael



---

archive/issue_comments_017050.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-13T04:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2515#issuecomment-17050",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002696.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-13T04:10:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2515",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2515#event-2696"
}
```
