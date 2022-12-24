# Issue 1012: fix some doctests

archive/issues_001012.json:
```json
{
    "body": "Assignee: failure\n\n\n```\nI have the following doctest failures on BSD (Intel Mac).  See below.\nAll are easy to fix doctests that changed because of recent improvements\nto Sage, I think.\n\n        sage -t  devel/sage-main/sage/groups/perm_gps/cubegroup.py\n        sage -t  devel/sage-main/sage/interfaces/gp.py\n        sage -t  devel/sage-main/sage/interfaces/maxima.py\nTotal time for all tests: 2982.5 seconds\n\nsage -t  devel/sage-main/sage/groups/perm_gps/cubegroup.py  **********************************************************************\nFile \"cubegroup.py\", line 1191:\n    sage: C.plot3d()\nExpected:\n    <class 'sage.plot.plot3d.base.TransformGroup'>\nGot:\n    <class 'base.TransformGroup'>\n************************************\n\n******************************\nFile \"gp.py\", line 365:\n    sage: ComplexField(10)(gp(11243.9812+15*I))\nExpected:\n     1.1e4 + 15*I\nGot:\n    1.1e4 + 15.*I\n**********************************************************************\n1 items had failures:\n   1 of   3 in __main__.example_11\n\n\nsage -t  devel/sage-main/sage/interfaces/maxima.py          **********************************************************************\nFile \"maxima.py\", line 1227:\n    sage: ComplexField(10)(maxima('2342.23482943872+234*%i'))\nExpected:\n     2300 + 230*I\nGot:\n    2300. + 230.*I\n**********************************************************************\n1 items had failures:\n\n\n\nI have the following doctest failures on sage.math:\n\n        sage -t  devel/sage-main/sage/groups/perm_gps/cubegroup.py\n        sage -t  devel/sage-main/sage/interfaces/gp.py\n        sage -t  devel/sage-main/sage/interfaces/maxima.py\n        sage -t  devel/sage-main/sage/rings/finite_field_givaro.pyx\n        sage -t  devel/sage-main/sage/rings/finite_field_ext_pari.py\nTotal time for all tests: 2332.1 seconds\n\nThe first givaro failure is:\n\nFile \"finite_field_givaro.pyx\", line 799:\n    sage: hash(GF(3^4, 'a'))\nExpected:\n    -4281682415996964816\nGot:\n    695660592\n\nThe second finite field failure is:\n\nsage -t  devel/sage-main/sage/rings/finite_field_ext_pari.py**********************************************************************\nFile \"finite_field_ext_pari.py\", line 593:\n    sage: hash(GF(9,'a'))\nExpected:\n    -8785304532306495574\nGot:\n    205387690\n**********************************************************************\nFile \"finite_field_ext_pari.py\", line 596:\n    sage: hash(GF(9,'b'))\nExpected:\n    5852897890058287069\nGot:\n    -74532899\n**********************************************************************\n1 items had failures:\n   2 of   4 in __main__.example_13\n\n\n William\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1012\n\n",
    "created_at": "2007-10-27T15:40:43Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.10",
    "title": "fix some doctests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1012",
    "user": "was"
}
```
Assignee: failure


```
I have the following doctest failures on BSD (Intel Mac).  See below.
All are easy to fix doctests that changed because of recent improvements
to Sage, I think.

        sage -t  devel/sage-main/sage/groups/perm_gps/cubegroup.py
        sage -t  devel/sage-main/sage/interfaces/gp.py
        sage -t  devel/sage-main/sage/interfaces/maxima.py
Total time for all tests: 2982.5 seconds

sage -t  devel/sage-main/sage/groups/perm_gps/cubegroup.py  **********************************************************************
File "cubegroup.py", line 1191:
    sage: C.plot3d()
Expected:
    <class 'sage.plot.plot3d.base.TransformGroup'>
Got:
    <class 'base.TransformGroup'>
************************************

******************************
File "gp.py", line 365:
    sage: ComplexField(10)(gp(11243.9812+15*I))
Expected:
     1.1e4 + 15*I
Got:
    1.1e4 + 15.*I
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_11


sage -t  devel/sage-main/sage/interfaces/maxima.py          **********************************************************************
File "maxima.py", line 1227:
    sage: ComplexField(10)(maxima('2342.23482943872+234*%i'))
Expected:
     2300 + 230*I
Got:
    2300. + 230.*I
**********************************************************************
1 items had failures:



I have the following doctest failures on sage.math:

        sage -t  devel/sage-main/sage/groups/perm_gps/cubegroup.py
        sage -t  devel/sage-main/sage/interfaces/gp.py
        sage -t  devel/sage-main/sage/interfaces/maxima.py
        sage -t  devel/sage-main/sage/rings/finite_field_givaro.pyx
        sage -t  devel/sage-main/sage/rings/finite_field_ext_pari.py
Total time for all tests: 2332.1 seconds

The first givaro failure is:

File "finite_field_givaro.pyx", line 799:
    sage: hash(GF(3^4, 'a'))
Expected:
    -4281682415996964816
Got:
    695660592

The second finite field failure is:

sage -t  devel/sage-main/sage/rings/finite_field_ext_pari.py**********************************************************************
File "finite_field_ext_pari.py", line 593:
    sage: hash(GF(9,'a'))
Expected:
    -8785304532306495574
Got:
    205387690
**********************************************************************
File "finite_field_ext_pari.py", line 596:
    sage: hash(GF(9,'b'))
Expected:
    5852897890058287069
Got:
    -74532899
**********************************************************************
1 items had failures:
   2 of   4 in __main__.example_13


 William
```


Issue created by migration from https://trac.sagemath.org/ticket/1012





---

archive/issue_comments_006198.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2007-10-27T15:41:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1012",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1012#issuecomment-6198",
    "user": "was"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_006199.json:
```json
{
    "body": "Changing assignee from failure to cwitty.",
    "created_at": "2007-10-27T16:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1012",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1012#issuecomment-6199",
    "user": "cwitty"
}
```

Changing assignee from failure to cwitty.



---

archive/issue_comments_006200.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-27T16:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1012",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1012#issuecomment-6200",
    "user": "cwitty"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006201.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-27T21:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1012",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1012#issuecomment-6201",
    "user": "cwitty"
}
```

Resolution: fixed
