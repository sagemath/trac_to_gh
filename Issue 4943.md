# Issue 4943: make sage -tp run sage -t when only one file is specified

archive/issues_004943.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: parallel doctest testing\n\nsage -tp is great, except it doesn't print synchronously when only one file is being tested.  It's irritating to wait for output when there are no race problems due to only a single parallel process.  Could we make sage -tp detect a single file and just run sage -t when that's the case?\n\nIssue created by migration from https://trac.sagemath.org/ticket/4943\n\n",
    "created_at": "2009-01-05T22:35:56Z",
    "labels": [
        "doctest coverage",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "make sage -tp run sage -t when only one file is specified",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4943",
    "user": "@ncalexan"
}
```
Assignee: mabshoff

Keywords: parallel doctest testing

sage -tp is great, except it doesn't print synchronously when only one file is being tested.  It's irritating to wait for output when there are no race problems due to only a single parallel process.  Could we make sage -tp detect a single file and just run sage -t when that's the case?

Issue created by migration from https://trac.sagemath.org/ticket/4943





---

archive/issue_comments_037525.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:25:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4943#issuecomment-37525",
    "user": "@aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_037526.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-03-14T20:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4943#issuecomment-37526",
    "user": "@roed314"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_037527.json:
```json
{
    "body": "This is resolved by #12415.",
    "created_at": "2013-03-14T20:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4943#issuecomment-37527",
    "user": "@roed314"
}
```

This is resolved by #12415.



---

archive/issue_comments_037528.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-03-14T20:38:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4943#issuecomment-37528",
    "user": "@roed314"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_037529.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-03-15T13:01:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4943#issuecomment-37529",
    "user": "@jdemeyer"
}
```

Resolution: duplicate
