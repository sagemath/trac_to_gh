# Issue 9488: [easy] parse make -j N as well as make -jN for parallel builds

archive/issues_009488.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nThe code in setup.py to pull the parallelization parameter out of the MAKE environment variable can't handle the extra space, but could easily be re-written. \n\nIssue created by migration from https://trac.sagemath.org/ticket/9488\n\n",
    "created_at": "2010-07-13T05:17:47Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[easy] parse make -j N as well as make -jN for parallel builds",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9488",
    "user": "robertwb"
}
```
Assignee: GeorgSWeber

The code in setup.py to pull the parallelization parameter out of the MAKE environment variable can't handle the extra space, but could easily be re-written. 

Issue created by migration from https://trac.sagemath.org/ticket/9488





---

archive/issue_comments_091096.json:
```json
{
    "body": "To work in accordance with the man page for GNU make, the following should also be acceptable\n\n\n```\nmake -j\n```\n\n\nin which case the number of threads is infinite - i.e. limited only by what the build system allows.",
    "created_at": "2010-07-13T07:11:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9488#issuecomment-91096",
    "user": "drkirkby"
}
```

To work in accordance with the man page for GNU make, the following should also be acceptable


```
make -j
```


in which case the number of threads is infinite - i.e. limited only by what the build system allows.



---

archive/issue_comments_091097.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-05-19T13:10:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9488#issuecomment-91097",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091098.json:
```json
{
    "body": "This already works.",
    "created_at": "2013-05-19T13:10:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9488#issuecomment-91098",
    "user": "jdemeyer"
}
```

This already works.



---

archive/issue_comments_091099.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-05-19T13:10:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9488#issuecomment-91099",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091100.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-05-21T07:22:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9488#issuecomment-91100",
    "user": "jdemeyer"
}
```

Resolution: worksforme
