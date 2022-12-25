# Issue 8366: make contour plot labels and linestyles work when fill=True

archive/issues_008366.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @kcrisman wcauchois @robert-marik\n\nKeywords: contour,plot\n\nWe have an artificial limitation in that contour labels and linestyles don't work when fill=True.  This patch lets these options work with filling.  Furthermore, it draws the contour lines on top of filled plots by default, which (at least I think) makes the plot look a little nicer anyway.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8366\n\n",
    "closed_at": "2010-04-15T23:44:44Z",
    "created_at": "2010-02-25T17:24:26Z",
    "labels": [
        "component: graphics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "make contour plot labels and linestyles work when fill=True",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8366",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

CC:  @kcrisman wcauchois @robert-marik

Keywords: contour,plot

We have an artificial limitation in that contour labels and linestyles don't work when fill=True.  This patch lets these options work with filling.  Furthermore, it draws the contour lines on top of filled plots by default, which (at least I think) makes the plot look a little nicer anyway.

Issue created by migration from https://trac.sagemath.org/ticket/8366





---

archive/issue_comments_074653.json:
```json
{
    "body": "Attachment [trac-8366-label-filled-contours.patch](tarball://root/attachments/some-uuid/ticket8366/trac-8366-label-filled-contours.patch) by @jasongrout created at 2010-02-25 17:25:45",
    "created_at": "2010-02-25T17:25:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8366#issuecomment-74653",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-8366-label-filled-contours.patch](tarball://root/attachments/some-uuid/ticket8366/trac-8366-label-filled-contours.patch) by @jasongrout created at 2010-02-25 17:25:45



---

archive/issue_comments_074654.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-25T17:26:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8366#issuecomment-74654",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074655.json:
```json
{
    "body": "apply after previous patch, this patch fixes docstrings",
    "created_at": "2010-03-04T16:17:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8366#issuecomment-74655",
    "user": "https://github.com/robert-marik"
}
```

apply after previous patch, this patch fixes docstrings



---

archive/issue_comments_074656.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-04T16:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8366#issuecomment-74656",
    "user": "https://github.com/robert-marik"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074657.json:
```json
{
    "body": "Attachment [trac-8366-fixed-docstrings.patch](tarball://root/attachments/some-uuid/ticket8366/trac-8366-fixed-docstrings.patch) by @robert-marik created at 2010-03-04 16:33:22\n\nWorks as advertaised, but region_plot gives error after installing this patch.\n\n```\nsage: x,y=var('x y')\nsage: region_plot(cos(x^2+y^2) <= 0, (x, -3, 3), (y, -3, 3))\n\nTraceback (click to the left of this block for traceback)\n...\nKeyError: 'linewidths'\n```\n\ndid you try this?\n\n```\n./sage -t devel/sage/sage/plot/contour_plot.py\n```\n\nMy patch fixes long lines (which make help for contour_plot too wide for typical screen) and split contour_plot exmaples into groups (this allows to try commands immediatelly when reading live reference manual).\n\nOne suggestion: could we set label_colors to something resonable (gray? red? blue?) when both fill and labels are True, but label_color is not specified?",
    "created_at": "2010-03-04T16:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8366#issuecomment-74657",
    "user": "https://github.com/robert-marik"
}
```

Attachment [trac-8366-fixed-docstrings.patch](tarball://root/attachments/some-uuid/ticket8366/trac-8366-fixed-docstrings.patch) by @robert-marik created at 2010-03-04 16:33:22

Works as advertaised, but region_plot gives error after installing this patch.

```
sage: x,y=var('x y')
sage: region_plot(cos(x^2+y^2) <= 0, (x, -3, 3), (y, -3, 3))

Traceback (click to the left of this block for traceback)
...
KeyError: 'linewidths'
```

did you try this?

```
./sage -t devel/sage/sage/plot/contour_plot.py
```

My patch fixes long lines (which make help for contour_plot too wide for typical screen) and split contour_plot exmaples into groups (this allows to try commands immediatelly when reading live reference manual).

One suggestion: could we set label_colors to something resonable (gray? red? blue?) when both fill and labels are True, but label_color is not specified?



---

archive/issue_comments_074658.json:
```json
{
    "body": "Jason, thank you for this patch and thank you also for the patch to #8368. I hope that the issue above could be fixed easily. I suggest you to include the ticket #8368 to this one -- this could make the life of our release manager easier :)",
    "created_at": "2010-03-04T16:44:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8366#issuecomment-74658",
    "user": "https://github.com/robert-marik"
}
```

Jason, thank you for this patch and thank you also for the patch to #8368. I hope that the issue above could be fixed easily. I suggest you to include the ticket #8368 to this one -- this could make the life of our release manager easier :)



---

archive/issue_comments_074659.json:
```json
{
    "body": "Replying to [comment:3 robert.marik]:\n> Jason, thank you for this patch and thank you also for the patch to #8368. I hope that the issue above could be fixed easily. I suggest you to include the ticket #8368 to this one -- this could make the life of our release manager easier :) \n\n\nI'm afraid I would get in trouble with our (wonderfully!) picky release manager for combining tickets which arguably have different issues.  (I really appreciate Minh's reminders about the details we need to follow!)",
    "created_at": "2010-03-04T18:34:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8366#issuecomment-74659",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:3 robert.marik]:
> Jason, thank you for this patch and thank you also for the patch to #8368. I hope that the issue above could be fixed easily. I suggest you to include the ticket #8368 to this one -- this could make the life of our release manager easier :) 


I'm afraid I would get in trouble with our (wonderfully!) picky release manager for combining tickets which arguably have different issues.  (I really appreciate Minh's reminders about the details we need to follow!)



