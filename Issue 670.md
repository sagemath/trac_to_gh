# Issue 670: Solaris 10: functions/piecewise.py doctests failure (numerical)

archive/issues_000670.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage -t  functions/piecewise.py                             **********************************************************************\nFile \"piecewise.py\", line 514:\n    sage: f(2.5)\nExpected:\n    12.18249396070347\nGot:\n    12.18249396070348\n**********************************************************************\n1 items had failures:\n   1 of   8 in __main__.example_13\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctest_piecewise.py\n         [10.0 s]\nsage -t  functions/special.py                               **********************************************************************\nFile \"special.py\", line 689:\n    sage: float(inverse_jacobi(\"sn\",0.47,1/2))\nExpected:\n    0.4990982313222197\nGot:\n    0.49909823132221959\n**********************************************************************\nFile \"special.py\", line 691:\n    sage: float(inverse_jacobi(\"sn\",0.4707504,0.5))\nExpected:\n    0.49999991146655459\nGot:\n    0.49999991146655481\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/670\n\n",
    "created_at": "2007-09-17T00:30:48Z",
    "labels": [
        "packages",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.1",
    "title": "Solaris 10: functions/piecewise.py doctests failure (numerical)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/670",
    "user": "mabshoff"
}
```
Assignee: was


```
sage -t  functions/piecewise.py                             **********************************************************************
File "piecewise.py", line 514:
    sage: f(2.5)
Expected:
    12.18249396070347
Got:
    12.18249396070348
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_13
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_piecewise.py
         [10.0 s]
sage -t  functions/special.py                               **********************************************************************
File "special.py", line 689:
    sage: float(inverse_jacobi("sn",0.47,1/2))
Expected:
    0.4990982313222197
Got:
    0.49909823132221959
**********************************************************************
File "special.py", line 691:
    sage: float(inverse_jacobi("sn",0.4707504,0.5))
Expected:
    0.49999991146655459
Got:
    0.49999991146655481
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/670





---

archive/issue_comments_003471.json:
```json
{
    "body": "Changing component from packages to doctest.",
    "created_at": "2007-09-17T01:23:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/670#issuecomment-3471",
    "user": "mabshoff"
}
```

Changing component from packages to doctest.



---

archive/issue_comments_003472.json:
```json
{
    "body": "Changing assignee from was to failure.",
    "created_at": "2007-09-17T01:23:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/670#issuecomment-3472",
    "user": "mabshoff"
}
```

Changing assignee from was to failure.



---

archive/issue_comments_003473.json:
```json
{
    "body": "Attachment [Sage-2.9-fix-numerical-doctests-in-piecewise.py-Solaris10.patch](tarball://root/attachments/some-uuid/ticket670/Sage-2.9-fix-numerical-doctests-in-piecewise.py-Solaris10.patch) by mabshoff created at 2007-12-21 12:50:32",
    "created_at": "2007-12-21T12:50:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/670#issuecomment-3473",
    "user": "mabshoff"
}
```

Attachment [Sage-2.9-fix-numerical-doctests-in-piecewise.py-Solaris10.patch](tarball://root/attachments/some-uuid/ticket670/Sage-2.9-fix-numerical-doctests-in-piecewise.py-Solaris10.patch) by mabshoff created at 2007-12-21 12:50:32



---

archive/issue_comments_003474.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-22T01:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/670#issuecomment-3474",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_003475.json:
```json
{
    "body": "merged in 2.9.1 alpha3",
    "created_at": "2007-12-22T01:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/670#issuecomment-3475",
    "user": "rlm"
}
```

merged in 2.9.1 alpha3
