# Issue 1385: Re-organize number field element inheritance hierarchy

archive/issues_001385.json:
```json
{
    "body": "Assignee: @williamstein\n\nCurrently the base NumberFieldElement class requires NTL. However, the quadratic number field elements, and (in the future) FLINT-based number field classes won't use NTL at all, but things need to be split out to make this clean. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1385\n\n",
    "created_at": "2007-12-03T20:32:39Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Re-organize number field element inheritance hierarchy",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1385",
    "user": "https://github.com/robertwb"
}
```
Assignee: @williamstein

Currently the base NumberFieldElement class requires NTL. However, the quadratic number field elements, and (in the future) FLINT-based number field classes won't use NTL at all, but things need to be split out to make this clean. 

Issue created by migration from https://trac.sagemath.org/ticket/1385





---

archive/issue_comments_008862.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T07:06:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1385#issuecomment-8862",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_008863.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-20T19:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1385#issuecomment-8863",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_comments_008864.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-20T19:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1385#issuecomment-8864",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to number fields.



---

archive/issue_comments_008865.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-10-09T11:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1385#issuecomment-8865",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_008866.json:
```json
{
    "body": "I don't see any reason to change things at the moment.  If we really re-implement number fields, that would be the correct time to change this.  Proposing to close as \"wontfix\".",
    "created_at": "2011-10-09T11:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1385#issuecomment-8866",
    "user": "https://github.com/jdemeyer"
}
```

I don't see any reason to change things at the moment.  If we really re-implement number fields, that would be the correct time to change this.  Proposing to close as "wontfix".



---

archive/issue_comments_008867.json:
```json
{
    "body": "I agree. Let's close this.",
    "created_at": "2011-10-09T17:18:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1385#issuecomment-8867",
    "user": "https://github.com/loefflerd"
}
```

I agree. Let's close this.



---

archive/issue_comments_008868.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-10-09T17:18:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1385#issuecomment-8868",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_008869.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2011-10-09T20:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1385#issuecomment-8869",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: invalid
