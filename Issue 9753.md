# Issue 9753: Simplify NumberFieldIdeal.gens_reduced()

archive/issues_009753.json:
```json
{
    "body": "Assignee: davidloeffler\n\nThe function NumberFieldIdeal.gens_reduced() can be simplified quite a bit without essentially changing its functionality.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9753\n\n",
    "created_at": "2010-08-15T19:56:54Z",
    "labels": [
        "number fields",
        "major",
        "bug"
    ],
    "title": "Simplify NumberFieldIdeal.gens_reduced()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9753",
    "user": "jdemeyer"
}
```
Assignee: davidloeffler

The function NumberFieldIdeal.gens_reduced() can be simplified quite a bit without essentially changing its functionality.

Issue created by migration from https://trac.sagemath.org/ticket/9753





---

archive/issue_comments_095502.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-08-15T20:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9753#issuecomment-95502",
    "user": "jdemeyer"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_095503.json:
```json
{
    "body": "I will wait to fix the doctests until after #9343 and #9400.",
    "created_at": "2010-08-15T20:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9753#issuecomment-95503",
    "user": "jdemeyer"
}
```

I will wait to fix the doctests until after #9343 and #9400.



---

archive/issue_comments_095504.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-13T07:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9753#issuecomment-95504",
    "user": "jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_095505.json:
```json
{
    "body": "Attachment [9753.patch](tarball://root/attachments/some-uuid/ticket9753/9753.patch) by jdemeyer created at 2010-09-16 00:43:33\n\nAdds function gens_two(), rewrites gens_reduced() and fixes doctests",
    "created_at": "2010-09-16T00:43:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9753#issuecomment-95505",
    "user": "jdemeyer"
}
```

Attachment [9753.patch](tarball://root/attachments/some-uuid/ticket9753/9753.patch) by jdemeyer created at 2010-09-16 00:43:33

Adds function gens_two(), rewrites gens_reduced() and fixes doctests



---

archive/issue_comments_095506.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-09-16T16:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9753#issuecomment-95506",
    "user": "jdemeyer"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_095507.json:
```json
{
    "body": "Changing keywords from \"\" to \"number field ideal gens_two idealtwoelt\".",
    "created_at": "2010-09-16T16:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9753#issuecomment-95507",
    "user": "jdemeyer"
}
```

Changing keywords from "" to "number field ideal gens_two idealtwoelt".



---

archive/issue_comments_095508.json:
```json
{
    "body": "Looks fine to me, and all tests pass on my machine.",
    "created_at": "2010-09-23T10:58:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9753#issuecomment-95508",
    "user": "davidloeffler"
}
```

Looks fine to me, and all tests pass on my machine.



---

archive/issue_comments_095509.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-23T10:58:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9753#issuecomment-95509",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095510.json:
```json
{
    "body": "Could someone update the patch commit string with a more descriptive first line (still including the ticket number) and restore the positive review?",
    "created_at": "2010-09-28T09:34:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9753#issuecomment-95510",
    "user": "mpatel"
}
```

Could someone update the patch commit string with a more descriptive first line (still including the ticket number) and restore the positive review?



---

archive/issue_comments_095511.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-28T09:34:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9753#issuecomment-95511",
    "user": "mpatel"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_095512.json:
```json
{
    "body": "Attachment [9753-better_commit_string.patch](tarball://root/attachments/some-uuid/ticket9753/9753-better_commit_string.patch) by davidloeffler created at 2010-09-28 09:41:42\n\nNew version with better commit string",
    "created_at": "2010-09-28T09:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9753#issuecomment-95512",
    "user": "davidloeffler"
}
```

Attachment [9753-better_commit_string.patch](tarball://root/attachments/some-uuid/ticket9753/9753-better_commit_string.patch) by davidloeffler created at 2010-09-28 09:41:42

New version with better commit string



---

archive/issue_comments_095513.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-09-28T09:42:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9753#issuecomment-95513",
    "user": "davidloeffler"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_095514.json:
```json
{
    "body": "Done.",
    "created_at": "2010-09-28T09:42:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9753#issuecomment-95514",
    "user": "davidloeffler"
}
```

Done.



---

archive/issue_comments_095515.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-28T10:55:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9753#issuecomment-95515",
    "user": "mpatel"
}
```

Resolution: fixed
