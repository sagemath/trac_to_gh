# Issue 2940: symbolic equation arithmetic is to restrictive

archive/issues_002940.json:
```json
{
    "body": "Assignee: was\n\nThe following should all work \n\n\n```\nsage: var('x,y')\n(x, y)\nsage: (a < 1) + (b < 2)\nb + a < 3\nsage: (a < 1) + (b <= 2)\na + b < 3\nsage: (a <= 1) + (b == 2)\na + b <= 3\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2940\n\n",
    "created_at": "2008-04-16T09:07:51Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "symbolic equation arithmetic is to restrictive",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2940",
    "user": "robertwb"
}
```
Assignee: was

The following should all work 


```
sage: var('x,y')
(x, y)
sage: (a < 1) + (b < 2)
b + a < 3
sage: (a < 1) + (b <= 2)
a + b < 3
sage: (a <= 1) + (b == 2)
a + b <= 3
```


Issue created by migration from https://trac.sagemath.org/ticket/2940





---

archive/issue_comments_020252.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2940#issuecomment-20252",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_020253.json:
```json
{
    "body": "This can be closed as fixed. \n\nSupport for this was added by Robert during the symbolics push before 4.0. There are similar doctests to the ones in the description in sage/symbolic/expression.pyx lines 1526 and 6006.",
    "created_at": "2009-06-10T11:17:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2940#issuecomment-20253",
    "user": "burcin"
}
```

This can be closed as fixed. 

Support for this was added by Robert during the symbolics push before 4.0. There are similar doctests to the ones in the description in sage/symbolic/expression.pyx lines 1526 and 6006.



---

archive/issue_comments_020254.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-24T15:15:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2940#issuecomment-20254",
    "user": "rlm"
}
```

Resolution: fixed
