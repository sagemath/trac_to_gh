# Issue 1493: polybori doesn't free m4ri data on exit

archive/issues_001493.json:
```json
{
    "body": "Assignee: burcin\n\nThe polybori wrapper initializes m4ri by building some tables, but this is not freed on exit. As polybori is now imported from top level, this shows up as still reachable memory on valgrind for every sage session.\n\nThe bundle attached fixes this, along with a minor modification to remove a workaround for a polybori bug which is now fixed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1493\n\n",
    "created_at": "2007-12-13T20:39:42Z",
    "labels": [
        "memleak",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "polybori doesn't free m4ri data on exit",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1493",
    "user": "burcin"
}
```
Assignee: burcin

The polybori wrapper initializes m4ri by building some tables, but this is not freed on exit. As polybori is now imported from top level, this shows up as still reachable memory on valgrind for every sage session.

The bundle attached fixes this, along with a minor modification to remove a workaround for a polybori bug which is now fixed.

Issue created by migration from https://trac.sagemath.org/ticket/1493





---

archive/issue_comments_009596.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-14T02:28:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1493#issuecomment-9596",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009597.json:
```json
{
    "body": "Attachment [polybori_m4ri_free.hg](tarball://root/attachments/some-uuid/ticket1493/polybori_m4ri_free.hg) by mabshoff created at 2007-12-14 02:28:18\n\nMerged in 2.9.alpha7.",
    "created_at": "2007-12-14T02:28:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1493#issuecomment-9597",
    "user": "mabshoff"
}
```

Attachment [polybori_m4ri_free.hg](tarball://root/attachments/some-uuid/ticket1493/polybori_m4ri_free.hg) by mabshoff created at 2007-12-14 02:28:18

Merged in 2.9.alpha7.
