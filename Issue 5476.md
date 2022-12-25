# Issue 5476: dimension of jacobian of curves broken

archive/issues_005476.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: k.<a> = GF(9); R.<x> = k[]\nsage: HyperellipticCurve(x^3 + x - 1, x+a).jacobian().dimension()\nboom!\n```\n\n\nThis was found during Alex G.'s talk at Sage Days 14.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5476\n\n",
    "created_at": "2009-03-10T22:02:08Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "dimension of jacobian of curves broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5476",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
sage: k.<a> = GF(9); R.<x> = k[]
sage: HyperellipticCurve(x^3 + x - 1, x+a).jacobian().dimension()
boom!
```


This was found during Alex G.'s talk at Sage Days 14.

Issue created by migration from https://trac.sagemath.org/ticket/5476





---

archive/issue_comments_042394.json:
```json
{
    "body": "Attachment [trac_5476.patch](tarball://root/attachments/some-uuid/ticket5476/trac_5476.patch) by @williamstein created at 2009-03-10 22:03:24",
    "created_at": "2009-03-10T22:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5476#issuecomment-42394",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5476.patch](tarball://root/attachments/some-uuid/ticket5476/trac_5476.patch) by @williamstein created at 2009-03-10 22:03:24



---

archive/issue_comments_042395.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-03-11T03:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5476#issuecomment-42395",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_042396.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-11T03:45:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5476#issuecomment-42396",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_042397.json:
```json
{
    "body": "Merged in Sage 3.4.final.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-11T03:45:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5476#issuecomment-42397",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.final.

Cheers,

Michael



---

archive/issue_events_005730.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-03-11T03:45:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5476",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5476#event-5730"
}
```
