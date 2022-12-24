# Issue 9462: warning in matrix_modn_dense.pyx

archive/issues_009462.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\ncython gives a warning when compiling `matrix_modn_dense.pyx`:\n\n\n```\nwarning: /data2/wpalenst/sage-4.5.alpha4/devel/sage-main/sage/matrix/matrix_modn_dense.pyx:105:8: Function signature does not match previous declaration\n```\n\n\nI'll upload a patch in an hour.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9462\n\n",
    "created_at": "2010-07-09T08:31:52Z",
    "labels": [
        "build",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "warning in matrix_modn_dense.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9462",
    "user": "@wjp"
}
```
Assignee: GeorgSWeber

cython gives a warning when compiling `matrix_modn_dense.pyx`:


```
warning: /data2/wpalenst/sage-4.5.alpha4/devel/sage-main/sage/matrix/matrix_modn_dense.pyx:105:8: Function signature does not match previous declaration
```


I'll upload a patch in an hour.

Issue created by migration from https://trac.sagemath.org/ticket/9462





---

archive/issue_comments_090743.json:
```json
{
    "body": "Attachment [trac_9462_duplicate_decl.patch](tarball://root/attachments/some-uuid/ticket9462/trac_9462_duplicate_decl.patch) by @wjp created at 2010-07-09 09:37:12",
    "created_at": "2010-07-09T09:37:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9462#issuecomment-90743",
    "user": "@wjp"
}
```

Attachment [trac_9462_duplicate_decl.patch](tarball://root/attachments/some-uuid/ticket9462/trac_9462_duplicate_decl.patch) by @wjp created at 2010-07-09 09:37:12



---

archive/issue_comments_090744.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-09T09:37:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9462#issuecomment-90744",
    "user": "@wjp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090745.json:
```json
{
    "body": "The patch makes the warning go away and all tests pass afterwards.  Since the declaration is already included via `include \"../ext/cdefs.pxi\"`, getting rid of the extra one looks fine.  Positive review.",
    "created_at": "2010-07-23T01:21:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9462#issuecomment-90745",
    "user": "@jhpalmieri"
}
```

The patch makes the warning go away and all tests pass afterwards.  Since the declaration is already included via `include "../ext/cdefs.pxi"`, getting rid of the extra one looks fine.  Positive review.



---

archive/issue_comments_090746.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-23T01:21:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9462#issuecomment-90746",
    "user": "@jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090747.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-26T02:18:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9462#issuecomment-90747",
    "user": "@dandrake"
}
```

Resolution: fixed
