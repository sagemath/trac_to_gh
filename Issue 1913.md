# Issue 1913: poles of gamma

archive/issues_001913.json:
```json
{
    "body": "Assignee: burcin\n\nSage cannot handle poles of the gamma function. For negative integers and 0, the result of `gamma(x)` should be unsigned infinity.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1913\n\n",
    "created_at": "2008-01-24T16:37:15Z",
    "labels": [
        "misc",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "poles of gamma",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1913",
    "user": "burcin"
}
```
Assignee: burcin

Sage cannot handle poles of the gamma function. For negative integers and 0, the result of `gamma(x)` should be unsigned infinity.

Issue created by migration from https://trac.sagemath.org/ticket/1913





---

archive/issue_comments_012121.json:
```json
{
    "body": "Attachment [1913-gamma_poles.patch](tarball://root/attachments/some-uuid/ticket1913/1913-gamma_poles.patch) by burcin created at 2008-01-24 16:40:29\n\nmake gamma return Infinity for 0, -1, ...",
    "created_at": "2008-01-24T16:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1913#issuecomment-12121",
    "user": "burcin"
}
```

Attachment [1913-gamma_poles.patch](tarball://root/attachments/some-uuid/ticket1913/1913-gamma_poles.patch) by burcin created at 2008-01-24 16:40:29

make gamma return Infinity for 0, -1, ...



---

archive/issue_comments_012122.json:
```json
{
    "body": "attachment:1913-gamma_poles.patch makes sage.rings.complex_number.ComplexNumber.gamma return Infinity for 0 and negative integers.",
    "created_at": "2008-01-25T08:48:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1913#issuecomment-12122",
    "user": "burcin"
}
```

attachment:1913-gamma_poles.patch makes sage.rings.complex_number.ComplexNumber.gamma return Infinity for 0 and negative integers.



---

archive/issue_comments_012123.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-25T08:48:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1913#issuecomment-12123",
    "user": "burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_012124.json:
```json
{
    "body": "Works fine for me.   Seems like a reasonable thing to do for now; definitely better than the current behavior.  (Though our infinity in Sage maybe isn't optimal for this sort of application...)",
    "created_at": "2008-01-25T13:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1913#issuecomment-12124",
    "user": "was"
}
```

Works fine for me.   Seems like a reasonable thing to do for now; definitely better than the current behavior.  (Though our infinity in Sage maybe isn't optimal for this sort of application...)



---

archive/issue_comments_012125.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-25T17:26:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1913#issuecomment-12125",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012126.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha2",
    "created_at": "2008-01-25T17:26:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1913#issuecomment-12126",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha2
