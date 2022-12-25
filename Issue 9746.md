# Issue 9746: documentation for plotting

archive/issues_009746.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @kcrisman\n\nI went through the \"live\" documentation for plots and found a number of places that computations should be split into separate cells, plots weren't displayed, etc.  This patch fixes these areas.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9746\n\n",
    "created_at": "2010-08-14T14:15:00Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "documentation for plotting",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9746",
    "user": "https://github.com/jasongrout"
}
```
Assignee: jason, was

CC:  @kcrisman

I went through the "live" documentation for plots and found a number of places that computations should be split into separate cells, plots weren't displayed, etc.  This patch fixes these areas.

Issue created by migration from https://trac.sagemath.org/ticket/9746





---

archive/issue_comments_095281.json:
```json
{
    "body": "Depends on #9740, and possibly on #9221",
    "created_at": "2010-08-14T16:06:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9746#issuecomment-95281",
    "user": "https://github.com/jasongrout"
}
```

Depends on #9740, and possibly on #9221



---

archive/issue_comments_095282.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-14T16:06:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9746#issuecomment-95282",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_095283.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-08-14T16:43:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9746#issuecomment-95283",
    "user": "https://github.com/jasongrout"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_095284.json:
```json
{
    "body": "There is a typo of 'primitve' in `plot/plot.py`.  Does this still apply to 4.6.alpha1?",
    "created_at": "2010-09-21T20:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9746#issuecomment-95284",
    "user": "https://github.com/kcrisman"
}
```

There is a typo of 'primitve' in `plot/plot.py`.  Does this still apply to 4.6.alpha1?



---

archive/issue_comments_095285.json:
```json
{
    "body": "Attachment [trac-9746-plot-doc-improvements.patch](tarball://root/attachments/some-uuid/ticket9746/trac-9746-plot-doc-improvements.patch) by @jasongrout created at 2010-09-28 16:01:41\n\nReplying to [comment:4 kcrisman]:\n> There is a typo of 'primitve' in `plot/plot.py`.  Does this still apply to 4.6.alpha1?  \n\nYes.  I also refreshed the patch to correct the typo.  This depends on #9740.  Do you have time to review that and this patch?",
    "created_at": "2010-09-28T16:01:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9746#issuecomment-95285",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-9746-plot-doc-improvements.patch](tarball://root/attachments/some-uuid/ticket9746/trac-9746-plot-doc-improvements.patch) by @jasongrout created at 2010-09-28 16:01:41

Replying to [comment:4 kcrisman]:
> There is a typo of 'primitve' in `plot/plot.py`.  Does this still apply to 4.6.alpha1?  

Yes.  I also refreshed the patch to correct the typo.  This depends on #9740.  Do you have time to review that and this patch?



---

archive/issue_comments_095286.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-28T16:16:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9746#issuecomment-95286",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_095287.json:
```json
{
    "body": "Replying to [comment:5 jason]:\n> Replying to [comment:4 kcrisman]:\n> > There is a typo of 'primitve' in `plot/plot.py`.  Does this still apply to 4.6.alpha1?  \n> \n> Yes.  I also refreshed the patch to correct the typo.  This depends on #9740.  Do you have time to review that and this patch?\nNot totally at this time, though I see some of the things it is trying to fix.  I did take a look at some things while checking out the new matplotlib, and noticed that the example with `plot(1.5/(1+e^(-x))` is not correctly formatted in the documentation, and doesn't become a live cell.  I'm sorry to make this a long process.",
    "created_at": "2010-09-28T16:16:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9746#issuecomment-95287",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:5 jason]:
> Replying to [comment:4 kcrisman]:
> > There is a typo of 'primitve' in `plot/plot.py`.  Does this still apply to 4.6.alpha1?  
> 
> Yes.  I also refreshed the patch to correct the typo.  This depends on #9740.  Do you have time to review that and this patch?
Not totally at this time, though I see some of the things it is trying to fix.  I did take a look at some things while checking out the new matplotlib, and noticed that the example with `plot(1.5/(1+e^(-x))` is not correctly formatted in the documentation, and doesn't become a live cell.  I'm sorry to make this a long process.



---

archive/issue_comments_095288.json:
```json
{
    "body": "(Also, there are lots of places where there are many specific examples all together, such as in `point?`\n\n```\npoint((1,2))\npoint((1,2,3))\npoint([(0,0), (1,1)])\npoint([(0,0,1), (1,1,1)]\n```\n\nbut that should be a separate ticket.  I may be responsible for some of those, not realizing the live documentation needed these separate - or does it?)",
    "created_at": "2010-09-28T16:19:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9746#issuecomment-95288",
    "user": "https://github.com/kcrisman"
}
```

(Also, there are lots of places where there are many specific examples all together, such as in `point?`

```
point((1,2))
point((1,2,3))
point([(0,0), (1,1)])
point([(0,0,1), (1,1,1)]
```

but that should be a separate ticket.  I may be responsible for some of those, not realizing the live documentation needed these separate - or does it?)



---

archive/issue_comments_095289.json:
```json
{
    "body": "Replying to [comment:7 kcrisman]:\n> (Also, there are lots of places where there are many specific examples all together, such as in `point?`\n> {{{\n> point((1,2))\n> point((1,2,3))\n> point([(0,0), (1,1)])\n> point([(0,0,1), (1,1,1)]\n> }}}\n> but that should be a separate ticket.  I may be responsible for some of those, not realizing the live documentation needed these separate - or does it?)\n\nThose are fixed in my version (after #9740, #9746, and #4342).",
    "created_at": "2010-09-28T16:34:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9746#issuecomment-95289",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:7 kcrisman]:
> (Also, there are lots of places where there are many specific examples all together, such as in `point?`
> {{{
> point((1,2))
> point((1,2,3))
> point([(0,0), (1,1)])
> point([(0,0,1), (1,1,1)]
> }}}
> but that should be a separate ticket.  I may be responsible for some of those, not realizing the live documentation needed these separate - or does it?)

Those are fixed in my version (after #9740, #9746, and #4342).



---

archive/issue_comments_095290.json:
```json
{
    "body": "Hilarious - I didn't make it far enough down to see that this exact one is on this ticket!  Well, like I said, I don't have time to check it all the way... I feel like there were other similar places, though.",
    "created_at": "2010-09-28T16:40:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9746#issuecomment-95290",
    "user": "https://github.com/kcrisman"
}
```

Hilarious - I didn't make it far enough down to see that this exact one is on this ticket!  Well, like I said, I don't have time to check it all the way... I feel like there were other similar places, though.



---

archive/issue_comments_095291.json:
```json
{
    "body": "I've attached a patch which takes care of the error pointed out above, and corrects two or three more things in the docs.",
    "created_at": "2010-09-28T16:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9746#issuecomment-95291",
    "user": "https://github.com/jasongrout"
}
```

I've attached a patch which takes care of the error pointed out above, and corrects two or three more things in the docs.



---

archive/issue_comments_095292.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-28T16:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9746#issuecomment-95292",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_095293.json:
```json
{
    "body": "apply on top of previous patches",
    "created_at": "2010-09-28T16:58:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9746#issuecomment-95293",
    "user": "https://github.com/jasongrout"
}
```

apply on top of previous patches



---

archive/issue_comments_095294.json:
```json
{
    "body": "Attachment [9746-review.patch](tarball://root/attachments/some-uuid/ticket9746/9746-review.patch) by @jasongrout created at 2010-09-28 19:08:27\n\nptestlong in 4.6.alpha1 (Ubuntu 10.04 64-bit) passes with the following tickets applied in order: #9221 (and new spkg), #9740, #9746, #4342.",
    "created_at": "2010-09-28T19:08:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9746#issuecomment-95294",
    "user": "https://github.com/jasongrout"
}
```

Attachment [9746-review.patch](tarball://root/attachments/some-uuid/ticket9746/9746-review.patch) by @jasongrout created at 2010-09-28 19:08:27

ptestlong in 4.6.alpha1 (Ubuntu 10.04 64-bit) passes with the following tickets applied in order: #9221 (and new spkg), #9740, #9746, #4342.



---

archive/issue_comments_095295.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-29T03:31:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9746#issuecomment-95295",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_095296.json:
```json
{
    "body": "Okay, here are comments.  A lot of them are very similar in style, but I tried to be exhaustive within the files you modified.  I am too tired to look for problems in the other files, though they are likely there and I likely introduced them :)  But overall this is good, I just found more of the same for most (a few other errors, though).  Here we go! \n\nIn scatterplot, there is another one of those 'these are equivalent' things, but they're not separated out.  Also, I get code{scatter_plot.options} instead of the actual code.  Should it be show() or `show()`?\n\nIn sage.plot.polygon.polygon we have something similar in the examples - somehow you only got some of them.  Again with the extra options guy, too.\n\nSame with the equivalent in point.py, in both `point` and `points`.\n\nIn the `plot_field.py` file, why did you once add the x,y variable declaration and once not?  It doesn't really matter to me, but I wonder if there is something I'm missing.  Again with the `show()` or show(), and the equivalent.  It's not so important to me with the equivalent showing two things, but I feel like maybe you changed that one place - or maybe not.\n\nIn plot.py, ironically, just above the place where you fixed the `1.5/(1+e^(-x))` thing, there are a bunch of plots I didn't separate in my custom ticks patch.  My apologies - but there they are!  I also still get an error 'ellipsis object not callable' or something in 'add grid lines at specific positions (using lists/tuples)'.  There's an ellipsis that got stuck in there still somehow - I think you got a different one of these.\n\nIn line.py, after the cool cat there are a couple things as in the previous files - one nonseparated, one equivalent issue/show() issue.\n\nIn disk.py, maybe the disk that is parallel to the `xy`-plane should be plotted, not just its type?  Same equiv/show question.\n\nI don't know what happened in density plot, but I think a tick is missing in the `DensityPlot` documentation - likely my fault?  This is in 'Examples'.\n\nIn contour plot, the very last example under `region_plot` should have two plots, but has one.  But they are different.\n\nThe circles also has the parallel to the `xy`-plane issue when it comes to giving the type, but not the plot.",
    "created_at": "2010-09-29T03:31:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9746#issuecomment-95296",
    "user": "https://github.com/kcrisman"
}
```

Okay, here are comments.  A lot of them are very similar in style, but I tried to be exhaustive within the files you modified.  I am too tired to look for problems in the other files, though they are likely there and I likely introduced them :)  But overall this is good, I just found more of the same for most (a few other errors, though).  Here we go! 

In scatterplot, there is another one of those 'these are equivalent' things, but they're not separated out.  Also, I get code{scatter_plot.options} instead of the actual code.  Should it be show() or `show()`?

In sage.plot.polygon.polygon we have something similar in the examples - somehow you only got some of them.  Again with the extra options guy, too.

Same with the equivalent in point.py, in both `point` and `points`.

In the `plot_field.py` file, why did you once add the x,y variable declaration and once not?  It doesn't really matter to me, but I wonder if there is something I'm missing.  Again with the `show()` or show(), and the equivalent.  It's not so important to me with the equivalent showing two things, but I feel like maybe you changed that one place - or maybe not.

In plot.py, ironically, just above the place where you fixed the `1.5/(1+e^(-x))` thing, there are a bunch of plots I didn't separate in my custom ticks patch.  My apologies - but there they are!  I also still get an error 'ellipsis object not callable' or something in 'add grid lines at specific positions (using lists/tuples)'.  There's an ellipsis that got stuck in there still somehow - I think you got a different one of these.

In line.py, after the cool cat there are a couple things as in the previous files - one nonseparated, one equivalent issue/show() issue.

In disk.py, maybe the disk that is parallel to the `xy`-plane should be plotted, not just its type?  Same equiv/show question.

I don't know what happened in density plot, but I think a tick is missing in the `DensityPlot` documentation - likely my fault?  This is in 'Examples'.

In contour plot, the very last example under `region_plot` should have two plots, but has one.  But they are different.

The circles also has the parallel to the `xy`-plane issue when it comes to giving the type, but not the plot.



---

archive/issue_comments_095297.json:
```json
{
    "body": "So, since a lot of tickets depend on this one, why don't we make all of these a separate ticket?  That's a great list for improving docs!",
    "created_at": "2010-09-29T04:08:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9746#issuecomment-95297",
    "user": "https://github.com/jasongrout"
}
```

So, since a lot of tickets depend on this one, why don't we make all of these a separate ticket?  That's a great list for improving docs!



---

archive/issue_comments_095298.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-29T04:08:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9746#issuecomment-95298",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_095299.json:
```json
{
    "body": "Okay, I'll cave in.  I don't know that 'a lot' of tickets depend on this (if #4342 counts as 'a lot') but a ticket with 'even more plot documentation improvements' sounds okay.  This is now #10032.\n\nPositive review to this patch, but noting that #10032 addresses more issues of a similar nature.",
    "created_at": "2010-09-29T18:00:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9746#issuecomment-95299",
    "user": "https://github.com/kcrisman"
}
```

Okay, I'll cave in.  I don't know that 'a lot' of tickets depend on this (if #4342 counts as 'a lot') but a ticket with 'even more plot documentation improvements' sounds okay.  This is now #10032.

Positive review to this patch, but noting that #10032 addresses more issues of a similar nature.



---

archive/issue_comments_095300.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-29T18:00:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9746#issuecomment-95300",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095301.json:
```json
{
    "body": "Replying to [comment:15 kcrisman]:\n> Okay, I'll cave in.  I don't know that 'a lot' of tickets depend on this (if #4342 counts as 'a lot') but a ticket with 'even more plot documentation improvements' sounds okay.  This is now #10032.\n\n\nI knew it was in the stack of patches I had applied, and other patches depended on it.  How about \"an important patch that has been waiting a very long time depends on this\"? :)\n\nMy purpose is to just narrow the scope of this ticket to exactly the improvements actually done in the patch.  Thanks for agreeing and opening up another ticket for more improvements.",
    "created_at": "2010-09-29T18:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9746#issuecomment-95301",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:15 kcrisman]:
> Okay, I'll cave in.  I don't know that 'a lot' of tickets depend on this (if #4342 counts as 'a lot') but a ticket with 'even more plot documentation improvements' sounds okay.  This is now #10032.


I knew it was in the stack of patches I had applied, and other patches depended on it.  How about "an important patch that has been waiting a very long time depends on this"? :)

My purpose is to just narrow the scope of this ticket to exactly the improvements actually done in the patch.  Thanks for agreeing and opening up another ticket for more improvements.



---

archive/issue_comments_095302.json:
```json
{
    "body": "Replying to [comment:16 jason]:\n> Replying to [comment:15 kcrisman]:\n> > Okay, I'll cave in.  I don't know that 'a lot' of tickets depend on this (if #4342 counts as 'a lot') but a ticket with 'even more plot documentation improvements' sounds okay.  This is now #10032.\n> \n> \n> I knew it was in the stack of patches I had applied, and other patches depended on it.  How about \"an important patch that has been waiting a very long time depends on this\"? :)\nI agree with that!\n> My purpose is to just narrow the scope of this ticket to exactly the improvements actually done in the patch.  Thanks for agreeing and opening up another ticket for more improvements.\nNo problem - although not using queues made this a little harder for me to test.",
    "created_at": "2010-09-29T18:26:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9746#issuecomment-95302",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:16 jason]:
> Replying to [comment:15 kcrisman]:
> > Okay, I'll cave in.  I don't know that 'a lot' of tickets depend on this (if #4342 counts as 'a lot') but a ticket with 'even more plot documentation improvements' sounds okay.  This is now #10032.
> 
> 
> I knew it was in the stack of patches I had applied, and other patches depended on it.  How about "an important patch that has been waiting a very long time depends on this"? :)
I agree with that!
> My purpose is to just narrow the scope of this ticket to exactly the improvements actually done in the patch.  Thanks for agreeing and opening up another ticket for more improvements.
No problem - although not using queues made this a little harder for me to test.



---

archive/issue_comments_095303.json:
```json
{
    "body": "This one\n\n```\n I also still get an error 'ellipsis object not callable' or something in 'add grid lines at specific positions (using lists/tuples)'. There's an ellipsis that got stuck in there still somehow - I think you got a different one of these.\n```\n\nin particular is aggravating, and should be fixed quickly, if possible.",
    "created_at": "2010-09-29T18:40:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9746#issuecomment-95303",
    "user": "https://github.com/kcrisman"
}
```

This one

```
 I also still get an error 'ellipsis object not callable' or something in 'add grid lines at specific positions (using lists/tuples)'. There's an ellipsis that got stuck in there still somehow - I think you got a different one of these.
```

in particular is aggravating, and should be fixed quickly, if possible.



---

archive/issue_comments_095304.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-10-03T06:35:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9746#issuecomment-95304",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
