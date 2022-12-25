# Issue 6789: 2 doctest failures in devel/sage/sage/symbolic/expression.pyx

archive/issues_006789.json:
```json
{
    "body": "Assignee: tbd\n\nOn Solaris 10 update 7 (SPARC), the following tests failed. Both ECL and Maxima were updated - ECL version 9.8.4, Maxima version 5.19.1. Sage was built with gcc 4.4.1\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nThu Aug 20 20:02:37 BST 2009\ndsage-trial tmp directory doesn't exist - creating ...\nThis script will run the unit tests for DSage\n```\n\n<SNIP>\n| Sage Version 4.1.1, Release Date: 2009-08-14                       |\n| Type notebook() for the GUI, and license() for information.        |\n\n```\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/symbolic/expression.pyx\", line 5541:\n    sage: solve(Q*sqrt(Q^2 + 2) - 1,Q)\nExpected:\n    [Q == 1/sqrt(-sqrt(2) + 1), Q == 1/sqrt(sqrt(2) + 1)]\nGot:\n/ailures\nGot:\n    [Q == 1/sqrt(sqrt(2) + 1)]\n**********************************************************************\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/symbolic/expression.pyx\", line 2467:\n    sage: sin(x/2).expand_trig(half_angles=True)\nExpected:\n    1/2*sqrt(-cos(x) + 1)*sqrt(2)\nGot:\n    1/2*sqrt(-cos(x) + 1)*sqrt(2)*(-1)^floor(1/2*x/pi)\n**********************************************************************\n2 items had failures:\n   1 of   6 in __main__.example_138\n   1 of  13 in __main__.example_61\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /export/home/drkirkby/sage/sage-4.1.1/tmp/.doctest_expression.py\n         [116.1 s]\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6789\n\n",
    "created_at": "2009-08-20T22:21:10Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "2 doctest failures in devel/sage/sage/symbolic/expression.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6789",
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
| Sage Version 4.1.1, Release Date: 2009-08-14                       |
| Type notebook() for the GUI, and license() for information.        |

```
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/symbolic/expression.pyx", line 5541:
    sage: solve(Q*sqrt(Q^2 + 2) - 1,Q)
Expected:
    [Q == 1/sqrt(-sqrt(2) + 1), Q == 1/sqrt(sqrt(2) + 1)]
Got:
/ailures
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
For whitespace errors, see the file /export/home/drkirkby/sage/sage-4.1.1/tmp/.doctest_expression.py
         [116.1 s]

```


Issue created by migration from https://trac.sagemath.org/ticket/6789





---

archive/issue_comments_055849.json:
```json
{
    "body": "Changing keywords from \"\" to \"maxima\".",
    "created_at": "2009-08-20T23:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6789#issuecomment-55849",
    "user": "https://github.com/aghitza"
}
```

Changing keywords from "" to "maxima".



---

archive/issue_comments_055850.json:
```json
{
    "body": "This is fixed by #6699.",
    "created_at": "2009-09-02T11:02:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6789#issuecomment-55850",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

This is fixed by #6699.



---

archive/issue_comments_055851.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-02T11:02:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6789#issuecomment-55851",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
