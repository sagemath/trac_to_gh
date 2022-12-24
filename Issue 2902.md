# Issue 2902: notebook -- resize of cell should also fire on paste into the cell

archive/issues_002902.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @williamstein @qed777\n\nWhen you paste into a cell it should resize as a result.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2902\n\n",
    "created_at": "2008-04-13T02:31:29Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "notebook -- resize of cell should also fire on paste into the cell",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2902",
    "user": "@williamstein"
}
```
Assignee: boothby

CC:  @williamstein @qed777

When you paste into a cell it should resize as a result.

Issue created by migration from https://trac.sagemath.org/ticket/2902





---

archive/issue_comments_019999.json:
```json
{
    "body": "This isn't an \"easy\" problem, but it looks [this](http://www.intridea.com/2007/12/16/faking-onpaste-in-firefox) should do the trick.",
    "created_at": "2008-04-13T16:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2902#issuecomment-19999",
    "user": "boothby"
}
```

This isn't an "easy" problem, but it looks [this](http://www.intridea.com/2007/12/16/faking-onpaste-in-firefox) should do the trick.



---

archive/issue_comments_020000.json:
```json
{
    "body": "Attachment [trac_2902-paste-resize.patch](tarball://root/attachments/some-uuid/ticket2902/trac_2902-paste-resize.patch) by @TimDumol created at 2009-11-19 19:05:26\n\nSets `onpaste` handler to resize cells.",
    "created_at": "2009-11-19T19:05:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2902#issuecomment-20000",
    "user": "@TimDumol"
}
```

Attachment [trac_2902-paste-resize.patch](tarball://root/attachments/some-uuid/ticket2902/trac_2902-paste-resize.patch) by @TimDumol created at 2009-11-19 19:05:26

Sets `onpaste` handler to resize cells.



---

archive/issue_comments_020001.json:
```json
{
    "body": "This patch should fix it. I don't know how to test this in Selenium (C-C is not always copy, and same with C-V (e.g., mine are C-Z C-C and C-Z C-V)).",
    "created_at": "2009-11-19T19:07:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2902#issuecomment-20001",
    "user": "@TimDumol"
}
```

This patch should fix it. I don't know how to test this in Selenium (C-C is not always copy, and same with C-V (e.g., mine are C-Z C-C and C-Z C-V)).



---

archive/issue_comments_020002.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-19T19:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2902#issuecomment-20002",
    "user": "@TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_020003.json:
```json
{
    "body": "Oh, depends on #7433.",
    "created_at": "2009-11-19T19:13:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2902#issuecomment-20003",
    "user": "@TimDumol"
}
```

Oh, depends on #7433.



---

archive/issue_comments_020004.json:
```json
{
    "body": "Replying to [comment:4 timdumol]:\n> Oh, depends on #7433.\nNevermind. It doesn't.",
    "created_at": "2009-11-19T20:57:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2902#issuecomment-20004",
    "user": "@TimDumol"
}
```

Replying to [comment:4 timdumol]:
> Oh, depends on #7433.
Nevermind. It doesn't.



---

archive/issue_comments_020005.json:
```json
{
    "body": "That will not work on cells that are created after the page loads.",
    "created_at": "2009-11-19T21:03:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2902#issuecomment-20005",
    "user": "boothby"
}
```

That will not work on cells that are created after the page loads.



---

archive/issue_comments_020006.json:
```json
{
    "body": "Would any of the \"auto-grow\" plug-ins mentioned [comment:1:ticket:7201 here] help?  I'll email preliminary patches for two of them to timdumol, in case they're useful.  Unfortunately, I can't work on either ticket right now.\n\nOn the plug-ins: I think at least one of them uses a resizing strategy similar to the notebook's.  At least one uses a different strategy.  But the two I tried both have their quirks, discussed (and possibly fixed) in the comments on their pages.",
    "created_at": "2009-11-19T21:17:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2902#issuecomment-20006",
    "user": "@qed777"
}
```

Would any of the "auto-grow" plug-ins mentioned [comment:1:ticket:7201 here] help?  I'll email preliminary patches for two of them to timdumol, in case they're useful.  Unfortunately, I can't work on either ticket right now.

On the plug-ins: I think at least one of them uses a resizing strategy similar to the notebook's.  At least one uses a different strategy.  But the two I tried both have their quirks, discussed (and possibly fixed) in the comments on their pages.



---

archive/issue_comments_020007.json:
```json
{
    "body": "Ticket #7201 is related.",
    "created_at": "2009-11-19T21:20:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2902#issuecomment-20007",
    "user": "@qed777"
}
```

Ticket #7201 is related.



---

archive/issue_comments_020008.json:
```json
{
    "body": "ISSUES:\n\n1.\n\n> That will not work on cells that are created after the page loads. \n\nIndeed.  I don't think this patch should go in with that major shortcoming.  Can we just set the onpaste handler for all worksheet cells whenever they are created? \n\n2. I just tried pasting text into both firefox and safari cells and they *already* do resize.  So is this whole ticket just invalid?   Maybe no patch is needed at all anyways?    That matches with my memory, which is that Tom and I fixed this problem a year ago or so by rewriting the textarea resize code.",
    "created_at": "2009-12-08T19:19:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2902#issuecomment-20008",
    "user": "@williamstein"
}
```

ISSUES:

1.

> That will not work on cells that are created after the page loads. 

Indeed.  I don't think this patch should go in with that major shortcoming.  Can we just set the onpaste handler for all worksheet cells whenever they are created? 

2. I just tried pasting text into both firefox and safari cells and they *already* do resize.  So is this whole ticket just invalid?   Maybe no patch is needed at all anyways?    That matches with my memory, which is that Tom and I fixed this problem a year ago or so by rewriting the textarea resize code.



---

archive/issue_comments_020009.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-08T19:19:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2902#issuecomment-20009",
    "user": "@williamstein"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_020010.json:
```json
{
    "body": "In FF 3.5.5 on Linux, the cells do not resize on paste.  V16 at #6855 includes a fix that seems to work.  I'll try to check other browser-OS combinations.",
    "created_at": "2009-12-08T19:30:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2902#issuecomment-20010",
    "user": "@qed777"
}
```

In FF 3.5.5 on Linux, the cells do not resize on paste.  V16 at #6855 includes a fix that seems to work.  I'll try to check other browser-OS combinations.



---

archive/issue_comments_020011.json:
```json
{
    "body": "Replying to [comment:11 mpatel]:\n> In FF 3.5.5 on Linux, the cells do not resize on paste.  V16 at #6855 includes a fix that seems to work.  I'll try to check other browser-OS combinations.\n\nGood point that I should remark that I was testing with FF 3.5.5 on OS X.\n\n -- William",
    "created_at": "2009-12-09T14:25:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2902#issuecomment-20011",
    "user": "@williamstein"
}
```

Replying to [comment:11 mpatel]:
> In FF 3.5.5 on Linux, the cells do not resize on paste.  V16 at #6855 includes a fix that seems to work.  I'll try to check other browser-OS combinations.

Good point that I should remark that I was testing with FF 3.5.5 on OS X.

 -- William



---

archive/issue_comments_020012.json:
```json
{
    "body": "#7666 subsumes this ticket.  Please close this ticket when that one merges.",
    "created_at": "2010-01-18T05:48:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2902#issuecomment-20012",
    "user": "@qed777"
}
```

#7666 subsumes this ticket.  Please close this ticket when that one merges.



---

archive/issue_comments_020013.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-01-19T02:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2902#issuecomment-20013",
    "user": "@TimDumol"
}
```

Resolution: duplicate



---

archive/issue_comments_020014.json:
```json
{
    "body": "Fixed with #7666 (sagenb-0.6)",
    "created_at": "2010-01-19T02:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2902#issuecomment-20014",
    "user": "@TimDumol"
}
```

Fixed with #7666 (sagenb-0.6)
