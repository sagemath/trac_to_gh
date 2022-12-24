# Issue 8965: decorate.py: clarify normalize_input, Parallel and parallel

archive/issues_008965.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  was\n\nClarify documentation, add some doctests, and slightly simplify the implementation of Parallel.__call__.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8965\n\n",
    "created_at": "2010-05-14T18:01:22Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "title": "decorate.py: clarify normalize_input, Parallel and parallel",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8965",
    "user": "jdc"
}
```
Assignee: mvngu

CC:  was

Clarify documentation, add some doctests, and slightly simplify the implementation of Parallel.__call__.

Issue created by migration from https://trac.sagemath.org/ticket/8965





---

archive/issue_comments_082625.json:
```json
{
    "body": "Attachment [trac_8965_decorate2.patch](tarball://root/attachments/some-uuid/ticket8965/trac_8965_decorate2.patch) by jdc created at 2010-05-14 18:09:12\n\nFound a typo in comment; apply both patches",
    "created_at": "2010-05-14T18:09:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8965#issuecomment-82625",
    "user": "jdc"
}
```

Attachment [trac_8965_decorate2.patch](tarball://root/attachments/some-uuid/ticket8965/trac_8965_decorate2.patch) by jdc created at 2010-05-14 18:09:12

Found a typo in comment; apply both patches



---

archive/issue_comments_082626.json:
```json
{
    "body": "Attachment [trac_8965-decorate-folded.patch](tarball://root/attachments/some-uuid/ticket8965/trac_8965-decorate-folded.patch) by mvngu created at 2010-05-15 02:38:25\n\nfolded the previous two patches into one patch; based on Sage 4.4.2.rc0",
    "created_at": "2010-05-15T02:38:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8965#issuecomment-82626",
    "user": "mvngu"
}
```

Attachment [trac_8965-decorate-folded.patch](tarball://root/attachments/some-uuid/ticket8965/trac_8965-decorate-folded.patch) by mvngu created at 2010-05-15 02:38:25

folded the previous two patches into one patch; based on Sage 4.4.2.rc0



---

archive/issue_comments_082627.json:
```json
{
    "body": "The patch [trac_8965-decorate-folded.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8965/trac_8965-decorate-folded.patch) folds the other two patches into one. That way, it would be easier for reviewers to see what changes are proposed, instead of having to inspect two different patches.",
    "created_at": "2010-05-15T02:41:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8965#issuecomment-82627",
    "user": "mvngu"
}
```

The patch [trac_8965-decorate-folded.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8965/trac_8965-decorate-folded.patch) folds the other two patches into one. That way, it would be easier for reviewers to see what changes are proposed, instead of having to inspect two different patches.



---

archive/issue_comments_082628.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-15T02:41:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8965#issuecomment-82628",
    "user": "mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082629.json:
```json
{
    "body": "Thanks for merging the patches.  I realized last night that my \"simplificiation\" of the __call__ method is incorrect.  I'll upload a better patch (with an additional doctest) later today.",
    "created_at": "2010-05-15T13:28:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8965#issuecomment-82629",
    "user": "jdc"
}
```

Thanks for merging the patches.  I realized last night that my "simplificiation" of the __call__ method is incorrect.  I'll upload a better patch (with an additional doctest) later today.



---

archive/issue_comments_082630.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-15T13:28:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8965#issuecomment-82630",
    "user": "jdc"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082631.json:
```json
{
    "body": "single patch, ready for review",
    "created_at": "2010-05-16T00:24:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8965#issuecomment-82631",
    "user": "jdc"
}
```

single patch, ready for review



---

archive/issue_comments_082632.json:
```json
{
    "body": "Attachment [trac_8965_decorate.patch](tarball://root/attachments/some-uuid/ticket8965/trac_8965_decorate.patch) by jdc created at 2010-05-16 00:29:13\n\nThe only patch needed now is trac_8965_decorate.patch.  (I couldn't figure out how to delete the others.)  It reverts to the original implementation of Parallel.__call__, since the simpler one didn't handle the case where the function being wrapped can be called with no arguments.  The latest patch includes doctests for this situation.\n\nThe latest patch only changes documentation or comments, besides one whitespace change to the code.",
    "created_at": "2010-05-16T00:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8965#issuecomment-82632",
    "user": "jdc"
}
```

Attachment [trac_8965_decorate.patch](tarball://root/attachments/some-uuid/ticket8965/trac_8965_decorate.patch) by jdc created at 2010-05-16 00:29:13

The only patch needed now is trac_8965_decorate.patch.  (I couldn't figure out how to delete the others.)  It reverts to the original implementation of Parallel.__call__, since the simpler one didn't handle the case where the function being wrapped can be called with no arguments.  The latest patch includes doctests for this situation.

The latest patch only changes documentation or comments, besides one whitespace change to the code.



---

archive/issue_comments_082633.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-16T00:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8965#issuecomment-82633",
    "user": "jdc"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082634.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-21T15:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8965#issuecomment-82634",
    "user": "cmullan"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082635.json:
```json
{
    "body": "EXAMPLES: should be EXAMPLES::",
    "created_at": "2010-07-21T15:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8965#issuecomment-82635",
    "user": "cmullan"
}
```

EXAMPLES: should be EXAMPLES::
