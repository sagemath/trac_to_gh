# Issue 5688: update to sympy 0.6.4

archive/issues_005688.json:
```json
{
    "body": "Assignee: @burcin\n\nThe spkg package is at:\n\nhttp://sympy.googlecode.com/files/sympy-0.6.4.spkg\n\nAll calculus tests run fine, I am now testing the whole sage. When it's done, I'll append the log.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5688\n\n",
    "created_at": "2009-04-05T08:13:22Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "update to sympy 0.6.4",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5688",
    "user": "https://github.com/certik"
}
```
Assignee: @burcin

The spkg package is at:

http://sympy.googlecode.com/files/sympy-0.6.4.spkg

All calculus tests run fine, I am now testing the whole sage. When it's done, I'll append the log.

Issue created by migration from https://trac.sagemath.org/ticket/5688





---

archive/issue_comments_044398.json:
```json
{
    "body": "Unfortunately, the tests hung. It may be that they hung on my machine even before uploading the new sympy. I used sage 3.4.1.alpha0.\n\nSo this should be investigated.",
    "created_at": "2009-04-05T08:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5688#issuecomment-44398",
    "user": "https://github.com/certik"
}
```

Unfortunately, the tests hung. It may be that they hung on my machine even before uploading the new sympy. I used sage 3.4.1.alpha0.

So this should be investigated.



---

archive/issue_comments_044399.json:
```json
{
    "body": "Ignore the sympy_test.2.log, I don't know how to delete it.\n\n\nsympy_test.log now contains the testsuite including the timeout failures.",
    "created_at": "2009-04-05T08:58:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5688#issuecomment-44399",
    "user": "https://github.com/certik"
}
```

Ignore the sympy_test.2.log, I don't know how to delete it.


sympy_test.log now contains the testsuite including the timeout failures.



---

archive/issue_comments_044400.json:
```json
{
    "body": "Do not attach logs to trac - copy and paste the failures into a comment. I have deleted both logs.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-05T09:07:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5688#issuecomment-44400",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Do not attach logs to trac - copy and paste the failures into a comment. I have deleted both logs.

Cheers,

Michael



---

archive/issue_comments_044401.json:
```json
{
    "body": "Please mark ticket with spkg properly do people are aware that there is something to review. I will do so in the short term and hopefully get this spkg merged.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T04:28:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5688#issuecomment-44401",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Please mark ticket with spkg properly do people are aware that there is something to review. I will do so in the short term and hopefully get this spkg merged.

Cheers,

Michael



---

archive/issue_comments_044402.json:
```json
{
    "body": "Spkg is clean, doctests pass. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T04:55:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5688#issuecomment-44402",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Spkg is clean, doctests pass. Positive review.

Cheers,

Michael



---

archive/issue_events_005930.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-06T04:55:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5688",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5688#event-5930"
}
```



---

archive/issue_comments_044403.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-06T04:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5688#issuecomment-44403",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_044404.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T04:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5688#issuecomment-44404",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc1.

Cheers,

Michael
