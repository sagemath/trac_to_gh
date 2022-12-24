# Issue 2071: SymbolicExpression conjugate() method assumes variables are real

archive/issues_002071.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: var('x')\nx\nsage: x.conjugate()\nx\n```\n\n\nUnder the assumption that x might be complex, this should really return conjugate(x).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2071\n\n",
    "created_at": "2008-02-06T06:37:57Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "SymbolicExpression conjugate() method assumes variables are real",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2071",
    "user": "cwitty"
}
```
Assignee: was


```
sage: var('x')
x
sage: x.conjugate()
x
```


Under the assumption that x might be complex, this should really return conjugate(x).


Issue created by migration from https://trac.sagemath.org/ticket/2071





---

archive/issue_comments_013394.json:
```json
{
    "body": "Changing assignee from was to gfurnish.",
    "created_at": "2008-03-16T20:10:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2071#issuecomment-13394",
    "user": "gfurnish"
}
```

Changing assignee from was to gfurnish.



---

archive/issue_comments_013395.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-16T20:10:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2071#issuecomment-13395",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_013396.json:
```json
{
    "body": "This could be handled using Maxima's declare facility:\n\n\n```\nsage: sage.calculus.calculus.maxima.eval('declare(x, complex)')\n'done'\nsage: x.conjugate()\nconjugate(x)\n```\n\n\nThis also fixed by Pynac:\n\n\n```\nsage: x = var('x', ns=1)\nsage: x\nx\nsage: x.conjugate()\nconjugate(x)\n```\n",
    "created_at": "2008-11-14T09:13:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2071#issuecomment-13396",
    "user": "mhansen"
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

archive/issue_comments_013397.json:
```json
{
    "body": "This is fixed in 4.0.rc0. There is a doctest in line 3871 of sage/symbolic/expression.pyx.\n\nThis bug should be closed as fixed.",
    "created_at": "2009-05-25T09:27:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2071#issuecomment-13397",
    "user": "burcin"
}
```

This is fixed in 4.0.rc0. There is a doctest in line 3871 of sage/symbolic/expression.pyx.

This bug should be closed as fixed.



---

archive/issue_comments_013398.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-26T16:17:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2071#issuecomment-13398",
    "user": "mhansen"
}
```

Resolution: fixed
