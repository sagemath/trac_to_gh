# Issue 6783: Doctest failure in sage-4.1.1/devel/sage/doc/en/constructions/linear_algebra.rst

archive/issues_006783.json:
```json
{
    "body": "Assignee: was\n\nOn Solaris (SPARC), the following test failed. Both ECL and Maxima were updated - ECL version 9.8.4, Maxima version 5.19.1\n\n\n```\n\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nThu Aug 20 20:02:37 BST 2009\ndsage-trial tmp directory doesn't exist - creating ...\nThis script will run the unit tests for DSage\n```\n\n| Sage Version 4.1.1, Release Date: 2009-08-14                       |\n| Type notebook() for the GUI, and license() for information.        |\n<SNIP>\n\n\n```\nsage -t  \"devel/sage/doc/en/constructions/linear_algebra.rst\"\n**********************************************************************\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/constructions/linear_algebra.rst\", line 276:\n    sage: eig\nExpected:\n    [[[-sqrt(3)*%i,sqrt(3)*%i],[1,1]],[1,(sqrt(3)*%i+1)/4],[1,-(sqrt(3)*%i-1)/4]]\nGot:\n    [[[-sqrt(3)*%i,sqrt(3)*%i],[1,1]],[[[1,(sqrt(3)*%i+1)/4]],[[1,-(sqrt(3)*%i-1)/4]]]]\n**********************************************************************\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/constructions/linear_algebra.rst\", line 291:\n    sage: A.eigenvectors()\nExpected:\n    [[[2,11],[1,2]],[0,0,1],[0,1,1/3]]\nGot:\n    [[[2,11],[1,2]],[[[0,0,1]],[[0,1,1/3]]]]\n**********************************************************************\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/constructions/linear_algebra.rst\", line 294:\n    sage: A.eigenvectors()\nExpected:\n     [[[-1,2],[2,1]],[0,1,-1],[0,0,1]]\nGot:\n    [[[-1,2],[2,1]],[[[0,1,-1]],[[0,0,1]]]]\n**********************************************************************\n2 items had failures:\n   1 of   5 in __main__.example_11\n   2 of   6 in __main__.example_12\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file /export/home/drkirkby/sage/sage-4.1.1/tmp/.doctest_linear_algebra.py\n         [19.2 s]\nsage -t  \"devel/sage/doc/en/constructions/number_theory.rst\"\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6783\n\n",
    "created_at": "2009-08-20T21:34:42Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "Doctest failure in sage-4.1.1/devel/sage/doc/en/constructions/linear_algebra.rst",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6783",
    "user": "drkirkby"
}
```
Assignee: was

On Solaris (SPARC), the following test failed. Both ECL and Maxima were updated - ECL version 9.8.4, Maxima version 5.19.1


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
sage -t  "devel/sage/doc/en/constructions/linear_algebra.rst"
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/constructions/linear_algebra.rst", line 276:
    sage: eig
Expected:
    [[[-sqrt(3)*%i,sqrt(3)*%i],[1,1]],[1,(sqrt(3)*%i+1)/4],[1,-(sqrt(3)*%i-1)/4]]
Got:
    [[[-sqrt(3)*%i,sqrt(3)*%i],[1,1]],[[[1,(sqrt(3)*%i+1)/4]],[[1,-(sqrt(3)*%i-1)/4]]]]
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/constructions/linear_algebra.rst", line 291:
    sage: A.eigenvectors()
Expected:
    [[[2,11],[1,2]],[0,0,1],[0,1,1/3]]
Got:
    [[[2,11],[1,2]],[[[0,0,1]],[[0,1,1/3]]]]
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/constructions/linear_algebra.rst", line 294:
    sage: A.eigenvectors()
Expected:
     [[[-1,2],[2,1]],[0,1,-1],[0,0,1]]
Got:
    [[[-1,2],[2,1]],[[[0,1,-1]],[[0,0,1]]]]
**********************************************************************
2 items had failures:
   1 of   5 in __main__.example_11
   2 of   6 in __main__.example_12
***Test Failed*** 3 failures.
For whitespace errors, see the file /export/home/drkirkby/sage/sage-4.1.1/tmp/.doctest_linear_algebra.py
         [19.2 s]
sage -t  "devel/sage/doc/en/constructions/number_theory.rst"
```


Issue created by migration from https://trac.sagemath.org/ticket/6783





---

archive/issue_comments_055906.json:
```json
{
    "body": "Changing keywords from \"\" to \"maxima\".",
    "created_at": "2009-08-20T23:27:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6783#issuecomment-55906",
    "user": "AlexGhitza"
}
```

Changing keywords from "" to "maxima".



---

archive/issue_comments_055907.json:
```json
{
    "body": "This is due to changes in Maxima's formatting of the output for eigenvectors.  See attached patch.",
    "created_at": "2009-08-20T23:27:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6783#issuecomment-55907",
    "user": "AlexGhitza"
}
```

This is due to changes in Maxima's formatting of the output for eigenvectors.  See attached patch.



---

archive/issue_comments_055908.json:
```json
{
    "body": "Attachment [trac_6783.patch](tarball://root/attachments/some-uuid/ticket6783/trac_6783.patch) by AlexGhitza created at 2009-08-20 23:28:28\n\napply after the spkg's at #6564 and #6699",
    "created_at": "2009-08-20T23:28:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6783#issuecomment-55908",
    "user": "AlexGhitza"
}
```

Attachment [trac_6783.patch](tarball://root/attachments/some-uuid/ticket6783/trac_6783.patch) by AlexGhitza created at 2009-08-20 23:28:28

apply after the spkg's at #6564 and #6699



---

archive/issue_comments_055909.json:
```json
{
    "body": "Changing assignee from was to AlexGhitza.",
    "created_at": "2009-08-20T23:29:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6783#issuecomment-55909",
    "user": "AlexGhitza"
}
```

Changing assignee from was to AlexGhitza.



---

archive/issue_comments_055910.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-08-20T23:29:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6783#issuecomment-55910",
    "user": "AlexGhitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_055911.json:
```json
{
    "body": "This is fixed by #6699.",
    "created_at": "2009-09-02T10:57:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6783#issuecomment-55911",
    "user": "mvngu"
}
```

This is fixed by #6699.



---

archive/issue_comments_055912.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-02T10:57:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6783#issuecomment-55912",
    "user": "mvngu"
}
```

Resolution: fixed
