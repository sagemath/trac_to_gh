# Issue 9203: plot ellipses

archive/issues_009203.json:
```json
{
    "body": "Assignee: @videlec\n\nCC:  @kcrisman @jasongrout\n\nKeywords: plot, geometry, ellipse\n\nAdding a primitive for plot ellipses that wraps the existing patch of matplotlib.\n\nThis is approximately the same stuff as the patch #9076 for plotting arcs (of circle and ellipse).\n\nIssue created by migration from https://trac.sagemath.org/ticket/9203\n\n",
    "created_at": "2010-06-10T13:43:14Z",
    "labels": [
        "component: geometry"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "plot ellipses",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9203",
    "user": "https://github.com/videlec"
}
```
Assignee: @videlec

CC:  @kcrisman @jasongrout

Keywords: plot, geometry, ellipse

Adding a primitive for plot ellipses that wraps the existing patch of matplotlib.

This is approximately the same stuff as the patch #9076 for plotting arcs (of circle and ellipse).

Issue created by migration from https://trac.sagemath.org/ticket/9203





---

archive/issue_comments_085989.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-10T13:45:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-85989",
    "user": "https://github.com/videlec"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085990.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-14T13:30:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-85990",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_085991.json:
```json
{
    "body": "This looks nice overall too, but again some things needed for best results.\n\n* Class def examples for reference guide\n\n* 'circle' still shows up a few times\n \n* This `_repr_` method is better than the arc one!\n\n* plot3d should open ticket or test `NotImplementedError`\n\n* I like that options are given explicitly in arc(), as well as test of `NotImplementedError`\n\nI'll try to work through the details of the `get_min_max_data` and test thoroughly on this and #9076 as soon as these things are addressed, because in general they're both good wraps and add much-needed functionality.  Good work!",
    "created_at": "2010-06-14T13:30:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-85991",
    "user": "https://github.com/kcrisman"
}
```

This looks nice overall too, but again some things needed for best results.

* Class def examples for reference guide

* 'circle' still shows up a few times
 
* This `_repr_` method is better than the arc one!

* plot3d should open ticket or test `NotImplementedError`

* I like that options are given explicitly in arc(), as well as test of `NotImplementedError`

I'll try to work through the details of the `get_min_max_data` and test thoroughly on this and #9076 as soon as these things are addressed, because in general they're both good wraps and add much-needed functionality.  Good work!



---

archive/issue_comments_085992.json:
```json
{
    "body": "Thank you for this careful review\n\n> * Class def examples for reference guide\n\nDone, if you mean examples in the docstring of the class Ellipse\n\n> * 'circle' still shows up a few times\n\nNo more (I hope)\n\n> * plot3d should open ticket or test `NotImplementedError`\n\nI will. But as I really do not like the one it is implemented for circle for many different reasons I don't know how general should be the corresponding ticket...\n\n> * I like that options are given explicitly in arc(), as well as test of `NotImplementedError`\n\nNow there is. And I add a link from the sage.plot.plot\n\n> I'll try to work through the details of the `get_min_max_data` and test thoroughly on this and #9076 as soon as these things are addressed, because in general they're both good wraps and add much-needed functionality.\n\nThe get_min_max_data for ellipse is just obtained by computing corresponding critical points. This is not the good way for arc but I will make an effort for it (as it is not too much complicate).",
    "created_at": "2010-06-14T16:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-85992",
    "user": "https://github.com/videlec"
}
```

Thank you for this careful review

> * Class def examples for reference guide

Done, if you mean examples in the docstring of the class Ellipse

> * 'circle' still shows up a few times

No more (I hope)

> * plot3d should open ticket or test `NotImplementedError`

I will. But as I really do not like the one it is implemented for circle for many different reasons I don't know how general should be the corresponding ticket...

> * I like that options are given explicitly in arc(), as well as test of `NotImplementedError`

Now there is. And I add a link from the sage.plot.plot

> I'll try to work through the details of the `get_min_max_data` and test thoroughly on this and #9076 as soon as these things are addressed, because in general they're both good wraps and add much-needed functionality.

The get_min_max_data for ellipse is just obtained by computing corresponding critical points. This is not the good way for arc but I will make an effort for it (as it is not too much complicate).



---

archive/issue_comments_085993.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-14T16:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-85993",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085994.json:
```json
{
    "body": "It appears that the get_min_max data is False. I'm working on it (post in few minutes)...",
    "created_at": "2010-06-14T18:51:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-85994",
    "user": "https://github.com/videlec"
}
```

