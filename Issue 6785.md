# Issue 6785: Doctest failure in sage-4.1.1/devel/sage/doc/en/constructions/plotting.rst

archive/issues_006785.json:
```json
{
    "body": "Assignee: was\n\nOn Solaris 10 update 7 (SPARC), the following test failed. Both ECL and Maxima were updated - ECL version 9.8.4, Maxima version 5.19.1. Sage was built with gcc 4.4.1\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nThu Aug 20 20:02:37 BST 2009\ndsage-trial tmp directory doesn't exist - creating ...\nThis script will run the unit tests for DSage\n```\n\n| Sage Version 4.1.1, Release Date: 2009-08-14                       |\n| Type notebook() for the GUI, and license() for information.        |\n<SNIP>\n\n\n```\n**********************************************************************\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/constructions/plotting.rst\", line 209:\n    sage: maxima.eval('load(\"plotdf\");')\nExpected:\n    '\".../local/share/maxima/5.16.3/share/dynamics/plotdf.lisp\"'\nGot:\n    '\"/export/home/drkirkby/sage/sage-4.1.1/local/share/maxima/5.19.1/share/dynamics/plotdf.lisp\"'\n**********************************************************************\n1 items had failures:\n   1 of   3 in __main__.example_11\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /export/home/drkirkby/sage/sage-4.1.1/tmp/.doctest_plotting.py\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6785\n\n",
    "created_at": "2009-08-20T21:48:32Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "Doctest failure in sage-4.1.1/devel/sage/doc/en/constructions/plotting.rst",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6785",
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
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/constructions/plotting.rst", line 209:
    sage: maxima.eval('load("plotdf");')
Expected:
    '".../local/share/maxima/5.16.3/share/dynamics/plotdf.lisp"'
Got:
    '"/export/home/drkirkby/sage/sage-4.1.1/local/share/maxima/5.19.1/share/dynamics/plotdf.lisp"'
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_11
***Test Failed*** 1 failures.
For whitespace errors, see the file /export/home/drkirkby/sage/sage-4.1.1/tmp/.doctest_plotting.py
```


Issue created by migration from https://trac.sagemath.org/ticket/6785





---

archive/issue_comments_055920.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-08-20T23:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6785#issuecomment-55920",
    "user": "AlexGhitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_055921.json:
```json
{
    "body": "Trivial: the Maxima version changed.  See attached patch.",
    "created_at": "2009-08-20T23:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6785#issuecomment-55921",
    "user": "AlexGhitza"
}
```

Trivial: the Maxima version changed.  See attached patch.



---

archive/issue_comments_055922.json:
```json
{
    "body": "Changing assignee from was to AlexGhitza.",
    "created_at": "2009-08-20T23:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6785#issuecomment-55922",
    "user": "AlexGhitza"
}
```

Changing assignee from was to AlexGhitza.



---

archive/issue_comments_055923.json:
```json
{
    "body": "Changing keywords from \"\" to \"maxima\".",
    "created_at": "2009-08-20T23:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6785#issuecomment-55923",
    "user": "AlexGhitza"
}
```

Changing keywords from "" to "maxima".



---

archive/issue_comments_055924.json:
```json
{
    "body": "Attachment [trac_6785.patch](tarball://root/attachments/some-uuid/ticket6785/trac_6785.patch) by AlexGhitza created at 2009-08-20 23:41:11\n\napply after the spkg's at #6564 and #6699",
    "created_at": "2009-08-20T23:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6785#issuecomment-55924",
    "user": "AlexGhitza"
}
```

Attachment [trac_6785.patch](tarball://root/attachments/some-uuid/ticket6785/trac_6785.patch) by AlexGhitza created at 2009-08-20 23:41:11

apply after the spkg's at #6564 and #6699



---

archive/issue_comments_055925.json:
```json
{
    "body": "This is fixed by #6699.",
    "created_at": "2009-09-02T10:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6785#issuecomment-55925",
    "user": "mvngu"
}
```

This is fixed by #6699.



---

archive/issue_comments_055926.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-02T10:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6785#issuecomment-55926",
    "user": "mvngu"
}
```

Resolution: fixed
