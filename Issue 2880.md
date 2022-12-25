# Issue 2880: Special code for elliptic curve cardinality for j=0 and j=1728

archive/issues_002880.json:
```json
{
    "body": "Assignee: @williamstein\n\nWhen the new code for point counting on elliptic curves over arbitrary finite fields was implemented, I left handling the special cases j=0 and j=1728 for a rainy day.  These cases were handled in not too bad a way, but as there are special formulas for these cases it was always going to be a good idea to implement them.\n\nNot having any reference which does everything needed here (especially for the really exceptional cases where the characteristic is 2 or 3 and j=0=1728) I worked it all out from scratch, and here is the result.\n\nThere are copious comments and doctests.  I will write up the full justification in due course.  In the meantime I hope we can merge this patch (based on 3.0.alpha1) quite soon!\n\nIssue created by migration from https://trac.sagemath.org/ticket/2880\n\n",
    "created_at": "2008-04-11T20:07:20Z",
    "labels": [
        "component: algebraic geometry",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Special code for elliptic curve cardinality for j=0 and j=1728",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2880",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @williamstein

When the new code for point counting on elliptic curves over arbitrary finite fields was implemented, I left handling the special cases j=0 and j=1728 for a rainy day.  These cases were handled in not too bad a way, but as there are special formulas for these cases it was always going to be a good idea to implement them.

Not having any reference which does everything needed here (especially for the really exceptional cases where the characteristic is 2 or 3 and j=0=1728) I worked it all out from scratch, and here is the result.

There are copious comments and doctests.  I will write up the full justification in due course.  In the meantime I hope we can merge this patch (based on 3.0.alpha1) quite soon!

Issue created by migration from https://trac.sagemath.org/ticket/2880





---

archive/issue_comments_019770.json:
```json
{
    "body": "Attachment [9384.patch](tarball://root/attachments/some-uuid/ticket2880/9384.patch) by @JohnCremona created at 2008-04-11 20:07:37",
    "created_at": "2008-04-11T20:07:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2880#issuecomment-19770",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [9384.patch](tarball://root/attachments/some-uuid/ticket2880/9384.patch) by @JohnCremona created at 2008-04-11 20:07:37



---

archive/issue_comments_019771.json:
```json
{
    "body": "Changing keywords from \"\" to \"elliptic curves\".",
    "created_at": "2008-04-11T20:10:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2880#issuecomment-19771",
    "user": "https://github.com/JohnCremona"
}
```

Changing keywords from "" to "elliptic curves".



---

archive/issue_comments_019772.json:
```json
{
    "body": "Attachment [9467.patch](tarball://root/attachments/some-uuid/ticket2880/9467.patch) by @JohnCremona created at 2008-04-11 21:17:53\n\nreplaces previous patch; applies to 3.0.alpha3",
    "created_at": "2008-04-11T21:17:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2880#issuecomment-19772",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [9467.patch](tarball://root/attachments/some-uuid/ticket2880/9467.patch) by @JohnCremona created at 2008-04-11 21:17:53

replaces previous patch; applies to 3.0.alpha3



---

archive/issue_comments_019773.json:
```json
{
    "body": "The original patch was based on 3.0.alpha1 and did not apply to alpha3.  The new one does apply ok to alpha3.",
    "created_at": "2008-04-11T21:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2880#issuecomment-19773",
    "user": "https://github.com/JohnCremona"
}
```

The original patch was based on 3.0.alpha1 and did not apply to alpha3.  The new one does apply ok to alpha3.



---

archive/issue_comments_019774.json:
```json
{
    "body": "Attachment [9468.patch](tarball://root/attachments/some-uuid/ticket2880/9468.patch) by @JohnCremona created at 2008-04-12 19:12:07\n\nApply after preceding main patch",
    "created_at": "2008-04-12T19:12:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2880#issuecomment-19774",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [9468.patch](tarball://root/attachments/some-uuid/ticket2880/9468.patch) by @JohnCremona created at 2008-04-12 19:12:07

Apply after preceding main patch



---

archive/issue_comments_019775.json:
```json
{
    "body": "Two small changes to be applied after the main patch:\n\n* In abelian_group() when j=0 or 1728 call cardinality() first, now that it is very fast, as that speeds up the group computation\n\n* In abelian_group(), a small adjustment to speed up the linear_relation() finding for the second generator.",
    "created_at": "2008-04-12T19:12:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2880#issuecomment-19775",
    "user": "https://github.com/JohnCremona"
}
```

Two small changes to be applied after the main patch:

* In abelian_group() when j=0 or 1728 call cardinality() first, now that it is very fast, as that speeds up the group computation

* In abelian_group(), a small adjustment to speed up the linear_relation() finding for the second generator.



---

archive/issue_comments_019776.json:
```json
{
    "body": "Patches look good.",
    "created_at": "2008-04-13T15:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2880#issuecomment-19776",
    "user": "https://github.com/aghitza"
}
```

Patches look good.



---

archive/issue_comments_019777.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-13T16:03:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2880#issuecomment-19777",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019778.json:
```json
{
    "body": "Merged 9467.patch and 9468.patch in Sage 3.0.alpha5",
    "created_at": "2008-04-13T16:03:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2880#issuecomment-19778",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 9467.patch and 9468.patch in Sage 3.0.alpha5



---

archive/issue_comments_019779.json:
```json
{
    "body": "Replying to [comment:5 AlexGhitza]:\n> Patches look good.\nThanks!  and sorry for the factor_integer() problem which these caused.  John",
    "created_at": "2008-04-14T13:25:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2880#issuecomment-19779",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:5 AlexGhitza]:
> Patches look good.
Thanks!  and sorry for the factor_integer() problem which these caused.  John
