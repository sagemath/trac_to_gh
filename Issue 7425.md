# Issue 7425: I.variety() doesn't check that I is zero-dimensional

archive/issues_007425.json:
```json
{
    "body": "Assignee: malb\n\n`I.variety()` should first check whether the ideal I is indeed 0-dimensional and refuse to continue otherwise.  This should be a fairly trivial fix.  Right now the following seems to run forever:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: R.<x, y, z> = QQ[]\nsage: I = R.ideal([x^2-y^3*z, x+y*z])\nsage: I.dimension()\n1\nsage: I.variety()\nverbose 0 (1808: multi_polynomial_ideal.py, variety) Warning: falling back to very slow toy implementation.\n```\n\n| Sage Version 4.2, Release Date: 2009-10-24                         |\n| Type notebook() for the GUI, and license() for information.        |\n\nIssue created by migration from https://trac.sagemath.org/ticket/7425\n\n",
    "created_at": "2009-11-10T23:11:29Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "title": "I.variety() doesn't check that I is zero-dimensional",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7425",
    "user": "AlexGhitza"
}
```
Assignee: malb

`I.variety()` should first check whether the ideal I is indeed 0-dimensional and refuse to continue otherwise.  This should be a fairly trivial fix.  Right now the following seems to run forever:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: R.<x, y, z> = QQ[]
sage: I = R.ideal([x^2-y^3*z, x+y*z])
sage: I.dimension()
1
sage: I.variety()
verbose 0 (1808: multi_polynomial_ideal.py, variety) Warning: falling back to very slow toy implementation.
```

| Sage Version 4.2, Release Date: 2009-10-24                         |
| Type notebook() for the GUI, and license() for information.        |

Issue created by migration from https://trac.sagemath.org/ticket/7425





---

archive/issue_comments_062491.json:
```json
{
    "body": "Attachment [trac_7425.patch](tarball://root/attachments/some-uuid/ticket7425/trac_7425.patch) by AlexGhitza created at 2009-11-11 13:33:48",
    "created_at": "2009-11-11T13:33:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7425#issuecomment-62491",
    "user": "AlexGhitza"
}
```

Attachment [trac_7425.patch](tarball://root/attachments/some-uuid/ticket7425/trac_7425.patch) by AlexGhitza created at 2009-11-11 13:33:48



---

archive/issue_comments_062492.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-11T13:34:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7425#issuecomment-62492",
    "user": "AlexGhitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062493.json:
```json
{
    "body": "patch looks good, applies cleanly against 4.2, doctests pass, reference manual builds without any warnings.",
    "created_at": "2009-11-11T14:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7425#issuecomment-62493",
    "user": "malb"
}
```

patch looks good, applies cleanly against 4.2, doctests pass, reference manual builds without any warnings.



---

archive/issue_comments_062494.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-11T14:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7425#issuecomment-62494",
    "user": "malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062495.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-12T07:21:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7425#issuecomment-62495",
    "user": "mhansen"
}
```

Resolution: fixed
