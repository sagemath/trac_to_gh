# Issue 9207: random_element does not work for BooleanPolynomialRing of degree 1 or 2

archive/issues_009207.json:
```json
{
    "body": "Assignee: @malb\n\nrandom_element does not work for BooleanPolynomialRing of degree 1 or 2; for example,\n\n\n```\nsage: n = 2\nsage: S = BooleanPolynomialRing(n,'y','lex')\nsage: S.random_element()\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9207\n\n",
    "created_at": "2010-06-10T20:03:45Z",
    "labels": [
        "component: commutative algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "random_element does not work for BooleanPolynomialRing of degree 1 or 2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9207",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```
Assignee: @malb

random_element does not work for BooleanPolynomialRing of degree 1 or 2; for example,


```
sage: n = 2
sage: S = BooleanPolynomialRing(n,'y','lex')
sage: S.random_element()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
```


Issue created by migration from https://trac.sagemath.org/ticket/9207





---

archive/issue_comments_086034.json:
```json
{
    "body": "Attachment [trac_9207.patch](tarball://root/attachments/some-uuid/ticket9207/trac_9207.patch) by @malb created at 2010-07-12 15:53:34",
    "created_at": "2010-07-12T15:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9207#issuecomment-86034",
    "user": "https://github.com/malb"
}
```

Attachment [trac_9207.patch](tarball://root/attachments/some-uuid/ticket9207/trac_9207.patch) by @malb created at 2010-07-12 15:53:34



---

archive/issue_comments_086035.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-12T15:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9207#issuecomment-86035",
    "user": "https://github.com/malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_086036.json:
```json
{
    "body": "\n```\nThis patch fixed the reported problem.\n\nsage-4.4.4.1 with this patch pass all tests\nwhen I do 'make testlong'\n\nThe patch code looks reasonable.\n\nPositive review.\n```\n",
    "created_at": "2010-07-13T14:13:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9207#issuecomment-86036",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```


```
This patch fixed the reported problem.

sage-4.4.4.1 with this patch pass all tests
when I do 'make testlong'

The patch code looks reasonable.

Positive review.
```




---

archive/issue_comments_086037.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-13T14:13:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9207#issuecomment-86037",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086038.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T01:45:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9207#issuecomment-86038",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_022676.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-21T01:45:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9207",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9207#event-22676"
}
```



---

archive/issue_events_022677.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-07-21T06:40:15Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9207",
    "milestone": "sage-4.5.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9207#event-22677"
}
```
