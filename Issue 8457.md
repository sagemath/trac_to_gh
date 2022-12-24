# Issue 8457: Yet more annoying warnings when building the reference manual

archive/issues_008457.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  jhpalmieri mvngu\n\nMostly of this sort:\n\n```\ncategories/examples/finite_semigroups.rst:6: (WARNING/2) error while formatting signature for sage.categories.examples.finite_semigroups.LeftRegularBand.Element.wrapped_class.center: arg is not a module, class, method, function, traceback, frame, or code object\n```\n\nThis may happen because `wrapped_class = str` is [an alias of] a builtin.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8457\n\n",
    "created_at": "2010-03-06T10:10:37Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Yet more annoying warnings when building the reference manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8457",
    "user": "mpatel"
}
```
Assignee: mvngu

CC:  jhpalmieri mvngu

Mostly of this sort:

```
categories/examples/finite_semigroups.rst:6: (WARNING/2) error while formatting signature for sage.categories.examples.finite_semigroups.LeftRegularBand.Element.wrapped_class.center: arg is not a module, class, method, function, traceback, frame, or code object
```

This may happen because `wrapped_class = str` is [an alias of] a builtin.

Issue created by migration from https://trac.sagemath.org/ticket/8457





---

archive/issue_comments_076122.json:
```json
{
    "body": "Attachment [trac_8457-doc_skip_builtins.patch](tarball://root/attachments/some-uuid/ticket8457/trac_8457-doc_skip_builtins.patch) by mpatel created at 2010-03-06 14:35:15\n\nSkip builtins.  Depends on #7448.",
    "created_at": "2010-03-06T14:35:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8457#issuecomment-76122",
    "user": "mpatel"
}
```

Attachment [trac_8457-doc_skip_builtins.patch](tarball://root/attachments/some-uuid/ticket8457/trac_8457-doc_skip_builtins.patch) by mpatel created at 2010-03-06 14:35:15

Skip builtins.  Depends on #7448.



---

archive/issue_comments_076123.json:
```json
{
    "body": "The attached patch appears to be enough for builtins, if we're willing to skip them.\n\nNote: It clashes with the first at #8452.",
    "created_at": "2010-03-06T14:44:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8457#issuecomment-76123",
    "user": "mpatel"
}
```

The attached patch appears to be enough for builtins, if we're willing to skip them.

Note: It clashes with the first at #8452.



---

archive/issue_comments_076124.json:
```json
{
    "body": "Attachment [trac_8457-doc_skip_builtins.2.patch](tarball://root/attachments/some-uuid/ticket8457/trac_8457-doc_skip_builtins.2.patch) by mpatel created at 2010-03-09 04:53:39\n\nRebased vs. #8452.",
    "created_at": "2010-03-09T04:53:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8457#issuecomment-76124",
    "user": "mpatel"
}
```

Attachment [trac_8457-doc_skip_builtins.2.patch](tarball://root/attachments/some-uuid/ticket8457/trac_8457-doc_skip_builtins.2.patch) by mpatel created at 2010-03-09 04:53:39

Rebased vs. #8452.



---

archive/issue_comments_076125.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-09T11:54:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8457#issuecomment-76125",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076126.json:
```json
{
    "body": "I think this is okay: I don't see a problem with skipping builtins.",
    "created_at": "2010-03-09T22:18:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8457#issuecomment-76126",
    "user": "jhpalmieri"
}
```

I think this is okay: I don't see a problem with skipping builtins.



---

archive/issue_comments_076127.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-09T22:18:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8457#issuecomment-76127",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076128.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-11T04:46:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8457#issuecomment-76128",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_076129.json:
```json
{
    "body": "Merged [trac_8457-doc_skip_builtins.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8457/trac_8457-doc_skip_builtins.2.patch).",
    "created_at": "2010-03-11T04:46:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8457#issuecomment-76129",
    "user": "mvngu"
}
```

Merged [trac_8457-doc_skip_builtins.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8457/trac_8457-doc_skip_builtins.2.patch).
