# Issue 9642: sage-maketest and sage-test-new should be able to run tests in parallel

archive/issues_009642.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @kcrisman\n\nReported on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/efae2db905b3ee8f/1a2312f22bc40d9a#1a2312f22bc40d9a) by K.-D. Crisman:\n\n```\nSubject: can sage -testall use threads?\n\nThat is, without setting NUM_THREADS or something.  I tried\n\n./sage -testall -p 8\n\nbut I just get lots of error messages in addition to my test output.\nI guess I have the same question about sage -tnew as well.\n```\n\n\nSomewhat related: #279\n\nIssue created by migration from https://trac.sagemath.org/ticket/9642\n\n",
    "created_at": "2010-07-29T22:46:39Z",
    "labels": [
        "component: doctest coverage",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sage-maketest and sage-test-new should be able to run tests in parallel",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9642",
    "user": "https://github.com/qed777"
}
```
Assignee: mvngu

CC:  @kcrisman

Reported on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/efae2db905b3ee8f/1a2312f22bc40d9a#1a2312f22bc40d9a) by K.-D. Crisman:

```
Subject: can sage -testall use threads?

That is, without setting NUM_THREADS or something.  I tried

./sage -testall -p 8

but I just get lots of error messages in addition to my test output.
I guess I have the same question about sage -tnew as well.
```


Somewhat related: #279

Issue created by migration from https://trac.sagemath.org/ticket/9642





---

archive/issue_comments_093306.json:
```json
{
    "body": "It seems the `sage -testall` and `sage -tnew` operators invoke `SAGE_LOCAL/bin/sage-maketest` and `sage-test-new`, respectively.  To run the tests, both scripts use `sage -t`, which calls the serial doctest runner `sage-test`.  Moreover, `sage-test-new` does not pass along command-line arguments.",
    "created_at": "2010-07-29T22:49:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9642#issuecomment-93306",
    "user": "https://github.com/qed777"
}
```

It seems the `sage -testall` and `sage -tnew` operators invoke `SAGE_LOCAL/bin/sage-maketest` and `sage-test-new`, respectively.  To run the tests, both scripts use `sage -t`, which calls the serial doctest runner `sage-test`.  Moreover, `sage-test-new` does not pass along command-line arguments.



---

archive/issue_comments_093307.json:
```json
{
    "body": "This is resolved by #12415.",
    "created_at": "2013-03-14T20:39:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9642#issuecomment-93307",
    "user": "https://github.com/roed314"
}
```

This is resolved by #12415.



---

archive/issue_comments_093308.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-03-14T20:39:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9642#issuecomment-93308",
    "user": "https://github.com/roed314"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093309.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-03-14T20:39:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9642#issuecomment-93309",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093310.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-03-15T13:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9642#issuecomment-93310",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
