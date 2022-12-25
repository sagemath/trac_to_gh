# Issue 6104: [with spkg, needs review] Fix Solaris specific build issue for libfplll.spkg

archive/issues_006104.json:
```json
{
    "body": "Assignee: mabshoff\n\ndpe.h was not including some headers for finite() and also due to system header differences there are template scope issues with NAN. The spkg at \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-4.0/rc0/libfplll-3.0.12.p0.spkg\n\nworks around that.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/6104\n\n",
    "created_at": "2009-05-21T04:26:44Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "[with spkg, needs review] Fix Solaris specific build issue for libfplll.spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6104",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

dpe.h was not including some headers for finite() and also due to system header differences there are template scope issues with NAN. The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-4.0/rc0/libfplll-3.0.12.p0.spkg

works around that.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/6104





---

archive/issue_comments_048668.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-21T04:27:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6104#issuecomment-48668",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_048669.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-28T06:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6104#issuecomment-48669",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_014356.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-05-28T06:49:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6104",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6104#event-14356"
}
```
