# Issue 9799: doctutils fails to run test suite when SAGE_CHECK=yes. Missing spkg-check

archive/issues_009799.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @nexttime @qed777\n\nThe `docutils` package, which is at version 0.5 in sage, lacks a spkg-check file, so the self-tests can't be run. But the package has a set of tests, which according to the `README.txt` is executed as below. \n\n\n```\nRunning the Test Suite\n======================\n\nTo run the entire test suite, after installation_ open a shell and use\nthe following commands::\n\n    cd <archive_directory_path>/test\n    ./alltests.py\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9800\n\n",
    "created_at": "2010-08-25T13:00:18Z",
    "labels": [
        "spkg-check",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "doctutils fails to run test suite when SAGE_CHECK=yes. Missing spkg-check",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9799",
    "user": "drkirkby"
}
```
Assignee: drkirkby

CC:  @nexttime @qed777

The `docutils` package, which is at version 0.5 in sage, lacks a spkg-check file, so the self-tests can't be run. But the package has a set of tests, which according to the `README.txt` is executed as below. 


```
Running the Test Suite
======================

To run the entire test suite, after installation_ open a shell and use
the following commands::

    cd <archive_directory_path>/test
    ./alltests.py
```



Issue created by migration from https://trac.sagemath.org/ticket/9800





---

archive/issue_comments_096290.json:
```json
{
    "body": "typo",
    "created_at": "2011-03-24T01:12:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9799#issuecomment-96290",
    "user": "@kini"
}
```

typo



---

archive/issue_comments_096291.json:
```json
{
    "body": "Changing keywords from \"\" to \"docutils\".",
    "created_at": "2011-03-24T01:12:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9799#issuecomment-96291",
    "user": "@kini"
}
```

Changing keywords from "" to "docutils".
