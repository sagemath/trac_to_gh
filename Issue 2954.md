# Issue 2954: [with spkg. needs review] ATLAS 3.8.1: Fix Itanium 2 detection on Itanium/gcc compiler flags on RHEL5/Itanium

archive/issues_002954.json:
```json
{
    "body": "Assignee: mabshoff\n\nItanium 2 on RHEL 5 and pretty much any other modern kernel is not properly detected. ATLAS also uses the -m64 flags which is not available on RHEL 5 on Itanium. The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/alpha6/atlas-3.8.1.p0.spkg\n\nfixes both issues.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2954\n\n",
    "created_at": "2008-04-19T04:00:01Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with spkg. needs review] ATLAS 3.8.1: Fix Itanium 2 detection on Itanium/gcc compiler flags on RHEL5/Itanium",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2954",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Itanium 2 on RHEL 5 and pretty much any other modern kernel is not properly detected. ATLAS also uses the -m64 flags which is not available on RHEL 5 on Itanium. The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/alpha6/atlas-3.8.1.p0.spkg

fixes both issues.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/2954





---

archive/issue_comments_020327.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-19T04:00:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2954#issuecomment-20327",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020328.json:
```json
{
    "body": "REPORT:\n\n Well I give #2954 a positive review if it builds and works for you.\nI've read the patches.",
    "created_at": "2008-04-19T05:31:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2954#issuecomment-20328",
    "user": "https://github.com/williamstein"
}
```

REPORT:

 Well I give #2954 a positive review if it builds and works for you.
I've read the patches.



---

archive/issue_comments_020329.json:
```json
{
    "body": "Build time on Itanium is quite bad, especially compared to x86-64, but I guess that it is partially the fault of gcc 4.1.1 I used.\n\nOh well,\n\nMichael",
    "created_at": "2008-04-19T06:52:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2954#issuecomment-20329",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Build time on Itanium is quite bad, especially compared to x86-64, but I guess that it is partially the fault of gcc 4.1.1 I used.

Oh well,

Michael



---

archive/issue_events_006752.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-19T06:52:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2954",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2954#event-6752"
}
```



---

archive/issue_comments_020330.json:
```json
{
    "body": "Merged in Sage 3.0.alpha6",
    "created_at": "2008-04-19T06:52:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2954#issuecomment-20330",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha6



---

archive/issue_comments_020331.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-19T06:52:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2954#issuecomment-20331",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
