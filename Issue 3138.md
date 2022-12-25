# Issue 3138: [with patch, needs review] Singular multivariate polynomial ring has redundant _repr_ method

archive/issues_003138.json:
```json
{
    "body": "Assignee: broune\n\nMPolynomialRing_libsingular in sage/rings/polynomial/multi_polynomial_libsingular.pyx defines a _repr_ method which does the same thing as the _repr_ method that it inherits from MPolynomialRing_generic in sage/rings/polynomial/multi_polynomial_ring_generic.pyx\n\nThus the _repr_ method is redundant and should be removed.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3138\n\n",
    "created_at": "2008-05-09T00:52:47Z",
    "labels": [
        "component: algebra",
        "trivial"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "[with patch, needs review] Singular multivariate polynomial ring has redundant _repr_ method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3138",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```
Assignee: broune

MPolynomialRing_libsingular in sage/rings/polynomial/multi_polynomial_libsingular.pyx defines a _repr_ method which does the same thing as the _repr_ method that it inherits from MPolynomialRing_generic in sage/rings/polynomial/multi_polynomial_ring_generic.pyx

Thus the _repr_ method is redundant and should be removed.


Issue created by migration from https://trac.sagemath.org/ticket/3138





---

archive/issue_comments_021744.json:
```json
{
    "body": "Attachment [no_singular_repr.changeset](tarball://root/attachments/some-uuid/ticket3138/no_singular_repr.changeset) by broune created at 2008-05-09 01:06:22",
    "created_at": "2008-05-09T01:06:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3138#issuecomment-21744",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```

Attachment [no_singular_repr.changeset](tarball://root/attachments/some-uuid/ticket3138/no_singular_repr.changeset) by broune created at 2008-05-09 01:06:22



---

archive/issue_comments_021745.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-09T01:06:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3138#issuecomment-21745",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```

Changing status from new to assigned.



---

archive/issue_comments_021746.json:
```json
{
    "body": "Yep, I wrote the libsingular version before the generic one. Positive review.",
    "created_at": "2008-05-09T08:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3138#issuecomment-21746",
    "user": "https://github.com/malb"
}
```

Yep, I wrote the libsingular version before the generic one. Positive review.



---

archive/issue_comments_021747.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha0",
    "created_at": "2008-05-09T13:11:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3138#issuecomment-21747",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.2.alpha0



---

archive/issue_comments_021748.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-09T13:11:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3138#issuecomment-21748",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_007094.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-09T13:11:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3138",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3138#event-7094"
}
```
