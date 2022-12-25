# Issue 6120: [with patch, positive review] P(0).total_degree() should return -1 for multivariate polynomial rings

archive/issues_006120.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @JohnCremona simonking\n\nbut it returns `0` now.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6120\n\n",
    "closed_at": "2009-05-31T23:57:29Z",
    "created_at": "2009-05-22T10:43:21Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "[with patch, positive review] P(0).total_degree() should return -1 for multivariate polynomial rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6120",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  @JohnCremona simonking

but it returns `0` now.

Issue created by migration from https://trac.sagemath.org/ticket/6120





---

archive/issue_comments_048814.json:
```json
{
    "body": "Attachment [mpoly_deg_0.patch](tarball://root/attachments/some-uuid/ticket6120/mpoly_deg_0.patch) by @malb created at 2009-05-22 11:06:08",
    "created_at": "2009-05-22T11:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6120#issuecomment-48814",
    "user": "https://github.com/malb"
}
```

Attachment [mpoly_deg_0.patch](tarball://root/attachments/some-uuid/ticket6120/mpoly_deg_0.patch) by @malb created at 2009-05-22 11:06:08



---

archive/issue_comments_048815.json:
```json
{
    "body": "At the same time we *must* do the same for the degree of univariate polynomials!  there is a degree() function in rings/polynomial/polynomial_element_generic.py which currently returns -1 for deg(0), but there may be other places too -- maybe malb knows if there are others?",
    "created_at": "2009-05-22T12:17:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6120#issuecomment-48815",
    "user": "https://github.com/JohnCremona"
}
```

At the same time we *must* do the same for the degree of univariate polynomials!  there is a degree() function in rings/polynomial/polynomial_element_generic.py which currently returns -1 for deg(0), but there may be other places too -- maybe malb knows if there are others?



---

archive/issue_comments_048816.json:
```json
{
    "body": "I checked a few implementations, they all seem to agree that deg(0) == -1.",
    "created_at": "2009-05-22T13:15:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6120#issuecomment-48816",
    "user": "https://github.com/malb"
}
```

I checked a few implementations, they all seem to agree that deg(0) == -1.



---

archive/issue_comments_048817.json:
```json
{
    "body": "Looks good, applies (with some fuzz) to 4.0.rc2, and passes doctests in sage/rings/polynomial.",
    "created_at": "2009-05-30T08:46:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6120#issuecomment-48817",
    "user": "https://github.com/aghitza"
}
```

Looks good, applies (with some fuzz) to 4.0.rc2, and passes doctests in sage/rings/polynomial.



---

archive/issue_comments_048818.json:
```json
{
    "body": "Merged in 4.0.1.alpha0.",
    "created_at": "2009-05-31T23:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6120#issuecomment-48818",
    "user": "https://github.com/mwhansen"
}
```

Merged in 4.0.1.alpha0.



---

archive/issue_comments_048819.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-31T23:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6120#issuecomment-48819",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_014414.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-05-31T23:57:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6120",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6120#event-14414"
}
```
