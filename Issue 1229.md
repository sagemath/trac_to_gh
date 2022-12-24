# Issue 1229: 2.8.13.rc1: sage/calculus/calculus.py doctest failure

archive/issues_001229.json:
```json
{
    "body": "Assignee: was\n\n\n```\nFile \"calculus.py\", line 209:\n     sage: expand((x+y)^3)\nExpected:\n     y^3 + 3*x*y^2 + 3*x^2*y + x^3\nGot:\n     x^6 + 3*x^5 + 3*x^4 + x^3\n```\n\nThis is likely fallout from #1215.\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1229\n\n",
    "created_at": "2007-11-20T23:06:20Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "2.8.13.rc1: sage/calculus/calculus.py doctest failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1229",
    "user": "mabshoff"
}
```
Assignee: was


```
File "calculus.py", line 209:
     sage: expand((x+y)^3)
Expected:
     y^3 + 3*x*y^2 + 3*x^2*y + x^3
Got:
     x^6 + 3*x^5 + 3*x^4 + x^3
```

This is likely fallout from #1215.


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1229





---

archive/issue_comments_007644.json:
```json
{
    "body": "Attachment [trac1229.patch](tarball://root/attachments/some-uuid/ticket1229/trac1229.patch) by was created at 2007-11-21 12:49:59",
    "created_at": "2007-11-21T12:49:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1229#issuecomment-7644",
    "user": "was"
}
```

Attachment [trac1229.patch](tarball://root/attachments/some-uuid/ticket1229/trac1229.patch) by was created at 2007-11-21 12:49:59



---

archive/issue_comments_007645.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-21T13:00:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1229#issuecomment-7645",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007646.json:
```json
{
    "body": "Merged in 2.8.13.rc2.",
    "created_at": "2007-11-21T13:00:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1229#issuecomment-7646",
    "user": "mabshoff"
}
```

Merged in 2.8.13.rc2.



---

archive/issue_comments_007647.json:
```json
{
    "body": "Changing assignee from was to mabshoff.",
    "created_at": "2007-11-21T13:00:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1229#issuecomment-7647",
    "user": "mabshoff"
}
```

Changing assignee from was to mabshoff.



---

archive/issue_comments_007648.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-21T13:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1229#issuecomment-7648",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007649.json:
```json
{
    "body": "Merged in 2.8.13.rc2.",
    "created_at": "2007-11-21T13:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1229#issuecomment-7649",
    "user": "mabshoff"
}
```

Merged in 2.8.13.rc2.
