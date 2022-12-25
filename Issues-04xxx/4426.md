# Issue 4426: Do not hard code RTLD_GLOBAL as 256 for libSingular

archive/issues_004426.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @malb\n\nWe currently hard code RTLD_GLOBAL as 256 when we dlopen libSingular. This is not true on AIX and Cygwin for example, so we should pull the value in from the system's dlfcn.h.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4426\n\n",
    "closed_at": "2008-11-02T19:25:33Z",
    "created_at": "2008-11-02T19:20:12Z",
    "labels": [
        "component: porting",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Do not hard code RTLD_GLOBAL as 256 for libSingular",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4426",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @malb

We currently hard code RTLD_GLOBAL as 256 when we dlopen libSingular. This is not true on AIX and Cygwin for example, so we should pull the value in from the system's dlfcn.h.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4426





---

archive/issue_events_010012.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-02T19:25:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4426",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4426#event-10012"
}
```



---

archive/issue_events_010013.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-02T19:25:33Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4426",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4426#event-10013"
}
```



---

archive/issue_comments_032478.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-11-02T19:25:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4426#issuecomment-32478",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: duplicate



---

archive/issue_comments_032479.json:
```json
{
    "body": "Ha, malb and I opened a ticket for the same issue, but since #4427 has a patch close this as a dupe.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-02T19:25:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4426#issuecomment-32479",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ha, malb and I opened a ticket for the same issue, but since #4427 has a patch close this as a dupe.

Cheers,

Michael
