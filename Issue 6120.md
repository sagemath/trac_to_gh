# Issue 6120: [with patch, needs review] P(0).total_degree() should return -1 for multivariate polynomial rings

archive/issues_006120.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @JohnCremona simonking\n\nbut it returns `0` now.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6120\n\n",
    "created_at": "2009-05-22T10:43:21Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "[with patch, needs review] P(0).total_degree() should return -1 for multivariate polynomial rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6120",
    "user": "@malb"
}
```
Assignee: @malb

CC:  @JohnCremona simonking

but it returns `0` now.

Issue created by migration from https://trac.sagemath.org/ticket/6120





---

archive/issue_comments_048909.json:
```json
{
    "body": "Attachment [mpoly_deg_0.patch](tarball://root/attachments/some-uuid/ticket6120/mpoly_deg_0.patch) by @malb created at 2009-05-22 11:06:08",
    "created_at": "2009-05-22T11:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6120#issuecomment-48909",
    "user": "@malb"
}
```

Attachment [mpoly_deg_0.patch](tarball://root/attachments/some-uuid/ticket6120/mpoly_deg_0.patch) by @malb created at 2009-05-22 11:06:08



---

archive/issue_comments_048910.json:
```json
{
    "body": "At the same time we *must* do the same for the degree of univariate polynomials!  there is a degree() function in rings/polynomial/polynomial_element_generic.py which currently returns -1 for deg(0), but there may be other places too -- maybe malb knows if there are others?",
    "created_at": "2009-05-22T12:17:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6120#issuecomment-48910",
    "user": "@JohnCremona"
}
```

At the same time we *must* do the same for the degree of univariate polynomials!  there is a degree() function in rings/polynomial/polynomial_element_generic.py which currently returns -1 for deg(0), but there may be other places too -- maybe malb knows if there are others?



---

archive/issue_comments_048911.json:
```json
{
    "body": "I checked a few implementations, they all seem to agree that deg(0) == -1.",
    "created_at": "2009-05-22T13:15:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6120#issuecomment-48911",
    "user": "@malb"
}
```

I checked a few implementations, they all seem to agree that deg(0) == -1.



---

archive/issue_comments_048912.json:
```json
{
    "body": "Looks good, applies (with some fuzz) to 4.0.rc2, and passes doctests in sage/rings/polynomial.",
    "created_at": "2009-05-30T08:46:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6120#issuecomment-48912",
    "user": "@aghitza"
}
```

Looks good, applies (with some fuzz) to 4.0.rc2, and passes doctests in sage/rings/polynomial.



---

archive/issue_comments_048913.json:
```json
{
    "body": "Merged in 4.0.1.alpha0.",
    "created_at": "2009-05-31T23:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6120#issuecomment-48913",
    "user": "@mwhansen"
}
```

Merged in 4.0.1.alpha0.



---

archive/issue_comments_048914.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-31T23:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6120#issuecomment-48914",
    "user": "@mwhansen"
}
```

Resolution: fixed
