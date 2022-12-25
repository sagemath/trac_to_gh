# Issue 2940: symbolic equation arithmetic is to restrictive

archive/issues_002940.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe following should all work \n\n\n```\nsage: var('x,y')\n(x, y)\nsage: (a < 1) + (b < 2)\nb + a < 3\nsage: (a < 1) + (b <= 2)\na + b < 3\nsage: (a <= 1) + (b == 2)\na + b <= 3\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2940\n\n",
    "created_at": "2008-04-16T09:07:51Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "symbolic equation arithmetic is to restrictive",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2940",
    "user": "https://github.com/robertwb"
}
```
Assignee: @williamstein

The following should all work 


```
sage: var('x,y')
(x, y)
sage: (a < 1) + (b < 2)
b + a < 3
sage: (a < 1) + (b <= 2)
a + b < 3
sage: (a <= 1) + (b == 2)
a + b <= 3
```


Issue created by migration from https://trac.sagemath.org/ticket/2940





---

archive/issue_events_006721.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-16T10:18:09Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2940",
    "milestone": "sage-3.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2940#event-6721"
}
```



---

archive/issue_comments_020210.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2940#issuecomment-20210",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_020211.json:
```json
{
    "body": "This can be closed as fixed. \n\nSupport for this was added by Robert during the symbolics push before 4.0. There are similar doctests to the ones in the description in sage/symbolic/expression.pyx lines 1526 and 6006.",
    "created_at": "2009-06-10T11:17:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2940#issuecomment-20211",
    "user": "https://github.com/burcin"
}
```

This can be closed as fixed. 

Support for this was added by Robert during the symbolics push before 4.0. There are similar doctests to the ones in the description in sage/symbolic/expression.pyx lines 1526 and 6006.



---

archive/issue_comments_020212.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-24T15:15:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2940#issuecomment-20212",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_006722.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2009-06-24T15:15:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2940",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2940#event-6722"
}
```



---

archive/issue_events_006723.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2009-06-24T15:16:37Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2940",
    "milestone": "sage-3.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2940#event-6723"
}
```



---

archive/issue_events_006724.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2009-06-24T15:16:37Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2940",
    "milestone": "sage-4.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2940#event-6724"
}
```
