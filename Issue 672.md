# Issue 672: Solaris 10: rings/complex_double.pyx doctests failure: nan vs. NaN

archive/issues_000672.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: Solaris 10, doctest, complex double\n\n\n```\nsage -t  rings/complex_double.pyx                           **********************************************************************\nFile \"complex_double.pyx\", line 621:\n    sage: ~(0*CDF(0,1))\nExpected:\n    nan + nan*I\nGot:\n    -NaN + NaN*I\n**********************************************************************\nFile \"complex_double.pyx\", line 1470:\n    sage: z^2 - z + 1\nExpected:\n    2.22044604925e-16 + 1.11022302463e-16*I\nGot:\n    2.22044604925e-16 + 2.22044604925e-16*I\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/672\n\n",
    "created_at": "2007-09-17T00:33:34Z",
    "labels": [
        "component: packages",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "Solaris 10: rings/complex_double.pyx doctests failure: nan vs. NaN",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/672",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @williamstein

Keywords: Solaris 10, doctest, complex double


```
sage -t  rings/complex_double.pyx                           **********************************************************************
File "complex_double.pyx", line 621:
    sage: ~(0*CDF(0,1))
Expected:
    nan + nan*I
Got:
    -NaN + NaN*I
**********************************************************************
File "complex_double.pyx", line 1470:
    sage: z^2 - z + 1
Expected:
    2.22044604925e-16 + 1.11022302463e-16*I
Got:
    2.22044604925e-16 + 2.22044604925e-16*I
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/672





---

archive/issue_comments_003467.json:
```json
{
    "body": "Changing component from packages to doctest.",
    "created_at": "2007-09-17T01:24:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/672#issuecomment-3467",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from packages to doctest.



---

archive/issue_comments_003468.json:
```json
{
    "body": "Changing assignee from @williamstein to failure.",
    "created_at": "2007-09-17T01:24:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/672#issuecomment-3468",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to failure.



---

archive/issue_comments_003469.json:
```json
{
    "body": "This has been fixed in Sage 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-17T10:54:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/672#issuecomment-3469",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This has been fixed in Sage 3.4.1.

Cheers,

Michael



---

archive/issue_comments_003470.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-17T10:54:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/672#issuecomment-3470",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
