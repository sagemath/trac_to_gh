# Issue 30: left multiplication of scalar times vector

archive/issues_000030.json:
```json
{
    "body": "Assignee: somebody\n\nthere is currently no easy way for people to implement \n    vectors with left multiplication.  In fact, left multiplication\n    doesn't even work right now. \n\nIssue created by migration from https://trac.sagemath.org/ticket/30\n\n",
    "created_at": "2006-09-12T23:26:40Z",
    "labels": [
        "component: basic arithmetic",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.3",
    "title": "left multiplication of scalar times vector",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/30",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

there is currently no easy way for people to implement 
    vectors with left multiplication.  In fact, left multiplication
    doesn't even work right now. 

Issue created by migration from https://trac.sagemath.org/ticket/30





---

archive/issue_comments_000207.json:
```json
{
    "body": "This seems to work for me:\n\n```\nsage: v = vector([1,2,3])\nsage: v*2\n(2, 4, 6)\nsage: 2*v\n(2, 4, 6)\n```\n\nSo, should we close this as \"worksforme\" or did I misunderstand?\n\nCheers,\n\nMichael",
    "created_at": "2007-08-24T13:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/30",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/30#issuecomment-207",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This seems to work for me:

```
sage: v = vector([1,2,3])
sage: v*2
(2, 4, 6)
sage: 2*v
(2, 4, 6)
```

So, should we close this as "worksforme" or did I misunderstand?

Cheers,

Michael



---

archive/issue_events_000029.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-30T00:00:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/30",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/30#event-29"
}
```



---

archive/issue_comments_000208.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-30T00:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/30",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/30#issuecomment-208",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
