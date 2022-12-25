# Issue 7574: clean up of MIP interface

archive/issues_007574.json:
```json
{
    "body": "Assignee: jkantor\n\nThere are a few issues with the MIP code:\n- ``max`` and ``min`` are built-in core functions in Python and shouldn't be used as variable names\n- ``id`` shouldn't be used as a variable name\n- I don't think we should have ``try: foo except: bar`` blocks without a specific ``except ThisandThatError``.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7574\n\n",
    "created_at": "2009-12-01T17:33:00Z",
    "labels": [
        "component: numerical"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "clean up of MIP interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7574",
    "user": "https://github.com/malb"
}
```
Assignee: jkantor

There are a few issues with the MIP code:
- ``max`` and ``min`` are built-in core functions in Python and shouldn't be used as variable names
- ``id`` shouldn't be used as a variable name
- I don't think we should have ``try: foo except: bar`` blocks without a specific ``except ThisandThatError``.

Issue created by migration from https://trac.sagemath.org/ticket/7574





---

archive/issue_comments_064355.json:
```json
{
    "body": "Changing keywords from \"\" to \"lp\".",
    "created_at": "2016-06-25T06:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7574#issuecomment-64355",
    "user": "https://github.com/mkoeppe"
}
```

Changing keywords from "" to "lp".



---

archive/issue_comments_064356.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-06-25T06:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7574#issuecomment-64356",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064357.json:
```json
{
    "body": "This is outdated. The first issue is duplicated in #20664. Can be closed.",
    "created_at": "2016-06-25T06:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7574#issuecomment-64357",
    "user": "https://github.com/mkoeppe"
}
```

This is outdated. The first issue is duplicated in #20664. Can be closed.



---

archive/issue_comments_064358.json:
```json
{
    "body": "ok",
    "created_at": "2016-07-13T18:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7574#issuecomment-64358",
    "user": "https://github.com/fchapoton"
}
```

ok



---

archive/issue_comments_064359.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-07-13T18:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7574#issuecomment-64359",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064360.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2016-08-30T13:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7574#issuecomment-64360",
    "user": "https://github.com/embray"
}
```

Resolution: wontfix



---

archive/issue_comments_064361.json:
```json
{
    "body": "Determined to be invalid/duplicate/wontfix (closing as \"wontfix\" as a catch-all resolution).",
    "created_at": "2016-08-30T13:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7574#issuecomment-64361",
    "user": "https://github.com/embray"
}
```

Determined to be invalid/duplicate/wontfix (closing as "wontfix" as a catch-all resolution).
