# Issue 1174: very minor bug in calculs _complex_ coercion.

archive/issues_001174.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1174\n\n",
    "created_at": "2007-11-15T07:46:36Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "very minor bug in calculs _complex_ coercion.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1174",
    "user": "@williamstein"
}
```
Assignee: @williamstein



Issue created by migration from https://trac.sagemath.org/ticket/1174





---

archive/issue_comments_007256.json:
```json
{
    "body": "Attachment [7349.patch](tarball://root/attachments/some-uuid/ticket1174/7349.patch) by @williamstein created at 2007-11-15 07:47:21\n\nI noticed this very slight mistake recently...",
    "created_at": "2007-11-15T07:47:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1174#issuecomment-7256",
    "user": "@williamstein"
}
```

Attachment [7349.patch](tarball://root/attachments/some-uuid/ticket1174/7349.patch) by @williamstein created at 2007-11-15 07:47:21

I noticed this very slight mistake recently...



---

archive/issue_comments_007257.json:
```json
{
    "body": "I approve.",
    "created_at": "2007-11-18T08:34:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1174#issuecomment-7257",
    "user": "@robertwb"
}
```

I approve.



---

archive/issue_comments_007258.json:
```json
{
    "body": "But there should be a doctest.",
    "created_at": "2007-11-18T08:34:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1174#issuecomment-7258",
    "user": "@robertwb"
}
```

But there should be a doctest.



---

archive/issue_comments_007259.json:
```json
{
    "body": "The patch is good, the problem is that none of the python functions (e.g. sqrt, sin) handle complex values.",
    "created_at": "2007-12-02T07:21:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1174#issuecomment-7259",
    "user": "@robertwb"
}
```

The patch is good, the problem is that none of the python functions (e.g. sqrt, sin) handle complex values.



---

archive/issue_comments_007260.json:
```json
{
    "body": "apply this after applying the other patch",
    "created_at": "2007-12-02T20:25:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1174#issuecomment-7260",
    "user": "@williamstein"
}
```

apply this after applying the other patch



---

archive/issue_comments_007261.json:
```json
{
    "body": "Attachment [trac-1174-part2.patch](tarball://root/attachments/some-uuid/ticket1174/trac-1174-part2.patch) by @williamstein created at 2007-12-02 20:25:48",
    "created_at": "2007-12-02T20:25:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1174#issuecomment-7261",
    "user": "@williamstein"
}
```

Attachment [trac-1174-part2.patch](tarball://root/attachments/some-uuid/ticket1174/trac-1174-part2.patch) by @williamstein created at 2007-12-02 20:25:48



---

archive/issue_comments_007262.json:
```json
{
    "body": "Attachment [trac-1174-part3.patch](tarball://root/attachments/some-uuid/ticket1174/trac-1174-part3.patch) by cwitty created at 2007-12-02 21:39:11\n\nLooks good to me; doctests pass in sage/calculus and sage/rings.  (Apply all three patches, in order.)",
    "created_at": "2007-12-02T21:39:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1174#issuecomment-7262",
    "user": "cwitty"
}
```

Attachment [trac-1174-part3.patch](tarball://root/attachments/some-uuid/ticket1174/trac-1174-part3.patch) by cwitty created at 2007-12-02 21:39:11

Looks good to me; doctests pass in sage/calculus and sage/rings.  (Apply all three patches, in order.)



---

archive/issue_comments_007263.json:
```json
{
    "body": "Merged in 2.8.15.rc0.",
    "created_at": "2007-12-02T22:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1174#issuecomment-7263",
    "user": "mabshoff"
}
```

Merged in 2.8.15.rc0.



---

archive/issue_comments_007264.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-02T22:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1174#issuecomment-7264",
    "user": "mabshoff"
}
```

Resolution: fixed
