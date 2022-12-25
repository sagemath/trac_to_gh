# Issue 2071: SymbolicExpression conjugate() method assumes variables are real

archive/issues_002071.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\nsage: var('x')\nx\nsage: x.conjugate()\nx\n```\n\nUnder the assumption that x might be complex, this should really return conjugate(x).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2071\n\n",
    "created_at": "2008-02-06T06:37:57Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "SymbolicExpression conjugate() method assumes variables are real",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2071",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @williamstein

```
sage: var('x')
x
sage: x.conjugate()
x
```

Under the assumption that x might be complex, this should really return conjugate(x).


Issue created by migration from https://trac.sagemath.org/ticket/2071





---

archive/issue_comments_013363.json:
```json
{
    "body": "Changing assignee from @williamstein to @garyfurnish.",
    "created_at": "2008-03-16T20:10:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2071#issuecomment-13363",
    "user": "https://github.com/garyfurnish"
}
```

Changing assignee from @williamstein to @garyfurnish.



---

archive/issue_comments_013364.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-16T20:10:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2071#issuecomment-13364",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_013365.json:
```json
{
    "body": "This could be handled using Maxima's declare facility:\n\n```\nsage: sage.calculus.calculus.maxima.eval('declare(x, complex)')\n'done'\nsage: x.conjugate()\nconjugate(x)\n```\n\nThis also fixed by Pynac:\n\n```\nsage: x = var('x', ns=1)\nsage: x\nx\nsage: x.conjugate()\nconjugate(x)\n```",
    "created_at": "2008-11-14T09:13:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2071#issuecomment-13365",
    "user": "https://github.com/mwhansen"
}
```

This could be handled using Maxima's declare facility:

```
sage: sage.calculus.calculus.maxima.eval('declare(x, complex)')
'done'
sage: x.conjugate()
conjugate(x)
```

This also fixed by Pynac:

```
sage: x = var('x', ns=1)
sage: x
x
sage: x.conjugate()
conjugate(x)
```



---

archive/issue_comments_013366.json:
```json
{
    "body": "This is fixed in 4.0.rc0. There is a doctest in line 3871 of sage/symbolic/expression.pyx.\n\nThis bug should be closed as fixed.",
    "created_at": "2009-05-25T09:27:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2071#issuecomment-13366",
    "user": "https://github.com/burcin"
}
```

This is fixed in 4.0.rc0. There is a doctest in line 3871 of sage/symbolic/expression.pyx.

This bug should be closed as fixed.



---

archive/issue_events_004965.json:
```json
{
    "actor": "https://github.com/burcin",
    "created_at": "2009-05-25T09:27:32Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2071",
    "milestone": "sage-4.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2071#event-4965"
}
```



---

archive/issue_comments_013367.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-26T16:17:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2071#issuecomment-13367",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_004966.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-05-26T16:17:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2071",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2071#event-4966"
}
```
