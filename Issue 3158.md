# Issue 3158: singular-3-0-4-2-20080405.p1 requires flex

archive/issues_003158.json:
```json
{
    "body": "Assignee: mabshoff\n\nsingular-3-0-4-2-20080405.p1 requires flex to build. This is because libparse.l has the same time stamp as libparse.cc:\n\n```\n[mabshoff@eno Singular]$ ls -al libparse.*\n-rw-r----- 1 mabshoff sage 109970 2008-03-19 13:44 libparse.cc\n-rw-r----- 1 mabshoff sage   1524 2008-03-25 11:04 libparse.h\n-rw-r----- 1 mabshoff sage  31422 2008-03-19 13:44 libparse.l\n-rw-r----- 1 mabshoff sage     52 1998-04-20 06:05 libparse.sed\n```\nThe fix is to touch libparse.cc so that the time stamp is older. I did that in the spkg linked at #2983.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3158\n\n",
    "created_at": "2008-05-11T12:35:49Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "singular-3-0-4-2-20080405.p1 requires flex",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3158",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

singular-3-0-4-2-20080405.p1 requires flex to build. This is because libparse.l has the same time stamp as libparse.cc:

```
[mabshoff@eno Singular]$ ls -al libparse.*
-rw-r----- 1 mabshoff sage 109970 2008-03-19 13:44 libparse.cc
-rw-r----- 1 mabshoff sage   1524 2008-03-25 11:04 libparse.h
-rw-r----- 1 mabshoff sage  31422 2008-03-19 13:44 libparse.l
-rw-r----- 1 mabshoff sage     52 1998-04-20 06:05 libparse.sed
```
The fix is to touch libparse.cc so that the time stamp is older. I did that in the spkg linked at #2983.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3158





---

archive/issue_comments_021861.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-11T12:36:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3158#issuecomment-21861",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_021862.json:
```json
{
    "body": "The spkg is functional (see review at #2983) and the issue is now resolved for the person who reported it. Positive review.",
    "created_at": "2008-05-11T13:12:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3158#issuecomment-21862",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```

The spkg is functional (see review at #2983) and the issue is now resolved for the person who reported it. Positive review.



---

archive/issue_comments_021863.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha0",
    "created_at": "2008-05-11T13:13:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3158#issuecomment-21863",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.2.alpha0



---

archive/issue_comments_021864.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-11T13:13:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3158#issuecomment-21864",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_007136.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-11T13:13:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3158",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3158#event-7136"
}
```
