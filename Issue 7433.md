# Issue 7433: notebook: changing title of worksheet changes title of corresponding published worksheet

archive/issues_007433.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  was mpatel\n\nThis is a really weird bug. \n\n1. Create a worksheet W and publish it to make a published worksheet P.  Do *not* check \"Automatically re-publish when changes are made\". \n\n2. Change the title of W and something in the body of W.  Notice that in the list of published worksheets the title of P doesn't change.  However, click on P in that list, and notice that the title *does* change at the top of the worksheet.  The body doesn't change, fortunately. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7433\n\n",
    "created_at": "2009-11-11T22:14:15Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "notebook: changing title of worksheet changes title of corresponding published worksheet",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7433",
    "user": "was"
}
```
Assignee: boothby

CC:  was mpatel

This is a really weird bug. 

1. Create a worksheet W and publish it to make a published worksheet P.  Do *not* check "Automatically re-publish when changes are made". 

2. Change the title of W and something in the body of W.  Notice that in the list of published worksheets the title of P doesn't change.  However, click on P in that list, and notice that the title *does* change at the top of the worksheet.  The body doesn't change, fortunately. 

Issue created by migration from https://trac.sagemath.org/ticket/7433





---

archive/issue_comments_062535.json:
```json
{
    "body": "Attachment [trac_7433-published-ws-rename.patch](tarball://root/attachments/some-uuid/ticket7433/trac_7433-published-ws-rename.patch) by timdumol created at 2009-11-14 13:16:02\n\nFixes template bug.",
    "created_at": "2009-11-14T13:16:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7433#issuecomment-62535",
    "user": "timdumol"
}
```

Attachment [trac_7433-published-ws-rename.patch](tarball://root/attachments/some-uuid/ticket7433/trac_7433-published-ws-rename.patch) by timdumol created at 2009-11-14 13:16:02

Fixes template bug.



---

archive/issue_comments_062536.json:
```json
{
    "body": "The problem was with a template bug referencing the original worksheet's title instead of the published worksheet's title. Patch up. I'll add the tests later (or whoever else wants to)",
    "created_at": "2009-11-14T13:16:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7433#issuecomment-62536",
    "user": "timdumol"
}
```

The problem was with a template bug referencing the original worksheet's title instead of the published worksheet's title. Patch up. I'll add the tests later (or whoever else wants to)



---

archive/issue_comments_062537.json:
```json
{
    "body": "Attachment [trac_7433-published-ws-rename.2.patch](tarball://root/attachments/some-uuid/ticket7433/trac_7433-published-ws-rename.2.patch) by timdumol created at 2009-11-14 16:49:02\n\nFixes template bug and adds Selenium tests.",
    "created_at": "2009-11-14T16:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7433#issuecomment-62537",
    "user": "timdumol"
}
```

Attachment [trac_7433-published-ws-rename.2.patch](tarball://root/attachments/some-uuid/ticket7433/trac_7433-published-ws-rename.2.patch) by timdumol created at 2009-11-14 16:49:02

Fixes template bug and adds Selenium tests.



---

archive/issue_comments_062538.json:
```json
{
    "body": "Alright, tests and template fix up.",
    "created_at": "2009-11-14T16:49:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7433#issuecomment-62538",
    "user": "timdumol"
}
```

Alright, tests and template fix up.



---

archive/issue_comments_062539.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-14T16:49:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7433#issuecomment-62539",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062540.json:
```json
{
    "body": "Attachment [sagenb_7433-rebase.patch](tarball://root/attachments/some-uuid/ticket7433/sagenb_7433-rebase.patch) by was created at 2009-12-08 20:55:07",
    "created_at": "2009-12-08T20:55:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7433#issuecomment-62540",
    "user": "was"
}
```

Attachment [sagenb_7433-rebase.patch](tarball://root/attachments/some-uuid/ticket7433/sagenb_7433-rebase.patch) by was created at 2009-12-08 20:55:07



---

archive/issue_comments_062541.json:
```json
{
    "body": "This works fine for me and fixes the problem. \n\nI haven't verified that the selenium tests work, since I can't run Selenium yet on my OS X computer. \n\nNote that the patch needed to be rebased for me, so I've posted a rebased patch.",
    "created_at": "2009-12-08T20:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7433#issuecomment-62541",
    "user": "was"
}
```

This works fine for me and fixes the problem. 

I haven't verified that the selenium tests work, since I can't run Selenium yet on my OS X computer. 

Note that the patch needed to be rebased for me, so I've posted a rebased patch.



---

archive/issue_comments_062542.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-08T20:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7433#issuecomment-62542",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062543.json:
```json
{
    "body": "merged into sagenb-0.4.6",
    "created_at": "2009-12-09T01:07:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7433#issuecomment-62543",
    "user": "was"
}
```

merged into sagenb-0.4.6



---

archive/issue_comments_062544.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-09T01:07:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7433#issuecomment-62544",
    "user": "was"
}
```

Resolution: fixed
