# Issue 7433: notebook: changing title of worksheet changes title of corresponding published worksheet

archive/issues_007433.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @williamstein @qed777\n\nThis is a really weird bug. \n\n1. Create a worksheet W and publish it to make a published worksheet P.  Do *not* check \"Automatically re-publish when changes are made\". \n\n2. Change the title of W and something in the body of W.  Notice that in the list of published worksheets the title of P doesn't change.  However, click on P in that list, and notice that the title *does* change at the top of the worksheet.  The body doesn't change, fortunately. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7433\n\n",
    "created_at": "2009-11-11T22:14:15Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "notebook: changing title of worksheet changes title of corresponding published worksheet",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7433",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

CC:  @williamstein @qed777

This is a really weird bug. 

1. Create a worksheet W and publish it to make a published worksheet P.  Do *not* check "Automatically re-publish when changes are made". 

2. Change the title of W and something in the body of W.  Notice that in the list of published worksheets the title of P doesn't change.  However, click on P in that list, and notice that the title *does* change at the top of the worksheet.  The body doesn't change, fortunately. 

Issue created by migration from https://trac.sagemath.org/ticket/7433





---

archive/issue_comments_062420.json:
```json
{
    "body": "Attachment [trac_7433-published-ws-rename.patch](tarball://root/attachments/some-uuid/ticket7433/trac_7433-published-ws-rename.patch) by @TimDumol created at 2009-11-14 13:16:02\n\nFixes template bug.",
    "created_at": "2009-11-14T13:16:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7433#issuecomment-62420",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7433-published-ws-rename.patch](tarball://root/attachments/some-uuid/ticket7433/trac_7433-published-ws-rename.patch) by @TimDumol created at 2009-11-14 13:16:02

Fixes template bug.



---

archive/issue_comments_062421.json:
```json
{
    "body": "The problem was with a template bug referencing the original worksheet's title instead of the published worksheet's title. Patch up. I'll add the tests later (or whoever else wants to)",
    "created_at": "2009-11-14T13:16:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7433#issuecomment-62421",
    "user": "https://github.com/TimDumol"
}
```

The problem was with a template bug referencing the original worksheet's title instead of the published worksheet's title. Patch up. I'll add the tests later (or whoever else wants to)



---

archive/issue_comments_062422.json:
```json
{
    "body": "Attachment [trac_7433-published-ws-rename.2.patch](tarball://root/attachments/some-uuid/ticket7433/trac_7433-published-ws-rename.2.patch) by @TimDumol created at 2009-11-14 16:49:02\n\nFixes template bug and adds Selenium tests.",
    "created_at": "2009-11-14T16:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7433#issuecomment-62422",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7433-published-ws-rename.2.patch](tarball://root/attachments/some-uuid/ticket7433/trac_7433-published-ws-rename.2.patch) by @TimDumol created at 2009-11-14 16:49:02

Fixes template bug and adds Selenium tests.



---

archive/issue_comments_062423.json:
```json
{
    "body": "Alright, tests and template fix up.",
    "created_at": "2009-11-14T16:49:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7433#issuecomment-62423",
    "user": "https://github.com/TimDumol"
}
```

Alright, tests and template fix up.



---

archive/issue_comments_062424.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-14T16:49:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7433#issuecomment-62424",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062425.json:
```json
{
    "body": "Attachment [sagenb_7433-rebase.patch](tarball://root/attachments/some-uuid/ticket7433/sagenb_7433-rebase.patch) by @williamstein created at 2009-12-08 20:55:07",
    "created_at": "2009-12-08T20:55:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7433#issuecomment-62425",
    "user": "https://github.com/williamstein"
}
```

Attachment [sagenb_7433-rebase.patch](tarball://root/attachments/some-uuid/ticket7433/sagenb_7433-rebase.patch) by @williamstein created at 2009-12-08 20:55:07



---

archive/issue_comments_062426.json:
```json
{
    "body": "This works fine for me and fixes the problem. \n\nI haven't verified that the selenium tests work, since I can't run Selenium yet on my OS X computer. \n\nNote that the patch needed to be rebased for me, so I've posted a rebased patch.",
    "created_at": "2009-12-08T20:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7433#issuecomment-62426",
    "user": "https://github.com/williamstein"
}
```

This works fine for me and fixes the problem. 

I haven't verified that the selenium tests work, since I can't run Selenium yet on my OS X computer. 

Note that the patch needed to be rebased for me, so I've posted a rebased patch.



---

archive/issue_comments_062427.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-08T20:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7433#issuecomment-62427",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062428.json:
```json
{
    "body": "merged into sagenb-0.4.6",
    "created_at": "2009-12-09T01:07:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7433#issuecomment-62428",
    "user": "https://github.com/williamstein"
}
```

merged into sagenb-0.4.6



---

archive/issue_events_007656.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2009-12-09T01:07:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7433",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7433#event-7656"
}
```



---

archive/issue_comments_062429.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-09T01:07:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7433#issuecomment-62429",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
