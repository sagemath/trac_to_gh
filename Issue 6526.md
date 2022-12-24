# Issue 6526: remove naive suffix trees

archive/issues_006526.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  @saliola\n\nThis is one of the obstructions to switching the graph backends over to Cython by default.\n\nTo quote Franco:\n\n```\nBut all the doctest failures occur in the NaiveSuffixTreeClass, which\nis a naive implementation. This code was only intended for testing\npurposes, so I think it is fine to delete it (delete both\nNaiveSuffixTree and NaiveSuffixTreeClass). I am pretty certain it is\nnot used anywhere else (it should not be, if it is), because it is a\nvery slow implementation (hence, the name naive).\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6526\n\n",
    "created_at": "2009-07-13T19:12:33Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "remove naive suffix trees",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6526",
    "user": "@rlmill"
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

archive/issue_comments_053219.json:
```json
{
    "body": "This will be based on #6519.",
    "created_at": "2009-07-13T19:12:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6526#issuecomment-53219",
    "user": "@rlmill"
}
```

This will be based on #6519.



---

archive/issue_comments_053220.json:
```json
{
    "body": "based on #6519",
    "created_at": "2009-07-14T16:05:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6526#issuecomment-53220",
    "user": "@rlmill"
}
```

based on #6519



---

archive/issue_comments_053221.json:
```json
{
    "body": "Attachment [trac_6526-remove-naive-suffix-tree.patch](tarball://root/attachments/some-uuid/ticket6526/trac_6526-remove-naive-suffix-tree.patch) by @rlmill created at 2009-07-14 16:05:59",
    "created_at": "2009-07-14T16:05:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6526#issuecomment-53221",
    "user": "@rlmill"
}
```

Attachment [trac_6526-remove-naive-suffix-tree.patch](tarball://root/attachments/some-uuid/ticket6526/trac_6526-remove-naive-suffix-tree.patch) by @rlmill created at 2009-07-14 16:05:59



---

archive/issue_comments_053222.json:
```json
{
    "body": "Positive review.",
    "created_at": "2009-07-16T23:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6526#issuecomment-53222",
    "user": "@saliola"
}
```

Positive review.



---

archive/issue_comments_053223.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-18T14:50:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6526#issuecomment-53223",
    "user": "mvngu"
}
```

Resolution: fixed
