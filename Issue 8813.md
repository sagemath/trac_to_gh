# Issue 8813: symbolic expression -- doctest failure in sage-4.4.1.alpha0

archive/issues_008813.json:
```json
{
    "body": "Assignee: @burcin\n\n\n```\n**********************************************************************\nFile \"/mnt/usb1/scratch/wstein/build/release/4.4.1/sage-4.4.1.alpha1/devel/sage/sage/symbolic/expression.pyx\", line 1284:\n    sage: (-t0)._is_negative()\nExpected:\n    False\nGot:\n    True\n**********************************************************************\n1 items had failures:\n   1 of   6 in __main__.example_40\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/wstein/sage//tmp/.doctest_expression.py\n         [34.8 s]\n\n-----------------------------------------------\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8813\n\n",
    "created_at": "2010-04-29T00:33:47Z",
    "labels": [
        "calculus",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "symbolic expression -- doctest failure in sage-4.4.1.alpha0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8813",
    "user": "@williamstein"
}
```
Assignee: @burcin


```
**********************************************************************
File "/mnt/usb1/scratch/wstein/build/release/4.4.1/sage-4.4.1.alpha1/devel/sage/sage/symbolic/expression.pyx", line 1284:
    sage: (-t0)._is_negative()
Expected:
    False
Got:
    True
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_40
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/wstein/sage//tmp/.doctest_expression.py
         [34.8 s]

-----------------------------------------------
```


Issue created by migration from https://trac.sagemath.org/ticket/8813





---

archive/issue_comments_080897.json:
```json
{
    "body": "This is fixed by the patch at #8565.",
    "created_at": "2010-04-29T03:28:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8813#issuecomment-80897",
    "user": "@burcin"
}
```

This is fixed by the patch at #8565.



---

archive/issue_comments_080898.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-04-29T04:19:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8813#issuecomment-80898",
    "user": "@williamstein"
}
```

Resolution: duplicate
