# Issue 979: printing error with small reals

archive/issues_000979.json:
```json
{
    "body": "Assignee: @mwhansen\n\n```\nsage: a = .00000000000000000000001;a\n0.000000000000000000000010000000000000000000000\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/979\n\n",
    "created_at": "2007-10-24T03:49:28Z",
    "labels": [
        "component: basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "printing error with small reals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/979",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @mwhansen

```
sage: a = .00000000000000000000001;a
0.000000000000000000000010000000000000000000000
```

Issue created by migration from https://trac.sagemath.org/ticket/979





---

archive/issue_comments_005951.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-24T05:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/979#issuecomment-5951",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005952.json:
```json
{
    "body": "Patch for this will be in the big patch for #962.",
    "created_at": "2007-10-24T05:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/979#issuecomment-5952",
    "user": "https://github.com/mwhansen"
}
```

Patch for this will be in the big patch for #962.



---

archive/issue_events_002706.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2007-10-24T20:18:48Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/979",
    "milestone": "sage-2.8.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/979#event-2706"
}
```



---

archive/issue_events_002707.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2007-10-28T19:01:18Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/979",
    "milestone": "sage-2.8.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/979#event-2707"
}
```



---

archive/issue_events_002708.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2007-10-28T19:01:18Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/979",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/979#event-2708"
}
```



---

archive/issue_comments_005953.json:
```json
{
    "body": "I believe this has already been taken care of.\n\nIn 2.8.15, we have\n\n```\nsage: a = .00000000000000000000001;a\n1.00000000000000e-23\n```",
    "created_at": "2007-12-06T21:21:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/979#issuecomment-5953",
    "user": "https://github.com/mwhansen"
}
```

I believe this has already been taken care of.

In 2.8.15, we have

```
sage: a = .00000000000000000000001;a
1.00000000000000e-23
```



---

archive/issue_events_002709.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2007-12-06T21:21:50Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/979",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/979#event-2709"
}
```



---

archive/issue_events_002710.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2007-12-06T21:21:50Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/979",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/979#event-2710"
}
```



---

archive/issue_comments_005954.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-06T21:32:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/979#issuecomment-5954",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002711.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-06T21:32:57Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/979",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/979#event-2711"
}
```



---

archive/issue_events_002712.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-06T21:32:57Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/979",
    "milestone": "sage-2.8.15",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/979#event-2712"
}
```



---

archive/issue_comments_005955.json:
```json
{
    "body": "Merged in 2.8.15.",
    "created_at": "2007-12-06T21:32:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/979#issuecomment-5955",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.15.



---

archive/issue_events_002713.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-06T21:32:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/979",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/979#event-2713"
}
```
