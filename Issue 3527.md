# Issue 3527: Build python with "-O2" instead of "-O3" on Itanium

archive/issues_003527.json:
```json
{
    "body": "Assignee: mabshoff\n\nWhen building Sage's pyhton and extensions with gcc 4.3 on Itanium we get some doctest failures that disappear with \"-O2\"\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3527\n\n",
    "created_at": "2008-06-28T09:32:34Z",
    "labels": [
        "component: build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "Build python with \"-O2\" instead of \"-O3\" on Itanium",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3527",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

When building Sage's pyhton and extensions with gcc 4.3 on Itanium we get some doctest failures that disappear with "-O2"

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3527





---

archive/issue_comments_024832.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-06-28T09:32:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3527#issuecomment-24832",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_024833.json:
```json
{
    "body": "This is starting to look invalid since all failures I see seem to be triggered by bugs not normally observed on non-Itanium, but valgrind finds faults in those cases on x86-64.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-07T22:28:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3527#issuecomment-24833",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is starting to look invalid since all failures I see seem to be triggered by bugs not normally observed on non-Itanium, but valgrind finds faults in those cases on x86-64.

Cheers,

Michael



---

archive/issue_events_003746.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-07-09T16:09:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3527",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3527#event-3746"
}
```



---

archive/issue_comments_024834.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-09T16:09:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3527#issuecomment-24834",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_024835.json:
```json
{
    "body": "positive review.",
    "created_at": "2008-07-09T16:09:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3527#issuecomment-24835",
    "user": "https://github.com/williamstein"
}
```

positive review.



---

archive/issue_comments_024836.json:
```json
{
    "body": "Merged in Sage 3.0.4.rc2",
    "created_at": "2008-07-09T16:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3527#issuecomment-24836",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.rc2
