# Issue 6324: optional doctest failure -- sloane functions and gap database

archive/issues_006324.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nsage -t -long --optional devel/sage/sage/combinat/sloane_functions.py\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/combinat/sloane_functions.py\", line 354:\n    sage: sloane.A000001._eval(51) #optional requires database_gap\nExpected nothing\nGot:\n    1\n**********************************************************************\n1 items had failures:\n   1 of   4 in __main__.example_13\n***Test Failed*** 1 failures.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6324\n\n",
    "created_at": "2009-06-16T14:54:36Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "optional doctest failure -- sloane functions and gap database",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6324",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd


```
sage -t -long --optional devel/sage/sage/combinat/sloane_functions.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/combinat/sloane_functions.py", line 354:
    sage: sloane.A000001._eval(51) #optional requires database_gap
Expected nothing
Got:
    1
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_13
***Test Failed*** 1 failures.
```


Issue created by migration from https://trac.sagemath.org/ticket/6324





---

archive/issue_comments_050378.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-07-13T12:24:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6324#issuecomment-50378",
    "user": "https://github.com/seblabbe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_050379.json:
```json
{
    "body": "On sage-6.8.beta8, this problem seems fixed:\n\n\n```\n$ sage -t --long --optional=sage,database_gap,internet src/sage/combinat/sloane_functions.py\nRunning doctests with ID 2015-07-13-14-22-17-a3f279bb.\nGit branch: develop\nUsing --optional=database_gap,internet,sage\nDoctesting 1 file.\nsage -t --long --warn-long 2.3 src/sage/combinat/sloane_functions.py\n    [1241 tests, 0.93 s]\n----------------------------------------------------------------------\nAll tests passed!\n----------------------------------------------------------------------\nTotal time for all tests: 1.2 seconds\n    cpu time: 0.7 seconds\n    cumulative wall time: 0.9 seconds\n\n```\n",
    "created_at": "2015-07-13T12:24:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6324#issuecomment-50379",
    "user": "https://github.com/seblabbe"
}
```

On sage-6.8.beta8, this problem seems fixed:


```
$ sage -t --long --optional=sage,database_gap,internet src/sage/combinat/sloane_functions.py
Running doctests with ID 2015-07-13-14-22-17-a3f279bb.
Git branch: develop
Using --optional=database_gap,internet,sage
Doctesting 1 file.
sage -t --long --warn-long 2.3 src/sage/combinat/sloane_functions.py
    [1241 tests, 0.93 s]
----------------------------------------------------------------------
All tests passed!
----------------------------------------------------------------------
Total time for all tests: 1.2 seconds
    cpu time: 0.7 seconds
    cumulative wall time: 0.9 seconds

```




---

archive/issue_comments_050380.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-07-13T13:39:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6324#issuecomment-50380",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_050381.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-07-17T20:05:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6324#issuecomment-50381",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_006570.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2015-07-17T20:05:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6324",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6324#event-6570"
}
```
