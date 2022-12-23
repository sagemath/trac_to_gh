# Issue 5688: update to sympy 0.6.4

archive/issues_005688.json:
```json
{
    "body": "Assignee: burcin\n\nThe spkg package is at:\n\nhttp://sympy.googlecode.com/files/sympy-0.6.4.spkg\n\nAll calculus tests run fine, I am now testing the whole sage. When it's done, I'll append the log.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5688\n\n",
    "created_at": "2009-04-05T08:13:22Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "update to sympy 0.6.4",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5688",
    "user": "certik"
}
```
Assignee: burcin

The spkg package is at:

http://sympy.googlecode.com/files/sympy-0.6.4.spkg

All calculus tests run fine, I am now testing the whole sage. When it's done, I'll append the log.

Issue created by migration from https://trac.sagemath.org/ticket/5688





---

archive/issue_comments_044483.json:
```json
{
    "body": "Unfortunately, the tests hung. It may be that they hung on my machine even before uploading the new sympy. I used sage 3.4.1.alpha0.\n\nSo this should be investigated.",
    "created_at": "2009-04-05T08:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5688#issuecomment-44483",
    "user": "certik"
}
```

Unfortunately, the tests hung. It may be that they hung on my machine even before uploading the new sympy. I used sage 3.4.1.alpha0.

So this should be investigated.



---

archive/issue_comments_044484.json:
```json
{
    "body": "Ignore the sympy_test.2.log, I don't know how to delete it.\n\n\nsympy_test.log now contains the testsuite including the timeout failures.",
    "created_at": "2009-04-05T08:58:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5688#issuecomment-44484",
    "user": "certik"
}
```

Ignore the sympy_test.2.log, I don't know how to delete it.


sympy_test.log now contains the testsuite including the timeout failures.



---

archive/issue_comments_044485.json:
```json
{
    "body": "Do not attach logs to trac - copy and paste the failures into a comment. I have deleted both logs.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-05T09:07:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5688#issuecomment-44485",
    "user": "mabshoff"
}
```

Do not attach logs to trac - copy and paste the failures into a comment. I have deleted both logs.

Cheers,

Michael



---

archive/issue_comments_044486.json:
```json
{
    "body": "Please mark ticket with spkg properly do people are aware that there is something to review. I will do so in the short term and hopefully get this spkg merged.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T04:28:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5688#issuecomment-44486",
    "user": "mabshoff"
}
```

Please mark ticket with spkg properly do people are aware that there is something to review. I will do so in the short term and hopefully get this spkg merged.

Cheers,

Michael



---

archive/issue_comments_044487.json:
```json
{
    "body": "Spkg is clean, doctests pass. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T04:55:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5688#issuecomment-44487",
    "user": "mabshoff"
}
```

Spkg is clean, doctests pass. Positive review.

Cheers,

Michael



---

archive/issue_comments_044488.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-06T04:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5688#issuecomment-44488",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_044489.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T04:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5688#issuecomment-44489",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc1.

Cheers,

Michael
