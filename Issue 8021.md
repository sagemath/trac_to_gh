# Issue 8021: ref manual for 4.3.1: error when building (Undefined control sequence \cross)

archive/issues_008021.json:
```json
{
    "body": "Assignee: mvngu\n\nIn several places in the Sage code, \"\\cross\" is used, and one of those instances causes an error when building the reference manual.  This is not a standard LaTeX command, and I think \"\\times\" is what is intended, so this patch makes that change.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8021\n\n",
    "created_at": "2010-01-21T06:26:45Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "title": "ref manual for 4.3.1: error when building (Undefined control sequence \\cross)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8021",
    "user": "jhpalmieri"
}
```
Assignee: mvngu

In several places in the Sage code, "\cross" is used, and one of those instances causes an error when building the reference manual.  This is not a standard LaTeX command, and I think "\times" is what is intended, so this patch makes that change.

Issue created by migration from https://trac.sagemath.org/ticket/8021





---

archive/issue_comments_070086.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-21T06:30:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8021#issuecomment-70086",
    "user": "jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070087.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-01-21T06:30:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8021#issuecomment-70087",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_070088.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-22T02:37:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8021#issuecomment-70088",
    "user": "mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070089.json:
```json
{
    "body": "This allows the HTML version of the reference manual to build without errors.",
    "created_at": "2010-01-22T02:37:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8021#issuecomment-70089",
    "user": "mvngu"
}
```

This allows the HTML version of the reference manual to build without errors.



---

archive/issue_comments_070090.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-23T16:58:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8021#issuecomment-70090",
    "user": "mvngu"
}
```

Resolution: fixed
