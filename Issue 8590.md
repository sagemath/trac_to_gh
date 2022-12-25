# Issue 8590: `A` still using old coercion framework

archive/issues_008590.json:
```json
{
    "body": "Assignee: @aghitza\n\nThere is a failure in the test of the file\n\nsage.categories.hopf_algebras_with_basis\n\nThe problem occurs during the test suite of an hopf algebra and returns the error\n\n\n```\n   RuntimeError: `A` still using old coercion framework\n```\n\n\nI am unfortunately not able to solve really this problem, but, if the competent people have no time right now, I can write a small patch predicting the error in the test so that the tests pass\n\nIssue created by migration from https://trac.sagemath.org/ticket/8590\n\n",
    "created_at": "2010-03-23T17:40:36Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "`A` still using old coercion framework",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8590",
    "user": "https://trac.sagemath.org/admin/accounts/users/vferay"
}
```
Assignee: @aghitza

There is a failure in the test of the file

sage.categories.hopf_algebras_with_basis

The problem occurs during the test suite of an hopf algebra and returns the error


```
   RuntimeError: `A` still using old coercion framework
```


I am unfortunately not able to solve really this problem, but, if the competent people have no time right now, I can write a small patch predicting the error in the test so that the tests pass

Issue created by migration from https://trac.sagemath.org/ticket/8590





---

archive/issue_comments_077683.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-02-02T11:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8590#issuecomment-77683",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077684.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-02-02T15:55:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8590#issuecomment-77684",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008767.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2014-02-02T20:43:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8590",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8590#event-8767"
}
```



---

archive/issue_comments_077685.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-02-02T20:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8590#issuecomment-77685",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
