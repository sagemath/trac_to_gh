# Issue 5608: Mertens' constant is named wrongly

archive/issues_005608.json:
```json
{
    "body": "Assignee: cwitty\n\nsage.functions.constants.Merten is named wrongly, as the mathematician's name is Franz Mertens and not Merten. The class and default instance should be renamed and \"Merten constant\" and \"Merten's second theorem\" in the docstring should be fixed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5608\n\n",
    "created_at": "2009-03-25T12:56:31Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.12",
    "title": "Mertens' constant is named wrongly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5608",
    "user": "@fredrik-johansson"
}
```
Assignee: cwitty

sage.functions.constants.Merten is named wrongly, as the mathematician's name is Franz Mertens and not Merten. The class and default instance should be renamed and "Merten constant" and "Merten's second theorem" in the docstring should be fixed.

Issue created by migration from https://trac.sagemath.org/ticket/5608





---

archive/issue_comments_043767.json:
```json
{
    "body": "#6200 has a fix for this. I would also like to see the wrongly named `merten` constant deprecated, though I don't know how we can do this.",
    "created_at": "2009-06-23T22:16:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43767",
    "user": "@burcin"
}
```

#6200 has a fix for this. I would also like to see the wrongly named `merten` constant deprecated, though I don't know how we can do this.



---

archive/issue_comments_043768.json:
```json
{
    "body": "Changing keywords from \"\" to \"documentation, typo\".",
    "created_at": "2013-08-21T16:23:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43768",
    "user": "@fchapoton"
}
```

Changing keywords from "" to "documentation, typo".



---

archive/issue_comments_043769.json:
```json
{
    "body": "here is a patch",
    "created_at": "2013-08-21T16:23:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43769",
    "user": "@fchapoton"
}
```

here is a patch



---

archive/issue_comments_043770.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-08-21T16:23:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43770",
    "user": "@fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_043771.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-08-28T02:33:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43771",
    "user": "@tscrim"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_043772.json:
```json
{
    "body": "Hey Frederic,\n\nThis was never deprecated, so we (unfortunately) cannot simply remove it. Instead we need to set a `deprecated_function_alias`.\n\nBest,\n\nTravis",
    "created_at": "2013-08-28T02:33:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43772",
    "user": "@tscrim"
}
```

Hey Frederic,

This was never deprecated, so we (unfortunately) cannot simply remove it. Instead we need to set a `deprecated_function_alias`.

Best,

Travis



---

archive/issue_comments_043773.json:
```json
{
    "body": "ok, done",
    "created_at": "2013-08-28T06:49:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43773",
    "user": "@fchapoton"
}
```

ok, done



---

archive/issue_comments_043774.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-08-28T06:49:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43774",
    "user": "@fchapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_043775.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-08-28T07:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43775",
    "user": "@fchapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_043776.json:
```json
{
    "body": "this does not work. working now on the problem",
    "created_at": "2013-08-28T07:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43776",
    "user": "@fchapoton"
}
```

this does not work. working now on the problem



---

archive/issue_comments_043777.json:
```json
{
    "body": "well, it is more complicated than expected.\n\nmerten is a constant, belonging to the symbolic ring.\n\nIt is not possible to use deprecated_function_alias, because it is not a function.\n\nSo far, I have found no way to deprecate merten. I would be tempted to remove it with no deprecation, even if this is not an orthodox procedure.",
    "created_at": "2013-08-28T07:27:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43777",
    "user": "@fchapoton"
}
```

well, it is more complicated than expected.

merten is a constant, belonging to the symbolic ring.

It is not possible to use deprecated_function_alias, because it is not a function.

So far, I have found no way to deprecate merten. I would be tempted to remove it with no deprecation, even if this is not an orthodox procedure.



---

archive/issue_comments_043778.json:
```json
{
    "body": "Hmmm...I think you're right; it's best to simply remove it. I don't think changing the API by turning it into a function with a deprecation for that is a good idea as well.",
    "created_at": "2013-08-28T16:40:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43778",
    "user": "@tscrim"
}
```

Hmmm...I think you're right; it's best to simply remove it. I don't think changing the API by turning it into a function with a deprecation for that is a good idea as well.



---

archive/issue_comments_043779.json:
```json
{
    "body": "Attachment [trac5608.patch](tarball://root/attachments/some-uuid/ticket5608/trac5608.patch) by @fchapoton created at 2013-08-28 16:50:56\n\nok, back to the original version of the patch",
    "created_at": "2013-08-28T16:50:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43779",
    "user": "@fchapoton"
}
```

Attachment [trac5608.patch](tarball://root/attachments/some-uuid/ticket5608/trac5608.patch) by @fchapoton created at 2013-08-28 16:50:56

ok, back to the original version of the patch



---

archive/issue_comments_043780.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-08-28T16:50:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43780",
    "user": "@fchapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_043781.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-08-28T17:00:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43781",
    "user": "@tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_043782.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-09-02T10:21:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43782",
    "user": "@jdemeyer"
}
```

Resolution: fixed
