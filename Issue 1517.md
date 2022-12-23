# Issue 1517: Make sure a minimum of space is available to build component

archive/issues_001517.json:
```json
{
    "body": "Assignee: was\n\nMany people have run out of disc space while building Sage. So check in `sage-spkg` if at least K MB are free on the partition we are building Sage in. K should be a couple hundred Megabytes in my opinion ;) We might also print a warning once we go below another, higher threshold. \n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1517\n\n",
    "created_at": "2007-12-15T02:35:11Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "Make sure a minimum of space is available to build component",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1517",
    "user": "mabshoff"
}
```
Assignee: was

Many people have run out of disc space while building Sage. So check in `sage-spkg` if at least K MB are free on the partition we are building Sage in. K should be a couple hundred Megabytes in my opinion ;) We might also print a warning once we go below another, higher threshold. 

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1517





---

archive/issue_comments_009723.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-06-13T12:31:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1517#issuecomment-9723",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_009724.json:
```json
{
    "body": "It's not the job of Sage to check filesystem space. Besides, this looks very hard to do in a portable way.",
    "created_at": "2013-06-13T12:31:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1517#issuecomment-9724",
    "user": "jdemeyer"
}
```

It's not the job of Sage to check filesystem space. Besides, this looks very hard to do in a portable way.



---

archive/issue_comments_009725.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-06-13T12:31:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1517#issuecomment-9725",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_009726.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2013-06-19T12:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1517#issuecomment-9726",
    "user": "jdemeyer"
}
```

Resolution: wontfix
