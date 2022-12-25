# Issue 6838: error creating matrices over GF(2) from elements of QQ

archive/issues_006838.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  was rbradshaw malb\n\nYet another thing I can't understand:\n\n\n```\nsage: GF(2)(1/3)\n1\nsage: MatrixSpace(GF(2), 1, 1)([1/3])\n[0]\n```\n\n\nFor the record:\n\n\n```\nsage: MatrixSpace(Zmod(4), 1, 1)([1/3])\n[3]\nsage: Zmod(4)(1/3)\n3\n```\n\n\nSo it's not always broken.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6838\n\n",
    "created_at": "2009-08-28T21:05:10Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "error creating matrices over GF(2) from elements of QQ",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6838",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @williamstein

CC:  was rbradshaw malb

Yet another thing I can't understand:


```
sage: GF(2)(1/3)
1
sage: MatrixSpace(GF(2), 1, 1)([1/3])
[0]
```


For the record:


```
sage: MatrixSpace(Zmod(4), 1, 1)([1/3])
[3]
sage: Zmod(4)(1/3)
3
```


So it's not always broken.

Issue created by migration from https://trac.sagemath.org/ticket/6838





---

archive/issue_comments_056297.json:
```json
{
    "body": "Attachment [trac_6838.patch](tarball://root/attachments/some-uuid/ticket6838/trac_6838.patch) by @mwhansen created at 2009-09-01 22:36:10",
    "created_at": "2009-09-01T22:36:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6838#issuecomment-56297",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_6838.patch](tarball://root/attachments/some-uuid/ticket6838/trac_6838.patch) by @mwhansen created at 2009-09-01 22:36:10



---

archive/issue_comments_056298.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-09-01T22:36:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6838#issuecomment-56298",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_056299.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2009-09-01T22:36:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6838#issuecomment-56299",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_056300.json:
```json
{
    "body": "Patch looks good.",
    "created_at": "2009-09-02T00:06:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6838#issuecomment-56300",
    "user": "https://github.com/malb"
}
```

Patch looks good.



---

archive/issue_comments_056301.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-02T16:50:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6838#issuecomment-56301",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_007071.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-02T16:50:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6838",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6838#event-7071"
}
```
