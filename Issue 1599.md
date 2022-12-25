# Issue 1599: another preparser edge case

archive/issues_001599.json:
```json
{
    "body": "Assignee: cwitty\n\n```\nsage: 3.xgcd(0)\n(3, 1, 0)\nsage: 3._xgcd(0)\n------------------------------------------------------------\n   File \"<ipython console>\", line 1\n     RealNumber('3.')_xgcd(Integer(0))\n                         ^\n<type 'exceptions.SyntaxError'>: invalid syntax\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1599\n\n",
    "created_at": "2007-12-26T15:21:56Z",
    "labels": [
        "component: misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "another preparser edge case",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1599",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: cwitty

```
sage: 3.xgcd(0)
(3, 1, 0)
sage: 3._xgcd(0)
------------------------------------------------------------
   File "<ipython console>", line 1
     RealNumber('3.')_xgcd(Integer(0))
                         ^
<type 'exceptions.SyntaxError'>: invalid syntax
```


Issue created by migration from https://trac.sagemath.org/ticket/1599





---

archive/issue_events_003976.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-27T04:07:16Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1599",
    "milestone": "sage-2.9.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1599#event-3976"
}
```



---

archive/issue_comments_010141.json:
```json
{
    "body": "Rolled into #5079",
    "created_at": "2009-01-23T22:30:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1599#issuecomment-10141",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Rolled into #5079



---

archive/issue_events_003977.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/boothby",
    "created_at": "2009-01-23T22:30:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1599",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1599#event-3977"
}
```



---

archive/issue_comments_010142.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-01-23T22:30:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1599#issuecomment-10142",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Resolution: duplicate



---

archive/issue_events_003978.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T15:32:55Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1599",
    "milestone": "sage-2.9.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1599#event-3978"
}
```



---

archive/issue_events_003979.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T15:32:55Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1599",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1599#event-3979"
}
```