---

archive/issue_comments_074660.json:
```json
{
    "body": "Attachment [trac-8366-fix-code.patch](tarball://root/attachments/some-uuid/ticket8366/trac-8366-fix-code.patch) by @jasongrout created at 2010-04-15 03:26:51\n\napply on top of previous patches",
    "created_at": "2010-04-15T03:26:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8366#issuecomment-74660",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-8366-fix-code.patch](tarball://root/attachments/some-uuid/ticket8366/trac-8366-fix-code.patch) by @jasongrout created at 2010-04-15 03:26:51

apply on top of previous patches



---

archive/issue_comments_074661.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-15T03:28:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8366#issuecomment-74661",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074662.json:
```json
{
    "body": "Replying to [comment:2 robert.marik]:\n> did you try this?\n> \n> ```\n> ./sage -t devel/sage/sage/plot/contour_plot.py\n> ```\n\n\n\nWeird---I thought I did.  Well, the new patch fixes this error.\n\n> One suggestion: could we set label_colors to something resonable (gray? red? blue?) when both fill and labels are True, but label_color is not specified?\n\n\nThe new patch addresses this issue as well.\n\nCan you look at this and review it again?\n\nThanks",
    "created_at": "2010-04-15T03:28:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8366#issuecomment-74662",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:2 robert.marik]:
> did you try this?
> 
> ```
> ./sage -t devel/sage/sage/plot/contour_plot.py
> ```



Weird---I thought I did.  Well, the new patch fixes this error.

> One suggestion: could we set label_colors to something resonable (gray? red? blue?) when both fill and labels are True, but label_color is not specified?


The new patch addresses this issue as well.

Can you look at this and review it again?

Thanks



---

archive/issue_comments_074663.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-15T09:49:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8366#issuecomment-74663",
    "user": "https://github.com/robert-marik"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074664.json:
```json
{
    "body": "Thanks for fixing - the patch introduces new functionality, tests passed now. Positive review.\n\nRelease manager: apply all three patches:  trac-8366-label-filled-contours.patch, trac-8366-fixed-docstrings.patch, trac-8366-fix-code.patch",
    "created_at": "2010-04-15T09:49:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8366#issuecomment-74664",
    "user": "https://github.com/robert-marik"
}
```

Thanks for fixing - the patch introduces new functionality, tests passed now. Positive review.

Release manager: apply all three patches:  trac-8366-label-filled-contours.patch, trac-8366-fixed-docstrings.patch, trac-8366-fix-code.patch



---

archive/issue_comments_074665.json:
```json
{
    "body": "Changing keywords from \"\" to \"contour,plot\".",
    "created_at": "2010-04-15T09:49:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8366#issuecomment-74665",
    "user": "https://github.com/robert-marik"
}
```

Changing keywords from "" to "contour,plot".



---

archive/issue_comments_074666.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T23:44:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8366#issuecomment-74666",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_events_020045.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-15T23:44:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8366",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8366#event-20045"
}
```



---

archive/issue_comments_074667.json:
```json
{
    "body": "Merged into 4.4.alpha0:\n- trac-8366-label-filled-contours.patch\n- trac-8366-fixed-docstrings.patch\n- trac-8366-fix-code.patch",
    "created_at": "2010-04-15T23:44:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8366#issuecomment-74667",
    "user": "https://github.com/jhpalmieri"
}
```

Merged into 4.4.alpha0:
- trac-8366-label-filled-contours.patch
- trac-8366-fixed-docstrings.patch
- trac-8366-fix-code.patch
