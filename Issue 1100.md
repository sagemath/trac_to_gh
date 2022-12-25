# Issue 1100: polynomial roots() method can return rational roots for polynomials over ZZ

archive/issues_001100.json:
```json
{
    "body": "Assignee: cwitty\n\nAccording to the documentation, .roots() is only supposed to return values from the base ring, so this is a bug:\n\n\n```\nsage: x = polygen(ZZ)\nsage: f = 2*x-3\nsage: f.roots()\n[(3/2, 1)]\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1100\n\n",
    "created_at": "2007-11-04T04:28:28Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.12",
    "title": "polynomial roots() method can return rational roots for polynomials over ZZ",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1100",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: cwitty

According to the documentation, .roots() is only supposed to return values from the base ring, so this is a bug:


```
sage: x = polygen(ZZ)
sage: f = 2*x-3
sage: f.roots()
[(3/2, 1)]
```



Issue created by migration from https://trac.sagemath.org/ticket/1100





---

archive/issue_comments_006639.json:
```json
{
    "body": "Attachment [1100.patch](tarball://root/attachments/some-uuid/ticket1100/1100.patch) by cwitty created at 2007-11-04 04:50:22",
    "created_at": "2007-11-04T04:50:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1100#issuecomment-6639",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [1100.patch](tarball://root/attachments/some-uuid/ticket1100/1100.patch) by cwitty created at 2007-11-04 04:50:22



---

archive/issue_comments_006640.json:
```json
{
    "body": "This patch was developed after #995, and may not apply cleanly if the patch from #995 has not yet been applied.",
    "created_at": "2007-11-04T04:52:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1100#issuecomment-6640",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

This patch was developed after #995, and may not apply cleanly if the patch from #995 has not yet been applied.



---

archive/issue_comments_006641.json:
```json
{
    "body": "applied to 2.8.12.rc0",
    "created_at": "2007-11-06T21:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1100#issuecomment-6641",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

applied to 2.8.12.rc0



---

archive/issue_events_001226.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-06T21:46:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1100",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1100#event-1226"
}
```



---

archive/issue_comments_006642.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-06T21:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1100#issuecomment-6642",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
