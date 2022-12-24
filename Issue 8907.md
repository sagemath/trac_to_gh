# Issue 8907: build Python as a shared library

archive/issues_008907.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nThis is needed by #8542 .  There is an spkg at http://sage.math.washington.edu/home/mhansen/python-2.6.4.p8.spkg but it requires lots of testing.  Also, the changes are not committed to the repository.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8907\n\n",
    "created_at": "2010-05-06T17:10:55Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.3",
    "title": "build Python as a shared library",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8907",
    "user": "mhansen"
}
```
Assignee: AlexGhitza

This is needed by #8542 .  There is an spkg at http://sage.math.washington.edu/home/mhansen/python-2.6.4.p8.spkg but it requires lots of testing.  Also, the changes are not committed to the repository.

Issue created by migration from https://trac.sagemath.org/ticket/8907





---

archive/issue_comments_082030.json:
```json
{
    "body": "Changing component from algebra to cygwin.",
    "created_at": "2010-05-06T17:11:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8907#issuecomment-82030",
    "user": "mhansen"
}
```

Changing component from algebra to cygwin.



---

archive/issue_comments_082031.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-06T17:11:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8907#issuecomment-82031",
    "user": "mhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082032.json:
```json
{
    "body": "Check on OS X, we don't need --enable-shared.  I'm check on t2 now.  The spkg will have to be updated accordingly.",
    "created_at": "2010-05-06T17:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8907#issuecomment-82032",
    "user": "mhansen"
}
```

Check on OS X, we don't need --enable-shared.  I'm check on t2 now.  The spkg will have to be updated accordingly.



---

archive/issue_comments_082033.json:
```json
{
    "body": "--enabled-shared fails on t2 because of http://bugs.python.org/issue1628484 .  We need to apply the patch there.",
    "created_at": "2010-05-25T05:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8907#issuecomment-82033",
    "user": "mhansen"
}
```

--enabled-shared fails on t2 because of http://bugs.python.org/issue1628484 .  We need to apply the patch there.



---

archive/issue_comments_082034.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-26T00:44:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8907#issuecomment-82034",
    "user": "was"
}
```

Resolution: fixed
