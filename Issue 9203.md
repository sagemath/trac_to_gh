# Issue 9203: plot ellipses

archive/issues_009203.json:
```json
{
    "body": "Assignee: vdelecroix\n\nCC:  kcrisman jason\n\nKeywords: plot, geometry, ellipse\n\nAdding a primitive for plot ellipses that wraps the existing patch of matplotlib.\n\nThis is approximately the same stuff as the patch #9076 for plotting arcs (of circle and ellipse).\n\nIssue created by migration from https://trac.sagemath.org/ticket/9203\n\n",
    "created_at": "2010-06-10T13:43:14Z",
    "labels": [
        "geometry",
        "major",
        "enhancement"
    ],
    "title": "plot ellipses",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9203",
    "user": "vdelecroix"
}
```
Assignee: vdelecroix

CC:  kcrisman jason

Keywords: plot, geometry, ellipse

Adding a primitive for plot ellipses that wraps the existing patch of matplotlib.

This is approximately the same stuff as the patch #9076 for plotting arcs (of circle and ellipse).

Issue created by migration from https://trac.sagemath.org/ticket/9203





---

archive/issue_comments_086127.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-10T13:45:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86127",
    "user": "vdelecroix"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_086128.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-14T13:30:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86128",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_086129.json:
```json
{
    "body": "This looks nice overall too, but again some things needed for best results.\n\n* Class def examples for reference guide\n\n* 'circle' still shows up a few times\n \n* This `_repr_` method is better than the arc one!\n\n* plot3d should open ticket or test `NotImplementedError`\n\n* I like that options are given explicitly in arc(), as well as test of `NotImplementedError`\n\nI'll try to work through the details of the `get_min_max_data` and test thoroughly on this and #9076 as soon as these things are addressed, because in general they're both good wraps and add much-needed functionality.  Good work!",
    "created_at": "2010-06-14T13:30:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86129",
    "user": "kcrisman"
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

archive/issue_comments_086130.json:
```json
{
    "body": "Thank you for this careful review\n\n> * Class def examples for reference guide\n\nDone, if you mean examples in the docstring of the class Ellipse\n\n> * 'circle' still shows up a few times\n\nNo more (I hope)\n\n> * plot3d should open ticket or test `NotImplementedError`\n\nI will. But as I really do not like the one it is implemented for circle for many different reasons I don't know how general should be the corresponding ticket...\n\n> * I like that options are given explicitly in arc(), as well as test of `NotImplementedError`\n\nNow there is. And I add a link from the sage.plot.plot\n\n> I'll try to work through the details of the `get_min_max_data` and test thoroughly on this and #9076 as soon as these things are addressed, because in general they're both good wraps and add much-needed functionality.\n\nThe get_min_max_data for ellipse is just obtained by computing corresponding critical points. This is not the good way for arc but I will make an effort for it (as it is not too much complicate).",
    "created_at": "2010-06-14T16:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86130",
    "user": "vdelecroix"
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

archive/issue_comments_086131.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-14T16:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86131",
    "user": "vdelecroix"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_086132.json:
```json
{
    "body": "It appears that the get_min_max data is False. I'm working on it (post in few minutes)...",
    "created_at": "2010-06-14T18:51:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86132",
    "user": "vdelecroix"
}
```

It appears that the get_min_max data is False. I'm working on it (post in few minutes)...



---

archive/issue_comments_086133.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-14T18:51:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86133",
    "user": "vdelecroix"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_086134.json:
```json
{
    "body": "The bounding box seems to work now. I joined a worksheet that perform a lot of drawings.",
    "created_at": "2010-06-14T19:23:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86134",
    "user": "vdelecroix"
}
```

The bounding box seems to work now. I joined a worksheet that perform a lot of drawings.



---

archive/issue_comments_086135.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-14T19:23:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86135",
    "user": "vdelecroix"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_086136.json:
```json
{
    "body": "See #9076 for comments on bounding box and worksheet, though for this ticket I think it's ok.  Obviously the `fmod` function can be used here too, as well as already using math.pi since it's imported (I think this should work) and initializing the radii etc. as just the input numbers, waiting to float them until `_render...` and so forth.  Very nice work otherwise.\n\nThis patch also depends on #9076, for others who might test it.",
    "created_at": "2010-06-16T15:02:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86136",
    "user": "kcrisman"
}
```

See #9076 for comments on bounding box and worksheet, though for this ticket I think it's ok.  Obviously the `fmod` function can be used here too, as well as already using math.pi since it's imported (I think this should work) and initializing the radii etc. as just the input numbers, waiting to float them until `_render...` and so forth.  Very nice work otherwise.

This patch also depends on #9076, for others who might test it.



---

archive/issue_comments_086137.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-16T15:02:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86137",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_086138.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-06-26T14:07:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86138",
    "user": "vdelecroix"
}
```

Attachment



---

archive/issue_comments_086139.json:
```json
{
    "body": "worksheet that tests the bounding box of arcs and ellipses",
    "created_at": "2010-06-26T14:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86139",
    "user": "vdelecroix"
}
```

worksheet that tests the bounding box of arcs and ellipses



---

archive/issue_comments_086140.json:
```json
{
    "body": "Attachment\n\nReplying to [comment:8 kcrisman]:\n> See #9076 for comments on bounding box and worksheet, though for this ticket I think it's ok.  Obviously the `fmod` function can be used here too, as well as already using math.pi since it's imported (I think this should work) and initializing the radii etc. as just the input numbers, waiting to float them until `_render...` and so forth.  Very nice work otherwise.\n> \n> This patch also depends on #9076, for others who might test it.",
    "created_at": "2010-06-26T14:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86140",
    "user": "vdelecroix"
}
```

Attachment

Replying to [comment:8 kcrisman]:
> See #9076 for comments on bounding box and worksheet, though for this ticket I think it's ok.  Obviously the `fmod` function can be used here too, as well as already using math.pi since it's imported (I think this should work) and initializing the radii etc. as just the input numbers, waiting to float them until `_render...` and so forth.  Very nice work otherwise.
> 
> This patch also depends on #9076, for others who might test it.



---

archive/issue_comments_086141.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-26T14:12:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86141",
    "user": "vdelecroix"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_086142.json:
```json
{
    "body": "Positive review!   This will be great.  \n\nTo release manager: very minor reviewer patch to be applied after `trac_9023-ellipse` patch.  This depends on #9076.",
    "created_at": "2010-08-10T15:06:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86142",
    "user": "kcrisman"
}
```

Positive review!   This will be great.  

To release manager: very minor reviewer patch to be applied after `trac_9023-ellipse` patch.  This depends on #9076.



---

archive/issue_comments_086143.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-10T15:06:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86143",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086144.json:
```json
{
    "body": "Attachment\n\nApply after initial patch",
    "created_at": "2010-08-10T15:06:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86144",
    "user": "kcrisman"
}
```

Attachment

Apply after initial patch



---

archive/issue_comments_086145.json:
```json
{
    "body": "Also, see ticket #9719 for a followup to the awesome worksheet.",
    "created_at": "2010-08-10T15:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86145",
    "user": "kcrisman"
}
```

Also, see ticket #9719 for a followup to the awesome worksheet.



---

archive/issue_comments_086146.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-08-15T09:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86146",
    "user": "mpatel"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_086147.json:
```json
{
    "body": "Please update [attachment:trac_9203-ellipse.patch] with a more descriptive commit string.",
    "created_at": "2010-08-15T09:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86147",
    "user": "mpatel"
}
```

Please update [attachment:trac_9203-ellipse.patch] with a more descriptive commit string.



---

archive/issue_comments_086148.json:
```json
{
    "body": "Replying to [comment:13 mpatel]:\n> Please update [attachment:trac_9203-ellipse.patch] with a more descriptive commit string.\nThe following patch is simply a hand-edited version to include a better commit message - it was not actually committed.  If that doesn't work/apply, we'll have to wait for the author to do this - but it would be really great to get this in!  Release manager can revert to positive review if this is satisfying.",
    "created_at": "2010-08-16T12:46:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86148",
    "user": "kcrisman"
}
```

Replying to [comment:13 mpatel]:
> Please update [attachment:trac_9203-ellipse.patch] with a more descriptive commit string.
The following patch is simply a hand-edited version to include a better commit message - it was not actually committed.  If that doesn't work/apply, we'll have to wait for the author to do this - but it would be really great to get this in!  Release manager can revert to positive review if this is satisfying.



---

archive/issue_comments_086149.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-16T12:46:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86149",
    "user": "kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_086150.json:
```json
{
    "body": "With better commit message, otherwise same",
    "created_at": "2010-08-16T12:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86150",
    "user": "kcrisman"
}
```

With better commit message, otherwise same



---

archive/issue_comments_086151.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-16T21:17:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86151",
    "user": "mpatel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086152.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-08-16T21:17:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86152",
    "user": "mpatel"
}
```

