# Issue 7281: numerical noise issue on fedora32 for 4.2.alpha1

archive/issues_007281.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nsage -t -long \"devel/sage/doc/en/tutorial/tour_algebra.rst\" \n**********************************************************************\nFile \"/tmp/wstein/farm/sage-4.2.alpha1/devel/sage/doc/en/tutorial/tour_algebra.rst\", line 87:\n    sage: find_root(cos(phi)==sin(phi),0,pi/2)\nExpected:\n    0.78539816339744839\nGot:\n    0.78539816339744828\n**********************************************************************\n1 items had failures:\n   1 of   4 in __main__.example_5\n***Test Failed*** 1 failures.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7281\n\n",
    "created_at": "2009-10-24T03:35:08Z",
    "labels": [
        "doctest coverage",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "numerical noise issue on fedora32 for 4.2.alpha1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7281",
    "user": "mhansen"
}
```
Assignee: tbd


```
sage -t -long "devel/sage/doc/en/tutorial/tour_algebra.rst" 
**********************************************************************
File "/tmp/wstein/farm/sage-4.2.alpha1/devel/sage/doc/en/tutorial/tour_algebra.rst", line 87:
    sage: find_root(cos(phi)==sin(phi),0,pi/2)
Expected:
    0.78539816339744839
Got:
    0.78539816339744828
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_5
***Test Failed*** 1 failures.
```


Issue created by migration from https://trac.sagemath.org/ticket/7281





---

archive/issue_comments_060604.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-10-24T03:40:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7281#issuecomment-60604",
    "user": "mhansen"
}
```

Resolution: duplicate



---

archive/issue_comments_060605.json:
```json
{
    "body": "Duplicate of #7275",
    "created_at": "2009-10-24T03:40:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7281#issuecomment-60605",
    "user": "mhansen"
}
```

Duplicate of #7275
