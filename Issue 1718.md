# Issue 1718: bug in parametric_plot

archive/issues_001718.json:
```json
{
    "body": "Assignee: @williamstein\n\nsage: parametric_plot([t, t + RR(pi)], -2, 2, rgbcolor=(1,0,0))\n\nworks but not this:\n\nsage: parametric_plot([t, t + pi], -2, 2, rgbcolor=(1,0,0))\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n....\n\n<type 'exceptions.AttributeError'>: 'Pi' object has no attribute\n'number_of_arguments'\n\nIssue created by migration from https://trac.sagemath.org/ticket/1718\n\n",
    "created_at": "2008-01-07T22:34:39Z",
    "labels": [
        "component: graphics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "bug in parametric_plot",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1718",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: @williamstein

sage: parametric_plot([t, t + RR(pi)], -2, 2, rgbcolor=(1,0,0))

works but not this:

sage: parametric_plot([t, t + pi], -2, 2, rgbcolor=(1,0,0))
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

....

<type 'exceptions.AttributeError'>: 'Pi' object has no attribute
'number_of_arguments'

Issue created by migration from https://trac.sagemath.org/ticket/1718





---

archive/issue_comments_010862.json:
```json
{
    "body": "Attachment [trac-1718.patch](tarball://root/attachments/some-uuid/ticket1718/trac-1718.patch) by @williamstein created at 2008-01-18 16:19:44",
    "created_at": "2008-01-18T16:19:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1718",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1718#issuecomment-10862",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-1718.patch](tarball://root/attachments/some-uuid/ticket1718/trac-1718.patch) by @williamstein created at 2008-01-18 16:19:44



---

archive/issue_comments_010863.json:
```json
{
    "body": "Looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-21T02:38:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1718",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1718#issuecomment-10863",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Looks good to me.

Cheers,

Michael



---

archive/issue_comments_010864.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha1",
    "created_at": "2008-01-21T02:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1718",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1718#issuecomment-10864",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha1



---

archive/issue_comments_010865.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha1 - and this time I closed the ticket, too.",
    "created_at": "2008-01-21T05:26:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1718",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1718#issuecomment-10865",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha1 - and this time I closed the ticket, too.



---

archive/issue_comments_010866.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-21T05:26:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1718",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1718#issuecomment-10866",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001877.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-21T05:26:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1718",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1718#event-1877"
}
```
