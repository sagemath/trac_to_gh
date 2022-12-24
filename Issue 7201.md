# Issue 7201: overflow: auto CSS on code cells

archive/issues_007201.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @williamstein @TimDumol\n\nEvery now and then, the auto-expansion of code cells doesn't quite get all of the code, which leads to frustration because you can't see the last line or two of your code in a cell.  I think this has happened when the code on a line wraps to the next line maybe (I don't have an example of it happening right now).\n\nAnyways, putting scroll bars on the code cells using the overflow attribute (so they're only there when they are needed) is an easy way to guard against errors in the auto-expansion code.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7201\n\n",
    "created_at": "2009-10-13T14:41:07Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "overflow: auto CSS on code cells",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7201",
    "user": "@jasongrout"
}
```
Assignee: boothby

CC:  @williamstein @TimDumol

Every now and then, the auto-expansion of code cells doesn't quite get all of the code, which leads to frustration because you can't see the last line or two of your code in a cell.  I think this has happened when the code on a line wraps to the next line maybe (I don't have an example of it happening right now).

Anyways, putting scroll bars on the code cells using the overflow attribute (so they're only there when they are needed) is an easy way to guard against errors in the auto-expansion code.

Issue created by migration from https://trac.sagemath.org/ticket/7201





---

archive/issue_comments_059758.json:
```json
{
    "body": "Potentially useful jQuery plug-ins:\n\n* [autoResize](http://james.padolsey.com/javascript/jquery-plugin-autoresize/).\n* [Elastic](http://www.unwrongest.com/projects/elastic/).\n* [Autogrow for jEditable](http://www.appelsiini.net/2008/4/autogrow-textarea-for-jeditable) or just [Autogrow](http://www.aclevercookie.com/facebook-like-auto-growing-textarea/)",
    "created_at": "2009-11-01T01:31:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7201#issuecomment-59758",
    "user": "@qed777"
}
```

Potentially useful jQuery plug-ins:

* [autoResize](http://james.padolsey.com/javascript/jquery-plugin-autoresize/).
* [Elastic](http://www.unwrongest.com/projects/elastic/).
* [Autogrow for jEditable](http://www.appelsiini.net/2008/4/autogrow-textarea-for-jeditable) or just [Autogrow](http://www.aclevercookie.com/facebook-like-auto-growing-textarea/)



---

archive/issue_comments_059759.json:
```json
{
    "body": "Ticket #2902 is related.",
    "created_at": "2009-11-19T21:20:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7201#issuecomment-59759",
    "user": "@qed777"
}
```

Ticket #2902 is related.



---

archive/issue_comments_059760.json:
```json
{
    "body": "Attachment [trac-7201-auto-flow-input-cells.patch](tarball://root/attachments/some-uuid/ticket7201/trac-7201-auto-flow-input-cells.patch) by @jasongrout created at 2010-05-13 11:41:57",
    "created_at": "2010-05-13T11:41:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7201#issuecomment-59760",
    "user": "@jasongrout"
}
```

Attachment [trac-7201-auto-flow-input-cells.patch](tarball://root/attachments/some-uuid/ticket7201/trac-7201-auto-flow-input-cells.patch) by @jasongrout created at 2010-05-13 11:41:57



---

archive/issue_comments_059761.json:
```json
{
    "body": "Patch is for the sagenb repository.",
    "created_at": "2010-05-13T11:42:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7201#issuecomment-59761",
    "user": "@jasongrout"
}
```

Patch is for the sagenb repository.



---

archive/issue_comments_059762.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-13T11:42:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7201#issuecomment-59762",
    "user": "@jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059763.json:
```json
{
    "body": "Attachment [trac_7201-reviewer.patch](tarball://root/attachments/some-uuid/ticket7201/trac_7201-reviewer.patch) by @TimDumol created at 2010-07-05 10:11:36\n\nEdits the SASS source files too.",
    "created_at": "2010-07-05T10:11:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7201#issuecomment-59763",
    "user": "@TimDumol"
}
```

Attachment [trac_7201-reviewer.patch](tarball://root/attachments/some-uuid/ticket7201/trac_7201-reviewer.patch) by @TimDumol created at 2010-07-05 10:11:36

Edits the SASS source files too.



---

archive/issue_comments_059764.json:
```json
{
    "body": "Looks ok to me. Here's a reviewer patch that edits the SASS source files as well. If the reviewer patch is alright, positive review.",
    "created_at": "2010-07-05T10:14:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7201#issuecomment-59764",
    "user": "@TimDumol"
}
```

Looks ok to me. Here's a reviewer patch that edits the SASS source files as well. If the reviewer patch is alright, positive review.



---

archive/issue_comments_059765.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-09-28T21:05:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7201#issuecomment-59765",
    "user": "@jasongrout"
}
```

Looks good to me.



---

archive/issue_comments_059766.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-28T21:05:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7201#issuecomment-59766",
    "user": "@jasongrout"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059767.json:
```json
{
    "body": "Well, after using it for a bit---in FF 3.6 on OSX, every time I press enter in a cell, the cell momentarily flashes a scrollbar before auto-resizing.  This makes all of the text jump just a bit, which is very jarring.  So I'm going to put this ticket as needs work until that issue is taken care of.",
    "created_at": "2010-09-28T21:13:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7201#issuecomment-59767",
    "user": "@jasongrout"
}
```

Well, after using it for a bit---in FF 3.6 on OSX, every time I press enter in a cell, the cell momentarily flashes a scrollbar before auto-resizing.  This makes all of the text jump just a bit, which is very jarring.  So I'm going to put this ticket as needs work until that issue is taken care of.



---

archive/issue_comments_059768.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-28T21:13:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7201#issuecomment-59768",
    "user": "@jasongrout"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_059769.json:
```json
{
    "body": "In addition, for some reason in the current notebook this breaks new cell creation by clicking.  Apparently - ?  I may have done something wrong.",
    "created_at": "2014-12-19T05:02:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7201#issuecomment-59769",
    "user": "@kcrisman"
}
```

In addition, for some reason in the current notebook this breaks new cell creation by clicking.  Apparently - ?  I may have done something wrong.



---

archive/issue_comments_059770.json:
```json
{
    "body": "Closing deprecated notebook tickets",
    "created_at": "2020-03-29T02:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7201#issuecomment-59770",
    "user": "boothby"
}
```

Closing deprecated notebook tickets



---

archive/issue_comments_059771.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-03-29T02:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7201#issuecomment-59771",
    "user": "boothby"
}
```

Resolution: invalid
