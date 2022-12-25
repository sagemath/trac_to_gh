# Issue 1388: failure in calculus/wester.py

archive/issues_001388.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\n\nsage -t  devel/sage-main/sage/calculus/wester.py            **********************************************************************\nFile \"wester.py\", line 399:\n    : print d.factor()\nExpected:\n    (-1) * (a - d) * (-a + b) * (b - d) * (a - c) * (b - c) * (c - d)\nGot:\n    (-1) * (-a + b) * (a - c) * (b - c) * (a - d) * (b - d) * (c - d)\n**********************************************************************\n1 items had failures:\n   1 of 188 in __main__.example_0\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctest_wester.py\n         [9.5 s]\nexit code: 256\n \n\n```\n\n\n\nThis seems to be a 32 bits issue!?\n\nIssue created by migration from https://trac.sagemath.org/ticket/1388\n\n",
    "created_at": "2007-12-03T21:13:08Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "failure in calculus/wester.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1388",
    "user": "https://github.com/jaapspies"
}
```
Assignee: @williamstein


```

sage -t  devel/sage-main/sage/calculus/wester.py            **********************************************************************
File "wester.py", line 399:
    : print d.factor()
Expected:
    (-1) * (a - d) * (-a + b) * (b - d) * (a - c) * (b - c) * (c - d)
Got:
    (-1) * (-a + b) * (a - c) * (b - c) * (a - d) * (b - d) * (c - d)
**********************************************************************
1 items had failures:
   1 of 188 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_wester.py
         [9.5 s]
exit code: 256
 

```



This seems to be a 32 bits issue!?

Issue created by migration from https://trac.sagemath.org/ticket/1388





---

archive/issue_comments_008876.json:
```json
{
    "body": "Changing assignee from @williamstein to failure.",
    "created_at": "2007-12-03T21:24:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1388#issuecomment-8876",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to failure.



---

archive/issue_comments_008877.json:
```json
{
    "body": "Changing component from algebraic geometry to doctest.",
    "created_at": "2007-12-03T21:24:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1388#issuecomment-8877",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from algebraic geometry to doctest.



---

archive/issue_comments_008878.json:
```json
{
    "body": "This only happens on Linux 32 bit, but not on OSX PPC 32 bit. So adding special `#32` and `#64` flags won't work.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-03T21:26:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1388#issuecomment-8878",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This only happens on Linux 32 bit, but not on OSX PPC 32 bit. So adding special `#32` and `#64` flags won't work.

Cheers,

Michael



---

archive/issue_comments_008879.json:
```json
{
    "body": "Fixed by #1392.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-04T14:29:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1388#issuecomment-8879",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed by #1392.

Cheers,

Michael



---

archive/issue_events_001532.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-12-04T14:29:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1388",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1388#event-1532"
}
```



---

archive/issue_comments_008880.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-04T14:29:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1388#issuecomment-8880",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
