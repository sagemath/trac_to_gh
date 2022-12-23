# Issue 9458: Bug with variable names in solve()

archive/issues_009458.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nKeywords: var solve name factorial\n\nSome variable names yield strange behavior with the solve() function. Here is an example:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: var('d2 d3 x')\n(d2, d3, x)\nsage: solve((d2+d3)*x==1, x)\n[x == factorial(2*k + 6*n)/(d3*factorial(2*k + 6*n) + factorial(k + 3*n - 1))]\n```\n\n| Sage Version 4.4.2, Release Date: 2010-05-19                       |\n| Type notebook() for the GUI, and license() for information.        |\nThese factorials are strange. They don't occur with other variable names, e.g.,\n\n\n```\nsage: var('y1 y2 x')\n(y1, y2, x)\nsage: solve((y1+y2)*x==1, x)\n[x == (1/(y1 + y2))]\n```\n\n\nDocumentation for solve() does not mention reserved variable names.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9458\n\n",
    "created_at": "2010-07-08T18:33:47Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "Bug with variable names in solve()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9458",
    "user": "tastalian"
}
```
Assignee: AlexGhitza

Keywords: var solve name factorial

Some variable names yield strange behavior with the solve() function. Here is an example:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: var('d2 d3 x')
(d2, d3, x)
sage: solve((d2+d3)*x==1, x)
[x == factorial(2*k + 6*n)/(d3*factorial(2*k + 6*n) + factorial(k + 3*n - 1))]
```

| Sage Version 4.4.2, Release Date: 2010-05-19                       |
| Type notebook() for the GUI, and license() for information.        |
These factorials are strange. They don't occur with other variable names, e.g.,


```
sage: var('y1 y2 x')
(y1, y2, x)
sage: solve((y1+y2)*x==1, x)
[x == (1/(y1 + y2))]
```


Documentation for solve() does not mention reserved variable names.

Issue created by migration from https://trac.sagemath.org/ticket/9458





---

archive/issue_comments_090677.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-07-08T19:37:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9458#issuecomment-90677",
    "user": "mhansen"
}
```

Resolution: duplicate



---

archive/issue_comments_090678.json:
```json
{
    "body": "This is basically a duplicate of #8734.",
    "created_at": "2010-07-08T19:37:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9458#issuecomment-90678",
    "user": "mhansen"
}
```

This is basically a duplicate of #8734.
