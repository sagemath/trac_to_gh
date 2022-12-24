# Issue 9180: Absolute interval arithmetic

archive/issues_009180.json:
```json
{
    "body": "Assignee: jason, jkantor\n\nCC:  rishi jdemeyer\n\nNeeded for #4475, but quite self contained and doesn't require any number theory to understand or review. \n\nIssue created by migration from https://trac.sagemath.org/ticket/9180\n\n",
    "created_at": "2010-06-07T20:40:08Z",
    "labels": [
        "numerical",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.2",
    "title": "Absolute interval arithmetic",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9180",
    "user": "robertwb"
}
```
Assignee: jason, jkantor

CC:  rishi jdemeyer

Needed for #4475, but quite self contained and doesn't require any number theory to understand or review. 

Issue created by migration from https://trac.sagemath.org/ticket/9180





---

archive/issue_comments_085882.json:
```json
{
    "body": "Attachment [9180-abs-interval.patch](tarball://root/attachments/some-uuid/ticket9180/9180-abs-interval.patch) by robertwb created at 2010-06-07 21:27:04",
    "created_at": "2010-06-07T21:27:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9180#issuecomment-85882",
    "user": "robertwb"
}
```

Attachment [9180-abs-interval.patch](tarball://root/attachments/some-uuid/ticket9180/9180-abs-interval.patch) by robertwb created at 2010-06-07 21:27:04



---

archive/issue_comments_085883.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-07T21:27:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9180#issuecomment-85883",
    "user": "robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085884.json:
```json
{
    "body": "apply on top of previous",
    "created_at": "2010-06-09T01:50:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9180#issuecomment-85884",
    "user": "robertwb"
}
```

apply on top of previous



---

archive/issue_comments_085885.json:
```json
{
    "body": "Attachment [9180-real-mpfi-conversion.patch](tarball://root/attachments/some-uuid/ticket9180/9180-real-mpfi-conversion.patch) by rishi created at 2010-08-08 02:47:42",
    "created_at": "2010-08-08T02:47:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9180#issuecomment-85885",
    "user": "rishi"
}
```

Attachment [9180-real-mpfi-conversion.patch](tarball://root/attachments/some-uuid/ticket9180/9180-real-mpfi-conversion.patch) by rishi created at 2010-08-08 02:47:42



---

archive/issue_comments_085886.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-06-18T13:32:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9180#issuecomment-85886",
    "user": "kedlaya"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085887.json:
```json
{
    "body": "Attachment [9180-bitrot.patch](tarball://root/attachments/some-uuid/ticket9180/9180-bitrot.patch) by kedlaya created at 2011-06-18 13:32:44\n\nApplies against 4.7, no long doctest failures. Looks fine to me.",
    "created_at": "2011-06-18T13:32:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9180#issuecomment-85887",
    "user": "kedlaya"
}
```

Attachment [9180-bitrot.patch](tarball://root/attachments/some-uuid/ticket9180/9180-bitrot.patch) by kedlaya created at 2011-06-18 13:32:44

Applies against 4.7, no long doctest failures. Looks fine to me.



---

archive/issue_comments_085888.json:
```json
{
    "body": "Should all 3 patches be applied?",
    "created_at": "2011-06-19T08:42:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9180#issuecomment-85888",
    "user": "jdemeyer"
}
```

Should all 3 patches be applied?



---

archive/issue_comments_085889.json:
```json
{
    "body": "All three patches should be applied in order, yes.",
    "created_at": "2011-06-19T14:13:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9180#issuecomment-85889",
    "user": "kedlaya"
}
```

All three patches should be applied in order, yes.



---

archive/issue_comments_085890.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-07-22T12:49:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9180#issuecomment-85890",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_085891.json:
```json
{
    "body": "This broke Cygwin, just FYI.  Needs library 'gmp'.  See #11744.  Patch should be very similar to one at #11499.",
    "created_at": "2011-08-25T16:59:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9180#issuecomment-85891",
    "user": "kcrisman"
}
```

This broke Cygwin, just FYI.  Needs library 'gmp'.  See #11744.  Patch should be very similar to one at #11499.
