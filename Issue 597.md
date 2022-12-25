# Issue 597: Why are single-argument arithmetic functions in the coercion model?

archive/issues_000597.json:
```json
{
    "body": "Assignee: somebody\n\nIs there any advantage to having _neg_c/_neg_/_neg_c_imple as opposed to overriding __neg__? \n\nIssue created by migration from https://trac.sagemath.org/ticket/597\n\n",
    "closed_at": "2008-11-14T08:56:35Z",
    "created_at": "2007-09-06T00:52:14Z",
    "labels": [
        "component: basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Why are single-argument arithmetic functions in the coercion model?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/597",
    "user": "https://github.com/robertwb"
}
```
Assignee: somebody

Is there any advantage to having _neg_c/_neg_/_neg_c_imple as opposed to overriding __neg__? 

Issue created by migration from https://trac.sagemath.org/ticket/597





---

archive/issue_events_001591.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-03T12:18:45Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/597",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/597#event-1591"
}
```



---

archive/issue_comments_003072.json:
```json
{
    "body": "Now that cpdef methods are used, one can just implement `__neg__` and `__inverse__`, we don't need this infrastructure for unary operations (and it slows them down). \n\nWe should do a full search of the source.",
    "created_at": "2008-11-14T07:12:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/597#issuecomment-3072",
    "user": "https://github.com/robertwb"
}
```

Now that cpdef methods are used, one can just implement `__neg__` and `__inverse__`, we don't need this infrastructure for unary operations (and it slows them down). 

We should do a full search of the source.



---

archive/issue_comments_003073.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-11-14T08:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/597#issuecomment-3073",
    "user": "https://github.com/mwhansen"
}
```

Resolution: duplicate



---

archive/issue_events_001592.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2008-11-14T08:56:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/597",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/597#event-1592"
}
```



---

archive/issue_events_001593.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2008-11-14T08:56:35Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/597",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/597#event-1593"
}
```



---

archive/issue_events_001594.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2008-11-14T08:56:35Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/597",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/597#event-1594"
}
```



---

archive/issue_comments_003074.json:
```json
{
    "body": "This is a now duplicate of #2072, which is more recent.",
    "created_at": "2008-11-14T08:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/597#issuecomment-3074",
    "user": "https://github.com/mwhansen"
}
```

This is a now duplicate of #2072, which is more recent.
