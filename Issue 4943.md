# Issue 4943: make sage -tp run sage -t when only one file is specified

archive/issues_004943.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: parallel doctest testing\n\nsage -tp is great, except it doesn't print synchronously when only one file is being tested.  It's irritating to wait for output when there are no race problems due to only a single parallel process.  Could we make sage -tp detect a single file and just run sage -t when that's the case?\n\nIssue created by migration from https://trac.sagemath.org/ticket/4943\n\n",
    "created_at": "2009-01-05T22:35:56Z",
    "labels": [
        "component: doctest coverage",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "make sage -tp run sage -t when only one file is specified",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4943",
    "user": "https://github.com/ncalexan"
}
```
Assignee: mabshoff

Keywords: parallel doctest testing

sage -tp is great, except it doesn't print synchronously when only one file is being tested.  It's irritating to wait for output when there are no race problems due to only a single parallel process.  Could we make sage -tp detect a single file and just run sage -t when that's the case?

Issue created by migration from https://trac.sagemath.org/ticket/4943





---

archive/issue_events_011410.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-06T01:08:29Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4943",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4943#event-11410"
}
```



---

archive/issue_events_011411.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-12T02:27:21Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4943",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4943#event-11411"
}
```



---

archive/issue_events_011412.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-12T02:27:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4943",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4943#event-11412"
}
```



---

archive/issue_comments_037453.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:25:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4943#issuecomment-37453",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_037454.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-03-14T20:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4943#issuecomment-37454",
    "user": "https://github.com/roed314"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_037455.json:
```json
{
    "body": "This is resolved by #12415.",
    "created_at": "2013-03-14T20:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4943#issuecomment-37455",
    "user": "https://github.com/roed314"
}
```

This is resolved by #12415.



---

archive/issue_events_011413.json:
```json
{
    "actor": "https://github.com/roed314",
    "created_at": "2013-03-14T20:38:00Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4943",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4943#event-11413"
}
```



---

archive/issue_events_011414.json:
```json
{
    "actor": "https://github.com/roed314",
    "created_at": "2013-03-14T20:38:00Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4943",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4943#event-11414"
}
```



---

archive/issue_comments_037456.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-03-14T20:38:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4943#issuecomment-37456",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_011415.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-03-15T13:01:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4943",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4943#event-11415"
}
```



---

archive/issue_comments_037457.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-03-15T13:01:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4943#issuecomment-37457",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
