# Issue 8248: Small improvement in checking for elliptic curve isogenies

archive/issues_008248.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nCC:  @categorie\n\nKeywords: isogenies\n\nWhen an isogeny is constructed from a kernel polynomial, by default (unless check=False) it is checked whether the given kernel polynomial divides the appropriate division polynomial.  This is expensive when the degree is large (e.g. 163!).\n\nWe provide a small patch which does this checking more efficiently.\n\nThe example in the patch which now takes 20s, used to take many minutes.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8248\n\n",
    "created_at": "2010-02-12T11:00:54Z",
    "labels": [
        "component: elliptic curves",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "Small improvement in checking for elliptic curve isogenies",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8248",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @JohnCremona

CC:  @categorie

Keywords: isogenies

When an isogeny is constructed from a kernel polynomial, by default (unless check=False) it is checked whether the given kernel polynomial divides the appropriate division polynomial.  This is expensive when the degree is large (e.g. 163!).

We provide a small patch which does this checking more efficiently.

The example in the patch which now takes 20s, used to take many minutes.

Issue created by migration from https://trac.sagemath.org/ticket/8248





---

archive/issue_comments_072829.json:
```json
{
    "body": "Attachment [trac_8248-isogeny.patch](tarball://root/attachments/some-uuid/ticket8248/trac_8248-isogeny.patch) by @JohnCremona created at 2010-02-12 11:04:19\n\nApplies to 4.3.2",
    "created_at": "2010-02-12T11:04:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8248#issuecomment-72829",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_8248-isogeny.patch](tarball://root/attachments/some-uuid/ticket8248/trac_8248-isogeny.patch) by @JohnCremona created at 2010-02-12 11:04:19

Applies to 4.3.2



---

archive/issue_comments_072830.json:
```json
{
    "body": "Applies fine to 4.3.3.aplha0.\nAll tests pass. (execpt heegner.py, which has nothing to do with this patch).\n\nThanks, John, for this improvement.\n\nChris.",
    "created_at": "2010-02-15T15:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8248#issuecomment-72830",
    "user": "https://github.com/categorie"
}
```

Applies fine to 4.3.3.aplha0.
All tests pass. (execpt heegner.py, which has nothing to do with this patch).

Thanks, John, for this improvement.

Chris.



---

archive/issue_comments_072831.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-15T15:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8248#issuecomment-72831",
    "user": "https://github.com/categorie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072832.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-15T15:10:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8248#issuecomment-72832",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008449.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-02-17T00:12:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8248",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8248#event-8449"
}
```



---

archive/issue_comments_072833.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-17T00:12:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8248#issuecomment-72833",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
