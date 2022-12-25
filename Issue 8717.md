# Issue 8717: Precision problem in E2 for Tate Curve

archive/issues_008717.json:
```json
{
    "body": "Assignee: @aghitza\n\n\n```\nsage: T = EllipticCurve('14').tate_curve(7)\nsage: T.E2(30)\n2 + 4*7 + 7^2 + 3*7^3 + 6*7^4 + 5*7^5 + 2*7^6 + 7^7 + 5*7^8 + 6*7^9 + 5*7^10 + 2*7^11 + 6*7^12 + 4*7^13 + 3*7^15 + 5*7^16 + 4*7^17 + 4*7^18 + O(7^20)\nsage: T.E2(30)\n2 + 4*7 + 7^2 + 3*7^3 + 6*7^4 + 5*7^5 + 2*7^6 + 7^7 + 5*7^8 + 6*7^9 + 5*7^10 + 2*7^11 + 6*7^12 + 4*7^13 + 3*7^15 + 5*7^16 + 4*7^17 + 4*7^18 + 2*7^20 + 7^21 + 5*7^22 + 4*7^23 + 4*7^24 + 3*7^25 + 6*7^26 + 3*7^27 + 6*7^28 + O(7^30)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8717\n\n",
    "created_at": "2010-04-19T18:28:37Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Precision problem in E2 for Tate Curve",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8717",
    "user": "https://github.com/roed314"
}
```
Assignee: @aghitza


```
sage: T = EllipticCurve('14').tate_curve(7)
sage: T.E2(30)
2 + 4*7 + 7^2 + 3*7^3 + 6*7^4 + 5*7^5 + 2*7^6 + 7^7 + 5*7^8 + 6*7^9 + 5*7^10 + 2*7^11 + 6*7^12 + 4*7^13 + 3*7^15 + 5*7^16 + 4*7^17 + 4*7^18 + O(7^20)
sage: T.E2(30)
2 + 4*7 + 7^2 + 3*7^3 + 6*7^4 + 5*7^5 + 2*7^6 + 7^7 + 5*7^8 + 6*7^9 + 5*7^10 + 2*7^11 + 6*7^12 + 4*7^13 + 3*7^15 + 5*7^16 + 4*7^17 + 4*7^18 + 2*7^20 + 7^21 + 5*7^22 + 4*7^23 + 4*7^24 + 3*7^25 + 6*7^26 + 3*7^27 + 6*7^28 + O(7^30)
```


Issue created by migration from https://trac.sagemath.org/ticket/8717





---

archive/issue_comments_079431.json:
```json
{
    "body": "Attachment [ell_tate.patch](tarball://root/attachments/some-uuid/ticket8717/ell_tate.patch) by @roed314 created at 2010-04-19 18:29:21",
    "created_at": "2010-04-19T18:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8717#issuecomment-79431",
    "user": "https://github.com/roed314"
}
```

Attachment [ell_tate.patch](tarball://root/attachments/some-uuid/ticket8717/ell_tate.patch) by @roed314 created at 2010-04-19 18:29:21



---

archive/issue_comments_079432.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-19T18:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8717#issuecomment-79432",
    "user": "https://github.com/roed314"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079433.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-05-18T13:40:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8717#issuecomment-79433",
    "user": "https://github.com/aghitza"
}
```

Looks good to me.



---

archive/issue_comments_079434.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-18T13:40:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8717#issuecomment-79434",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079435.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T08:22:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8717#issuecomment-79435",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_021163.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-06T08:22:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8717",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8717#event-21163"
}
```
