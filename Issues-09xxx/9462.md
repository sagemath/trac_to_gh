# Issue 9462: warning in matrix_modn_dense.pyx

archive/issues_009462.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\ncython gives a warning when compiling `matrix_modn_dense.pyx`:\n\n```\nwarning: /data2/wpalenst/sage-4.5.alpha4/devel/sage-main/sage/matrix/matrix_modn_dense.pyx:105:8: Function signature does not match previous declaration\n```\n\nI've uploaded a patch that removes the duplicate declaration (of `memcpy`), and also removes the unused declaration of `memcmp`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9462\n\n",
    "closed_at": "2010-07-26T02:18:57Z",
    "created_at": "2010-07-09T08:31:52Z",
    "labels": [
        "component: build",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "warning in matrix_modn_dense.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9462",
    "user": "https://github.com/wjp"
}
```
Assignee: GeorgSWeber

cython gives a warning when compiling `matrix_modn_dense.pyx`:

```
warning: /data2/wpalenst/sage-4.5.alpha4/devel/sage-main/sage/matrix/matrix_modn_dense.pyx:105:8: Function signature does not match previous declaration
```

I've uploaded a patch that removes the duplicate declaration (of `memcpy`), and also removes the unused declaration of `memcmp`.

Issue created by migration from https://trac.sagemath.org/ticket/9462





---

archive/issue_comments_090592.json:
```json
{
    "body": "Attachment [trac_9462_duplicate_decl.patch](tarball://root/attachments/some-uuid/ticket9462/trac_9462_duplicate_decl.patch) by @wjp created at 2010-07-09 09:37:12",
    "created_at": "2010-07-09T09:37:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9462#issuecomment-90592",
    "user": "https://github.com/wjp"
}
```

Attachment [trac_9462_duplicate_decl.patch](tarball://root/attachments/some-uuid/ticket9462/trac_9462_duplicate_decl.patch) by @wjp created at 2010-07-09 09:37:12



---

archive/issue_comments_090593.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-09T09:37:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9462#issuecomment-90593",
    "user": "https://github.com/wjp"
}
```

Changing status from new to needs_review.



---

archive/issue_events_023439.json:
```json
{
    "actor": "https://github.com/wjp",
    "created_at": "2010-07-17T10:53:42Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9462",
    "milestone": "sage-4.5.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9462#event-23439"
}
```



---

archive/issue_comments_090594.json:
```json
{
    "body": "The patch makes the warning go away and all tests pass afterwards.  Since the declaration is already included via `include \"../ext/cdefs.pxi\"`, getting rid of the extra one looks fine.  Positive review.",
    "created_at": "2010-07-23T01:21:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9462#issuecomment-90594",
    "user": "https://github.com/jhpalmieri"
}
```

The patch makes the warning go away and all tests pass afterwards.  Since the declaration is already included via `include "../ext/cdefs.pxi"`, getting rid of the extra one looks fine.  Positive review.



---

archive/issue_comments_090595.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-23T01:21:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9462#issuecomment-90595",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_023440.json:
```json
{
    "actor": "https://github.com/dandrake",
    "created_at": "2010-07-26T02:18:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9462",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9462#event-23440"
}
```



---

archive/issue_comments_090596.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-26T02:18:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9462#issuecomment-90596",
    "user": "https://github.com/dandrake"
}
```

Resolution: fixed
