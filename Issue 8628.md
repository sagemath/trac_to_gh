# Issue 8628: confusing defaults for p-adic precision types

archive/issues_008628.json:
```json
{
    "body": "Assignee: roed\n\n(sage 4.3.1)\n\nabsolute or relative is the default?\n\n\n```\nsage: R = Zp(5)\nsage: R\n5-adic Ring with capped relative precision 20\nsage: R.<a> = Zq(25)\nsage: R\nUnramified Extension of 5-adic Ring with capped absolute precision 20 in a defined by (1 + O(5^20))*x^2 + (4 + O(5^20))*x + (2 + O(5^20))\nsage: R = Zq(5)\nsage: R\n5-adic Ring with capped absolute precision 20\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8628\n\n",
    "created_at": "2010-03-30T00:50:51Z",
    "labels": [
        "padics",
        "major",
        "bug"
    ],
    "title": "confusing defaults for p-adic precision types",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8628",
    "user": "dmharvey"
}
```
Assignee: roed

(sage 4.3.1)

absolute or relative is the default?


```
sage: R = Zp(5)
sage: R
5-adic Ring with capped relative precision 20
sage: R.<a> = Zq(25)
sage: R
Unramified Extension of 5-adic Ring with capped absolute precision 20 in a defined by (1 + O(5^20))*x^2 + (4 + O(5^20))*x + (2 + O(5^20))
sage: R = Zq(5)
sage: R
5-adic Ring with capped absolute precision 20
```



Issue created by migration from https://trac.sagemath.org/ticket/8628





---

archive/issue_comments_078224.json:
```json
{
    "body": "New commits:",
    "created_at": "2016-03-21T17:14:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8628#issuecomment-78224",
    "user": "maurimo"
}
```

New commits:



---

archive/issue_comments_078225.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-03-21T17:14:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8628#issuecomment-78225",
    "user": "maurimo"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078226.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-03-22T21:14:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8628#issuecomment-78226",
    "user": "marmas"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078227.json:
```json
{
    "body": "Changing keywords from \"\" to \"days71\".",
    "created_at": "2016-03-26T14:53:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8628#issuecomment-78227",
    "user": "jen"
}
```

Changing keywords from "" to "days71".



---

archive/issue_comments_078228.json:
```json
{
    "body": "merge conflict, please merge in the next beta",
    "created_at": "2016-04-04T22:06:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8628#issuecomment-78228",
    "user": "vbraun"
}
```

merge conflict, please merge in the next beta



---

archive/issue_comments_078229.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2016-04-04T22:06:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8628#issuecomment-78229",
    "user": "vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_078230.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-11-17T23:08:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8628#issuecomment-78230",
    "user": "roed"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_078231.json:
```json
{
    "body": "This now merges.  \n----\nNew commits:",
    "created_at": "2016-11-17T23:08:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8628#issuecomment-78231",
    "user": "roed"
}
```

This now merges.  
----
New commits:



---

archive/issue_comments_078232.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-11-17T23:16:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8628#issuecomment-78232",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_078233.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-11-17T23:18:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8628#issuecomment-78233",
    "user": "saraedum"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078234.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-11-19T22:10:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8628#issuecomment-78234",
    "user": "vbraun"
}
```

Resolution: fixed



---

archive/issue_comments_078235.json:
```json
{
    "body": "Branch change was caused by a bug in the git-trac feature I'm working on.",
    "created_at": "2016-11-20T00:53:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8628#issuecomment-78235",
    "user": "roed"
}
```

Branch change was caused by a bug in the git-trac feature I'm working on.
