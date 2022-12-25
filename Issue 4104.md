# Issue 4104: [with patch, positive review] Create plot_slope_field function

archive/issues_004104.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe attached patch adds a plot_slope_field function and also exposes a bit more of the quiver API to the vector field plotting routines.  I wish I had had this when I started teaching differential equations!\n\nIssue created by migration from https://trac.sagemath.org/ticket/4104\n\n",
    "closed_at": "2008-09-19T03:14:04Z",
    "created_at": "2008-09-12T04:15:51Z",
    "labels": [
        "component: graphics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "[with patch, positive review] Create plot_slope_field function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4104",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

The attached patch adds a plot_slope_field function and also exposes a bit more of the quiver API to the vector field plotting routines.  I wish I had had this when I started teaching differential equations!

Issue created by migration from https://trac.sagemath.org/ticket/4104





---

archive/issue_comments_029658.json:
```json
{
    "body": "Attachment [plot_slope_field.patch](tarball://root/attachments/some-uuid/ticket4104/plot_slope_field.patch) by @jasongrout created at 2008-09-12 04:16:01",
    "created_at": "2008-09-12T04:16:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4104#issuecomment-29658",
    "user": "https://github.com/jasongrout"
}
```

Attachment [plot_slope_field.patch](tarball://root/attachments/some-uuid/ticket4104/plot_slope_field.patch) by @jasongrout created at 2008-09-12 04:16:01



---

archive/issue_comments_029659.json:
```json
{
    "body": "This patch depends on #4103.",
    "created_at": "2008-09-12T04:16:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4104#issuecomment-29659",
    "user": "https://github.com/jasongrout"
}
```

This patch depends on #4103.



---

archive/issue_comments_029660.json:
```json
{
    "body": "It refused to apply for me:\n\n```\nwdj@hera:~/sagefiles/sage-3.1.2.alpha4$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading SAGE library. Current Mercurial branch is: plot-slope\nsage: hg_sage.apply(\"/home/wdj/sagefiles/plot_slope_field.patch\")\ncd \"/home/wdj/sagefiles/sage-3.1.2.alpha4/devel/sage\" && hg status\ncd \"/home/wdj/sagefiles/sage-3.1.2.alpha4/devel/sage\" && hg status\ncd \"/home/wdj/sagefiles/sage-3.1.2.alpha4/devel/sage\" && hg import   \"/home/wdj/sagefiles/plot_slope_field.patch\"\napplying /home/wdj/sagefiles/plot_slope_field.patch\npatching file sage/plot/plot.py\nHunk #1 FAILED at 2242\n1 out of 2 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej\nabort: patch failed to apply\n```",
    "created_at": "2008-09-13T12:54:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4104#issuecomment-29660",
    "user": "https://github.com/wdjoyner"
}
```

It refused to apply for me:

```
wdj@hera:~/sagefiles/sage-3.1.2.alpha4$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: plot-slope
sage: hg_sage.apply("/home/wdj/sagefiles/plot_slope_field.patch")
cd "/home/wdj/sagefiles/sage-3.1.2.alpha4/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.2.alpha4/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.2.alpha4/devel/sage" && hg import   "/home/wdj/sagefiles/plot_slope_field.patch"
applying /home/wdj/sagefiles/plot_slope_field.patch
patching file sage/plot/plot.py
Hunk #1 FAILED at 2242
1 out of 2 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej
abort: patch failed to apply
```



---

archive/issue_comments_029661.json:
```json
{
    "body": "wdj: just checking, did you apply #4103 first?  This patch depends on that one (i.e., it's supposed to be applied on top of that one).",
    "created_at": "2008-09-17T16:17:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4104#issuecomment-29661",
    "user": "https://github.com/jasongrout"
}
```

wdj: just checking, did you apply #4103 first?  This patch depends on that one (i.e., it's supposed to be applied on top of that one).



---

archive/issue_comments_029662.json:
```json
{
    "body": "I just tried (to 3.1.2.alpha4) and the patch for #4103 would not apply. Could you rebase them both for 3.1.2? It is probably a mistake on my part and I hate to make you go to extra effort. \nMaybe someone else who doesn't have trouble can referee them easier?",
    "created_at": "2008-09-17T18:09:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4104#issuecomment-29662",
    "user": "https://github.com/wdjoyner"
}
```

I just tried (to 3.1.2.alpha4) and the patch for #4103 would not apply. Could you rebase them both for 3.1.2? It is probably a mistake on my part and I hate to make you go to extra effort. 
Maybe someone else who doesn't have trouble can referee them easier?



---

archive/issue_comments_029663.json:
```json
{
    "body": "I just applied both #4103 and this patch to 3.1.2final and they didn't give any errors.  It's quite possible that I was working from something later than alpha4.  Can you try them against 3.1.2final?\n\nThanks.",
    "created_at": "2008-09-18T04:26:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4104#issuecomment-29663",
    "user": "https://github.com/jasongrout"
}
```

I just applied both #4103 and this patch to 3.1.2final and they didn't give any errors.  It's quite possible that I was working from something later than alpha4.  Can you try them against 3.1.2final?

Thanks.



---

archive/issue_comments_029664.json:
```json
{
    "body": "This and #4103 apply to 3.1.2 and pass sage -testall. It does a great job and is a very valuable addition.\n\nA question for possibly a future patch: it will not plot\n\n```\nplot_slope_field(x/y, (x,-3,3), (y,-3,3)).show(aspect_ratio=1)\n```\nbecause of the problem at y=0. However, should it? A slope of plus or minus infinity has a well-defined meaning. Should one try to trap singularities like that and just plot them as vertical direction fields in the future?\n\nAnyway, thanks Jason for this nice addition! This will be very useful for teaching differential equations.",
    "created_at": "2008-09-18T13:59:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4104#issuecomment-29664",
    "user": "https://github.com/wdjoyner"
}
```

This and #4103 apply to 3.1.2 and pass sage -testall. It does a great job and is a very valuable addition.

A question for possibly a future patch: it will not plot

```
plot_slope_field(x/y, (x,-3,3), (y,-3,3)).show(aspect_ratio=1)
```
because of the problem at y=0. However, should it? A slope of plus or minus infinity has a well-defined meaning. Should one try to trap singularities like that and just plot them as vertical direction fields in the future?

Anyway, thanks Jason for this nice addition! This will be very useful for teaching differential equations.



---

archive/issue_comments_029665.json:
```json
{
    "body": "I'm aware of the problem, but decided to post the patch anyway when I saw that plot_vector_field had the same problem: the plot is blank when an evaluation is undefined.  I thought about trapping these things and plotting them as vertical lines, but really we ought to do something in plot_vector_field to take care of things when a vector has an infinite or NaN coordinate.  I ran out of time to fix plot_vector_field.",
    "created_at": "2008-09-18T14:40:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4104#issuecomment-29665",
    "user": "https://github.com/jasongrout"
}
```

I'm aware of the problem, but decided to post the patch anyway when I saw that plot_vector_field had the same problem: the plot is blank when an evaluation is undefined.  I thought about trapping these things and plotting them as vertical lines, but really we ought to do something in plot_vector_field to take care of things when a vector has an infinite or NaN coordinate.  I ran out of time to fix plot_vector_field.



---

archive/issue_comments_029666.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-19T03:14:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4104#issuecomment-29666",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029667.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha0",
    "created_at": "2008-09-19T03:14:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4104#issuecomment-29667",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.alpha0



---

archive/issue_events_009354.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-19T03:14:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4104",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4104#event-9354"
}
```
