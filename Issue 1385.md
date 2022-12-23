# Issue 1385: Re-organize number field element inheritance hierarchy

archive/issues_001385.json:
```json
{
    "body": "Assignee: was\n\nCurrently the base NumberFieldElement class requires NTL. However, the quadratic number field elements, and (in the future) FLINT-based number field classes won't use NTL at all, but things need to be split out to make this clean. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1385\n\n",
    "created_at": "2007-12-03T20:32:39Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "Re-organize number field element inheritance hierarchy",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1385",
    "user": "robertwb"
}
```
Assignee: was

Currently the base NumberFieldElement class requires NTL. However, the quadratic number field elements, and (in the future) FLINT-based number field classes won't use NTL at all, but things need to be split out to make this clean. 

Issue created by migration from https://trac.sagemath.org/ticket/1385





---

archive/issue_comments_008886.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T07:06:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1385#issuecomment-8886",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_008887.json:
```json
{
    "body": "Changing assignee from was to davidloeffler.",
    "created_at": "2009-07-20T19:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1385#issuecomment-8887",
    "user": "davidloeffler"
}
```

Changing assignee from was to davidloeffler.



---

archive/issue_comments_008888.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-20T19:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1385#issuecomment-8888",
    "user": "davidloeffler"
}
```

Changing component from number theory to number fields.



---

archive/issue_comments_008889.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-10-09T11:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1385#issuecomment-8889",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_008890.json:
```json
{
    "body": "I don't see any reason to change things at the moment.  If we really re-implement number fields, that would be the correct time to change this.  Proposing to close as \"wontfix\".",
    "created_at": "2011-10-09T11:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1385#issuecomment-8890",
    "user": "jdemeyer"
}
```

I don't see any reason to change things at the moment.  If we really re-implement number fields, that would be the correct time to change this.  Proposing to close as "wontfix".



---

archive/issue_comments_008891.json:
```json
{
    "body": "I agree. Let's close this.",
    "created_at": "2011-10-09T17:18:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1385#issuecomment-8891",
    "user": "davidloeffler"
}
```

I agree. Let's close this.



---

archive/issue_comments_008892.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-10-09T17:18:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1385#issuecomment-8892",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_008893.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2011-10-09T20:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1385#issuecomment-8893",
    "user": "jdemeyer"
}
```

Resolution: invalid
