# Issue 9649: c_lib/include/interrupt.h: rename FOO_H

archive/issues_009649.json:
```json
{
    "body": "Assignee: @jasongrout\n\nIn c_lib/include/interrupt.h, there is\n\n```\n#ifndef FOO_H\n#define FOO_H\n```\n\nto protect the header.  This FOO_H should be changed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9649\n\n",
    "created_at": "2010-07-31T08:23:54Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "c_lib/include/interrupt.h: rename FOO_H",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9649",
    "user": "@jdemeyer"
}
```
Assignee: @jasongrout

In c_lib/include/interrupt.h, there is

```
#ifndef FOO_H
#define FOO_H
```

to protect the header.  This FOO_H should be changed.

Issue created by migration from https://trac.sagemath.org/ticket/9649





---

archive/issue_comments_093571.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-31T08:24:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9649#issuecomment-93571",
    "user": "@jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093572.json:
```json
{
    "body": "Rename FOO_H to C_LIB_INCLUDE_INTERRUPT_H",
    "created_at": "2010-07-31T08:25:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9649#issuecomment-93572",
    "user": "@jdemeyer"
}
```

Rename FOO_H to C_LIB_INCLUDE_INTERRUPT_H



---

archive/issue_comments_093573.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-31T19:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9649#issuecomment-93573",
    "user": "@robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093574.json:
```json
{
    "body": "Attachment [9649.patch](tarball://root/attachments/some-uuid/ticket9649/9649.patch) by @robertwb created at 2010-07-31 19:00:35\n\nThis is obviously code that went in before the referee process :).",
    "created_at": "2010-07-31T19:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9649#issuecomment-93574",
    "user": "@robertwb"
}
```

Attachment [9649.patch](tarball://root/attachments/some-uuid/ticket9649/9649.patch) by @robertwb created at 2010-07-31 19:00:35

This is obviously code that went in before the referee process :).



---

archive/issue_comments_093575.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-09T09:41:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9649#issuecomment-93575",
    "user": "@qed777"
}
```

Resolution: fixed