It appears that the get_min_max data is False. I'm working on it (post in few minutes)...



---

archive/issue_comments_085995.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-14T18:51:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-85995",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_085996.json:
```json
{
    "body": "The bounding box seems to work now. I joined a worksheet that perform a lot of drawings.",
    "created_at": "2010-06-14T19:23:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-85996",
    "user": "https://github.com/videlec"
}
```

The bounding box seems to work now. I joined a worksheet that perform a lot of drawings.



---

archive/issue_comments_085997.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-14T19:23:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-85997",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085998.json:
```json
{
    "body": "See #9076 for comments on bounding box and worksheet, though for this ticket I think it's ok.  Obviously the `fmod` function can be used here too, as well as already using math.pi since it's imported (I think this should work) and initializing the radii etc. as just the input numbers, waiting to float them until `_render...` and so forth.  Very nice work otherwise.\n\nThis patch also depends on #9076, for others who might test it.",
    "created_at": "2010-06-16T15:02:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-85998",
    "user": "https://github.com/kcrisman"
}
```

See #9076 for comments on bounding box and worksheet, though for this ticket I think it's ok.  Obviously the `fmod` function can be used here too, as well as already using math.pi since it's imported (I think this should work) and initializing the radii etc. as just the input numbers, waiting to float them until `_render...` and so forth.  Very nice work otherwise.

This patch also depends on #9076, for others who might test it.



---

archive/issue_comments_085999.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-16T15:02:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-85999",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_086000.json:
```json
{
    "body": "Attachment [trac_9203-ellipse.patch](tarball://root/attachments/some-uuid/ticket9203/trac_9203-ellipse.patch) by @videlec created at 2010-06-26 14:07:24",
    "created_at": "2010-06-26T14:07:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86000",
    "user": "https://github.com/videlec"
}
```

