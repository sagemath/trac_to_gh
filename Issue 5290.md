# Issue 5290: Sage 3.3.rc1: Sage fails to start due to dangling missed import in plot.py

archive/issues_005290.json:
```json
{
    "body": "Assignee: mabshoff\n\nIt wasn't my fault, but patch is coming up.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5290\n\n",
    "created_at": "2009-02-17T02:17:57Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Sage 3.3.rc1: Sage fails to start due to dangling missed import in plot.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5290",
    "user": "mabshoff"
}
```
Assignee: mabshoff

It wasn't my fault, but patch is coming up.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5290





---

archive/issue_comments_040651.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-17T02:18:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5290#issuecomment-40651",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040652.json:
```json
{
    "body": "We all agree that the correct fix is to *delete* the offending line, not just comment it out.",
    "created_at": "2009-02-17T05:36:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5290#issuecomment-40652",
    "user": "jason"
}
```

We all agree that the correct fix is to *delete* the offending line, not just comment it out.



---

archive/issue_comments_040653.json:
```json
{
    "body": "Attachment [trac_5290.patch](tarball://root/attachments/some-uuid/ticket5290/trac_5290.patch) by mabshoff created at 2009-02-17 05:41:25",
    "created_at": "2009-02-17T05:41:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5290#issuecomment-40653",
    "user": "mabshoff"
}
```

Attachment [trac_5290.patch](tarball://root/attachments/some-uuid/ticket5290/trac_5290.patch) by mabshoff created at 2009-02-17 05:41:25



---

archive/issue_comments_040654.json:
```json
{
    "body": "If the patch is changed to deleting the line instead of just commenting it out, positive review.  It fixes my rc1 so that it starts up.",
    "created_at": "2009-02-17T05:44:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5290#issuecomment-40654",
    "user": "jason"
}
```

If the patch is changed to deleting the line instead of just commenting it out, positive review.  It fixes my rc1 so that it starts up.



---

archive/issue_comments_040655.json:
```json
{
    "body": "Attachment [trac_5290-deletion.patch](tarball://root/attachments/some-uuid/ticket5290/trac_5290-deletion.patch) by mabshoff created at 2009-02-17 06:29:41",
    "created_at": "2009-02-17T06:29:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5290#issuecomment-40655",
    "user": "mabshoff"
}
```

Attachment [trac_5290-deletion.patch](tarball://root/attachments/some-uuid/ticket5290/trac_5290-deletion.patch) by mabshoff created at 2009-02-17 06:29:41



---

archive/issue_comments_040656.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-17T06:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5290#issuecomment-40656",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040657.json:
```json
{
    "body": "Merged both patches in Sage 3.3.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-17T06:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5290#issuecomment-40657",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.3.rc2.

Cheers,

Michael



---

archive/issue_comments_040658.json:
```json
{
    "body": "Ok, changing the review to an offical positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-17T07:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5290#issuecomment-40658",
    "user": "mabshoff"
}
```

Ok, changing the review to an offical positive review.

Cheers,

Michael
