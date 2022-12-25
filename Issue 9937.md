# Issue 9937: GAP does not start if the path to the GAP workspace file contains more than 82 characters

archive/issues_009937.json:
```json
{
    "body": "Assignee: @saliola\n\nCC:  @seblabbe mrobado\n\nKeywords: gap\n\nAs pointed out in \n[this thread](http://groups.google.com/group/sage-support/browse_thread/thread/7e169e371308838/a1403ee743fd6ea6?lnk=gst&q=tremblay+gap#a1403ee743fd6ea6), on some machines one there is a problem starting GAP from within Sage:\n\n```\nsage: gap('3+2')\nA workspace appears to have been corrupted... automatically rebuilding (this is harmless).\n---------------------------------------------------------------------------\n...\nTypeError: Unable to start gap\n```\nThe problem is in Sage's attempt to rebuild the GAP workspace. It turns out that Sage calls GAP's `SaveWorkspace` command incorrectly in a particular case.\n\nTo explain the problem, first recall the process used by the GAP interface to evaluate a line of GAP code, say `LineOfGapCode`. It begins by checking the length `LineOfGapCode` (as a string). If this length is greater than 100 (a pre-defined cut-off value), then a file is created containing:\n\n```\nPrint(LineOfGapCode);\n```\nThis file is read into GAP using the expect interface and the output is parsed and returned to Sage. (There is no problem if the length is less than 100, because the interface does not use a file.)\n\nLet's apply this to the case where we need to rebuild a workspace. The workspace is just a file contained in a user's .sage directory. If the number of characters in the path to the workspace is greater than the cut-off, then Sage tries to execute the following command:\n\n```\nPrint(SaveWorkspace(\"PathToWorkspaceFile\"));\n```\nThis is not permitted by GAP, as explained in the [GAP Reference Manual](http://www.gap-system.org/Manuals/doc/htm/ref/CHAP003.htm#SSEC011.1):\n\n```\nSaveWorkspace can only be used at the main gap> prompt. It cannot be included in the body of a loop or function, or called from a break loop.\n```\nSo to fix this, we need to force the interface not to use a file to execute the `SaveWorkspace` command.\n\n(This problem has plagued all the computers in our computer lab for months since a user's home directory is located on a network drive with a long name.)\n\nThis is reproducible:\n\n```\nsage: ws = sage.interfaces.gap.WORKSPACE\nsage: sage.interfaces.gap.WORKSPACE += \"0\"*(83-len(ws))\nsage: gap = Gap()\nsage: gap('3+2')\n```\nBoom!\n\nIssue created by migration from https://trac.sagemath.org/ticket/9938\n\n",
    "closed_at": "2010-09-28T09:14:39Z",
    "created_at": "2010-09-17T21:31:06Z",
    "labels": [
        "component: interfaces",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "GAP does not start if the path to the GAP workspace file contains more than 82 characters",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9937",
    "user": "https://github.com/saliola"
}
```
Assignee: @saliola

CC:  @seblabbe mrobado

Keywords: gap

As pointed out in 
[this thread](http://groups.google.com/group/sage-support/browse_thread/thread/7e169e371308838/a1403ee743fd6ea6?lnk=gst&q=tremblay+gap#a1403ee743fd6ea6), on some machines one there is a problem starting GAP from within Sage:

```
sage: gap('3+2')
A workspace appears to have been corrupted... automatically rebuilding (this is harmless).
---------------------------------------------------------------------------
...
TypeError: Unable to start gap
```
The problem is in Sage's attempt to rebuild the GAP workspace. It turns out that Sage calls GAP's `SaveWorkspace` command incorrectly in a particular case.

To explain the problem, first recall the process used by the GAP interface to evaluate a line of GAP code, say `LineOfGapCode`. It begins by checking the length `LineOfGapCode` (as a string). If this length is greater than 100 (a pre-defined cut-off value), then a file is created containing:

```
Print(LineOfGapCode);
```
This file is read into GAP using the expect interface and the output is parsed and returned to Sage. (There is no problem if the length is less than 100, because the interface does not use a file.)

Let's apply this to the case where we need to rebuild a workspace. The workspace is just a file contained in a user's .sage directory. If the number of characters in the path to the workspace is greater than the cut-off, then Sage tries to execute the following command:

```
Print(SaveWorkspace("PathToWorkspaceFile"));
```
This is not permitted by GAP, as explained in the [GAP Reference Manual](http://www.gap-system.org/Manuals/doc/htm/ref/CHAP003.htm#SSEC011.1):

```
SaveWorkspace can only be used at the main gap> prompt. It cannot be included in the body of a loop or function, or called from a break loop.
```
So to fix this, we need to force the interface not to use a file to execute the `SaveWorkspace` command.

(This problem has plagued all the computers in our computer lab for months since a user's home directory is located on a network drive with a long name.)

This is reproducible:

```
sage: ws = sage.interfaces.gap.WORKSPACE
sage: sage.interfaces.gap.WORKSPACE += "0"*(83-len(ws))
sage: gap = Gap()
sage: gap('3+2')
```
Boom!

Issue created by migration from https://trac.sagemath.org/ticket/9938





---

archive/issue_comments_098766.json:
```json
{
    "body": "Changing assignee from @williamstein to @saliola.",
    "created_at": "2010-09-17T21:50:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9937#issuecomment-98766",
    "user": "https://github.com/saliola"
}
```

Changing assignee from @williamstein to @saliola.



---

archive/issue_comments_098767.json:
```json
{
    "body": "Attachment [trac9938.2.patch](tarball://root/attachments/some-uuid/ticket9938/trac9938.2.patch) by @saliola created at 2010-09-17 22:33:38",
    "created_at": "2010-09-17T22:33:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9937#issuecomment-98767",
    "user": "https://github.com/saliola"
}
```

Attachment [trac9938.2.patch](tarball://root/attachments/some-uuid/ticket9938/trac9938.2.patch) by @saliola created at 2010-09-17 22:33:38



---

archive/issue_comments_098768.json:
```json
{
    "body": "Attachment [trac9938.patch](tarball://root/attachments/some-uuid/ticket9938/trac9938.patch) by @saliola created at 2010-09-17 22:34:15\n\napply only this patch!",
    "created_at": "2010-09-17T22:34:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9937#issuecomment-98768",
    "user": "https://github.com/saliola"
}
```

Attachment [trac9938.patch](tarball://root/attachments/some-uuid/ticket9938/trac9938.patch) by @saliola created at 2010-09-17 22:34:15

apply only this patch!



---

archive/issue_comments_098769.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-18T02:42:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9937#issuecomment-98769",
    "user": "https://github.com/saliola"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098770.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-18T02:43:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9937#issuecomment-98770",
    "user": "https://github.com/saliola"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_098771.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-18T02:43:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9937#issuecomment-98771",
    "user": "https://github.com/saliola"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_098772.json:
```json
{
    "body": "Attachment [trac9938-review-sl.patch](tarball://root/attachments/some-uuid/ticket9938/trac9938-review-sl.patch) by @seblabbe created at 2010-09-18 13:39:00\n\nApplies over the precedent patch",
    "created_at": "2010-09-18T13:39:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9937#issuecomment-98772",
    "user": "https://github.com/seblabbe"
}
```

Attachment [trac9938-review-sl.patch](tarball://root/attachments/some-uuid/ticket9938/trac9938-review-sl.patch) by @seblabbe created at 2010-09-18 13:39:00

Applies over the precedent patch



---

archive/issue_comments_098773.json:
```json
{
    "body": "I was able to reproduce the problem on my osx 10.5 running sage-4.5.3. The patch fixes the problem. All tests pass on sage/interfaces/gap.py. Documentation builds fine.\n\nI added a review patch that simply puts back the constant `sage.interfaces.gap.WORKSPACE` to its original value since the new value was used in all the rest of the doctests.\n\nI am giving a positive review to Franco's patch. I let him change the status of this ticket to positive review if he agrees with my small fix.\n\nI did not manage to apply a patch on the sage install of LaCIM laboratory by ssh. Maybe J\u00e9r\u00f4me could test the patch on Monday.",
    "created_at": "2010-09-18T13:52:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9937#issuecomment-98773",
    "user": "https://github.com/seblabbe"
}
```

I was able to reproduce the problem on my osx 10.5 running sage-4.5.3. The patch fixes the problem. All tests pass on sage/interfaces/gap.py. Documentation builds fine.

I added a review patch that simply puts back the constant `sage.interfaces.gap.WORKSPACE` to its original value since the new value was used in all the rest of the doctests.

I am giving a positive review to Franco's patch. I let him change the status of this ticket to positive review if he agrees with my small fix.

I did not manage to apply a patch on the sage install of LaCIM laboratory by ssh. Maybe Jérôme could test the patch on Monday.



---

archive/issue_comments_098774.json:
```json
{
    "body": "I'm okay with your changes, S\u00e9bastien.\n\nApply patches in this order:\n\n1. [attachment:trac9938.patch]\n2. [attachment:trac9938-review-sl.patch]",
    "created_at": "2010-09-19T14:35:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9937#issuecomment-98774",
    "user": "https://github.com/saliola"
}
```

I'm okay with your changes, Sébastien.

Apply patches in this order:

1. [attachment:trac9938.patch]
2. [attachment:trac9938-review-sl.patch]



---

archive/issue_comments_098775.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-19T14:35:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9937#issuecomment-98775",
    "user": "https://github.com/saliola"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098776.json:
```json
{
    "body": "> I did not manage to apply a patch on the sage install of LaCIM laboratory by ssh. Maybe J\u00e9r\u00f4me could test the patch on Monday.\n\n\nLast Monday, I tested the patch on one of the computer in the lab and I can confirm the patches solve the problem. Great!",
    "created_at": "2010-09-24T01:31:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9937#issuecomment-98776",
    "user": "https://github.com/seblabbe"
}
```

> I did not manage to apply a patch on the sage install of LaCIM laboratory by ssh. Maybe Jérôme could test the patch on Monday.


Last Monday, I tested the patch on one of the computer in the lab and I can confirm the patches solve the problem. Great!



---

archive/issue_comments_098777.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-28T09:14:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9937#issuecomment-98777",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_025068.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-28T09:14:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9937",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9937#event-25068"
}
```



---

archive/issue_comments_098778.json:
```json
{
    "body": "Thanks for fixing this!  I encountered just this problem about two days ago when doctesting with a long `DOT_SAGE`.",
    "created_at": "2010-09-28T09:14:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9937#issuecomment-98778",
    "user": "https://github.com/qed777"
}
```

Thanks for fixing this!  I encountered just this problem about two days ago when doctesting with a long `DOT_SAGE`.
