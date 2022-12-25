# Issue 7802: Mention that RNDN is the "ties toward even" version in RealField

archive/issues_007802.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @robertwb mvngu\n\nThe IEEE754 standard has two versions of \"round to nearest\".  It appears that ours is the \"ties toward even\" version (see http://www.mpfr.org/mpfr-current/mpfr.html#MPFR-Basics).  We ought to mention this in the docs to RealField when it talks about the rounding modes.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7802\n\n",
    "created_at": "2010-01-01T10:52:06Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Mention that RNDN is the \"ties toward even\" version in RealField",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7802",
    "user": "https://github.com/jasongrout"
}
```
Assignee: mvngu

CC:  @robertwb mvngu

The IEEE754 standard has two versions of "round to nearest".  It appears that ours is the "ties toward even" version (see http://www.mpfr.org/mpfr-current/mpfr.html#MPFR-Basics).  We ought to mention this in the docs to RealField when it talks about the rounding modes.

Issue created by migration from https://trac.sagemath.org/ticket/7802





---

archive/issue_comments_067385.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-20T06:14:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7802#issuecomment-67385",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067386.json:
```json
{
    "body": "Attachment [trac-7802-ties-to-even-doc.patch](tarball://root/attachments/some-uuid/ticket7802/trac-7802-ties-to-even-doc.patch) by @jasongrout created at 2010-01-20 06:14:08",
    "created_at": "2010-01-20T06:14:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7802#issuecomment-67386",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-7802-ties-to-even-doc.patch](tarball://root/attachments/some-uuid/ticket7802/trac-7802-ties-to-even-doc.patch) by @jasongrout created at 2010-01-20 06:14:08



---

archive/issue_comments_067387.json:
```json
{
    "body": "Looks good. Applies OK against Sage 4.3.1.rc1. Just make sure you first merge #7999 before applying [trac-7802-ties-to-even-doc.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7802/trac-7802-ties-to-even-doc.patch). Otherwise, the HTML version of the reference manual won't build successfully.",
    "created_at": "2010-01-20T08:00:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7802#issuecomment-67387",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Looks good. Applies OK against Sage 4.3.1.rc1. Just make sure you first merge #7999 before applying [trac-7802-ties-to-even-doc.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7802/trac-7802-ties-to-even-doc.patch). Otherwise, the HTML version of the reference manual won't build successfully.



---

archive/issue_comments_067388.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T08:00:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7802#issuecomment-67388",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067389.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-23T16:57:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7802#issuecomment-67389",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
