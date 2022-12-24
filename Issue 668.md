# Issue 668: Solaris 10: calculus/calculus.py doctests failure (numerical)

archive/issues_000668.json:
```json
{
    "body": "Assignee: was\n\nKeywords: Solaris 10, doctest\n\n\n```\nsage -t  calculus/calculus.py                               **********************************************************************\nFile \"calculus.py\", line 1695:\n    sage: f.nintegral(x, 0, 1)\nExpected:\n    (0.52848223531423055, 4.1633141378838452e-11, 231, 0)\nGot:\n    (0.52848223531423055, 4.163291933423352e-11, 231, 0)\n**********************************************************************\n1 items had failures:\n   1 of   3 in __main__.example_35\n***Test Failed*** 1 failures.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/668\n\n",
    "created_at": "2007-09-17T00:29:00Z",
    "labels": [
        "packages",
        "major",
        "bug"
    ],
    "title": "Solaris 10: calculus/calculus.py doctests failure (numerical)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/668",
    "user": "mabshoff"
}
```
Assignee: was

Keywords: Solaris 10, doctest


```
sage -t  calculus/calculus.py                               **********************************************************************
File "calculus.py", line 1695:
    sage: f.nintegral(x, 0, 1)
Expected:
    (0.52848223531423055, 4.1633141378838452e-11, 231, 0)
Got:
    (0.52848223531423055, 4.163291933423352e-11, 231, 0)
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_35
***Test Failed*** 1 failures.
```


Issue created by migration from https://trac.sagemath.org/ticket/668





---

archive/issue_comments_003462.json:
```json
{
    "body": "Changing component from packages to doctest.",
    "created_at": "2007-09-17T01:23:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/668#issuecomment-3462",
    "user": "mabshoff"
}
```

Changing component from packages to doctest.



---

archive/issue_comments_003463.json:
```json
{
    "body": "Changing assignee from was to failure.",
    "created_at": "2007-09-17T01:23:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/668#issuecomment-3463",
    "user": "mabshoff"
}
```

Changing assignee from was to failure.



---

archive/issue_comments_003464.json:
```json
{
    "body": "Attachment [Sage-2.9-fix-numerical-doctests-in-calculus.py-Solaris10.patch](tarball://root/attachments/some-uuid/ticket668/Sage-2.9-fix-numerical-doctests-in-calculus.py-Solaris10.patch) by mabshoff created at 2007-12-21 12:49:46",
    "created_at": "2007-12-21T12:49:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/668#issuecomment-3464",
    "user": "mabshoff"
}
```

Attachment [Sage-2.9-fix-numerical-doctests-in-calculus.py-Solaris10.patch](tarball://root/attachments/some-uuid/ticket668/Sage-2.9-fix-numerical-doctests-in-calculus.py-Solaris10.patch) by mabshoff created at 2007-12-21 12:49:46



---

archive/issue_comments_003465.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-22T01:06:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/668#issuecomment-3465",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_003466.json:
```json
{
    "body": "merged in 2.9.1 alpha3",
    "created_at": "2007-12-22T01:06:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/668#issuecomment-3466",
    "user": "rlm"
}
```

merged in 2.9.1 alpha3
