# Issue 451: flintqs Solaris build fixes

archive/issues_000451.json:
```json
{
    "body": "Assignee: mabshoff\n\nflintqs-20070505 uses linux-ism for types. In lanzos.h add\n\n#ifdef __sun\n#define u_int32_t unsigned int\n#define u_int64_t unsigned long long\n#endif \n\nIssue created by migration from https://trac.sagemath.org/ticket/451\n\n",
    "created_at": "2007-08-19T07:55:51Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "flintqs Solaris build fixes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/451",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

flintqs-20070505 uses linux-ism for types. In lanzos.h add

#ifdef __sun
#define u_int32_t unsigned int
#define u_int64_t unsigned long long
#endif 

Issue created by migration from https://trac.sagemath.org/ticket/451





---

archive/issue_comments_002240.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-08-22T19:38:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/451#issuecomment-2240",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002241.json:
```json
{
    "body": "This has been fixed upstream by Bill some time before Sage 2.8.3\n\nCheers,\n\nMichael",
    "created_at": "2007-09-04T11:51:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/451#issuecomment-2241",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This has been fixed upstream by Bill some time before Sage 2.8.3

Cheers,

Michael



---

archive/issue_events_000478.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-09-04T11:51:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/451",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/451#event-478"
}
```



---

archive/issue_comments_002242.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-04T11:51:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/451#issuecomment-2242",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
