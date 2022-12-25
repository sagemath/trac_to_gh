# Issue 6786: fix doctest failures in doc/en/tutorial/tour_algebra.rst due to upgrade to Maxima 5.19.1

archive/issues_006786.json:
```json
{
    "body": "Assignee: @aghitza\n\nKeywords: maxima\n\nOn Solaris 10 update 7 (SPARC), the following test failed. Both ECL and Maxima were updated - ECL version 9.8.4, Maxima version 5.19.1. Sage was built with gcc 4.4.1\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nThu Aug 20 20:02:37 BST 2009\ndsage-trial tmp directory doesn't exist - creating ...\nThis script will run the unit tests for DSage\n```\n<SNIP>\n| Sage Version 4.1.1, Release Date: 2009-08-14                       |\n| Type notebook() for the GUI, and license() for information.        |\n```\nsage -t  \"devel/sage/doc/en/tutorial/tour_algebra.rst\"\n**********************************************************************\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/tour_algebra.rst\", line 205:\n    sage: lde1 = de1.laplace(\"t\",\"s\"); lde1\nExpected:\n    2*(-?%at('diff(x(t),t,1),t=0)+s^2*?%laplace(x(t),t,s)-x(0)*s)-2*?%laplace(y(t),t,s)+6*?%laplace(x(t),t,s)\nGot:\n    2*(-?%at('diff(x(t),t,1),t=0)+s^2*'laplace(x(t),t,s)-x(0)*s)-2*'laplace(y(t),t,s)+6*'laplace(x(t),t,s)\n**********************************************************************\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/tour_algebra.rst\", line 220:\n    sage: lde2 = de2.laplace(\"t\",\"s\"); lde2\nExpected:\n    -?%at('diff(y(t),t,1),t=0)+s^2*?%laplace(y(t),t,s)+2*?%laplace(y(t),t,s)-2*?%laplace(x(t),t,s)-y(0)*s\nGot:\n    -?%at('diff(y(t),t,1),t=0)+s^2*'laplace(y(t),t,s)+2*'laplace(y(t),t,s)-2*'laplace(x(t),t,s)-y(0)*s\n**********************************************************************\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/tour_algebra.rst\", line 410:\n    sage: maxima.eval(\"f:bessel_y(v, w)\")\nExpected:\n    '?%bessel_y(v,w)'\nGot:\n    'bessel_y(v,w)'\n**********************************************************************\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/tour_algebra.rst\", line 412:\n    sage: maxima.eval(\"diff(f,w)\")\nExpected:\n    '(?%bessel_y(v-1,w)-?%bessel_y(v+1,w))/2'\nGot:\n    '(bessel_y(v-1,w)-bessel_y(v+1,w))/2'\n**********************************************************************\n3 items had failures:\n   1 of   4 in __main__.example_11\n   1 of   4 in __main__.example_12\n   2 of   4 in __main__.example_20\n***Test Failed*** 4 failures.\nFor whitespace errors, see the file /export/home/drkirkby/sage/sage-4.1.1/tmp/.doctest_tour_algebra.py\n\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/6786\n\n",
    "closed_at": "2009-09-02T11:00:00Z",
    "created_at": "2009-08-20T21:55:52Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "fix doctest failures in doc/en/tutorial/tour_algebra.rst due to upgrade to Maxima 5.19.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6786",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: @aghitza

Keywords: maxima

On Solaris 10 update 7 (SPARC), the following test failed. Both ECL and Maxima were updated - ECL version 9.8.4, Maxima version 5.19.1. Sage was built with gcc 4.4.1

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
sage -t  "devel/sage/doc/en/tutorial/tour_algebra.rst"
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/tour_algebra.rst", line 205:
    sage: lde1 = de1.laplace("t","s"); lde1
Expected:
    2*(-?%at('diff(x(t),t,1),t=0)+s^2*?%laplace(x(t),t,s)-x(0)*s)-2*?%laplace(y(t),t,s)+6*?%laplace(x(t),t,s)
Got:
    2*(-?%at('diff(x(t),t,1),t=0)+s^2*'laplace(x(t),t,s)-x(0)*s)-2*'laplace(y(t),t,s)+6*'laplace(x(t),t,s)
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/tour_algebra.rst", line 220:
    sage: lde2 = de2.laplace("t","s"); lde2
Expected:
    -?%at('diff(y(t),t,1),t=0)+s^2*?%laplace(y(t),t,s)+2*?%laplace(y(t),t,s)-2*?%laplace(x(t),t,s)-y(0)*s
Got:
    -?%at('diff(y(t),t,1),t=0)+s^2*'laplace(y(t),t,s)+2*'laplace(y(t),t,s)-2*'laplace(x(t),t,s)-y(0)*s
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/tour_algebra.rst", line 410:
    sage: maxima.eval("f:bessel_y(v, w)")
Expected:
    '?%bessel_y(v,w)'
Got:
    'bessel_y(v,w)'
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/tutorial/tour_algebra.rst", line 412:
    sage: maxima.eval("diff(f,w)")
Expected:
    '(?%bessel_y(v-1,w)-?%bessel_y(v+1,w))/2'
Got:
    '(bessel_y(v-1,w)-bessel_y(v+1,w))/2'
**********************************************************************
3 items had failures:
   1 of   4 in __main__.example_11
   1 of   4 in __main__.example_12
   2 of   4 in __main__.example_20
***Test Failed*** 4 failures.
For whitespace errors, see the file /export/home/drkirkby/sage/sage-4.1.1/tmp/.doctest_tour_algebra.py

```

Issue created by migration from https://trac.sagemath.org/ticket/6786





---

archive/issue_comments_055825.json:
```json
{
    "body": "Changing assignee from tbd to @aghitza.",
    "created_at": "2009-08-20T23:49:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6786#issuecomment-55825",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from tbd to @aghitza.



---

archive/issue_comments_055826.json:
```json
{
    "body": "Simple changes to Maxima formatting.  See attached patch.",
    "created_at": "2009-08-20T23:49:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6786#issuecomment-55826",
    "user": "https://github.com/aghitza"
}
```

Simple changes to Maxima formatting.  See attached patch.



---

archive/issue_comments_055827.json:
```json
{
    "body": "Changing keywords from \"\" to \"maxima\".",
    "created_at": "2009-08-20T23:49:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6786#issuecomment-55827",
    "user": "https://github.com/aghitza"
}
```

Changing keywords from "" to "maxima".



---

archive/issue_comments_055828.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-08-20T23:49:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6786#issuecomment-55828",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_055829.json:
```json
{
    "body": "I don't see any patch attached.",
    "created_at": "2009-08-22T02:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6786#issuecomment-55829",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I don't see any patch attached.



---

archive/issue_comments_055830.json:
```json
{
    "body": "This is fixed by #6699.",
    "created_at": "2009-09-02T11:00:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6786#issuecomment-55830",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

This is fixed by #6699.



---

archive/issue_comments_055831.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-02T11:00:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6786#issuecomment-55831",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_015987.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-02T11:00:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6786",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6786#event-15987"
}
```
