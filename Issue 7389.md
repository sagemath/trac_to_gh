# Issue 7389: Fallback _point_morphism_class() has wrong signature

archive/issues_007389.json:
```json
{
    "body": "Assignee: @aghitza\n\nThe default `Scheme._point_morphism_class()` has a different signature than the versions in the subclasses of Scheme, causing a `TypeError` when it is called instead of the intended `NotImplementedError`.\n\nSmall nonsensical example to trigger it in sage 4.2:\n\n\n```\nsage: S = Spec(ZZ)\nsage: f = S.identity_morphism()\nsage: from sage.schemes.generic.glue import GluedScheme\nsage: T = GluedScheme(f,f)\nsage: S.hom([1],T)\nTypeError: _point_morphism_class() takes exactly 1 non-keyword argument (3 given)\n```\n\n\nThe attached patch should fix it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7389\n\n",
    "created_at": "2009-11-04T19:45:30Z",
    "labels": [
        "component: algebraic geometry",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Fallback _point_morphism_class() has wrong signature",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7389",
    "user": "https://github.com/wjp"
}
```
Assignee: @aghitza

The default `Scheme._point_morphism_class()` has a different signature than the versions in the subclasses of Scheme, causing a `TypeError` when it is called instead of the intended `NotImplementedError`.

Small nonsensical example to trigger it in sage 4.2:


```
sage: S = Spec(ZZ)
sage: f = S.identity_morphism()
sage: from sage.schemes.generic.glue import GluedScheme
sage: T = GluedScheme(f,f)
sage: S.hom([1],T)
TypeError: _point_morphism_class() takes exactly 1 non-keyword argument (3 given)
```


The attached patch should fix it.

Issue created by migration from https://trac.sagemath.org/ticket/7389





---

archive/issue_comments_062023.json:
```json
{
    "body": "Attachment [trac_7389-morphism_TypeError.patch](tarball://root/attachments/some-uuid/ticket7389/trac_7389-morphism_TypeError.patch) by @wjp created at 2009-11-04 19:47:37",
    "created_at": "2009-11-04T19:47:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7389#issuecomment-62023",
    "user": "https://github.com/wjp"
}
```

Attachment [trac_7389-morphism_TypeError.patch](tarball://root/attachments/some-uuid/ticket7389/trac_7389-morphism_TypeError.patch) by @wjp created at 2009-11-04 19:47:37



---

archive/issue_comments_062024.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-04T19:48:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7389#issuecomment-62024",
    "user": "https://github.com/wjp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062025.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-15T10:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7389#issuecomment-62025",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_062026.json:
```json
{
    "body": "Please add a doctest that illustrates the problem being fixed (so that if someone messes this up again we can catch it automatically).  Even what you call the \"small nonsensical example\" would do; of course if you can come up with a small sensical one, that would be even better :).",
    "created_at": "2009-11-15T10:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7389#issuecomment-62026",
    "user": "https://github.com/aghitza"
}
```

Please add a doctest that illustrates the problem being fixed (so that if someone messes this up again we can catch it automatically).  Even what you call the "small nonsensical example" would do; of course if you can come up with a small sensical one, that would be even better :).



---

archive/issue_comments_062027.json:
```json
{
    "body": "apply after the previous patch",
    "created_at": "2010-01-01T23:25:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7389#issuecomment-62027",
    "user": "https://github.com/aghitza"
}
```

apply after the previous patch



---

archive/issue_comments_062028.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-01T23:36:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7389#issuecomment-62028",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062029.json:
```json
{
    "body": "Attachment [trac_7389-doctest.patch](tarball://root/attachments/some-uuid/ticket7389/trac_7389-doctest.patch) by @aghitza created at 2010-01-01 23:36:42\n\nOK, I've put up a patch with the doctest given in the description of this ticket.\n\nI'm happy with Willem's patch, now if someone can look at mine we're set.",
    "created_at": "2010-01-01T23:36:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7389#issuecomment-62029",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_7389-doctest.patch](tarball://root/attachments/some-uuid/ticket7389/trac_7389-doctest.patch) by @aghitza created at 2010-01-01 23:36:42

OK, I've put up a patch with the doctest given in the description of this ticket.

I'm happy with Willem's patch, now if someone can look at mine we're set.



---

archive/issue_comments_062030.json:
```json
{
    "body": "Willem, could you review my patch here?",
    "created_at": "2010-01-20T09:48:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7389#issuecomment-62030",
    "user": "https://github.com/aghitza"
}
```

Willem, could you review my patch here?



---

archive/issue_comments_062031.json:
```json
{
    "body": "Sorry, I completely missed the trac email from your previous comment. Thanks for the review; your doctest patch looks good.",
    "created_at": "2010-01-20T22:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7389#issuecomment-62031",
    "user": "https://github.com/wjp"
}
```

Sorry, I completely missed the trac email from your previous comment. Thanks for the review; your doctest patch looks good.



---

archive/issue_comments_062032.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T22:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7389#issuecomment-62032",
    "user": "https://github.com/wjp"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062033.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-22T18:02:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7389#issuecomment-62033",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_007614.json:
```json
{
    "actor": "mvngu",
    "created_at": "2010-01-22T18:02:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7389",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7389#event-7614"
}
```
