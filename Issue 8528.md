# Issue 8528: type in an exception

archive/issues_008528.json:
```json
{
    "body": "Assignee: @burcin\n\nhere it is\n\n```\nsage: x.n()\nTraceback (most recent call last)\n...\nTypeError: cannot evaluate symbolic expresssion numerically\n                                         ^^^\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/8528\n\n",
    "created_at": "2010-03-13T21:53:53Z",
    "labels": [
        "component: symbolics",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "type in an exception",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8528",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```
Assignee: @burcin

here it is

```
sage: x.n()
Traceback (most recent call last)
...
TypeError: cannot evaluate symbolic expresssion numerically
                                         ^^^
```

Issue created by migration from https://trac.sagemath.org/ticket/8528





---

archive/issue_comments_076938.json:
```json
{
    "body": "Attachment [trac_8528-typo.patch](tarball://root/attachments/some-uuid/ticket8528/trac_8528-typo.patch) by mvngu created at 2010-03-14 00:39:35\n\nbased on Sage 4.3.4.alpha1",
    "created_at": "2010-03-14T00:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8528#issuecomment-76938",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8528-typo.patch](tarball://root/attachments/some-uuid/ticket8528/trac_8528-typo.patch) by mvngu created at 2010-03-14 00:39:35

based on Sage 4.3.4.alpha1



---

archive/issue_events_020520.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-03-14T00:40:08Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8528",
    "milestone": "sage-4.3.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8528#event-20520"
}
```



---

archive/issue_comments_076939.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-14T00:40:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8528#issuecomment-76939",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076940.json:
```json
{
    "body": "Changing priority from trivial to minor.",
    "created_at": "2010-03-14T05:49:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8528#issuecomment-76940",
    "user": "https://github.com/jhpalmieri"
}
```

Changing priority from trivial to minor.



---

archive/issue_comments_076941.json:
```json
{
    "body": "How about a doctest?  Here's a patch.  (Your patch gets a positive review.)",
    "created_at": "2010-03-14T05:49:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8528#issuecomment-76941",
    "user": "https://github.com/jhpalmieri"
}
```

How about a doctest?  Here's a patch.  (Your patch gets a positive review.)



---

archive/issue_comments_076942.json:
```json
{
    "body": "apply on top of other patch",
    "created_at": "2010-03-14T05:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8528#issuecomment-76942",
    "user": "https://github.com/jhpalmieri"
}
```

apply on top of other patch



---

archive/issue_comments_076943.json:
```json
{
    "body": "Attachment [trac_8528-doctests.patch](tarball://root/attachments/some-uuid/ticket8528/trac_8528-doctests.patch) by mvngu created at 2010-03-14 06:23:43",
    "created_at": "2010-03-14T06:23:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8528#issuecomment-76943",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8528-doctests.patch](tarball://root/attachments/some-uuid/ticket8528/trac_8528-doctests.patch) by mvngu created at 2010-03-14 06:23:43



---

archive/issue_comments_076944.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-14T06:23:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8528#issuecomment-76944",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076945.json:
```json
{
    "body": "Merged in this order:\n\n1. [trac_8528-typo.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8528/trac_8528-typo.patch)\n2. [trac_8528-doctests.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8528/trac_8528-doctests.patch)",
    "created_at": "2010-03-14T22:39:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8528#issuecomment-76945",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged in this order:

1. [trac_8528-typo.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8528/trac_8528-typo.patch)
2. [trac_8528-doctests.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8528/trac_8528-doctests.patch)



---

archive/issue_comments_076946.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-14T22:39:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8528#issuecomment-76946",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_020521.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-03-14T22:39:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8528",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8528#event-20521"
}
```
