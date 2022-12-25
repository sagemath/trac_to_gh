# Issue 427: backslash infix operator does not print properly in documentation

archive/issues_000427.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @mwhansen\n\nThe infix operator '\\' does not print properly in the notebook\nwhen used in the examples of solve_right (for a matrix)\n(file:\n`local/lib/python/site-packages/sage/matrix/matrix2.pyx`)\nI suspect that these backslashes simply end up escaping the space after them. Some more preprocessing may be needed to escape backslashes occurring in examples in documentation?\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/427\n\n",
    "created_at": "2007-08-13T20:50:31Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "backslash infix operator does not print properly in documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/427",
    "user": "https://github.com/nbruin"
}
```
Assignee: @williamstein

CC:  @mwhansen

The infix operator '\' does not print properly in the notebook
when used in the examples of solve_right (for a matrix)
(file:
`local/lib/python/site-packages/sage/matrix/matrix2.pyx`)
I suspect that these backslashes simply end up escaping the space after them. Some more preprocessing may be needed to escape backslashes occurring in examples in documentation?


Issue created by migration from https://trac.sagemath.org/ticket/427





---

archive/issue_comments_002129.json:
```json
{
    "body": "Changing component from algebraic geometry to user interface.",
    "created_at": "2007-08-13T20:50:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/427#issuecomment-2129",
    "user": "https://github.com/nbruin"
}
```

Changing component from algebraic geometry to user interface.



---

archive/issue_comments_002130.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2007-08-13T20:50:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/427#issuecomment-2130",
    "user": "https://github.com/nbruin"
}
```

Changing priority from major to minor.



---

archive/issue_comments_002131.json:
```json
{
    "body": "What is the status here?\n\nCheers,\n\nMichael",
    "created_at": "2008-10-26T02:33:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/427#issuecomment-2131",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

What is the status here?

Cheers,

Michael



---

archive/issue_events_001043.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-01-22T13:57:45Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/427",
    "milestone": "sage-3.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/427#event-1043"
}
```



---

archive/issue_comments_002132.json:
```json
{
    "body": "This behaves fine in the Sphinx documentation.",
    "created_at": "2009-01-22T13:57:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/427#issuecomment-2132",
    "user": "https://github.com/mwhansen"
}
```

This behaves fine in the Sphinx documentation.



---

archive/issue_comments_002133.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2009-01-22T13:57:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/427#issuecomment-2133",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_002134.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-22T13:57:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/427#issuecomment-2134",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002135.json:
```json
{
    "body": "Yes, please close this.",
    "created_at": "2009-02-21T23:41:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/427#issuecomment-2135",
    "user": "https://github.com/jhpalmieri"
}
```

Yes, please close this.



---

archive/issue_comments_002136.json:
```json
{
    "body": "Replying to [comment:5 jhpalmieri]:\n> Yes, please close this.\n\n\nThanks John, this will be closed once the ReST patches are in.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-21T23:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/427#issuecomment-2136",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:5 jhpalmieri]:
> Yes, please close this.


Thanks John, this will be closed once the ReST patches are in.

Cheers,

Michael



---

archive/issue_events_001044.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-24T19:57:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/427",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/427#event-1044"
}
```



---

archive/issue_comments_002137.json:
```json
{
    "body": "Fixed by the ReST merge in 3.4.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T19:57:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/427#issuecomment-2137",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed by the ReST merge in 3.4.alpha0.

Cheers,

Michael



---

archive/issue_comments_002138.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T19:57:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/427#issuecomment-2138",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
