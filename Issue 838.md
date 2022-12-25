# Issue 838: doctest runner should share SAGE initialization using fork()

archive/issues_000838.json:
```json
{
    "body": "Assignee: failure\n\nCC:  @garyfurnish\n\nOn my machine, every file that gets doctested takes 0.8s for initializing SAGE (before it even gets to running the tests).  It would be nice if this overhead could be eliminated somehow; and I think it might be possible, by having a single process do the SAGE initialization, then fork() before doctesting a particular file.  (This sort of architecture might also make it easier to implement #639.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/838\n\n",
    "created_at": "2007-10-07T17:03:12Z",
    "labels": [
        "component: doctest coverage"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "doctest runner should share SAGE initialization using fork()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/838",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: failure

CC:  @garyfurnish

On my machine, every file that gets doctested takes 0.8s for initializing SAGE (before it even gets to running the tests).  It would be nice if this overhead could be eliminated somehow; and I think it might be possible, by having a single process do the SAGE initialization, then fork() before doctesting a particular file.  (This sort of architecture might also make it easier to implement #639.)

Issue created by migration from https://trac.sagemath.org/ticket/838





---

archive/issue_comments_005161.json:
```json
{
    "body": "This is not a dupe of #4699, but seems closely related since -tp 1 would basically work that way.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-05T04:51:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/838#issuecomment-5161",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is not a dupe of #4699, but seems closely related since -tp 1 would basically work that way.

Cheers,

Michael



---

archive/issue_comments_005162.json:
```json
{
    "body": "This will be resolved by #12415.",
    "created_at": "2012-02-06T03:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/838#issuecomment-5162",
    "user": "https://github.com/roed314"
}
```

This will be resolved by #12415.



---

archive/issue_events_000951.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2013-02-08T13:55:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/838",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/838#event-951"
}
```



---

archive/issue_comments_005163.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-02-08T13:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/838#issuecomment-5163",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
