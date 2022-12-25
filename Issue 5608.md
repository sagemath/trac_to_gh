# Issue 5608: Mertens' constant is named wrongly

archive/issues_005608.json:
```json
{
    "body": "Assignee: cwitty\n\nsage.functions.constants.Merten is named wrongly, as the mathematician's name is Franz Mertens and not Merten. The class and default instance should be renamed and \"Merten constant\" and \"Merten's second theorem\" in the docstring should be fixed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5608\n\n",
    "created_at": "2009-03-25T12:56:31Z",
    "labels": [
        "component: misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.12",
    "title": "Mertens' constant is named wrongly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5608",
    "user": "https://github.com/fredrik-johansson"
}
```
Assignee: cwitty

sage.functions.constants.Merten is named wrongly, as the mathematician's name is Franz Mertens and not Merten. The class and default instance should be renamed and "Merten constant" and "Merten's second theorem" in the docstring should be fixed.

Issue created by migration from https://trac.sagemath.org/ticket/5608





---

archive/issue_comments_043683.json:
```json
{
    "body": "#6200 has a fix for this. I would also like to see the wrongly named `merten` constant deprecated, though I don't know how we can do this.",
    "created_at": "2009-06-23T22:16:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43683",
    "user": "https://github.com/burcin"
}
```

#6200 has a fix for this. I would also like to see the wrongly named `merten` constant deprecated, though I don't know how we can do this.



---

archive/issue_comments_043684.json:
```json
{
    "body": "Changing keywords from \"\" to \"documentation, typo\".",
    "created_at": "2013-08-21T16:23:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43684",
    "user": "https://github.com/fchapoton"
}
```

Changing keywords from "" to "documentation, typo".



---

archive/issue_comments_043685.json:
```json
{
    "body": "here is a patch",
    "created_at": "2013-08-21T16:23:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43685",
    "user": "https://github.com/fchapoton"
}
```

here is a patch



---

archive/issue_comments_043686.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-08-21T16:23:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43686",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_043687.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-08-28T02:33:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43687",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_043688.json:
```json
{
    "body": "Hey Frederic,\n\nThis was never deprecated, so we (unfortunately) cannot simply remove it. Instead we need to set a `deprecated_function_alias`.\n\nBest,\n\nTravis",
    "created_at": "2013-08-28T02:33:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43688",
    "user": "https://github.com/tscrim"
}
```

Hey Frederic,

This was never deprecated, so we (unfortunately) cannot simply remove it. Instead we need to set a `deprecated_function_alias`.

Best,

Travis



---

archive/issue_comments_043689.json:
```json
{
    "body": "ok, done",
    "created_at": "2013-08-28T06:49:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43689",
    "user": "https://github.com/fchapoton"
}
```

ok, done



---

archive/issue_comments_043690.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-08-28T06:49:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43690",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_043691.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-08-28T07:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43691",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_043692.json:
```json
{
    "body": "this does not work. working now on the problem",
    "created_at": "2013-08-28T07:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43692",
    "user": "https://github.com/fchapoton"
}
```

this does not work. working now on the problem



---

archive/issue_comments_043693.json:
```json
{
    "body": "well, it is more complicated than expected.\n\nmerten is a constant, belonging to the symbolic ring.\n\nIt is not possible to use deprecated_function_alias, because it is not a function.\n\nSo far, I have found no way to deprecate merten. I would be tempted to remove it with no deprecation, even if this is not an orthodox procedure.",
    "created_at": "2013-08-28T07:27:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43693",
    "user": "https://github.com/fchapoton"
}
```

well, it is more complicated than expected.

merten is a constant, belonging to the symbolic ring.

It is not possible to use deprecated_function_alias, because it is not a function.

So far, I have found no way to deprecate merten. I would be tempted to remove it with no deprecation, even if this is not an orthodox procedure.



---

archive/issue_comments_043694.json:
```json
{
    "body": "Hmmm...I think you're right; it's best to simply remove it. I don't think changing the API by turning it into a function with a deprecation for that is a good idea as well.",
    "created_at": "2013-08-28T16:40:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43694",
    "user": "https://github.com/tscrim"
}
```

Hmmm...I think you're right; it's best to simply remove it. I don't think changing the API by turning it into a function with a deprecation for that is a good idea as well.



---

archive/issue_comments_043695.json:
```json
{
    "body": "Attachment [trac5608.patch](tarball://root/attachments/some-uuid/ticket5608/trac5608.patch) by @fchapoton created at 2013-08-28 16:50:56\n\nok, back to the original version of the patch",
    "created_at": "2013-08-28T16:50:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43695",
    "user": "https://github.com/fchapoton"
}
```

Attachment [trac5608.patch](tarball://root/attachments/some-uuid/ticket5608/trac5608.patch) by @fchapoton created at 2013-08-28 16:50:56

ok, back to the original version of the patch



---

archive/issue_comments_043696.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-08-28T16:50:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43696",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_043697.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-08-28T17:00:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43697",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_043698.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-09-02T10:21:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5608#issuecomment-43698",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
