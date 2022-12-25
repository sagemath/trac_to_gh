# Issue 1352: [with patch] doctest error in 2.8.15.alpha0 polynomial_element.pyx

archive/issues_001352.json:
```json
{
    "body": "Assignee: @mwhansen\n\n```\nsage: R.<x> = QQ[]; S.<y> = R[]\nsage: f = x+y*x+y^2\nsage: f(x=sqrt(2))\n...\nIndexError: tuple index out of range\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/1352\n\n",
    "closed_at": "2007-12-01T19:05:15Z",
    "created_at": "2007-12-01T18:32:53Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "[with patch] doctest error in 2.8.15.alpha0 polynomial_element.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1352",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @mwhansen

```
sage: R.<x> = QQ[]; S.<y> = R[]
sage: f = x+y*x+y^2
sage: f(x=sqrt(2))
...
IndexError: tuple index out of range
```

Issue created by migration from https://trac.sagemath.org/ticket/1352





---

archive/issue_comments_008638.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-01T19:05:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1352#issuecomment-8638",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_008639.json:
```json
{
    "body": "Attachment [1352.patch](tarball://root/attachments/some-uuid/ticket1352/1352.patch) by mabshoff created at 2007-12-01 19:05:15\n\nMerged in 2.8.15.alpha1.",
    "created_at": "2007-12-01T19:05:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1352#issuecomment-8639",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [1352.patch](tarball://root/attachments/some-uuid/ticket1352/1352.patch) by mabshoff created at 2007-12-01 19:05:15

Merged in 2.8.15.alpha1.



---

archive/issue_events_003499.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-01T19:05:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1352",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1352#event-3499"
}
```
