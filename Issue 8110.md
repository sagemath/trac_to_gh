# Issue 8110: fix issue with multi_polynomial.pyx in sage-4.3.2.alpha0

archive/issues_008110.json:
```json
{
    "body": "Assignee: @malb\n\nThe patch at #7109 mistakenly removed some code from `rings/polynomial/multi_polynomial.pyx`, which causes doctest trouble in sage-4.3.2.alpha0.\n\nA patch fixing this is on its way.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8110\n\n",
    "created_at": "2010-01-28T12:30:54Z",
    "labels": [
        "commutative algebra",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "fix issue with multi_polynomial.pyx in sage-4.3.2.alpha0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8110",
    "user": "@aghitza"
}
```
Assignee: @malb

The patch at #7109 mistakenly removed some code from `rings/polynomial/multi_polynomial.pyx`, which causes doctest trouble in sage-4.3.2.alpha0.

A patch fixing this is on its way.


Issue created by migration from https://trac.sagemath.org/ticket/8110





---

archive/issue_comments_071194.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-28T12:35:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8110#issuecomment-71194",
    "user": "@aghitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071195.json:
```json
{
    "body": "Attachment [trac_8110.patch](tarball://root/attachments/some-uuid/ticket8110/trac_8110.patch) by @aghitza created at 2010-01-28 12:35:51",
    "created_at": "2010-01-28T12:35:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8110#issuecomment-71195",
    "user": "@aghitza"
}
```

Attachment [trac_8110.patch](tarball://root/attachments/some-uuid/ticket8110/trac_8110.patch) by @aghitza created at 2010-01-28 12:35:51



---

archive/issue_comments_071196.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-28T13:18:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8110#issuecomment-71196",
    "user": "@malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071197.json:
```json
{
    "body": "* patch looks good\n  * applies cleanly against alpha0\n  * doctests pass on sage.math",
    "created_at": "2010-01-28T13:18:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8110#issuecomment-71197",
    "user": "@malb"
}
```

* patch looks good
  * applies cleanly against alpha0
  * doctests pass on sage.math



---

archive/issue_comments_071198.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-30T23:33:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8110#issuecomment-71198",
    "user": "mvngu"
}
```

Resolution: fixed
