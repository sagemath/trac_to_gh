# Issue 5164: NTL.spkg: Set SHAREDFALGS to -fnocommon on Darwin

archive/issues_005164.json:
```json
{
    "body": "Assignee: mabshoff\n\nIn #5161 I removed some global SHAREDFLAGS setting from sage-env. NTL on Darwin needs -fnocommon to work around some linker stupidity.\n\nspkg coming up.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5164\n\n",
    "created_at": "2009-02-03T05:00:34Z",
    "labels": [
        "component: porting",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "NTL.spkg: Set SHAREDFALGS to -fnocommon on Darwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5164",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

In #5161 I removed some global SHAREDFLAGS setting from sage-env. NTL on Darwin needs -fnocommon to work around some linker stupidity.

spkg coming up.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5164





---

archive/issue_comments_039498.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-03T05:00:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5164#issuecomment-39498",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_039499.json:
```json
{
    "body": "The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha5/ntl-5.4.2.p6.spkg\n\nfixes the problem.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-03T18:04:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5164#issuecomment-39499",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha5/ntl-5.4.2.p6.spkg

fixes the problem.

Cheers,

Michael



---

archive/issue_comments_039500.json:
```json
{
    "body": "No issues with building on other OSes Fedora 9, Fedora 10 and Ubuntu 8.10, 32 bits\n\nJaap",
    "created_at": "2009-02-03T19:51:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5164#issuecomment-39500",
    "user": "https://github.com/jaapspies"
}
```

No issues with building on other OSes Fedora 9, Fedora 10 and Ubuntu 8.10, 32 bits

Jaap



---

archive/issue_comments_039501.json:
```json
{
    "body": "Merged in Sage 3.3.alpha5.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-03T19:55:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5164#issuecomment-39501",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha5.

Cheers,

Michael



---

archive/issue_comments_039502.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-03T19:55:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5164#issuecomment-39502",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005414.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-03T19:55:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5164",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5164#event-5414"
}
```
