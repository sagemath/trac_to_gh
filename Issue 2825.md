# Issue 2825: notebook -- document js.py some more

archive/issues_002825.json:
```json
{
    "body": "Assignee: boothby\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2825\n\n",
    "created_at": "2008-04-06T07:53:14Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "notebook -- document js.py some more",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2825",
    "user": "was"
}
```
Assignee: boothby



Issue created by migration from https://trac.sagemath.org/ticket/2825





---

archive/issue_comments_019399.json:
```json
{
    "body": "NOTE: In this patch, I fixed a weird design choice.  Namely, in the list of completion dialog, pressing the up arrow at the very top killed the whole dialog instead of wrapping around.  This is weird because the list wraps around in all other directions except up.  Also, esc gets one out of the dialog, so up arrow isn't needed to do this.  I suspect it was just tricky to implement this as wrap around, so Tom didn't.  But now in this patch it is \"fixed\".",
    "created_at": "2008-04-06T08:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2825#issuecomment-19399",
    "user": "was"
}
```

NOTE: In this patch, I fixed a weird design choice.  Namely, in the list of completion dialog, pressing the up arrow at the very top killed the whole dialog instead of wrapping around.  This is weird because the list wraps around in all other directions except up.  Also, esc gets one out of the dialog, so up arrow isn't needed to do this.  I suspect it was just tricky to implement this as wrap around, so Tom didn't.  But now in this patch it is "fixed".



---

archive/issue_comments_019400.json:
```json
{
    "body": "Attachment [sage-2825.patch](tarball://root/attachments/some-uuid/ticket2825/sage-2825.patch) by was created at 2008-04-06 09:48:08",
    "created_at": "2008-04-06T09:48:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2825#issuecomment-19400",
    "user": "was"
}
```

Attachment [sage-2825.patch](tarball://root/attachments/some-uuid/ticket2825/sage-2825.patch) by was created at 2008-04-06 09:48:08



---

archive/issue_comments_019401.json:
```json
{
    "body": "Patch looks good to me. One minor spelling issue:\n\n```\n Discard the curretn worksheet and quit the currently\n```\n\nI am fixing that in the patch I am applying.\n\nCheers,\n\nMichaeel",
    "created_at": "2008-04-06T14:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2825#issuecomment-19401",
    "user": "mabshoff"
}
```

Patch looks good to me. One minor spelling issue:

```
 Discard the curretn worksheet and quit the currently
```

I am fixing that in the patch I am applying.

Cheers,

Michaeel



---

archive/issue_comments_019402.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2",
    "created_at": "2008-04-06T14:43:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2825#issuecomment-19402",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha2



---

archive/issue_comments_019403.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-06T14:43:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2825#issuecomment-19403",
    "user": "mabshoff"
}
```

Resolution: fixed
