# Issue 6793: 1 doctest timed out in devel/sage/sage/schemes/elliptic_curves/ell_point.py

archive/issues_006793.json:
```json
{
    "body": "Assignee: davidloeffler\n\nOn Solaris 10 update 7 (SPARC), the following tests failed. Both ECL and Maxima were updated - ECL version 9.8.4, Maxima version 5.19.1. Sage was built with gcc 4.4.1\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nThu Aug 20 20:02:37 BST 2009\ndsage-trial tmp directory doesn't exist - creating ...\nThis script will run the unit tests for DSage\n```\n\n<SNIP>\n\n```\nsage -t  \"devel/sage/sage/schemes/elliptic_curves/ell_point.py\"\n*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n*** *** Error: TIMED OUT! *** ***\n*** *** Error: TIMED OUT! *** ***\n         [361.6 s]\n```\n\n| Sage Version 4.1.1, Release Date: 2009-08-14                       |\n| Type notebook() for the GUI, and license() for information.        |\n\nIssue created by migration from https://trac.sagemath.org/ticket/6793\n\n",
    "created_at": "2009-08-20T23:03:45Z",
    "labels": [
        "elliptic curves",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "1 doctest timed out in devel/sage/sage/schemes/elliptic_curves/ell_point.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6793",
    "user": "drkirkby"
}
```
Assignee: davidloeffler

On Solaris 10 update 7 (SPARC), the following tests failed. Both ECL and Maxima were updated - ECL version 9.8.4, Maxima version 5.19.1. Sage was built with gcc 4.4.1

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Thu Aug 20 20:02:37 BST 2009
dsage-trial tmp directory doesn't exist - creating ...
This script will run the unit tests for DSage
```

<SNIP>

```
sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_point.py"
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
*** *** Error: TIMED OUT! *** ***
         [361.6 s]
```

| Sage Version 4.1.1, Release Date: 2009-08-14                       |
| Type notebook() for the GUI, and license() for information.        |

Issue created by migration from https://trac.sagemath.org/ticket/6793





---

archive/issue_comments_055969.json:
```json
{
    "body": "Changing keywords from \"\" to \"maxima\".",
    "created_at": "2009-08-21T00:01:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6793#issuecomment-55969",
    "user": "AlexGhitza"
}
```

Changing keywords from "" to "maxima".



---

archive/issue_comments_055970.json:
```json
{
    "body": "Remove assignee davidloeffler.",
    "created_at": "2009-10-09T09:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6793#issuecomment-55970",
    "user": "davidloeffler"
}
```

Remove assignee davidloeffler.



---

archive/issue_comments_055971.json:
```json
{
    "body": "Changing component from elliptic curves to solaris.",
    "created_at": "2009-11-28T04:37:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6793#issuecomment-55971",
    "user": "AlexGhitza"
}
```

Changing component from elliptic curves to solaris.



---

archive/issue_comments_055972.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-12-02T20:51:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6793#issuecomment-55972",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_055973.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-12-02T20:51:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6793#issuecomment-55973",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_055974.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-12-05T08:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6793#issuecomment-55974",
    "user": "jdemeyer"
}
```

Resolution: invalid
