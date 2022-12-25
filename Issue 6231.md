# Issue 6231: Solving a system of equations ignores multiplicities

archive/issues_006231.json:
```json
{
    "body": "Keywords: multiplicities system of equations\n\nA follow-up from http://groups.google.com/group/sage-support/browse_thread/thread/d8e22deb18d97253 but different from #6228:\n\n```\nsage: solve((x^2-1)^3==0, x, multiplicities=True)\n([x == -1, x == 1], [3, 3])\nsage: solve(((x^2-1)^3==0,(x^2-1)^3==0), x, multiplicities=True)\n[[x == 1], [x == -1]]\n```\n\nSo, at least in this example, we get the correct multiplicities for a single equation, but we don't get any multiplicity when the same equation together with a copy of itself forms a *system* of equations.\n\nNote that ``maxima`` provides the correct answer:\n\n```\nsage: maxima.eval('solve(((x^2-1)^3,(x^2-1)^3),x)')\n'[x=-1,x=1]'\nsage: maxima.eval('multiplicities')\n'[3,3]'\n\n```\n\nProbably this bug can be easily done by working at the code of the ``solve`` command.\n\nWhat format should the multiplicities be provided in?\n\n- When one solves a single equation with a single variable, the solutions are given by a simple list. Accordingly, the multiplicities are given as a simple list.\n- When a system of equations in a single variable is given, the solutions are given by a list of lists. So, should the multiplicities be given by a list of lists?\n\nIssue created by migration from https://trac.sagemath.org/ticket/6231\n\n",
    "created_at": "2009-06-06T07:20:46Z",
    "labels": [
        "component: symbolics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-wishlist",
    "title": "Solving a system of equations ignores multiplicities",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6231",
    "user": "https://github.com/simon-king-jena"
}
```
Keywords: multiplicities system of equations

A follow-up from http://groups.google.com/group/sage-support/browse_thread/thread/d8e22deb18d97253 but different from #6228:

```
sage: solve((x^2-1)^3==0, x, multiplicities=True)
([x == -1, x == 1], [3, 3])
sage: solve(((x^2-1)^3==0,(x^2-1)^3==0), x, multiplicities=True)
[[x == 1], [x == -1]]
```

So, at least in this example, we get the correct multiplicities for a single equation, but we don't get any multiplicity when the same equation together with a copy of itself forms a *system* of equations.

Note that ``maxima`` provides the correct answer:

```
sage: maxima.eval('solve(((x^2-1)^3,(x^2-1)^3),x)')
'[x=-1,x=1]'
sage: maxima.eval('multiplicities')
'[3,3]'

```

Probably this bug can be easily done by working at the code of the ``solve`` command.

What format should the multiplicities be provided in?

- When one solves a single equation with a single variable, the solutions are given by a simple list. Accordingly, the multiplicities are given as a simple list.
- When a system of equations in a single variable is given, the solutions are given by a list of lists. So, should the multiplicities be given by a list of lists?

Issue created by migration from https://trac.sagemath.org/ticket/6231





---

archive/issue_events_014607.json:
```json
{
    "actor": "https://github.com/simon-king-jena",
    "created_at": "2009-06-06T16:33:24Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6231",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6231#event-14607"
}
```
