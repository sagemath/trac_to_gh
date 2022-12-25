# Issue 3527: [with spkg, positive review] Disable "-fwrapv" on Itanium when building python

archive/issues_003527.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe spkg at \n\nhttp://sage.math.washington.edu/home/mabshoff/python-2.5.2.p3.spkg\n\ndisables \"-fwrapv\" on Itanium and OSX. This fixes a number of doctest failures on at least Itanium. \"-fwrapv\" enables some seemingly sketchy floating point optimizations that are not part of \"-O3\", so good riddance for them.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3527\n\n",
    "closed_at": "2008-07-09T16:09:25Z",
    "created_at": "2008-06-28T09:32:34Z",
    "labels": [
        "component: build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with spkg, positive review] Disable \"-fwrapv\" on Itanium when building python",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3527",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

The spkg at 

http://sage.math.washington.edu/home/mabshoff/python-2.5.2.p3.spkg

disables "-fwrapv" on Itanium and OSX. This fixes a number of doctest failures on at least Itanium. "-fwrapv" enables some seemingly sketchy floating point optimizations that are not part of "-O3", so good riddance for them.

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

archive/issue_events_008056.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-07T22:28:50Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3527",
    "milestone": "sage-3.0.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3527#event-8056"
}
```



---

archive/issue_events_008057.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-07-09T16:09:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3527",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3527#event-8057"
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



---

archive/issue_events_008058.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-09T16:18:11Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3527",
    "milestone": "sage-3.0.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3527#event-8058"
}
```



---

archive/issue_events_008059.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-09T16:18:11Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3527",
    "milestone": "sage-3.0.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3527#event-8059"
}
```
