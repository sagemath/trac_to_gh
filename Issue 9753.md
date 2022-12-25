# Issue 9753: Simplify NumberFieldIdeal.gens_reduced()

archive/issues_009753.json:
```json
{
    "body": "Assignee: @loefflerd\n\nThe function NumberFieldIdeal.gens_reduced() can be simplified quite a bit without essentially changing its functionality.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9753\n\n",
    "created_at": "2010-08-15T19:56:54Z",
    "labels": [
        "component: number fields",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Simplify NumberFieldIdeal.gens_reduced()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9753",
    "user": "https://github.com/jdemeyer"
}
```
Assignee: @loefflerd

The function NumberFieldIdeal.gens_reduced() can be simplified quite a bit without essentially changing its functionality.

Issue created by migration from https://trac.sagemath.org/ticket/9753





---

archive/issue_comments_095343.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-08-15T20:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9753#issuecomment-95343",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_095344.json:
```json
{
    "body": "I will wait to fix the doctests until after #9343 and #9400.",
    "created_at": "2010-08-15T20:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9753#issuecomment-95344",
    "user": "https://github.com/jdemeyer"
}
```

I will wait to fix the doctests until after #9343 and #9400.



---

archive/issue_comments_095345.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-13T07:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9753#issuecomment-95345",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_095346.json:
```json
{
    "body": "Attachment [9753.patch](tarball://root/attachments/some-uuid/ticket9753/9753.patch) by @jdemeyer created at 2010-09-16 00:43:33\n\nAdds function gens_two(), rewrites gens_reduced() and fixes doctests",
    "created_at": "2010-09-16T00:43:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9753#issuecomment-95346",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [9753.patch](tarball://root/attachments/some-uuid/ticket9753/9753.patch) by @jdemeyer created at 2010-09-16 00:43:33

Adds function gens_two(), rewrites gens_reduced() and fixes doctests



---

archive/issue_comments_095347.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-09-16T16:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9753#issuecomment-95347",
    "user": "https://github.com/jdemeyer"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_095348.json:
```json
{
    "body": "Changing keywords from \"\" to \"number field ideal gens_two idealtwoelt\".",
    "created_at": "2010-09-16T16:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9753#issuecomment-95348",
    "user": "https://github.com/jdemeyer"
}
```

Changing keywords from "" to "number field ideal gens_two idealtwoelt".



---

archive/issue_comments_095349.json:
```json
{
    "body": "Looks fine to me, and all tests pass on my machine.",
    "created_at": "2010-09-23T10:58:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9753#issuecomment-95349",
    "user": "https://github.com/loefflerd"
}
```

Looks fine to me, and all tests pass on my machine.



---

archive/issue_comments_095350.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-23T10:58:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9753#issuecomment-95350",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095351.json:
```json
{
    "body": "Could someone update the patch commit string with a more descriptive first line (still including the ticket number) and restore the positive review?",
    "created_at": "2010-09-28T09:34:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9753#issuecomment-95351",
    "user": "https://github.com/qed777"
}
```

Could someone update the patch commit string with a more descriptive first line (still including the ticket number) and restore the positive review?



---

archive/issue_comments_095352.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-28T09:34:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9753#issuecomment-95352",
    "user": "https://github.com/qed777"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_095353.json:
```json
{
    "body": "Attachment [9753-better_commit_string.patch](tarball://root/attachments/some-uuid/ticket9753/9753-better_commit_string.patch) by @loefflerd created at 2010-09-28 09:41:42\n\nNew version with better commit string",
    "created_at": "2010-09-28T09:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9753#issuecomment-95353",
    "user": "https://github.com/loefflerd"
}
```

Attachment [9753-better_commit_string.patch](tarball://root/attachments/some-uuid/ticket9753/9753-better_commit_string.patch) by @loefflerd created at 2010-09-28 09:41:42

New version with better commit string



---

archive/issue_comments_095354.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-09-28T09:42:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9753#issuecomment-95354",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_095355.json:
```json
{
    "body": "Done.",
    "created_at": "2010-09-28T09:42:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9753#issuecomment-95355",
    "user": "https://github.com/loefflerd"
}
```

Done.



---

archive/issue_comments_095356.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-28T10:55:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9753#issuecomment-95356",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
