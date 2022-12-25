# Issue 6791: 2 doctest failures in devel/sage/sage/symbolic/expression.pyx

archive/issues_006791.json:
```json
{
    "body": "Assignee: tbd\n\nOn Solaris 10 update 7 (SPARC), the following tests failed. Both ECL and Maxima were updated - ECL version 9.8.4, Maxima version 5.19.1. Sage was built with gcc 4.4.1\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nThu Aug 20 20:02:37 BST 2009\ndsage-trial tmp directory doesn't exist - creating ...\nThis script will run the unit tests for DSage\n```\n\n<SNIP>\n\n```\n**********************************************************************\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/symbolic/expression.pyx\", line 5541:\n    sage: solve(Q*sqrt(Q^2 + 2) - 1,Q)\nExpected:\n    [Q == 1/sqrt(-sqrt(2) + 1), Q == 1/sqrt(sqrt(2) + 1)]\nGot:\n    [Q == 1/sqrt(sqrt(2) + 1)]\n**********************************************************************\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/symbolic/expression.pyx\", line 2467:\n    sage: sin(x/2).expand_trig(half_angles=True)\nExpected:\n    1/2*sqrt(-cos(x) + 1)*sqrt(2)\nGot:\n    1/2*sqrt(-cos(x) + 1)*sqrt(2)*(-1)^floor(1/2*x/pi)\n**********************************************************************\n2 items had failures:\n   1 of   6 in __main__.example_138\n   1 of  13 in __main__.example_61\n***Test Failed*** 2 failures.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6791\n\n",
    "created_at": "2009-08-20T22:45:07Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "2 doctest failures in devel/sage/sage/symbolic/expression.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6791",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

On Solaris 10 update 7 (SPARC), the following tests failed. Both ECL and Maxima were updated - ECL version 9.8.4, Maxima version 5.19.1. Sage was built with gcc 4.4.1

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Thu Aug 20 20:02:37 BST 2009
dsage-trial tmp directory doesn't exist - creating ...
This script will run the unit tests for DSage
```

<SNIP>

```
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/symbolic/expression.pyx", line 5541:
    sage: solve(Q*sqrt(Q^2 + 2) - 1,Q)
Expected:
    [Q == 1/sqrt(-sqrt(2) + 1), Q == 1/sqrt(sqrt(2) + 1)]
Got:
    [Q == 1/sqrt(sqrt(2) + 1)]
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/symbolic/expression.pyx", line 2467:
    sage: sin(x/2).expand_trig(half_angles=True)
Expected:
    1/2*sqrt(-cos(x) + 1)*sqrt(2)
Got:
    1/2*sqrt(-cos(x) + 1)*sqrt(2)*(-1)^floor(1/2*x/pi)
**********************************************************************
2 items had failures:
   1 of   6 in __main__.example_138
   1 of  13 in __main__.example_61
***Test Failed*** 2 failures.
```


Issue created by migration from https://trac.sagemath.org/ticket/6791





---

archive/issue_comments_055856.json:
```json
{
    "body": "Duplicate of #6789.",
    "created_at": "2009-08-20T23:59:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6791#issuecomment-55856",
    "user": "https://github.com/aghitza"
}
```

Duplicate of #6789.



---

archive/issue_comments_055857.json:
```json
{
    "body": "To release manager: Sounds like this should be closed, then.",
    "created_at": "2009-09-15T13:11:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6791#issuecomment-55857",
    "user": "https://github.com/kcrisman"
}
```

To release manager: Sounds like this should be closed, then.



---

archive/issue_comments_055858.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-10-05T14:17:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6791#issuecomment-55858",
    "user": "https://github.com/williamstein"
}
```

Resolution: duplicate



---

archive/issue_events_015995.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-10-05T14:17:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6791",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6791#event-15995"
}
```



---

archive/issue_events_015996.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-10-14T17:00:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6791",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6791#event-15996"
}
```
