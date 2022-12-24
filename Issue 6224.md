# Issue 6224: sage startup takes way to long

archive/issues_006224.json:
```json
{
    "body": "Assignee: tbd\n\nThis is after the cache is warm, otherwise it's even worse: \n\n\n```\nRobert-Bradshaws-Laptop:~/sage robert$ echo \"\" | time sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: referee\nsage: sage: \nExiting SAGE (CPU time 0m0.08s, Wall time 0m0.17s).\n        2.58 real         1.23 user         1.19 sys\n| Sage Version 4.0, Release Date: 2009-05-29                         |\n| Type notebook() for the GUI, and license() for information.        |\n```\n\n\nWe need to go through and audit the startup imports again. \n\nIssue created by migration from https://trac.sagemath.org/ticket/6224\n\n",
    "created_at": "2009-06-05T10:16:36Z",
    "labels": [
        "performance",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "sage startup takes way to long",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6224",
    "user": "@robertwb"
}
```
Assignee: tbd

This is after the cache is warm, otherwise it's even worse: 


```
Robert-Bradshaws-Laptop:~/sage robert$ echo "" | time sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: referee
sage: sage: 
Exiting SAGE (CPU time 0m0.08s, Wall time 0m0.17s).
        2.58 real         1.23 user         1.19 sys
| Sage Version 4.0, Release Date: 2009-05-29                         |
| Type notebook() for the GUI, and license() for information.        |
```


We need to go through and audit the startup imports again. 

Issue created by migration from https://trac.sagemath.org/ticket/6224





---

archive/issue_comments_049692.json:
```json
{
    "body": "I should mention, this is OS X 10.4 with a 2.33 core duo. (OS X is known to be particularly bad, but < 1 second shouldn't be unreasonable.)",
    "created_at": "2009-06-05T10:17:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6224",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6224#issuecomment-49692",
    "user": "@robertwb"
}
```

I should mention, this is OS X 10.4 with a 2.33 core duo. (OS X is known to be particularly bad, but < 1 second shouldn't be unreasonable.)