Attachment [trac_9203-ellipse.patch](tarball://root/attachments/some-uuid/ticket9203/trac_9203-ellipse.patch) by @videlec created at 2010-06-26 14:07:24



---

archive/issue_comments_086001.json:
```json
{
    "body": "worksheet that tests the bounding box of arcs and ellipses",
    "created_at": "2010-06-26T14:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86001",
    "user": "https://github.com/videlec"
}
```

worksheet that tests the bounding box of arcs and ellipses



---

archive/issue_comments_086002.json:
```json
{
    "body": "Attachment [arcs and ellipses.sws](tarball://root/attachments/some-uuid/ticket9203/arcs and ellipses.sws) by @videlec created at 2010-06-26 14:09:45\n\nReplying to [comment:8 kcrisman]:\n> See #9076 for comments on bounding box and worksheet, though for this ticket I think it's ok.  Obviously the `fmod` function can be used here too, as well as already using math.pi since it's imported (I think this should work) and initializing the radii etc. as just the input numbers, waiting to float them until `_render...` and so forth.  Very nice work otherwise.\n> \n> This patch also depends on #9076, for others who might test it.",
    "created_at": "2010-06-26T14:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86002",
    "user": "https://github.com/videlec"
}
```

Attachment [arcs and ellipses.sws](tarball://root/attachments/some-uuid/ticket9203/arcs and ellipses.sws) by @videlec created at 2010-06-26 14:09:45

Replying to [comment:8 kcrisman]:
> See #9076 for comments on bounding box and worksheet, though for this ticket I think it's ok.  Obviously the `fmod` function can be used here too, as well as already using math.pi since it's imported (I think this should work) and initializing the radii etc. as just the input numbers, waiting to float them until `_render...` and so forth.  Very nice work otherwise.
> 
> This patch also depends on #9076, for others who might test it.



---

archive/issue_comments_086003.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-26T14:12:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86003",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_086004.json:
```json
{
    "body": "Positive review!   This will be great.  \n\nTo release manager: very minor reviewer patch to be applied after `trac_9023-ellipse` patch.  This depends on #9076.",
    "created_at": "2010-08-10T15:06:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86004",
    "user": "https://github.com/kcrisman"
}
```

Positive review!   This will be great.  

To release manager: very minor reviewer patch to be applied after `trac_9023-ellipse` patch.  This depends on #9076.



---

archive/issue_comments_086005.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-10T15:06:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86005",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086006.json:
```json
{
    "body": "Attachment [trac_9203-ellipse-reviewer.patch](tarball://root/attachments/some-uuid/ticket9203/trac_9203-ellipse-reviewer.patch) by @kcrisman created at 2010-08-10 15:06:54\n\nApply after initial patch",
    "created_at": "2010-08-10T15:06:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86006",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_9203-ellipse-reviewer.patch](tarball://root/attachments/some-uuid/ticket9203/trac_9203-ellipse-reviewer.patch) by @kcrisman created at 2010-08-10 15:06:54

Apply after initial patch



---

archive/issue_comments_086007.json:
```json
{
    "body": "Also, see ticket #9719 for a followup to the awesome worksheet.",
    "created_at": "2010-08-10T15:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86007",
    "user": "https://github.com/kcrisman"
}
```

Also, see ticket #9719 for a followup to the awesome worksheet.



---

archive/issue_comments_086008.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-08-15T09:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86008",
    "user": "https://github.com/qed777"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_086009.json:
```json
{
    "body": "Please update [attachment:trac_9203-ellipse.patch] with a more descriptive commit string.",
    "created_at": "2010-08-15T09:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86009",
    "user": "https://github.com/qed777"
}
```

Please update [attachment:trac_9203-ellipse.patch] with a more descriptive commit string.



---

archive/issue_comments_086010.json:
```json
{
    "body": "Replying to [comment:13 mpatel]:\n> Please update [attachment:trac_9203-ellipse.patch] with a more descriptive commit string.\nThe following patch is simply a hand-edited version to include a better commit message - it was not actually committed.  If that doesn't work/apply, we'll have to wait for the author to do this - but it would be really great to get this in!  Release manager can revert to positive review if this is satisfying.",
    "created_at": "2010-08-16T12:46:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86010",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:13 mpatel]:
> Please update [attachment:trac_9203-ellipse.patch] with a more descriptive commit string.
The following patch is simply a hand-edited version to include a better commit message - it was not actually committed.  If that doesn't work/apply, we'll have to wait for the author to do this - but it would be really great to get this in!  Release manager can revert to positive review if this is satisfying.



---

archive/issue_comments_086011.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-16T12:46:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86011",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_086012.json:
```json
{
    "body": "With better commit message, otherwise same",
    "created_at": "2010-08-16T12:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86012",
    "user": "https://github.com/kcrisman"
}
```

With better commit message, otherwise same



---

archive/issue_comments_086013.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-16T21:17:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86013",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086014.json:
```json
{
    "body": "Attachment [trac_9203-ellipse.2.patch](tarball://root/attachments/some-uuid/ticket9203/trac_9203-ellipse.2.patch) by @qed777 created at 2010-08-16 21:17:40",
    "created_at": "2010-08-16T21:17:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86014",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_9203-ellipse.2.patch](tarball://root/attachments/some-uuid/ticket9203/trac_9203-ellipse.2.patch) by @qed777 created at 2010-08-16 21:17:40



---

archive/issue_comments_086015.json:
```json
{
    "body": "Replying to [comment:14 kcrisman]:\n> Replying to [comment:13 mpatel]:\n> > Please update [attachment:trac_9203-ellipse.patch] with a more descriptive commit string.\n> The following patch is simply a hand-edited version to include a better commit message - it was not actually committed.  If that doesn't work/apply, we'll have to wait for the author to do this - but it would be really great to get this in!  Release manager can revert to positive review if this is satisfying.\n\nThanks for updating the patch.\n\nSince the 4.5.3 series is now in feature freeze --- it's just open to blocker problems such as build errors, doctest fixes, etc. --- and we'll merge the PARI upgrade into 4.6.alpha0, it's very likely that merging this ticket and #9076 will have to wait until 4.6.alpha1, at least.",
    "created_at": "2010-08-16T21:49:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86015",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:14 kcrisman]:
> Replying to [comment:13 mpatel]:
> > Please update [attachment:trac_9203-ellipse.patch] with a more descriptive commit string.
> The following patch is simply a hand-edited version to include a better commit message - it was not actually committed.  If that doesn't work/apply, we'll have to wait for the author to do this - but it would be really great to get this in!  Release manager can revert to positive review if this is satisfying.

Thanks for updating the patch.

Since the 4.5.3 series is now in feature freeze --- it's just open to blocker problems such as build errors, doctest fixes, etc. --- and we'll merge the PARI upgrade into 4.6.alpha0, it's very likely that merging this ticket and #9076 will have to wait until 4.6.alpha1, at least.



---

archive/issue_comments_086016.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T10:40:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86016",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_022662.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-15T10:40:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9203#event-22662"
}
```
