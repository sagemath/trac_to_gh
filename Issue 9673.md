# Issue 9673: Referring to flag for doc-testing only changed files

archive/issues_009673.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @fchapoton\n\nKeywords: doctest\n\nIn the Developer's Guide there is no reference to the \"-tnew\" flag to the sage executable, which will instruct Sage to only doctest changed files. I suggest adding such a reference in \"Walking through the development process\" as well as \"Parallel Testing the Sage Library\".\n\nIssue created by migration from https://trac.sagemath.org/ticket/9673\n\n",
    "closed_at": "2016-06-12T12:02:30Z",
    "created_at": "2010-08-03T07:56:52Z",
    "labels": [
        "component: documentation",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Referring to flag for doc-testing only changed files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9673",
    "user": "https://github.com/johanrosenkilde"
}
```
Assignee: mvngu

CC:  @fchapoton

Keywords: doctest

In the Developer's Guide there is no reference to the "-tnew" flag to the sage executable, which will instruct Sage to only doctest changed files. I suggest adding such a reference in "Walking through the development process" as well as "Parallel Testing the Sage Library".

Issue created by migration from https://trac.sagemath.org/ticket/9673





---

archive/issue_comments_093838.json:
```json
{
    "body": "Does anyone know how the \"-tnew\" flag works in detail? In particular, does it doctest every file that has been changed *as well as its dependencies*? If it is the case, this should be mentioned in the documentation. Otherwise, shouldn't it?",
    "created_at": "2010-08-03T07:59:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9673#issuecomment-93838",
    "user": "https://github.com/johanrosenkilde"
}
```

Does anyone know how the "-tnew" flag works in detail? In particular, does it doctest every file that has been changed *as well as its dependencies*? If it is the case, this should be mentioned in the documentation. Otherwise, shouldn't it?



---

archive/issue_comments_093839.json:
```json
{
    "body": "Of course, the above shouldn't say \"its dependencies\" but rather \"the files depending on them\".",
    "created_at": "2010-08-03T08:04:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9673#issuecomment-93839",
    "user": "https://github.com/johanrosenkilde"
}
```

Of course, the above shouldn't say "its dependencies" but rather "the files depending on them".



---

archive/issue_events_024136.json:
```json
{
    "actor": "https://github.com/jm58660",
    "created_at": "2016-04-22T10:43:08Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9673",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9673#event-24136"
}
```



---

archive/issue_comments_093840.json:
```json
{
    "body": "This has been done, see http://doc.sagemath.org/html/en/developer/doctesting.html#testing-changed-files, so I suggest this one to be closed. Fr\u00e9d\u00e9ric, please click *positive_review* if you agree.",
    "created_at": "2016-04-22T10:43:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9673#issuecomment-93840",
    "user": "https://github.com/jm58660"
}
```

This has been done, see http://doc.sagemath.org/html/en/developer/doctesting.html#testing-changed-files, so I suggest this one to be closed. Frédéric, please click *positive_review* if you agree.



---

archive/issue_comments_093841.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-04-22T10:43:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9673#issuecomment-93841",
    "user": "https://github.com/jm58660"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093842.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-04-22T11:32:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9673#issuecomment-93842",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_024137.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2016-06-12T12:02:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9673",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9673#event-24137"
}
```



---

archive/issue_comments_093843.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-06-12T12:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9673#issuecomment-93843",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
