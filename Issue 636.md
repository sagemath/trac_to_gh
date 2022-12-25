# Issue 636: cvxopt doesn't fully work yet in SAGE under Linux

archive/issues_000636.json:
```json
{
    "body": "Assignee: jkantor\n\nIf I build cvxopt on any *Linux* system, then it doesn't work, as follows:\n\n```\nsage: import cvxopt.base\n---------------------------------------------------------------------------\n<type 'exceptions.ImportError'>           Traceback (most recent call last)\n\n/home2/sage/<ipython console> in <module>()\n\n<type 'exceptions.ImportError'>: /home2/sage/s/local/lib/python2.5/site-packages/cvxopt/base.so: undefined symbol: _g95_ioparm\n```\n\n\nWe need to:\n1. Figure out why this fails.\n\n2. Add doctests to SAGE core library to illustrate cvxopt and make sure it fully work, so the above sort of thing won't happen again.  Base these on the cvxopt tutorial, etc.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/636\n\n",
    "created_at": "2007-09-10T21:51:52Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "cvxopt doesn't fully work yet in SAGE under Linux",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/636",
    "user": "https://github.com/williamstein"
}
```
Assignee: jkantor

If I build cvxopt on any *Linux* system, then it doesn't work, as follows:

```
sage: import cvxopt.base
---------------------------------------------------------------------------
<type 'exceptions.ImportError'>           Traceback (most recent call last)

/home2/sage/<ipython console> in <module>()

<type 'exceptions.ImportError'>: /home2/sage/s/local/lib/python2.5/site-packages/cvxopt/base.so: undefined symbol: _g95_ioparm
```


We need to:
1. Figure out why this fails.

2. Add doctests to SAGE core library to illustrate cvxopt and make sure it fully work, so the above sort of thing won't happen again.  Base these on the cvxopt tutorial, etc.  

Issue created by migration from https://trac.sagemath.org/ticket/636





---

archive/issue_comments_003266.json:
```json
{
    "body": "Changing component from algebraic geometry to packages.",
    "created_at": "2007-09-11T05:25:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/636#issuecomment-3266",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from algebraic geometry to packages.



---

archive/issue_comments_003267.json:
```json
{
    "body": "Yep, in retroperspective I am surprised that nobody caught the issue earlier. I never got cvxopt to compile on Solaris (it complains about a missing complex.h), but there were no specific doctest failures that I could attribute to the missing cvxopt.\n\nCheers,\n\nMichael",
    "created_at": "2007-09-11T05:25:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/636#issuecomment-3267",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Yep, in retroperspective I am surprised that nobody caught the issue earlier. I never got cvxopt to compile on Solaris (it complains about a missing complex.h), but there were no specific doctest failures that I could attribute to the missing cvxopt.

Cheers,

Michael



---

archive/issue_comments_003268.json:
```json
{
    "body": "This ticket is related to #709 and #636. Once #709 goes in the other two tickets should be resolved.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-19T18:41:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/636#issuecomment-3268",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This ticket is related to #709 and #636. Once #709 goes in the other two tickets should be resolved.

Cheers,

Michael



---

archive/issue_events_001696.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-19T18:41:27Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/636",
    "milestone": "sage-2.8.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/636#event-1696"
}
```



---

archive/issue_comments_003269.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-20T20:21:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/636#issuecomment-3269",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_001697.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-20T20:21:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/636",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/636#event-1697"
}
```
