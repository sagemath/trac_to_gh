# Issue 3562: Do not doctest pbuild files in devel/sage

archive/issues_003562.json:
```json
{
    "body": "Assignee: mabshoff\n\nCurrently `-tp` doctests the three pbuild files \n\n* sagebuild.py\n* clib.py\n* build.py\n\nDon't do it :).\n\nI need to check if `-t` also picks up those files or if they are treated differently. We certainly don't doctest setup.py.\n\nCheers,\n\nMichael\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3562\n\n",
    "created_at": "2008-07-06T11:35:14Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Do not doctest pbuild files in devel/sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3562",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Currently `-tp` doctests the three pbuild files 

* sagebuild.py
* clib.py
* build.py

Don't do it :).

I need to check if `-t` also picks up those files or if they are treated differently. We certainly don't doctest setup.py.

Cheers,

Michael


Issue created by migration from https://trac.sagemath.org/ticket/3562





---

archive/issue_comments_025172.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-07-06T11:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3562#issuecomment-25172",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_025173.json:
```json
{
    "body": "I now tend to blame this on my stupidity doctesting devel/sage instead of devel/sage/sage as I should. But I am also wondering whether to add `nodoctest` to the three files above nonetheless to prevent accidental testing.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-06T17:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3562#issuecomment-25173",
    "user": "mabshoff"
}
```

I now tend to blame this on my stupidity doctesting devel/sage instead of devel/sage/sage as I should. But I am also wondering whether to add `nodoctest` to the three files above nonetheless to prevent accidental testing.

Cheers,

Michael



---

archive/issue_comments_025174.json:
```json
{
    "body": "This is invalid and just to blame on my stupidity.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-06T17:43:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3562#issuecomment-25174",
    "user": "mabshoff"
}
```

This is invalid and just to blame on my stupidity.

Cheers,

Michael



---

archive/issue_comments_025175.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-07-06T17:43:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3562#issuecomment-25175",
    "user": "mabshoff"
}
```

Resolution: invalid
