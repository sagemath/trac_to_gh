# Issue 7389: Fallback _point_morphism_class() has wrong signature

archive/issues_007389.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nThe default `Scheme._point_morphism_class()` has a different signature than the versions in the subclasses of Scheme, causing a `TypeError` when it is called instead of the intended `NotImplementedError`.\n\nSmall nonsensical example to trigger it in sage 4.2:\n\n\n```\nsage: S = Spec(ZZ)\nsage: f = S.identity_morphism()\nsage: from sage.schemes.generic.glue import GluedScheme\nsage: T = GluedScheme(f,f)\nsage: S.hom([1],T)\nTypeError: _point_morphism_class() takes exactly 1 non-keyword argument (3 given)\n```\n\n\nThe attached patch should fix it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7389\n\n",
    "created_at": "2009-11-04T19:45:30Z",
    "labels": [
        "algebraic geometry",
        "minor",
        "bug"
    ],
    "title": "Fallback _point_morphism_class() has wrong signature",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7389",
    "user": "wjp"
}
```
Assignee: AlexGhitza

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

archive/issue_comments_062138.json:
```json
{
    "body": "Attachment [trac_7389-morphism_TypeError.patch](tarball://root/attachments/some-uuid/ticket7389/trac_7389-morphism_TypeError.patch) by wjp created at 2009-11-04 19:47:37",
    "created_at": "2009-11-04T19:47:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7389#issuecomment-62138",
    "user": "wjp"
}
```

Attachment [trac_7389-morphism_TypeError.patch](tarball://root/attachments/some-uuid/ticket7389/trac_7389-morphism_TypeError.patch) by wjp created at 2009-11-04 19:47:37



---

archive/issue_comments_062139.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-04T19:48:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7389#issuecomment-62139",
    "user": "wjp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062140.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-15T10:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7389#issuecomment-62140",
    "user": "AlexGhitza"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_062141.json:
```json
{
    "body": "Please add a doctest that illustrates the problem being fixed (so that if someone messes this up again we can catch it automatically).  Even what you call the \"small nonsensical example\" would do; of course if you can come up with a small sensical one, that would be even better :).",
    "created_at": "2009-11-15T10:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7389#issuecomment-62141",
    "user": "AlexGhitza"
}
```

Please add a doctest that illustrates the problem being fixed (so that if someone messes this up again we can catch it automatically).  Even what you call the "small nonsensical example" would do; of course if you can come up with a small sensical one, that would be even better :).



---

archive/issue_comments_062142.json:
```json
{
    "body": "apply after the previous patch",
    "created_at": "2010-01-01T23:25:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7389#issuecomment-62142",
    "user": "AlexGhitza"
}
```

apply after the previous patch



---

archive/issue_comments_062143.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-01T23:36:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7389#issuecomment-62143",
    "user": "AlexGhitza"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062144.json:
```json
{
    "body": "Attachment [trac_7389-doctest.patch](tarball://root/attachments/some-uuid/ticket7389/trac_7389-doctest.patch) by AlexGhitza created at 2010-01-01 23:36:42\n\nOK, I've put up a patch with the doctest given in the description of this ticket.\n\nI'm happy with Willem's patch, now if someone can look at mine we're set.",
    "created_at": "2010-01-01T23:36:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7389#issuecomment-62144",
    "user": "AlexGhitza"
}
```

Attachment [trac_7389-doctest.patch](tarball://root/attachments/some-uuid/ticket7389/trac_7389-doctest.patch) by AlexGhitza created at 2010-01-01 23:36:42

OK, I've put up a patch with the doctest given in the description of this ticket.

I'm happy with Willem's patch, now if someone can look at mine we're set.



---

archive/issue_comments_062145.json:
```json
{
    "body": "Willem, could you review my patch here?",
    "created_at": "2010-01-20T09:48:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7389#issuecomment-62145",
    "user": "AlexGhitza"
}
```

Willem, could you review my patch here?



---

archive/issue_comments_062146.json:
```json
{
    "body": "Sorry, I completely missed the trac email from your previous comment. Thanks for the review; your doctest patch looks good.",
    "created_at": "2010-01-20T22:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7389#issuecomment-62146",
    "user": "wjp"
}
```

Sorry, I completely missed the trac email from your previous comment. Thanks for the review; your doctest patch looks good.



---

archive/issue_comments_062147.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T22:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7389#issuecomment-62147",
    "user": "wjp"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062148.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-22T18:02:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7389#issuecomment-62148",
    "user": "mvngu"
}
```

Resolution: fixed
