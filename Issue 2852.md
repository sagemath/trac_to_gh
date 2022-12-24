# Issue 2852: ctrl-enter broken in firefox/linux

archive/issues_002852.json:
```json
{
    "body": "Assignee: boothby\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2852\n\n",
    "created_at": "2008-04-08T05:35:26Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "ctrl-enter broken in firefox/linux",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2852",
    "user": "boothby"
}
```
Assignee: boothby



Issue created by migration from https://trac.sagemath.org/ticket/2852





---

archive/issue_comments_019574.json:
```json
{
    "body": "Attachment [2852-keyfixes.patch](tarball://root/attachments/some-uuid/ticket2852/2852-keyfixes.patch) by boothby created at 2008-04-08 05:40:36\n\nThe attached should be approached with distrust.  It makes a very low-level change to how key events are handled.  Test all keycodes in all browsers before and after applying this patch.",
    "created_at": "2008-04-08T05:40:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2852#issuecomment-19574",
    "user": "boothby"
}
```

Attachment [2852-keyfixes.patch](tarball://root/attachments/some-uuid/ticket2852/2852-keyfixes.patch) by boothby created at 2008-04-08 05:40:36

The attached should be approached with distrust.  It makes a very low-level change to how key events are handled.  Test all keycodes in all browsers before and after applying this patch.



---

archive/issue_comments_019575.json:
```json
{
    "body": "It looks good to me.  I'm going to test the heck out of the notebook before 3.0 is released anyways, so I say we apply this. \n\nNOTE: I updated a comment that should be updated because of this patch, but that will go in a subsequent \"fix of a few small bugs\" notebook patch I'll post shortly.",
    "created_at": "2008-04-08T13:27:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2852#issuecomment-19575",
    "user": "@williamstein"
}
```

It looks good to me.  I'm going to test the heck out of the notebook before 3.0 is released anyways, so I say we apply this. 

NOTE: I updated a comment that should be updated because of this patch, but that will go in a subsequent "fix of a few small bugs" notebook patch I'll post shortly.



---

archive/issue_comments_019576.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-08T15:33:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2852#issuecomment-19576",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019577.json:
```json
{
    "body": "Merged in Sage 3.0.alpha3",
    "created_at": "2008-04-08T15:33:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2852#issuecomment-19577",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha3
