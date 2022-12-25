# Issue 9239: delete the (ridiculous) method __copy__ from matrix0.pyx

archive/issues_009239.json:
```json
{
    "body": "Assignee: jason, was\n\n`__copy__` was overloaded, never used.\n\nSee this [sage-devel thread](http://groups.google.com/group/sage-devel/browse_thread/thread/bd4f3088ba73d6a5) for background information.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9239\n\n",
    "closed_at": "2010-07-20T08:21:26Z",
    "created_at": "2010-06-14T23:39:58Z",
    "labels": [
        "component: linear algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "delete the (ridiculous) method __copy__ from matrix0.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9239",
    "user": "https://github.com/williamstein"
}
```
Assignee: jason, was

`__copy__` was overloaded, never used.

See this [sage-devel thread](http://groups.google.com/group/sage-devel/browse_thread/thread/bd4f3088ba73d6a5) for background information.

Issue created by migration from https://trac.sagemath.org/ticket/9239





---

archive/issue_comments_086751.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-15T00:15:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9239#issuecomment-86751",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_086752.json:
```json
{
    "body": "Attachment [trac_9239-matrix_copy_remove-fh.patch](tarball://root/attachments/some-uuid/ticket9239/trac_9239-matrix_copy_remove-fh.patch) by @hivert created at 2010-06-15 00:15:12\n\nNote: the doctest where duplicated from the `.copy()` method so I didn't kept them.\n\nPlease review",
    "created_at": "2010-06-15T00:15:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9239#issuecomment-86752",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_9239-matrix_copy_remove-fh.patch](tarball://root/attachments/some-uuid/ticket9239/trac_9239-matrix_copy_remove-fh.patch) by @hivert created at 2010-06-15 00:15:12

Note: the doctest where duplicated from the `.copy()` method so I didn't kept them.

Please review



---

archive/issue_comments_086753.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-15T02:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9239#issuecomment-86753",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086754.json:
```json
{
    "body": "Yep.",
    "created_at": "2010-06-15T02:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9239#issuecomment-86754",
    "user": "https://github.com/williamstein"
}
```

Yep.



---

archive/issue_comments_086755.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T08:21:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9239#issuecomment-86755",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_022749.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-20T08:21:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9239",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9239#event-22749"
}
```
