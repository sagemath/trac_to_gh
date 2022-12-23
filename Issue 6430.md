# Issue 6430: Cython problem with hashing Laurent series elements over CDF

archive/issues_006430.json:
```json
{
    "body": "Assignee: malb\n\nCC:  mhansen\n\nKeywords: hash Laurent series\n\n\n```\nsage: hash(1/CDF[['t']].gen())\n-2\nsage: hash(1/CDF[['t']].gen()^2)\n---------------------------------------------------------------------------\nSystemError                               Traceback (most recent call last)\n\n/Users/ncalexan/Documents/School/period_matrix/riemann_surface.py in <module>()\n\nSystemError: error return without exception set\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6430\n\n",
    "created_at": "2009-06-27T04:37:25Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "title": "Cython problem with hashing Laurent series elements over CDF",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6430",
    "user": "ncalexan"
}
```
Assignee: malb

CC:  mhansen

Keywords: hash Laurent series


```
sage: hash(1/CDF[['t']].gen())
-2
sage: hash(1/CDF[['t']].gen()^2)
---------------------------------------------------------------------------
SystemError                               Traceback (most recent call last)

/Users/ncalexan/Documents/School/period_matrix/riemann_surface.py in <module>()

SystemError: error return without exception set
```


Issue created by migration from https://trac.sagemath.org/ticket/6430





---

archive/issue_comments_051643.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2018-08-22T18:48:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6430#issuecomment-51643",
    "user": "chapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_051644.json:
```json
{
    "body": "works fine in 8.4.b1",
    "created_at": "2018-08-22T18:48:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6430#issuecomment-51644",
    "user": "chapoton"
}
```

works fine in 8.4.b1



---

archive/issue_comments_051645.json:
```json
{
    "body": "Confirmed.",
    "created_at": "2018-08-22T22:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6430#issuecomment-51645",
    "user": "tscrim"
}
```

Confirmed.



---

archive/issue_comments_051646.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-08-22T22:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6430#issuecomment-51646",
    "user": "tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_051647.json:
```json
{
    "body": "Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.",
    "created_at": "2019-02-26T13:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6430#issuecomment-51647",
    "user": "embray"
}
```

Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.



---

archive/issue_comments_051648.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2019-02-26T13:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6430#issuecomment-51648",
    "user": "embray"
}
```

Resolution: invalid
