# Issue 8717: Precision problem in E2 for Tate Curve

archive/issues_008717.json:
```json
{
    "body": "Assignee: AlexGhitza\n\n\n```\nsage: T = EllipticCurve('14').tate_curve(7)\nsage: T.E2(30)\n2 + 4*7 + 7^2 + 3*7^3 + 6*7^4 + 5*7^5 + 2*7^6 + 7^7 + 5*7^8 + 6*7^9 + 5*7^10 + 2*7^11 + 6*7^12 + 4*7^13 + 3*7^15 + 5*7^16 + 4*7^17 + 4*7^18 + O(7^20)\nsage: T.E2(30)\n2 + 4*7 + 7^2 + 3*7^3 + 6*7^4 + 5*7^5 + 2*7^6 + 7^7 + 5*7^8 + 6*7^9 + 5*7^10 + 2*7^11 + 6*7^12 + 4*7^13 + 3*7^15 + 5*7^16 + 4*7^17 + 4*7^18 + 2*7^20 + 7^21 + 5*7^22 + 4*7^23 + 4*7^24 + 3*7^25 + 6*7^26 + 3*7^27 + 6*7^28 + O(7^30)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8717\n\n",
    "created_at": "2010-04-19T18:28:37Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "Precision problem in E2 for Tate Curve",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8717",
    "user": "roed"
}
```
Assignee: AlexGhitza


```
sage: T = EllipticCurve('14').tate_curve(7)
sage: T.E2(30)
2 + 4*7 + 7^2 + 3*7^3 + 6*7^4 + 5*7^5 + 2*7^6 + 7^7 + 5*7^8 + 6*7^9 + 5*7^10 + 2*7^11 + 6*7^12 + 4*7^13 + 3*7^15 + 5*7^16 + 4*7^17 + 4*7^18 + O(7^20)
sage: T.E2(30)
2 + 4*7 + 7^2 + 3*7^3 + 6*7^4 + 5*7^5 + 2*7^6 + 7^7 + 5*7^8 + 6*7^9 + 5*7^10 + 2*7^11 + 6*7^12 + 4*7^13 + 3*7^15 + 5*7^16 + 4*7^17 + 4*7^18 + 2*7^20 + 7^21 + 5*7^22 + 4*7^23 + 4*7^24 + 3*7^25 + 6*7^26 + 3*7^27 + 6*7^28 + O(7^30)
```


Issue created by migration from https://trac.sagemath.org/ticket/8717





---

archive/issue_comments_079561.json:
```json
{
    "body": "Attachment [ell_tate.patch](tarball://root/attachments/some-uuid/ticket8717/ell_tate.patch) by roed created at 2010-04-19 18:29:21",
    "created_at": "2010-04-19T18:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8717#issuecomment-79561",
    "user": "roed"
}
```

Attachment [ell_tate.patch](tarball://root/attachments/some-uuid/ticket8717/ell_tate.patch) by roed created at 2010-04-19 18:29:21



---

archive/issue_comments_079562.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-19T18:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8717#issuecomment-79562",
    "user": "roed"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079563.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-05-18T13:40:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8717#issuecomment-79563",
    "user": "AlexGhitza"
}
```

Looks good to me.



---

archive/issue_comments_079564.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-18T13:40:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8717#issuecomment-79564",
    "user": "AlexGhitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079565.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T08:22:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8717#issuecomment-79565",
    "user": "mhansen"
}
```

Resolution: fixed
