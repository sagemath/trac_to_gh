# Issue 1106: speed up dense matrix comparison

archive/issues_001106.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe general implementation right now is:\n\n```\ncdef int _cmp_c_impl(self, Element right) except -2:\n    return cmp(self._list(), right._list())\n```\n\nwhich has a huge memory overhead. This should be optimised. Also, Matrix_modn_dense should have a faster special cmp method.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1106\n\n",
    "created_at": "2007-11-05T12:22:36Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.1",
    "title": "speed up dense matrix comparison",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1106",
    "user": "https://github.com/malb"
}
```
Assignee: @williamstein

The general implementation right now is:

```
cdef int _cmp_c_impl(self, Element right) except -2:
    return cmp(self._list(), right._list())
```

which has a huge memory overhead. This should be optimised. Also, Matrix_modn_dense should have a faster special cmp method.

Issue created by migration from https://trac.sagemath.org/ticket/1106





---

archive/issue_comments_006672.json:
```json
{
    "body": "Attachment [1106.patch](tarball://root/attachments/some-uuid/ticket1106/1106.patch) by @mwhansen created at 2007-12-22 17:38:24",
    "created_at": "2007-12-22T17:38:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1106#issuecomment-6672",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1106.patch](tarball://root/attachments/some-uuid/ticket1106/1106.patch) by @mwhansen created at 2007-12-22 17:38:24



---

archive/issue_comments_006673.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-22T17:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1106#issuecomment-6673",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006674.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2007-12-22T17:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1106#issuecomment-6674",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_006675.json:
```json
{
    "body": "merged in 2.9.1 rc0",
    "created_at": "2007-12-22T18:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1106#issuecomment-6675",
    "user": "https://github.com/rlmill"
}
```

merged in 2.9.1 rc0



---

archive/issue_comments_006676.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-22T18:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1106#issuecomment-6676",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_001232.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2007-12-22T18:08:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1106",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1106#event-1232"
}
```
