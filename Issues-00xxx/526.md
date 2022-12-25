# Issue 526: [easy?] better support for parallel make

archive/issues_000526.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  dmharvey@math.harvard.edu\n\nKeywords: package audit\n\na.k.a. `make -j`\n\nSee discussion at\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/a88d59dc35404507\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/526\n\n",
    "closed_at": "2008-09-26T09:18:33Z",
    "created_at": "2007-08-30T04:30:52Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "[easy?] better support for parallel make",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/526",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: mabshoff

CC:  dmharvey@math.harvard.edu

Keywords: package audit

a.k.a. `make -j`

See discussion at

http://groups.google.com/group/sage-devel/browse_thread/thread/a88d59dc35404507


Issue created by migration from https://trac.sagemath.org/ticket/526





---

archive/issue_events_001350.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-09-11T00:42:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/526",
    "milestone": "sage-feature",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/526#event-1350"
}
```



---

archive/issue_comments_002660.json:
```json
{
    "body": "Changing keywords from \"\" to \"package audit\".",
    "created_at": "2007-11-20T14:09:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/526#issuecomment-2660",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing keywords from "" to "package audit".



---

archive/issue_comments_002661.json:
```json
{
    "body": "The issue has been solved and needs to be properly documented. If you do\n\n```\nexport MAKE=\"make -j4\"\nmake\n```\nSage will be build with up to 4 jobs in parallel. Spkgs like Singular which do not build properly with parallel make make sure that MAKE is reset while building themselves.\n\nSo somebody send us a patch for the manual. We also need to audit all packages and change make to $MAKE.\n\nCheers,\n\nMichaek",
    "created_at": "2007-11-20T14:09:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/526#issuecomment-2661",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The issue has been solved and needs to be properly documented. If you do

```
export MAKE="make -j4"
make
```
Sage will be build with up to 4 jobs in parallel. Spkgs like Singular which do not build properly with parallel make make sure that MAKE is reset while building themselves.

So somebody send us a patch for the manual. We also need to audit all packages and change make to $MAKE.

Cheers,

Michaek



---

archive/issue_events_001351.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-20T14:09:14Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/526",
    "milestone": "sage-feature",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/526#event-1351"
}
```



---

archive/issue_events_001352.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-20T14:09:14Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/526",
    "milestone": "sage-2.8.13",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/526#event-1352"
}
```



---

archive/issue_comments_002662.json:
```json
{
    "body": "Changing assignee from @williamstein to @garyfurnish.",
    "created_at": "2008-03-09T05:15:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/526#issuecomment-2662",
    "user": "https://github.com/garyfurnish"
}
```

Changing assignee from @williamstein to @garyfurnish.



---

archive/issue_comments_002663.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-09T05:15:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/526#issuecomment-2663",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002664.json:
```json
{
    "body": "Changing assignee from @garyfurnish to mabshoff.",
    "created_at": "2008-09-26T09:18:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/526#issuecomment-2664",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @garyfurnish to mabshoff.



---

archive/issue_comments_002665.json:
```json
{
    "body": "This has been fixed. Every spkg that can be build in parallel does get build that way.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-26T09:18:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/526#issuecomment-2665",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This has been fixed. Every spkg that can be build in parallel does get build that way.

Cheers,

Michael



---

archive/issue_comments_002666.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2008-09-26T09:18:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/526#issuecomment-2666",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from assigned to new.



---

archive/issue_comments_002667.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-26T09:18:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/526#issuecomment-2667",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001353.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-26T09:18:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/526",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/526#event-1353"
}
```