Attachment



---

archive/issue_comments_086153.json:
```json
{
    "body": "Replying to [comment:14 kcrisman]:\n> Replying to [comment:13 mpatel]:\n> > Please update [attachment:trac_9203-ellipse.patch] with a more descriptive commit string.\n> The following patch is simply a hand-edited version to include a better commit message - it was not actually committed.  If that doesn't work/apply, we'll have to wait for the author to do this - but it would be really great to get this in!  Release manager can revert to positive review if this is satisfying.\n\nThanks for updating the patch.\n\nSince the 4.5.3 series is now in feature freeze --- it's just open to blocker problems such as build errors, doctest fixes, etc. --- and we'll merge the PARI upgrade into 4.6.alpha0, it's very likely that merging this ticket and #9076 will have to wait until 4.6.alpha1, at least.",
    "created_at": "2010-08-16T21:49:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86153",
    "user": "mpatel"
}
```

Replying to [comment:14 kcrisman]:
> Replying to [comment:13 mpatel]:
> > Please update [attachment:trac_9203-ellipse.patch] with a more descriptive commit string.
> The following patch is simply a hand-edited version to include a better commit message - it was not actually committed.  If that doesn't work/apply, we'll have to wait for the author to do this - but it would be really great to get this in!  Release manager can revert to positive review if this is satisfying.

Thanks for updating the patch.

Since the 4.5.3 series is now in feature freeze --- it's just open to blocker problems such as build errors, doctest fixes, etc. --- and we'll merge the PARI upgrade into 4.6.alpha0, it's very likely that merging this ticket and #9076 will have to wait until 4.6.alpha1, at least.



---

archive/issue_comments_086154.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T10:40:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9203#issuecomment-86154",
    "user": "mpatel"
}
```

Resolution: fixed
