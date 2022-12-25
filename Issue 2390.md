# Issue 2390: numerical noise in devel/sage-main/sage/structure/factorization.py

archive/issues_002390.json:
```json
{
    "body": "Assignee: cwitty\n\n\n\n```\n[jaap@paix sage-2.10.3.rc1]$ ./sage -t  devel/sage-main/sage/structure/factorization.py\nsage -t  devel/sage-main/sage/structure/factorization.py    **********************************************************************\nFile \".doctest_factorization.py\", line 479, in __main__.example_17\nFailed example:\n    F = factor(-Integer(2)*x**Integer(2) - Integer(1)); F###line 602:_sage_    >>> F = factor(-2*x^2 - 1); F\nExpected:\n    (-2.0) * (1.0*x^2 + 0.5) * (1.0*x^2 + 1.11022302463e-16*x + 0.5)  \nGot:\n    (-2.0) * (1.0*x^2 - 1.82173070032e-16*x + 0.5) * (1.0*x^2 + 0.5)\n**********************************************************************\n1 items had failures:\n   1 of   3 in __main__.example_17\n***Test Failed*** 1 failures.\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n         [2.7 s]\nexit code: 256\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  devel/sage-main/sage/structure/factorization.py\nTotal time for all tests: 2.7 seconds\n[jaap@paix sage-2.10.3.rc1]$ \n\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2390\n\n",
    "created_at": "2008-03-05T00:11:06Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "numerical noise in devel/sage-main/sage/structure/factorization.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2390",
    "user": "https://github.com/jaapspies"
}
```
Assignee: cwitty



```
[jaap@paix sage-2.10.3.rc1]$ ./sage -t  devel/sage-main/sage/structure/factorization.py
sage -t  devel/sage-main/sage/structure/factorization.py    **********************************************************************
File ".doctest_factorization.py", line 479, in __main__.example_17
Failed example:
    F = factor(-Integer(2)*x**Integer(2) - Integer(1)); F###line 602:_sage_    >>> F = factor(-2*x^2 - 1); F
Expected:
    (-2.0) * (1.0*x^2 + 0.5) * (1.0*x^2 + 1.11022302463e-16*x + 0.5)  
Got:
    (-2.0) * (1.0*x^2 - 1.82173070032e-16*x + 0.5) * (1.0*x^2 + 0.5)
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_17
***Test Failed*** 1 failures.

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.
         [2.7 s]
exit code: 256
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage-main/sage/structure/factorization.py
Total time for all tests: 2.7 seconds
[jaap@paix sage-2.10.3.rc1]$ 

```



Issue created by migration from https://trac.sagemath.org/ticket/2390





---

archive/issue_comments_016092.json:
```json
{
    "body": "Changing assignee from cwitty to @williamstein.",
    "created_at": "2008-03-05T00:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2390#issuecomment-16092",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from cwitty to @williamstein.



---

archive/issue_comments_016093.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-04T22:12:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2390#issuecomment-16093",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002566.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-04T22:12:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2390",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2390#event-2566"
}
```



---

archive/issue_comments_016094.json:
```json
{
    "body": "This has been fixed in Sage 2.10.3.final. I believe the patch was contributed by Gary Furnish, but my recollection might be a little hazy here.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-04T22:12:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2390#issuecomment-16094",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This has been fixed in Sage 2.10.3.final. I believe the patch was contributed by Gary Furnish, but my recollection might be a little hazy here.

Cheers,

Michael
