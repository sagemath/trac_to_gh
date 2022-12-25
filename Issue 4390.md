# Issue 4390: elliptic curves: heegner_index command broken

archive/issues_004390.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\nsage: EllipticCurve('675b').heegner_index(-11)\nTraceback (most recent call last):\n...\nTypeError: regulator() got an unexpected keyword argument 'verbose'\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/4390\n\n",
    "created_at": "2008-10-30T05:35:53Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "elliptic curves: heegner_index command broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4390",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

```
sage: EllipticCurve('675b').heegner_index(-11)
Traceback (most recent call last):
...
TypeError: regulator() got an unexpected keyword argument 'verbose'
```

Issue created by migration from https://trac.sagemath.org/ticket/4390





---

archive/issue_comments_032248.json:
```json
{
    "body": "Attachment [sage-4390.patch](tarball://root/attachments/some-uuid/ticket4390/sage-4390.patch) by @williamstein created at 2008-10-30 05:40:48",
    "created_at": "2008-10-30T05:40:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4390#issuecomment-32248",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-4390.patch](tarball://root/attachments/some-uuid/ticket4390/sage-4390.patch) by @williamstein created at 2008-10-30 05:40:48



---

archive/issue_comments_032249.json:
```json
{
    "body": "Looks good.",
    "created_at": "2008-10-30T05:43:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4390#issuecomment-32249",
    "user": "https://github.com/craigcitro"
}
```

Looks good.



---

archive/issue_comments_032250.json:
```json
{
    "body": "Merged in Sage 3.2.alpha2",
    "created_at": "2008-10-30T05:46:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4390#issuecomment-32250",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha2



---

archive/issue_comments_032251.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-30T05:46:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4390#issuecomment-32251",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_009912.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-30T05:46:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4390",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4390#event-9912"
}
```
