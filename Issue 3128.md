# Issue 3128: PolynomialRing's behaviour does not match docstring

archive/issues_003128.json:
```json
{
    "body": "Assignee: tbd\n\nThe docstring for the function PolynomialRing states\n\n```\n    OUTPUT:\n        PolynomialRing(base_ring, name, sparse=False) returns a univariate\n        polynomial ring; all other input formats return a multivariate\n        polynomial ring.\n```\nwhich is not what PolynomialRing actually does, since\n\n```\nsage: PolynomialRing(QQ, names=['x'])\nUnivariate Polynomial Ring in x over Rational Field\n```\nEither PolynomialRing has a bug or the docstring should be corrected.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3128\n\n",
    "created_at": "2008-05-07T22:31:00Z",
    "labels": [
        "component: algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "PolynomialRing's behaviour does not match docstring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3128",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```
Assignee: tbd

The docstring for the function PolynomialRing states

```
    OUTPUT:
        PolynomialRing(base_ring, name, sparse=False) returns a univariate
        polynomial ring; all other input formats return a multivariate
        polynomial ring.
```
which is not what PolynomialRing actually does, since

```
sage: PolynomialRing(QQ, names=['x'])
Univariate Polynomial Ring in x over Rational Field
```
Either PolynomialRing has a bug or the docstring should be corrected.

Issue created by migration from https://trac.sagemath.org/ticket/3128





---

archive/issue_comments_021625.json:
```json
{
    "body": "To be more precise, the problem is that the docstring of PolynomialRing says there is only one way to get a univariate polynomial ring, but in fact PolynomialRing tries to be clever and returns univariate rings in other cases too.",
    "created_at": "2008-05-12T10:14:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3128#issuecomment-21625",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```

To be more precise, the problem is that the docstring of PolynomialRing says there is only one way to get a univariate polynomial ring, but in fact PolynomialRing tries to be clever and returns univariate rings in other cases too.



---

archive/issue_comments_021626.json:
```json
{
    "body": "Attachment [PolynomialRingDoc.patch](tarball://root/attachments/some-uuid/ticket3128/PolynomialRingDoc.patch) by @simon-king-jena created at 2009-01-22 06:16:49\n\nFixing wrong docstring statement and adding more doctests",
    "created_at": "2009-01-22T06:16:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3128#issuecomment-21626",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [PolynomialRingDoc.patch](tarball://root/attachments/some-uuid/ticket3128/PolynomialRingDoc.patch) by @simon-king-jena created at 2009-01-22 06:16:49

Fixing wrong docstring statement and adding more doctests



---

archive/issue_comments_021627.json:
```json
{
    "body": "I think the new doc string covers all use cases. It also provides the corner cases (zero or one variables) as doc tests.",
    "created_at": "2009-01-22T06:23:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3128#issuecomment-21627",
    "user": "https://github.com/simon-king-jena"
}
```

I think the new doc string covers all use cases. It also provides the corner cases (zero or one variables) as doc tests.



---

archive/issue_comments_021628.json:
```json
{
    "body": "```\nNote that a multivariate polynomial ring is returned even if the \ngiven number of variables is zero or one. \n```\n\nshould be replaced with\n\n```\nNote that a multivariate polynomial ring is returned when an explicit number is given.\n```",
    "created_at": "2009-01-24T09:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3128#issuecomment-21628",
    "user": "https://github.com/malb"
}
```

```
Note that a multivariate polynomial ring is returned even if the 
given number of variables is zero or one. 
```

should be replaced with

```
Note that a multivariate polynomial ring is returned when an explicit number is given.
```



---

archive/issue_comments_021629.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-19T19:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3128#issuecomment-21629",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_021630.json:
```json
{
    "body": "Attachment [trac_3128.patch](tarball://root/attachments/some-uuid/ticket3128/trac_3128.patch) by @mwhansen created at 2009-10-19 19:12:02\n\nI rebased the patch and changed the docstring as per malb's suggestion.",
    "created_at": "2009-10-19T19:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3128#issuecomment-21630",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3128.patch](tarball://root/attachments/some-uuid/ticket3128/trac_3128.patch) by @mwhansen created at 2009-10-19 19:12:02

I rebased the patch and changed the docstring as per malb's suggestion.



---

archive/issue_comments_021631.json:
```json
{
    "body": "I think that this can go in.",
    "created_at": "2009-11-05T02:28:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3128#issuecomment-21631",
    "user": "https://github.com/mwhansen"
}
```

I think that this can go in.



---

archive/issue_comments_021632.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-05T02:28:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3128#issuecomment-21632",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_021633.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-05T02:29:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3128#issuecomment-21633",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_007064.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-05T02:29:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3128",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3128#event-7064"
}
```
