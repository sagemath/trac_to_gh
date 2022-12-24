# Issue 1082: "sage -upgrade" behaves poorly when sage-main has not-checked-in changes

archive/issues_001082.json:
```json
{
    "body": "Assignee: @williamstein\n\nCurrently, \"sage -upgrade\" automatically checks in code in sage-main (asking you for a commit message, etc.) without explaining what's happening, and what exactly is being checked in.\n\nInstead, \"sage -upgrade\" should either explain what's going on before it checks in the code, or explain what's going on and then exit without doing anything, so the user can use hg_sage.ci().\n\nIssue created by migration from https://trac.sagemath.org/ticket/1082\n\n",
    "created_at": "2007-11-03T18:08:01Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "\"sage -upgrade\" behaves poorly when sage-main has not-checked-in changes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1082",
    "user": "cwitty"
}
```
Assignee: @williamstein

Currently, "sage -upgrade" automatically checks in code in sage-main (asking you for a commit message, etc.) without explaining what's happening, and what exactly is being checked in.

Instead, "sage -upgrade" should either explain what's going on before it checks in the code, or explain what's going on and then exit without doing anything, so the user can use hg_sage.ci().

Issue created by migration from https://trac.sagemath.org/ticket/1082





---

archive/issue_comments_006539.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-02-02T10:54:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1082#issuecomment-6539",
    "user": "@mezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_006540.json:
```json
{
    "body": "No more relevant?",
    "created_at": "2014-02-02T10:54:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1082#issuecomment-6540",
    "user": "@mezzarobba"
}
```

No more relevant?



---

archive/issue_comments_006541.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-02-09T21:36:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1082#issuecomment-6541",
    "user": "@a-andre"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_006542.json:
```json
{
    "body": "No longer relevant.",
    "created_at": "2014-02-09T21:36:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1082#issuecomment-6542",
    "user": "@a-andre"
}
```

No longer relevant.



---

archive/issue_comments_006543.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2014-02-11T21:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1082#issuecomment-6543",
    "user": "@vbraun"
}
```

Resolution: wontfix
