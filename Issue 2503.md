# Issue 2503: Sage 2.10.4.alpha4: doctest failout in sage/misc/functional.py from #2421

archive/issues_002503.json:
```json
{
    "body": "Assignee: failure\n\nThe following doctest failure in sage/misc/functional.py happends due to #2421:\n\n```\nsage -t -long devel/sage-main/sage/misc/functional.py\n**********************************************************************\nFile \"functional.py\", line 848:\n    sage: round(b)\nExpected:\n    5.0000000000000000\nGot:\n    5\n**********************************************************************\n1 items had failures:\n   1 of   5 in __main__.example_52\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctest_functional.py\n         [5.0 s]\nexit code: 256\n\n----------------------------------------------------------------------\n```\n\nThe fix is obvious - patch coming up.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2503\n\n",
    "created_at": "2008-03-12T21:19:49Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "Sage 2.10.4.alpha4: doctest failout in sage/misc/functional.py from #2421",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2503",
    "user": "mabshoff"
}
```
Assignee: failure

The following doctest failure in sage/misc/functional.py happends due to #2421:

```
sage -t -long devel/sage-main/sage/misc/functional.py
**********************************************************************
File "functional.py", line 848:
    sage: round(b)
Expected:
    5.0000000000000000
Got:
    5
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_52
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_functional.py
         [5.0 s]
exit code: 256

----------------------------------------------------------------------
```

The fix is obvious - patch coming up.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/2503





---

archive/issue_comments_016959.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-03-12T21:23:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2503#issuecomment-16959",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_016960.json:
```json
{
    "body": "Works for me.",
    "created_at": "2008-03-13T02:54:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2503#issuecomment-16960",
    "user": "mhansen"
}
```

Works for me.



---

archive/issue_comments_016961.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-13T06:01:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2503#issuecomment-16961",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016962.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-13T06:01:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2503#issuecomment-16962",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.4.alpha0
