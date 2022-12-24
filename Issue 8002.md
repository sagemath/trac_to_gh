# Issue 8002: remove dead code from sage-ptest

archive/issues_008002.json:
```json
{
    "body": "Assignee: tbd\n\nThe `sage-ptest` parallel doctesting script has some dead code in it: a function `run` that's unused, and a `-sage` flag that triggers a call to a no longer existing `sage-doctest_tex` script.\n\nI'm attaching a patch that cleans this up, and as a side effect allows `sage-ptest` to test files with a `.sage` extension.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8002\n\n",
    "created_at": "2010-01-19T19:13:52Z",
    "labels": [
        "doctest coverage",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "remove dead code from sage-ptest",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8002",
    "user": "@wjp"
}
```
Assignee: tbd

The `sage-ptest` parallel doctesting script has some dead code in it: a function `run` that's unused, and a `-sage` flag that triggers a call to a no longer existing `sage-doctest_tex` script.

I'm attaching a patch that cleans this up, and as a side effect allows `sage-ptest` to test files with a `.sage` extension.

Issue created by migration from https://trac.sagemath.org/ticket/8002





---

archive/issue_comments_069927.json:
```json
{
    "body": "Attachment [scripts_8002_ptest_cleanup.patch](tarball://root/attachments/some-uuid/ticket8002/scripts_8002_ptest_cleanup.patch) by @wjp created at 2010-01-19 19:26:13",
    "created_at": "2010-01-19T19:26:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8002#issuecomment-69927",
    "user": "@wjp"
}
```

Attachment [scripts_8002_ptest_cleanup.patch](tarball://root/attachments/some-uuid/ticket8002/scripts_8002_ptest_cleanup.patch) by @wjp created at 2010-01-19 19:26:13



---

archive/issue_comments_069928.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T19:26:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8002#issuecomment-69928",
    "user": "@wjp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069929.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-21T01:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8002#issuecomment-69929",
    "user": "@rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069930.json:
```json
{
    "body": "Written as advertised, `run()` routine is never called, `doctest_tex` is no longer shipped as part of Sage.\n\nApplies cleanly and works fine in limited testing.\n\nPositive review.",
    "created_at": "2010-01-21T01:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8002#issuecomment-69930",
    "user": "@rbeezer"
}
```

Written as advertised, `run()` routine is never called, `doctest_tex` is no longer shipped as part of Sage.

Applies cleanly and works fine in limited testing.

Positive review.



---

archive/issue_comments_069931.json:
```json
{
    "body": "Merged in script repository.",
    "created_at": "2010-01-23T10:23:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8002#issuecomment-69931",
    "user": "mvngu"
}
```

Merged in script repository.



---

archive/issue_comments_069932.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-23T10:23:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8002#issuecomment-69932",
    "user": "mvngu"
}
```

Resolution: fixed
