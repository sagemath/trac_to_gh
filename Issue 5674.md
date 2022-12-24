# Issue 5674: [with patch, needs review] Enhanced handling of elliptic curve twists

archive/issues_005674.json:
```json
{
    "body": "Assignee: was\n\nCC:  wuthrich\n\nKeywords: elliptic curve twist\n\nThe patch does the following related things:\n\n1. Implements in ell_generic functions is_quadratic_twist(), is_quartic_twist(), is_sextic_twist(), which detect twists between curves (returning the appropriate twisting paramenter)\n2. Deprecates the EllipticCurve(j) constructor, replacing it with EllipticCurve_from_j(j).  Over Q this gives the minimal twist, i.e. a curve with the correct j and minimal conductor.\n3. Rewrites the function minimal_quadratic_twist() introduced in #4667 to use the previous function, with extra work in case j=0, 1728 since we need the minimal __quadratic__ twist, not the minimal twist.\n\nThere is likely to be a necessary change to documentation (pages 38 and 39 of the tutorial) which have not yet been made.\n\nThe patch is based on 3.4.1.alpha0 + patches at #4667.\nI have tested all files in sage/schemes/elliptic_curves.  There are two failures in sha_tate which I do not understand, so I am posting the patch anyway.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5674\n\n",
    "created_at": "2009-04-03T11:09:11Z",
    "labels": [
        "number theory",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, needs review] Enhanced handling of elliptic curve twists",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5674",
    "user": "cremona"
}
```
Assignee: was

CC:  wuthrich

Keywords: elliptic curve twist

The patch does the following related things:

1. Implements in ell_generic functions is_quadratic_twist(), is_quartic_twist(), is_sextic_twist(), which detect twists between curves (returning the appropriate twisting paramenter)
2. Deprecates the EllipticCurve(j) constructor, replacing it with EllipticCurve_from_j(j).  Over Q this gives the minimal twist, i.e. a curve with the correct j and minimal conductor.
3. Rewrites the function minimal_quadratic_twist() introduced in #4667 to use the previous function, with extra work in case j=0, 1728 since we need the minimal __quadratic__ twist, not the minimal twist.

There is likely to be a necessary change to documentation (pages 38 and 39 of the tutorial) which have not yet been made.

The patch is based on 3.4.1.alpha0 + patches at #4667.
I have tested all files in sage/schemes/elliptic_curves.  There are two failures in sha_tate which I do not understand, so I am posting the patch anyway.


Issue created by migration from https://trac.sagemath.org/ticket/5674





---

archive/issue_comments_044392.json:
```json
{
    "body": "Attachment [twist.patch](tarball://root/attachments/some-uuid/ticket5674/twist.patch) by cremona created at 2009-04-03 11:09:50\n\napply to 3.4.1.apha0 + #4667 patches",
    "created_at": "2009-04-03T11:09:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5674#issuecomment-44392",
    "user": "cremona"
}
```

Attachment [twist.patch](tarball://root/attachments/some-uuid/ticket5674/twist.patch) by cremona created at 2009-04-03 11:09:50

apply to 3.4.1.apha0 + #4667 patches



---

archive/issue_comments_044393.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-04-03T11:14:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5674#issuecomment-44393",
    "user": "cremona"
}
```

Resolution: duplicate



---

archive/issue_comments_044394.json:
```json
{
    "body": "Sorry I must have pressed too many buttons...",
    "created_at": "2009-04-03T11:14:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5674#issuecomment-44394",
    "user": "cremona"
}
```

Sorry I must have pressed too many buttons...
