# Issue 3355: invoke the libdir rewrite script on "sage -upgrade"

archive/issues_003355.json:
```json
{
    "body": "Assignee: cwitty\n\nAll the *.la files in $SAGE_LOCAL/lib have their libdir variable rewritten when Sage is moved. Do this also when installing any spkg since we might have moved the tree. This will likely cause a number of upgrade problems.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3355\n\n",
    "created_at": "2008-06-03T05:33:54Z",
    "labels": [
        "relocation",
        "blocker",
        "bug"
    ],
    "title": "invoke the libdir rewrite script on \"sage -upgrade\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3355",
    "user": "mabshoff"
}
```
Assignee: cwitty

All the *.la files in $SAGE_LOCAL/lib have their libdir variable rewritten when Sage is moved. Do this also when installing any spkg since we might have moved the tree. This will likely cause a number of upgrade problems.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3355





---

archive/issue_comments_023324.json:
```json
{
    "body": "Changing priority from blocker to critical.",
    "created_at": "2009-06-15T23:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3355#issuecomment-23324",
    "user": "was"
}
```

Changing priority from blocker to critical.



---

archive/issue_comments_023325.json:
```json
{
    "body": "If we've released for months and months without fixing this, it doesn't make sense to keep it as a blocker.",
    "created_at": "2009-06-15T23:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3355#issuecomment-23325",
    "user": "was"
}
```

If we've released for months and months without fixing this, it doesn't make sense to keep it as a blocker.



---

archive/issue_comments_023326.json:
```json
{
    "body": "* **Priority** changed from *critical* to *major*\n\nIf we've released for years and years without fixing this, it doesn't make sense to keep it as critical.\n\n... just kidding!",
    "created_at": "2012-03-21T00:04:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3355#issuecomment-23326",
    "user": "kini"
}
```

* **Priority** changed from *critical* to *major*

If we've released for years and years without fixing this, it doesn't make sense to keep it as critical.

... just kidding!



---

archive/issue_comments_023327.json:
```json
{
    "body": "`sage-location` actually does this now.",
    "created_at": "2013-03-28T22:57:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3355#issuecomment-23327",
    "user": "jdemeyer"
}
```

`sage-location` actually does this now.



---

archive/issue_comments_023328.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-03-28T22:57:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3355#issuecomment-23328",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_023329.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-03-28T22:57:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3355#issuecomment-23329",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_023330.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-03-29T19:00:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3355#issuecomment-23330",
    "user": "jdemeyer"
}
```

Resolution: worksforme
