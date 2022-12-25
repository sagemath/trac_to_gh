# Issue 472: Drop dependencies on flex and bison

archive/issues_000472.json:
```json
{
    "body": "Assignee: @jmbr\n\nTo build Singular we need flex and bison but we could make sure those programs are not needed by using some spkg-install trickery.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/472\n\n",
    "closed_at": "2007-08-29T21:13:57Z",
    "created_at": "2007-08-20T23:13:13Z",
    "labels": [
        "component: packages: standard",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.3",
    "title": "Drop dependencies on flex and bison",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/472",
    "user": "https://github.com/jmbr"
}
```
Assignee: @jmbr

To build Singular we need flex and bison but we could make sure those programs are not needed by using some spkg-install trickery.


Issue created by migration from https://trac.sagemath.org/ticket/472





---

archive/issue_events_001188.json:
```json
{
    "actor": "https://github.com/jmbr",
    "created_at": "2007-08-23T00:04:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/472",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/472#event-1188"
}
```



---

archive/issue_comments_002349.json:
```json
{
    "body": "Replying to [ticket:472 jmbr]:\n> To build Singular we need flex and bison but we could make sure those programs are not needed by using some spkg-install trickery.\n\n\nMake will invoke flex and bison if the *.[ly] files are newer than the C++ files they generate.  Thus, we have to make sure the C++ files are fresher.",
    "created_at": "2007-08-23T00:04:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/472#issuecomment-2349",
    "user": "https://github.com/jmbr"
}
```

Replying to [ticket:472 jmbr]:
> To build Singular we need flex and bison but we could make sure those programs are not needed by using some spkg-install trickery.


Make will invoke flex and bison if the *.[ly] files are newer than the C++ files they generate.  Thus, we have to make sure the C++ files are fresher.



---

archive/issue_comments_002350.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2007-08-23T00:04:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/472#issuecomment-2350",
    "user": "https://github.com/jmbr"
}
```

Resolution: worksforme



---

archive/issue_comments_002351.json:
```json
{
    "body": "This is not closed, since there isn't a singular spkg yet that implements it.",
    "created_at": "2007-08-29T03:43:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/472#issuecomment-2351",
    "user": "https://github.com/williamstein"
}
```

This is not closed, since there isn't a singular spkg yet that implements it.



---

archive/issue_comments_002352.json:
```json
{
    "body": "Resolution changed from worksforme to ",
    "created_at": "2007-08-29T03:43:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/472#issuecomment-2352",
    "user": "https://github.com/williamstein"
}
```

Resolution changed from worksforme to 



---

archive/issue_comments_002353.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-08-29T03:43:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/472#issuecomment-2353",
    "user": "https://github.com/williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_events_001189.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-29T03:43:24Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/472",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/472#event-1189"
}
```



---

archive/issue_events_001190.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-29T03:43:30Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/472",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/472#event-1190"
}
```



---

archive/issue_comments_002354.json:
```json
{
    "body": "If malb's new singular.spkg goes in this is resolved.\n\nCheers,\n\nMichael",
    "created_at": "2007-08-29T21:08:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/472#issuecomment-2354",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

If malb's new singular.spkg goes in this is resolved.

Cheers,

Michael



---

archive/issue_events_001191.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-08-29T21:08:25Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/472",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/472#event-1191"
}
```



---

archive/issue_events_001192.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-08-29T21:08:25Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/472",
    "milestone": "sage-2.8.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/472#event-1192"
}
```



---

archive/issue_comments_002355.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-29T21:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/472#issuecomment-2355",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_001193.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-29T21:13:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/472",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/472#event-1193"
}
```
