# Issue 427: backslash infix operator does not print properly in documentation

archive/issues_000427.json:
```json
{
    "body": "Assignee: was\n\nCC:  mhansen\n\nThe infix operator '\\' does not print properly in the notebook\nwhen used in the examples of solve_right (for a matrix)\n(file:\n`local/lib/python/site-packages/sage/matrix/matrix2.pyx`)\nI suspect that these backslashes simply end up escaping the space after them. Some more preprocessing may be needed to escape backslashes occurring in examples in documentation?\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/427\n\n",
    "created_at": "2007-08-13T20:50:31Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "backslash infix operator does not print properly in documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/427",
    "user": "nbruin"
}
```
Assignee: was

CC:  mhansen

The infix operator '\' does not print properly in the notebook
when used in the examples of solve_right (for a matrix)
(file:
`local/lib/python/site-packages/sage/matrix/matrix2.pyx`)
I suspect that these backslashes simply end up escaping the space after them. Some more preprocessing may be needed to escape backslashes occurring in examples in documentation?


Issue created by migration from https://trac.sagemath.org/ticket/427





---

archive/issue_comments_002138.json:
```json
{
    "body": "Changing component from algebraic geometry to user interface.",
    "created_at": "2007-08-13T20:50:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/427#issuecomment-2138",
    "user": "nbruin"
}
```

Changing component from algebraic geometry to user interface.



---

archive/issue_comments_002139.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2007-08-13T20:50:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/427#issuecomment-2139",
    "user": "nbruin"
}
```

Changing priority from major to minor.



---

archive/issue_comments_002140.json:
```json
{
    "body": "What is the status here?\n\nCheers,\n\nMichael",
    "created_at": "2008-10-26T02:33:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/427#issuecomment-2140",
    "user": "mabshoff"
}
```

What is the status here?

Cheers,

Michael



---

archive/issue_comments_002141.json:
```json
{
    "body": "This behaves fine in the Sphinx documentation.",
    "created_at": "2009-01-22T13:57:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/427#issuecomment-2141",
    "user": "mhansen"
}
```

This behaves fine in the Sphinx documentation.



---

archive/issue_comments_002142.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2009-01-22T13:57:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/427#issuecomment-2142",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_002143.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-22T13:57:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/427#issuecomment-2143",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002144.json:
```json
{
    "body": "Yes, please close this.",
    "created_at": "2009-02-21T23:41:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/427#issuecomment-2144",
    "user": "jhpalmieri"
}
```

Yes, please close this.



---

archive/issue_comments_002145.json:
```json
{
    "body": "Replying to [comment:5 jhpalmieri]:\n> Yes, please close this.\n\nThanks John, this will be closed once the ReST patches are in.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-21T23:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/427#issuecomment-2145",
    "user": "mabshoff"
}
```

Replying to [comment:5 jhpalmieri]:
> Yes, please close this.

Thanks John, this will be closed once the ReST patches are in.

Cheers,

Michael



---

archive/issue_comments_002146.json:
```json
{
    "body": "Fixed by the ReST merge in 3.4.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T19:57:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/427#issuecomment-2146",
    "user": "mabshoff"
}
```

Fixed by the ReST merge in 3.4.alpha0.

Cheers,

Michael



---

archive/issue_comments_002147.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T19:57:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/427#issuecomment-2147",
    "user": "mabshoff"
}
```

Resolution: fixed
