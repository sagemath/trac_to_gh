# Issue 6200: Use mpmath to compute constants

archive/issues_006200.json:
```json
{
    "body": "Assignee: jkantor\n\nAssumes that mpmath has been added to Sage (#6196)\n\nPatch summary:\n\nUse mpmath to compute numerical values of constants.\n\nPreviously khinchin, mertens and twinprime were LimitedPrecisionConstant,\nbut with this patch they can be computed to any precision.\n\nThe patch also adds the Glaisher constant (which is available in mpmath)\nand corrects the name of the Mertens constant.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6200\n\n",
    "created_at": "2009-06-03T20:29:36Z",
    "labels": [
        "component: numerical"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "Use mpmath to compute constants",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6200",
    "user": "https://github.com/fredrik-johansson"
}
```
Assignee: jkantor

Assumes that mpmath has been added to Sage (#6196)

Patch summary:

Use mpmath to compute numerical values of constants.

Previously khinchin, mertens and twinprime were LimitedPrecisionConstant,
but with this patch they can be computed to any precision.

The patch also adds the Glaisher constant (which is available in mpmath)
and corrects the name of the Mertens constant.

Issue created by migration from https://trac.sagemath.org/ticket/6200





---

archive/issue_comments_049440.json:
```json
{
    "body": "Attachment [constants.patch](tarball://root/attachments/some-uuid/ticket6200/constants.patch) by @fredrik-johansson created at 2009-06-19 17:30:38",
    "created_at": "2009-06-19T17:30:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6200#issuecomment-49440",
    "user": "https://github.com/fredrik-johansson"
}
```

Attachment [constants.patch](tarball://root/attachments/some-uuid/ticket6200/constants.patch) by @fredrik-johansson created at 2009-06-19 17:30:38



---

archive/issue_comments_049441.json:
```json
{
    "body": "Attachment [trac_6200-review.patch](tarball://root/attachments/some-uuid/ticket6200/trac_6200-review.patch) by @mwhansen created at 2009-06-19 23:06:59",
    "created_at": "2009-06-19T23:06:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6200#issuecomment-49441",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_6200-review.patch](tarball://root/attachments/some-uuid/ticket6200/trac_6200-review.patch) by @mwhansen created at 2009-06-19 23:06:59



---

archive/issue_comments_049442.json:
```json
{
    "body": "For backward compatibility, I added merten as an alias to mertens.  Other than that, the patch looks good.",
    "created_at": "2009-06-19T23:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6200#issuecomment-49442",
    "user": "https://github.com/mwhansen"
}
```

For backward compatibility, I added merten as an alias to mertens.  Other than that, the patch looks good.



---

archive/issue_comments_049443.json:
```json
{
    "body": "Looks good to me.  Apply both patches.",
    "created_at": "2009-06-19T23:18:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6200#issuecomment-49443",
    "user": "https://github.com/ncalexan"
}
```

Looks good to me.  Apply both patches.



---

archive/issue_comments_049444.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-03T16:55:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6200#issuecomment-49444",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
