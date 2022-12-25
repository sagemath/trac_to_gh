# Issue 8628: confusing defaults for p-adic precision types

archive/issues_008628.json:
```json
{
    "body": "Assignee: @roed314\n\nKeywords: days71\n\n(sage 4.3.1)\n\nabsolute or relative is the default?\n\n```\nsage: R = Zp(5)\nsage: R\n5-adic Ring with capped relative precision 20\nsage: R.<a> = Zq(25)\nsage: R\nUnramified Extension of 5-adic Ring with capped absolute precision 20 in a defined by (1 + O(5^20))*x^2 + (4 + O(5^20))*x + (2 + O(5^20))\nsage: R = Zq(5)\nsage: R\n5-adic Ring with capped absolute precision 20\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8628\n\n",
    "closed_at": "2016-11-19T22:10:05Z",
    "created_at": "2010-03-30T00:50:51Z",
    "labels": [
        "component: padics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-7.2",
    "title": "confusing defaults for p-adic precision types",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8628",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: @roed314

Keywords: days71

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

archive/issue_comments_078095.json:
```json
{
    "body": "New commits:",
    "created_at": "2016-03-21T17:14:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8628#issuecomment-78095",
    "user": "https://trac.sagemath.org/admin/accounts/users/maurimo"
}
```

New commits:



---

archive/issue_comments_078096.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-03-21T17:14:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8628#issuecomment-78096",
    "user": "https://trac.sagemath.org/admin/accounts/users/maurimo"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078097.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-03-22T21:14:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8628#issuecomment-78097",
    "user": "https://trac.sagemath.org/admin/accounts/users/marmas"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078098.json:
```json
{
    "body": "Changing keywords from \"\" to \"days71\".",
    "created_at": "2016-03-26T14:53:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8628#issuecomment-78098",
    "user": "https://github.com/jbalakrishnan"
}
```

Changing keywords from "" to "days71".



---

archive/issue_events_020883.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2016-04-04T16:50:31Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8628",
    "milestone": "sage-7.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8628#event-20883"
}
```



---

archive/issue_comments_078099.json:
```json
{
    "body": "merge conflict, please merge in the next beta",
    "created_at": "2016-04-04T22:06:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8628#issuecomment-78099",
    "user": "https://github.com/vbraun"
}
```

merge conflict, please merge in the next beta



---

archive/issue_comments_078100.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2016-04-04T22:06:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8628#issuecomment-78100",
    "user": "https://github.com/vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_078101.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-11-17T23:08:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8628#issuecomment-78101",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_078102.json:
```json
{
    "body": "This now merges.  \n\n---\nNew commits:",
    "created_at": "2016-11-17T23:08:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8628#issuecomment-78102",
    "user": "https://github.com/roed314"
}
```

This now merges.  

---
New commits:



---

archive/issue_comments_078103.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-11-17T23:16:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8628#issuecomment-78103",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_078104.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-11-17T23:18:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8628#issuecomment-78104",
    "user": "https://github.com/saraedum"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_020884.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2016-11-19T22:10:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8628",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8628#event-20884"
}
```



---

archive/issue_comments_078105.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-11-19T22:10:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8628#issuecomment-78105",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_comments_078106.json:
```json
{
    "body": "Branch change was caused by a bug in the git-trac feature I'm working on.",
    "created_at": "2016-11-20T00:53:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8628#issuecomment-78106",
    "user": "https://github.com/roed314"
}
```

Branch change was caused by a bug in the git-trac feature I'm working on.
