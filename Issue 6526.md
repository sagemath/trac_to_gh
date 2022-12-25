# Issue 6526: remove naive suffix trees

archive/issues_006526.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  @saliola\n\nThis is one of the obstructions to switching the graph backends over to Cython by default.\n\nTo quote Franco:\n\n```\nBut all the doctest failures occur in the NaiveSuffixTreeClass, which\nis a naive implementation. This code was only intended for testing\npurposes, so I think it is fine to delete it (delete both\nNaiveSuffixTree and NaiveSuffixTreeClass). I am pretty certain it is\nnot used anywhere else (it should not be, if it is), because it is a\nvery slow implementation (hence, the name naive).\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/6526\n\n",
    "created_at": "2009-07-13T19:12:33Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "remove naive suffix trees",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6526",
    "user": "https://github.com/rlmill"
}
```
Assignee: @mwhansen

CC:  @saliola

This is one of the obstructions to switching the graph backends over to Cython by default.

To quote Franco:

```
But all the doctest failures occur in the NaiveSuffixTreeClass, which
is a naive implementation. This code was only intended for testing
purposes, so I think it is fine to delete it (delete both
NaiveSuffixTree and NaiveSuffixTreeClass). I am pretty certain it is
not used anywhere else (it should not be, if it is), because it is a
very slow implementation (hence, the name naive).
```

Issue created by migration from https://trac.sagemath.org/ticket/6526





---

archive/issue_comments_053119.json:
```json
{
    "body": "This will be based on #6519.",
    "created_at": "2009-07-13T19:12:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6526#issuecomment-53119",
    "user": "https://github.com/rlmill"
}
```

This will be based on #6519.



---

archive/issue_comments_053120.json:
```json
{
    "body": "based on #6519",
    "created_at": "2009-07-14T16:05:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6526#issuecomment-53120",
    "user": "https://github.com/rlmill"
}
```

based on #6519



---

archive/issue_comments_053121.json:
```json
{
    "body": "Attachment [trac_6526-remove-naive-suffix-tree.patch](tarball://root/attachments/some-uuid/ticket6526/trac_6526-remove-naive-suffix-tree.patch) by @rlmill created at 2009-07-14 16:05:59",
    "created_at": "2009-07-14T16:05:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6526#issuecomment-53121",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_6526-remove-naive-suffix-tree.patch](tarball://root/attachments/some-uuid/ticket6526/trac_6526-remove-naive-suffix-tree.patch) by @rlmill created at 2009-07-14 16:05:59



---

archive/issue_comments_053122.json:
```json
{
    "body": "Positive review.",
    "created_at": "2009-07-16T23:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6526#issuecomment-53122",
    "user": "https://github.com/saliola"
}
```

Positive review.



---

archive/issue_events_015399.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-07-18T14:50:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6526",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6526#event-15399"
}
```



---

archive/issue_comments_053123.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-18T14:50:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6526#issuecomment-53123",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
