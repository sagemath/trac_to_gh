# Issue 3138: [with patch, needs review] Singular multivariate polynomial ring has redundant _repr_ method

archive/issues_003138.json:
```json
{
    "body": "Assignee: broune\n\nMPolynomialRing_libsingular in sage/rings/polynomial/multi_polynomial_libsingular.pyx defines a _repr_ method which does the same thing as the _repr_ method that it inherits from MPolynomialRing_generic in sage/rings/polynomial/multi_polynomial_ring_generic.pyx\n\nThus the _repr_ method is redundant and should be removed.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3138\n\n",
    "created_at": "2008-05-09T00:52:47Z",
    "labels": [
        "algebra",
        "trivial",
        "enhancement"
    ],
    "title": "[with patch, needs review] Singular multivariate polynomial ring has redundant _repr_ method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3138",
    "user": "broune"
}
```
Assignee: broune

MPolynomialRing_libsingular in sage/rings/polynomial/multi_polynomial_libsingular.pyx defines a _repr_ method which does the same thing as the _repr_ method that it inherits from MPolynomialRing_generic in sage/rings/polynomial/multi_polynomial_ring_generic.pyx

Thus the _repr_ method is redundant and should be removed.


Issue created by migration from https://trac.sagemath.org/ticket/3138





---

archive/issue_comments_021790.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-05-09T01:06:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3138#issuecomment-21790",
    "user": "broune"
}
```

Attachment



---

archive/issue_comments_021791.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-09T01:06:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3138#issuecomment-21791",
    "user": "broune"
}
```

Changing status from new to assigned.



---

archive/issue_comments_021792.json:
```json
{
    "body": "Yep, I wrote the libsingular version before the generic one. Positive review.",
    "created_at": "2008-05-09T08:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3138#issuecomment-21792",
    "user": "malb"
}
```

Yep, I wrote the libsingular version before the generic one. Positive review.



---

archive/issue_comments_021793.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha0",
    "created_at": "2008-05-09T13:11:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3138#issuecomment-21793",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.2.alpha0



---

archive/issue_comments_021794.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-09T13:11:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3138#issuecomment-21794",
    "user": "mabshoff"
}
```

Resolution: fixed
