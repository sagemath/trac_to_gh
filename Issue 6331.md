# Issue 6331: optional doctest failure -- magma interface slight problems

archive/issues_006331.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nsage -t -long --optional devel/sage/sage/interfaces/mathematica.py\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/mathematica.py\", line 181:\n    sage: n.FactorInteger()                  # optional - mathematica\nExpected:\n    {{2, 2}, {3, 2}, {5, 3}, {541, 1}}       # optional - mathematica\nGot:\n    {{2, 2}, {3, 2}, {5, 3}, {541, 1}}\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/mathematica.py\", line 236:\n    sage: math_bessel_K(2,I)                      # optional - mathematica\nExpected:\n    0.180489972066962*I - 2.592886175491197\nGot:\n    -2.592886175491196978 + 0.1804899720669620266*I\n**********************************************************************\n1 items had failures:\n   2 of  62 in __main__.example_0\n***Test Failed*** 2 failures.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6331\n\n",
    "created_at": "2009-06-16T15:08:39Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "optional doctest failure -- magma interface slight problems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6331",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd


```
sage -t -long --optional devel/sage/sage/interfaces/mathematica.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/mathematica.py", line 181:
    sage: n.FactorInteger()                  # optional - mathematica
Expected:
    {{2, 2}, {3, 2}, {5, 3}, {541, 1}}       # optional - mathematica
Got:
    {{2, 2}, {3, 2}, {5, 3}, {541, 1}}
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/mathematica.py", line 236:
    sage: math_bessel_K(2,I)                      # optional - mathematica
Expected:
    0.180489972066962*I - 2.592886175491197
Got:
    -2.592886175491196978 + 0.1804899720669620266*I
**********************************************************************
1 items had failures:
   2 of  62 in __main__.example_0
***Test Failed*** 2 failures.
```


Issue created by migration from https://trac.sagemath.org/ticket/6331





---

archive/issue_comments_050449.json:
```json
{
    "body": "Both these errors are addressed in #4948.  The first error (an extra \"# optional - mathematica\") is fixed properly.  The second error is probably due to 32/64 bit versions of mathematica, or maybe even just different versions of mathematica.  The patch in #4948 adds -2.592886175491196978 + 0.1804899720669620266*I as a legitimate solution.",
    "created_at": "2009-09-14T07:17:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6331#issuecomment-50449",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Both these errors are addressed in #4948.  The first error (an extra "# optional - mathematica") is fixed properly.  The second error is probably due to 32/64 bit versions of mathematica, or maybe even just different versions of mathematica.  The patch in #4948 adds -2.592886175491196978 + 0.1804899720669620266*I as a legitimate solution.



---

archive/issue_comments_050450.json:
```json
{
    "body": "I believe that this should be fixed in 4.1.2.alpha2 since #4948 was merged.",
    "created_at": "2009-09-23T04:20:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6331#issuecomment-50450",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

I believe that this should be fixed in 4.1.2.alpha2 since #4948 was merged.



---

archive/issue_comments_050451.json:
```json
{
    "body": "Seems good to me.  Fixed by #4948.",
    "created_at": "2009-10-05T04:47:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6331#issuecomment-50451",
    "user": "https://github.com/mwhansen"
}
```

Seems good to me.  Fixed by #4948.



---

archive/issue_events_014871.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-05T04:47:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6331",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6331#event-14871"
}
```



---

archive/issue_events_014872.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-05T04:47:25Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6331",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6331#event-14872"
}
```



---

archive/issue_comments_050452.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-10-05T04:47:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6331#issuecomment-50452",
    "user": "https://github.com/mwhansen"
}
```

Resolution: duplicate
