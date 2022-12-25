# Issue 2944: [with patch, needs review] add E2 parameter to padic_height_via_multiply

archive/issues_002944.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis patch adds an optional E2 parameter to `padic_height_via_multiply`. The idea is to make it possible to use a precomputed value of E2. Since the E2 computation is very expensive relative to the p-adic height computation, this makes it easier to do profiling work on the p-adic height portion of the computation.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2944\n\n",
    "created_at": "2008-04-16T22:32:27Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch, needs review] add E2 parameter to padic_height_via_multiply",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2944",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: @williamstein

This patch adds an optional E2 parameter to `padic_height_via_multiply`. The idea is to make it possible to use a precomputed value of E2. Since the E2 computation is very expensive relative to the p-adic height computation, this makes it easier to do profiling work on the p-adic height portion of the computation.


Issue created by migration from https://trac.sagemath.org/ticket/2944





---

archive/issue_comments_020262.json:
```json
{
    "body": "Attachment [height-E2.patch](tarball://root/attachments/some-uuid/ticket2944/height-E2.patch) by dmharvey created at 2008-04-16 22:32:44",
    "created_at": "2008-04-16T22:32:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2944#issuecomment-20262",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Attachment [height-E2.patch](tarball://root/attachments/some-uuid/ticket2944/height-E2.patch) by dmharvey created at 2008-04-16 22:32:44



---

archive/issue_comments_020263.json:
```json
{
    "body": "Fine by me.",
    "created_at": "2008-04-17T05:12:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2944#issuecomment-20263",
    "user": "https://github.com/ncalexan"
}
```

Fine by me.



---

archive/issue_events_006729.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-17T06:13:04Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2944",
    "milestone": "sage-3.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2944#event-6729"
}
```



---

archive/issue_events_006730.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-17T06:13:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2944",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2944#event-6730"
}
```



---

archive/issue_comments_020264.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-17T06:13:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2944#issuecomment-20264",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020265.json:
```json
{
    "body": "Merged in Sage 3.0.alpha6",
    "created_at": "2008-04-17T06:13:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2944#issuecomment-20265",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha6
