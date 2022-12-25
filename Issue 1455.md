# Issue 1455: 2.9.alpha4: numerical noise doctest failure on OSX 10.4

archive/issues_001455.json:
```json
{
    "body": "Assignee: mabshoff\n\nRishikesh reported:\n\n```\nsage -t  devel/sage-main/sage/numerical/optimize.py\n**********************************************************************\nFile \"optimize.py\", line 93:\n    sage: find_maximum_on_interval(f, 0,5)\nExpected:\n    (0.561096338191, 0.860333589015)\nGot:\n    (0.561096338191, 0.860333589074)\n**********************************************************************\n\nsage -t  devel/sage-main/sage/calculus/calculus.py\n********************\n**************************************************\nFile \"calculus.py\", line 2446:\n    sage: f.find_maximum_on_interval(0,5)\nExpected:\n    (0.5610963381910451, 0.860333589015)\nGot:\n    (0.5610963381910451, 0.860333589074)\n********************************************************************** \n```\n\n\nCheers,\nMichael\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1455\n\n",
    "created_at": "2007-12-10T22:40:47Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "2.9.alpha4: numerical noise doctest failure on OSX 10.4",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1455",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Rishikesh reported:

```
sage -t  devel/sage-main/sage/numerical/optimize.py
**********************************************************************
File "optimize.py", line 93:
    sage: find_maximum_on_interval(f, 0,5)
Expected:
    (0.561096338191, 0.860333589015)
Got:
    (0.561096338191, 0.860333589074)
**********************************************************************

sage -t  devel/sage-main/sage/calculus/calculus.py
********************
**************************************************
File "calculus.py", line 2446:
    sage: f.find_maximum_on_interval(0,5)
Expected:
    (0.5610963381910451, 0.860333589015)
Got:
    (0.5610963381910451, 0.860333589074)
********************************************************************** 
```


Cheers,
Michael


Issue created by migration from https://trac.sagemath.org/ticket/1455





---

archive/issue_comments_009356.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-10T22:41:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1455#issuecomment-9356",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009357.json:
```json
{
    "body": "Merged in 2.9.alpha5.",
    "created_at": "2007-12-11T01:01:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1455#issuecomment-9357",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.alpha5.



---

archive/issue_comments_009358.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-11T01:01:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1455#issuecomment-9358",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
