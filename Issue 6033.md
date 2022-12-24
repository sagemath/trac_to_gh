# Issue 6033: Bring plot/disk.py to 100% coverage

archive/issues_006033.json:
```json
{
    "body": "Assignee: tba\n\nBring plot/disk.py to 100% coverage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6033\n\n",
    "created_at": "2009-05-13T01:38:15Z",
    "labels": [
        "documentation",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "Bring plot/disk.py to 100% coverage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6033",
    "user": "kcrisman"
}
```
Assignee: tba

Bring plot/disk.py to 100% coverage.

Issue created by migration from https://trac.sagemath.org/ticket/6033





---

archive/issue_comments_048033.json:
```json
{
    "body": "Attachment [trac_6033.patch](tarball://root/attachments/some-uuid/ticket6033/trac_6033.patch) by kcrisman created at 2009-05-13 01:40:12",
    "created_at": "2009-05-13T01:40:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6033#issuecomment-48033",
    "user": "kcrisman"
}
```

Attachment [trac_6033.patch](tarball://root/attachments/some-uuid/ticket6033/trac_6033.patch) by kcrisman created at 2009-05-13 01:40:12



---

archive/issue_comments_048034.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-13T01:42:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6033#issuecomment-48034",
    "user": "kcrisman"
}
```

Changing status from new to assigned.



---

archive/issue_comments_048035.json:
```json
{
    "body": "This patch brings coverage to 100% for plot/disk.py, clarifies that disk really means sector/wedge of a circle, and adds a plot3d method for disks.\n\nSee [http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43](http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43) for why there is no loads(dumps()) test.",
    "created_at": "2009-05-13T01:42:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6033#issuecomment-48035",
    "user": "kcrisman"
}
```

This patch brings coverage to 100% for plot/disk.py, clarifies that disk really means sector/wedge of a circle, and adds a plot3d method for disks.

See [http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43](http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43) for why there is no loads(dumps()) test.



---

archive/issue_comments_048036.json:
```json
{
    "body": "Changing assignee from tba to kcrisman.",
    "created_at": "2009-05-13T01:42:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6033#issuecomment-48036",
    "user": "kcrisman"
}
```

Changing assignee from tba to kcrisman.



---

archive/issue_comments_048037.json:
```json
{
    "body": "No review, no milestone 4.0 ;)\n\nCheers,\n\nMichael",
    "created_at": "2009-05-14T05:36:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6033#issuecomment-48037",
    "user": "mabshoff"
}
```

No review, no milestone 4.0 ;)

Cheers,

Michael



---

archive/issue_comments_048038.json:
```json
{
    "body": "Both depend on #6023",
    "created_at": "2009-05-14T16:17:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6033#issuecomment-48038",
    "user": "kcrisman"
}
```

Both depend on #6023



---

archive/issue_comments_048039.json:
```json
{
    "body": "Attachment [trac_6033-fix.patch](tarball://root/attachments/some-uuid/ticket6033/trac_6033-fix.patch) by jason created at 2009-05-30 03:57:40\n\napply on top of previous patches",
    "created_at": "2009-05-30T03:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6033#issuecomment-48039",
    "user": "jason"
}
```

Attachment [trac_6033-fix.patch](tarball://root/attachments/some-uuid/ticket6033/trac_6033-fix.patch) by jason created at 2009-05-30 03:57:40

apply on top of previous patches



---

archive/issue_comments_048040.json:
```json
{
    "body": "Attachment [trac_6033-referee.patch](tarball://root/attachments/some-uuid/ticket6033/trac_6033-referee.patch) by jason created at 2009-05-30 03:58:32\n\nI added the 'color' synonym to rgbcolor and changed the docs accordingly.  I also added another sentence.\n\nPositive review for kcrisman's patches.  kcrisman: can you review my patch?",
    "created_at": "2009-05-30T03:58:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6033#issuecomment-48040",
    "user": "jason"
}
```

Attachment [trac_6033-referee.patch](tarball://root/attachments/some-uuid/ticket6033/trac_6033-referee.patch) by jason created at 2009-05-30 03:58:32

I added the 'color' synonym to rgbcolor and changed the docs accordingly.  I also added another sentence.

Positive review for kcrisman's patches.  kcrisman: can you review my patch?



---

archive/issue_comments_048041.json:
```json
{
    "body": "Attachment [trac_6033-ref-of-ref.2.patch](tarball://root/attachments/some-uuid/ticket6033/trac_6033-ref-of-ref.2.patch) by kcrisman created at 2009-06-01 14:18:32\n\nPositive review of referee patch; jason, can you review this final patch which makes a couple things more clear (e.g. if someone tried to plot the first example without using thickness and then view it, they might get confused, 2nd example should keep color since that is part of the subplot rendering, etc.)?  \n\nThen apply all four patches once reviewed.  I had some trouble attaching the last one, so if there are two identical ones with the same name only use one of them!",
    "created_at": "2009-06-01T14:18:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6033#issuecomment-48041",
    "user": "kcrisman"
}
```

Attachment [trac_6033-ref-of-ref.2.patch](tarball://root/attachments/some-uuid/ticket6033/trac_6033-ref-of-ref.2.patch) by kcrisman created at 2009-06-01 14:18:32

Positive review of referee patch; jason, can you review this final patch which makes a couple things more clear (e.g. if someone tried to plot the first example without using thickness and then view it, they might get confused, 2nd example should keep color since that is part of the subplot rendering, etc.)?  

Then apply all four patches once reviewed.  I had some trouble attaching the last one, so if there are two identical ones with the same name only use one of them!



---

archive/issue_comments_048042.json:
```json
{
    "body": "The last patch looks fine to me.\n\nMerged in 4.0.1.rc1.",
    "created_at": "2009-06-04T19:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6033#issuecomment-48042",
    "user": "mhansen"
}
```

The last patch looks fine to me.

Merged in 4.0.1.rc1.



---

archive/issue_comments_048043.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-04T19:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6033#issuecomment-48043",
    "user": "mhansen"
}
```

Resolution: fixed
