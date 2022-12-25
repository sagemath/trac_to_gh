# Issue 8853: fix M_PI_4 in complex_double on Cygwin

archive/issues_008853.json:
```json
{
    "body": "Assignee: tbd\n\nApparently, it is not picked up from math.h.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8853\n\n",
    "created_at": "2010-05-03T12:29:15Z",
    "labels": [
        "component: porting: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.3",
    "title": "fix M_PI_4 in complex_double on Cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8853",
    "user": "https://github.com/mwhansen"
}
```
Assignee: tbd

Apparently, it is not picked up from math.h.

Issue created by migration from https://trac.sagemath.org/ticket/8853





---

archive/issue_comments_081230.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-03T13:18:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8853#issuecomment-81230",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081231.json:
```json
{
    "body": "Attachment [trac_8853-fix_complex_double.patch](tarball://root/attachments/some-uuid/ticket8853/trac_8853-fix_complex_double.patch) by @mwhansen created at 2010-05-03 13:18:04",
    "created_at": "2010-05-03T13:18:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8853#issuecomment-81231",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_8853-fix_complex_double.patch](tarball://root/attachments/some-uuid/ticket8853/trac_8853-fix_complex_double.patch) by @mwhansen created at 2010-05-03 13:18:04



---

archive/issue_comments_081232.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-25T02:08:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8853#issuecomment-81232",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081233.json:
```json
{
    "body": "works, but I created a referee patch that has more precision (using the #define on OS X; this can't hurt)...",
    "created_at": "2010-05-25T02:08:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8853#issuecomment-81233",
    "user": "https://github.com/williamstein"
}
```

works, but I created a referee patch that has more precision (using the #define on OS X; this can't hurt)...



---

archive/issue_events_009018.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2010-05-25T02:09:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8853",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8853#event-9018"
}
```



---

archive/issue_comments_081234.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-25T02:09:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8853#issuecomment-81234",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_081235.json:
```json
{
    "body": "Attachment [trac_8853-referee_version.patch](tarball://root/attachments/some-uuid/ticket8853/trac_8853-referee_version.patch) by @williamstein created at 2010-05-25 02:11:25",
    "created_at": "2010-05-25T02:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8853#issuecomment-81235",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_8853-referee_version.patch](tarball://root/attachments/some-uuid/ticket8853/trac_8853-referee_version.patch) by @williamstein created at 2010-05-25 02:11:25
