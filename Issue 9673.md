# Issue 9673: Referring to flag for doc-testing only changed files

archive/issues_009673.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  chapoton\n\nKeywords: doctest\n\nIn the Developer's Guide there is no reference to the \"-tnew\" flag to the sage executable, which will instruct Sage to only doctest changed files. I suggest adding such a reference in \"Walking through the development process\" as well as \"Parallel Testing the Sage Library\".\n\nIssue created by migration from https://trac.sagemath.org/ticket/9673\n\n",
    "created_at": "2010-08-03T07:56:52Z",
    "labels": [
        "documentation",
        "minor",
        "enhancement"
    ],
    "title": "Referring to flag for doc-testing only changed files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9673",
    "user": "jsrn"
}
```
Assignee: mvngu

CC:  chapoton

Keywords: doctest

In the Developer's Guide there is no reference to the "-tnew" flag to the sage executable, which will instruct Sage to only doctest changed files. I suggest adding such a reference in "Walking through the development process" as well as "Parallel Testing the Sage Library".

Issue created by migration from https://trac.sagemath.org/ticket/9673





---

archive/issue_comments_093995.json:
```json
{
    "body": "Does anyone know how the \"-tnew\" flag works in detail? In particular, does it doctest every file that has been changed *as well as its dependencies*? If it is the case, this should be mentioned in the documentation. Otherwise, shouldn't it?",
    "created_at": "2010-08-03T07:59:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9673#issuecomment-93995",
    "user": "jsrn"
}
```

Does anyone know how the "-tnew" flag works in detail? In particular, does it doctest every file that has been changed *as well as its dependencies*? If it is the case, this should be mentioned in the documentation. Otherwise, shouldn't it?



---

archive/issue_comments_093996.json:
```json
{
    "body": "Of course, the above shouldn't say \"its dependencies\" but rather \"the files depending on them\".",
    "created_at": "2010-08-03T08:04:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9673#issuecomment-93996",
    "user": "jsrn"
}
```

Of course, the above shouldn't say "its dependencies" but rather "the files depending on them".



---

archive/issue_comments_093997.json:
```json
{
    "body": "This has been done, see http://doc.sagemath.org/html/en/developer/doctesting.html#testing-changed-files, so I suggest this one to be closed. Fr\u00e9d\u00e9ric, please click *positive_review* if you agree.",
    "created_at": "2016-04-22T10:43:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9673#issuecomment-93997",
    "user": "jmantysalo"
}
```

This has been done, see http://doc.sagemath.org/html/en/developer/doctesting.html#testing-changed-files, so I suggest this one to be closed. Frédéric, please click *positive_review* if you agree.



---

archive/issue_comments_093998.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-04-22T10:43:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9673#issuecomment-93998",
    "user": "jmantysalo"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093999.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-04-22T11:32:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9673#issuecomment-93999",
    "user": "chapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_094000.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-06-12T12:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9673#issuecomment-94000",
    "user": "vbraun"
}
```

Resolution: fixed
