# Issue 4456: sage-3.2.alpha3 -- numerical noise on osx 32-bit intel

archive/issues_004456.json:
```json
{
    "body": "Assignee: mabshoff\n\n```\nsage -t  devel/sage/sage/calculus/wester.py\n**********************************************************************\nFile \"/Users/was/build/sage-3.2.alpha3/tmp/wester.py\", line 261:\n   : [float(f(i/10)) for i in range(1,5)]\nExpected:\n   <BLANKLINE>\n   [-0.00033670040754082975,\n    -0.0027778004096620235,\n    -0.00989099409140...,\n    -0.025411145508414...]\nGot:\n   [-0.00033670040754081587, -0.0027778004096621622,\n-0.0098909940914039818, -0.025411145508414779]\n**********************************************************************\n1 items had failures:\n  1 of 193 in __main__.example_0\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file\n/Users/was/build/sage-3.2.alpha3/tmp/.doctest_wester.py\n        [11.4 s]\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/4456\n\n",
    "closed_at": "2008-11-09T00:29:00Z",
    "created_at": "2008-11-06T21:28:19Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sage-3.2.alpha3 -- numerical noise on osx 32-bit intel",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4456",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

```
sage -t  devel/sage/sage/calculus/wester.py
**********************************************************************
File "/Users/was/build/sage-3.2.alpha3/tmp/wester.py", line 261:
   : [float(f(i/10)) for i in range(1,5)]
Expected:
   <BLANKLINE>
   [-0.00033670040754082975,
    -0.0027778004096620235,
    -0.00989099409140...,
    -0.025411145508414...]
Got:
   [-0.00033670040754081587, -0.0027778004096621622,
-0.0098909940914039818, -0.025411145508414779]
**********************************************************************
1 items had failures:
  1 of 193 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file
/Users/was/build/sage-3.2.alpha3/tmp/.doctest_wester.py
        [11.4 s]
```

Issue created by migration from https://trac.sagemath.org/ticket/4456





---

archive/issue_comments_032809.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-11-09T00:29:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4456#issuecomment-32809",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: duplicate



---

archive/issue_comments_032810.json:
```json
{
    "body": "Oops, I opened a dupe of this at #4472, but since I will post a patch there I am closing this ticket :)\n\nCheers,\n\nMichael",
    "created_at": "2008-11-09T00:29:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4456#issuecomment-32810",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Oops, I opened a dupe of this at #4472, but since I will post a patch there I am closing this ticket :)

Cheers,

Michael



---

archive/issue_events_010057.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-09T00:29:00Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4456",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4456#event-10057"
}
```



---

archive/issue_events_010058.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-09T00:29:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4456",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4456#event-10058"
}
```
