# Issue 9930: Implement conversion from EllipticCurvePoint to PARI

archive/issues_009930.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nKeywords: elliptic curve point pari\n\nCurrently, points on elliptic curves cannot automatically be converted to PARI:\n\n\n```\nsage: E = EllipticCurve([0,0,0,3,0])\nsage: P = E.point([1,2]); P\n(1 : 2 : 1)\nsage: pari(P)\nTraceback (most recent call last):\n...\nRuntimeError: evaluating PARI string\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9931\n\n",
    "created_at": "2010-09-17T09:50:24Z",
    "labels": [
        "elliptic curves",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Implement conversion from EllipticCurvePoint to PARI",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9930",
    "user": "@jdemeyer"
}
```
Assignee: @JohnCremona

Keywords: elliptic curve point pari

Currently, points on elliptic curves cannot automatically be converted to PARI:


```
sage: E = EllipticCurve([0,0,0,3,0])
sage: P = E.point([1,2]); P
(1 : 2 : 1)
sage: pari(P)
Traceback (most recent call last):
...
RuntimeError: evaluating PARI string
```


Issue created by migration from https://trac.sagemath.org/ticket/9931





---

archive/issue_comments_098888.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-19T12:18:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9930#issuecomment-98888",
    "user": "@jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098889.json:
```json
{
    "body": "Attachment [9931_ell_point_pari.patch](tarball://root/attachments/some-uuid/ticket9931/9931_ell_point_pari.patch) by @jdemeyer created at 2010-09-19 12:18:04",
    "created_at": "2010-09-19T12:18:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9930#issuecomment-98889",
    "user": "@jdemeyer"
}
```

Attachment [9931_ell_point_pari.patch](tarball://root/attachments/some-uuid/ticket9931/9931_ell_point_pari.patch) by @jdemeyer created at 2010-09-19 12:18:04



---

archive/issue_comments_098890.json:
```json
{
    "body": "Note that the patch removes `_pari_` for elliptic curves over p-adic and finite fields.  This is justified because the general case covers these special cases (and doctests have been copied to check that).",
    "created_at": "2010-09-19T14:07:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9930#issuecomment-98890",
    "user": "@jdemeyer"
}
```

Note that the patch removes `_pari_` for elliptic curves over p-adic and finite fields.  This is justified because the general case covers these special cases (and doctests have been copied to check that).



---

archive/issue_comments_098891.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-23T11:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9930#issuecomment-98891",
    "user": "@loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098892.json:
```json
{
    "body": "Looks fine to me.",
    "created_at": "2010-09-23T11:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9930#issuecomment-98892",
    "user": "@loefflerd"
}
```

Looks fine to me.



---

archive/issue_comments_098893.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T04:24:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9930#issuecomment-98893",
    "user": "@qed777"
}
```

Resolution: fixed
