# Issue 9302: Heegner point_exact is wrong for 5077a with discriminant -7

archive/issues_009302.json:
```json
{
    "body": "Assignee: cremona\n\n\n```\nsage: E = EllipticCurve('5077a')\nsage: E.heegner_discriminants(100)\n[-3, -4, -7, -19, -40, -47, -55, -59, -71, -79, -84, -88]\nsage: P = E.heegner_point(-7)\nsage: P.numerical_approx(prec=100)\n(0 : 1.0000000000000000000000000000 : 0)\nsage: P.point_exact(prec=100)\n(0 : 2 : 1)\n```\n\n\nBut point_exact should be the point at infinity. \n\nIssue created by migration from https://trac.sagemath.org/ticket/9302\n\n",
    "created_at": "2010-06-22T00:28:56Z",
    "labels": [
        "elliptic curves",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Heegner point_exact is wrong for 5077a with discriminant -7",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9302",
    "user": "was"
}
```
Assignee: cremona


```
sage: E = EllipticCurve('5077a')
sage: E.heegner_discriminants(100)
[-3, -4, -7, -19, -40, -47, -55, -59, -71, -79, -84, -88]
sage: P = E.heegner_point(-7)
sage: P.numerical_approx(prec=100)
(0 : 1.0000000000000000000000000000 : 0)
sage: P.point_exact(prec=100)
(0 : 2 : 1)
```


But point_exact should be the point at infinity. 

Issue created by migration from https://trac.sagemath.org/ticket/9302





---

archive/issue_comments_087623.json:
```json
{
    "body": "Attachment [9302-heegner.patch](tarball://root/attachments/some-uuid/ticket9302/9302-heegner.patch) by robertwb created at 2010-06-23 04:01:50",
    "created_at": "2010-06-23T04:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9302#issuecomment-87623",
    "user": "robertwb"
}
```

Attachment [9302-heegner.patch](tarball://root/attachments/some-uuid/ticket9302/9302-heegner.patch) by robertwb created at 2010-06-23 04:01:50



---

archive/issue_comments_087624.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-23T04:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9302#issuecomment-87624",
    "user": "robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087625.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-23T04:05:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9302#issuecomment-87625",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087626.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T07:13:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9302#issuecomment-87626",
    "user": "mpatel"
}
```

Resolution: fixed
