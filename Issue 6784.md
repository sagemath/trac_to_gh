# Issue 6784: Doctest failure in sage-4.1.1/devel/sage/doc/en/constructions/interface_issues.rst

archive/issues_006784.json:
```json
{
    "body": "Assignee: was\n\nOn Solaris 10 update 7 (SPARC), the following test failed. Both ECL and Maxima were updated - ECL version 9.8.4, Maxima version 5.19.1. Sage was built with gcc 4.4.1\n\n\n```\n\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nThu Aug 20 20:02:37 BST 2009\ndsage-trial tmp directory doesn't exist - creating ...\nThis script will run the unit tests for DSage\n```\n\n| Sage Version 4.1.1, Release Date: 2009-08-14                       |\n| Type notebook() for the GUI, and license() for information.        |\n<SNIP>\n\n```\nsage -t  \"devel/sage/doc/en/constructions/interface_issues.rst\"\n**********************************************************************\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/constructions/interface_issues.rst\", line 478:\n    sage: maxima.eval(\"f:bessel_y (v, w)\")\nExpected:\n    '?%bessel_y(v,w)'\nGot:\n    'bessel_y(v,w)'\n**********************************************************************\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/constructions/interface_issues.rst\", line 480:\n    sage: maxima.eval(\"diff(f,w)\")\nExpected:\n    '(?%bessel_y(v-1,w)-?%bessel_y(v+1,w))/2'\nGot:\n    '(bessel_y(v-1,w)-bessel_y(v+1,w))/2'\n**********************************************************************\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/constructions/interface_issues.rst\", line 482:\n    sage: maxima.eval(\"diff (jacobi_sn (u, m), u)\")\nExpected:\n    '?%jacobi_cn(u,m)*?%jacobi_dn(u,m)'\nGot:\n    'jacobi_cn(u,m)*jacobi_dn(u,m)'\n**********************************************************************\n1 items had failures:\n   3 of   9 in __main__.example_3\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file /export/home/drkirkby/sage/sage-4.1.1/tmp/.doctest_interface_issues.py\n         [19.8 s]\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6784\n\n",
    "created_at": "2009-08-20T21:43:53Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Doctest failure in sage-4.1.1/devel/sage/doc/en/constructions/interface_issues.rst",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6784",
    "user": "drkirkby"
}
```
Assignee: was

On Solaris 10 update 7 (SPARC), the following test failed. Both ECL and Maxima were updated - ECL version 9.8.4, Maxima version 5.19.1. Sage was built with gcc 4.4.1


```

----------------------------------------------------------------------
----------------------------------------------------------------------
Thu Aug 20 20:02:37 BST 2009
dsage-trial tmp directory doesn't exist - creating ...
This script will run the unit tests for DSage
```

| Sage Version 4.1.1, Release Date: 2009-08-14                       |
| Type notebook() for the GUI, and license() for information.        |
<SNIP>

```
sage -t  "devel/sage/doc/en/constructions/interface_issues.rst"
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/constructions/interface_issues.rst", line 478:
    sage: maxima.eval("f:bessel_y (v, w)")
Expected:
    '?%bessel_y(v,w)'
Got:
    'bessel_y(v,w)'
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/constructions/interface_issues.rst", line 480:
    sage: maxima.eval("diff(f,w)")
Expected:
    '(?%bessel_y(v-1,w)-?%bessel_y(v+1,w))/2'
Got:
    '(bessel_y(v-1,w)-bessel_y(v+1,w))/2'
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/constructions/interface_issues.rst", line 482:
    sage: maxima.eval("diff (jacobi_sn (u, m), u)")
Expected:
    '?%jacobi_cn(u,m)*?%jacobi_dn(u,m)'
Got:
    'jacobi_cn(u,m)*jacobi_dn(u,m)'
**********************************************************************
1 items had failures:
   3 of   9 in __main__.example_3
***Test Failed*** 3 failures.
For whitespace errors, see the file /export/home/drkirkby/sage/sage-4.1.1/tmp/.doctest_interface_issues.py
         [19.8 s]

```


Issue created by migration from https://trac.sagemath.org/ticket/6784





---

archive/issue_comments_055913.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-08-20T23:34:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6784#issuecomment-55913",
    "user": "AlexGhitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_055914.json:
```json
{
    "body": "Changing keywords from \"\" to \"maxima\".",
    "created_at": "2009-08-20T23:34:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6784#issuecomment-55914",
    "user": "AlexGhitza"
}
```

Changing keywords from "" to "maxima".



---

archive/issue_comments_055915.json:
```json
{
    "body": "Changing assignee from was to AlexGhitza.",
    "created_at": "2009-08-20T23:34:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6784#issuecomment-55915",
    "user": "AlexGhitza"
}
```

Changing assignee from was to AlexGhitza.



---

archive/issue_comments_055916.json:
```json
{
    "body": "Simply due to new Maxima de-uglifying its output.  See attached patch.",
    "created_at": "2009-08-20T23:34:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6784#issuecomment-55916",
    "user": "AlexGhitza"
}
```

Simply due to new Maxima de-uglifying its output.  See attached patch.



---

archive/issue_comments_055917.json:
```json
{
    "body": "Attachment [trac_6784.patch](tarball://root/attachments/some-uuid/ticket6784/trac_6784.patch) by AlexGhitza created at 2009-08-20 23:35:21\n\napply after spkg's at #6564 and #6699",
    "created_at": "2009-08-20T23:35:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6784#issuecomment-55917",
    "user": "AlexGhitza"
}
```

Attachment [trac_6784.patch](tarball://root/attachments/some-uuid/ticket6784/trac_6784.patch) by AlexGhitza created at 2009-08-20 23:35:21

apply after spkg's at #6564 and #6699



---

archive/issue_comments_055918.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-02T10:58:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6784#issuecomment-55918",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_055919.json:
```json
{
    "body": "This is fixed by #6699.",
    "created_at": "2009-09-02T10:58:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6784#issuecomment-55919",
    "user": "mvngu"
}
```

This is fixed by #6699.
