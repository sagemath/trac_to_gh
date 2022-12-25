# Issue 1913: poles of gamma

archive/issues_001913.json:
```json
{
    "body": "Assignee: @burcin\n\nSage cannot handle poles of the gamma function. For negative integers and 0, the result of `gamma(x)` should be unsigned infinity.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1913\n\n",
    "created_at": "2008-01-24T16:37:15Z",
    "labels": [
        "component: misc",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "poles of gamma",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1913",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

Sage cannot handle poles of the gamma function. For negative integers and 0, the result of `gamma(x)` should be unsigned infinity.

Issue created by migration from https://trac.sagemath.org/ticket/1913





---

archive/issue_comments_012091.json:
```json
{
    "body": "Attachment [1913-gamma_poles.patch](tarball://root/attachments/some-uuid/ticket1913/1913-gamma_poles.patch) by @burcin created at 2008-01-24 16:40:29\n\nmake gamma return Infinity for 0, -1, ...",
    "created_at": "2008-01-24T16:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1913#issuecomment-12091",
    "user": "https://github.com/burcin"
}
```

Attachment [1913-gamma_poles.patch](tarball://root/attachments/some-uuid/ticket1913/1913-gamma_poles.patch) by @burcin created at 2008-01-24 16:40:29

make gamma return Infinity for 0, -1, ...



---

archive/issue_comments_012092.json:
```json
{
    "body": "attachment:1913-gamma_poles.patch makes sage.rings.complex_number.ComplexNumber.gamma return Infinity for 0 and negative integers.",
    "created_at": "2008-01-25T08:48:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1913#issuecomment-12092",
    "user": "https://github.com/burcin"
}
```

attachment:1913-gamma_poles.patch makes sage.rings.complex_number.ComplexNumber.gamma return Infinity for 0 and negative integers.



---

archive/issue_comments_012093.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-25T08:48:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1913#issuecomment-12093",
    "user": "https://github.com/burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_012094.json:
```json
{
    "body": "Works fine for me.   Seems like a reasonable thing to do for now; definitely better than the current behavior.  (Though our infinity in Sage maybe isn't optimal for this sort of application...)",
    "created_at": "2008-01-25T13:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1913#issuecomment-12094",
    "user": "https://github.com/williamstein"
}
```

Works fine for me.   Seems like a reasonable thing to do for now; definitely better than the current behavior.  (Though our infinity in Sage maybe isn't optimal for this sort of application...)



---

archive/issue_comments_012095.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-25T17:26:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1913#issuecomment-12095",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002069.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-01-25T17:26:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1913",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1913#event-2069"
}
```



---

archive/issue_comments_012096.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha2",
    "created_at": "2008-01-25T17:26:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1913#issuecomment-12096",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha2
