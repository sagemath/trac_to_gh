# Issue 1106: speed up dense matrix comparison

archive/issues_001106.json:
```json
{
    "body": "Assignee: was\n\nThe general implementation right now is:\n\n```\ncdef int _cmp_c_impl(self, Element right) except -2:\n    return cmp(self._list(), right._list())\n```\n\nwhich has a huge memory overhead. This should be optimised. Also, Matrix_modn_dense should have a faster special cmp method.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1106\n\n",
    "created_at": "2007-11-05T12:22:36Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "title": "speed up dense matrix comparison",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1106",
    "user": "malb"
}
```
Assignee: was

The general implementation right now is:

```
cdef int _cmp_c_impl(self, Element right) except -2:
    return cmp(self._list(), right._list())
```

which has a huge memory overhead. This should be optimised. Also, Matrix_modn_dense should have a faster special cmp method.

Issue created by migration from https://trac.sagemath.org/ticket/1106





---

archive/issue_comments_006692.json:
```json
{
    "body": "Attachment [1106.patch](tarball://root/attachments/some-uuid/ticket1106/1106.patch) by mhansen created at 2007-12-22 17:38:24",
    "created_at": "2007-12-22T17:38:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1106#issuecomment-6692",
    "user": "mhansen"
}
```

Attachment [1106.patch](tarball://root/attachments/some-uuid/ticket1106/1106.patch) by mhansen created at 2007-12-22 17:38:24



---

archive/issue_comments_006693.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-22T17:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1106#issuecomment-6693",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006694.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2007-12-22T17:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1106#issuecomment-6694",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_006695.json:
```json
{
    "body": "merged in 2.9.1 rc0",
    "created_at": "2007-12-22T18:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1106#issuecomment-6695",
    "user": "rlm"
}
```

merged in 2.9.1 rc0



---

archive/issue_comments_006696.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-22T18:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1106#issuecomment-6696",
    "user": "rlm"
}
```

Resolution: fixed
