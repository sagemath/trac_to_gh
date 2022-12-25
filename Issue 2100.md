# Issue 2100: sensible defaults for aspect ratio

archive/issues_002100.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @kcrisman mhampton @qed777\n\nIf we are plotting a circle or sphere with circle.show(), we ought to see a circle and not have to manually specify the aspect ratio.  The aspect ratio should have sensible defaults that depend on the thing that is being plotted.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2100\n\n",
    "created_at": "2008-02-08T04:49:50Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.2",
    "title": "sensible defaults for aspect ratio",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2100",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

CC:  @kcrisman mhampton @qed777

If we are plotting a circle or sphere with circle.show(), we ought to see a circle and not have to manually specify the aspect ratio.  The aspect ratio should have sensible defaults that depend on the thing that is being plotted.

Issue created by migration from https://trac.sagemath.org/ticket/2100





---

archive/issue_comments_013562.json:
```json
{
    "body": "For reference, in Mathematica (see http://reference.wolfram.com/mathematica/ref/AspectRatio.html?q=AspectRatio&lang=en )\n\n* Graphics objects use Automatic aspect ratio\n* plot and listplot use 1/golden ratio\n* parametric plot uses automatic\n* contour plot uses aspect ratio of 1\n\nAutomatic is an aspect ratio determined by the pixels in the plot.  It does not distort the plot (i.e., circles are still circles).",
    "created_at": "2008-03-30T05:03:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13562",
    "user": "https://github.com/jasongrout"
}
```

For reference, in Mathematica (see http://reference.wolfram.com/mathematica/ref/AspectRatio.html?q=AspectRatio&lang=en )

* Graphics objects use Automatic aspect ratio
* plot and listplot use 1/golden ratio
* parametric plot uses automatic
* contour plot uses aspect ratio of 1

Automatic is an aspect ratio determined by the pixels in the plot.  It does not distort the plot (i.e., circles are still circles).



---

archive/issue_comments_013563.json:
```json
{
    "body": "Jason,\n\ndidn't we fix this recently?\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T05:41:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13563",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Jason,

didn't we fix this recently?

Cheers,

Michael



---

archive/issue_comments_013564.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13564",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_013565.json:
```json
{
    "body": "#9813 takes care of two cases of these.\n\nInterestingly, from the above list, it seems like the golden ratio is only used for a minority of functions (i.e., \"plot\" and \"list_plot\").  So maybe we ought to change the global default to aspect_ratio=1 and just set plot and list_plot to have default golden ratio aspect ratios.",
    "created_at": "2010-09-07T03:34:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13565",
    "user": "https://github.com/jasongrout"
}
```

#9813 takes care of two cases of these.

Interestingly, from the above list, it seems like the golden ratio is only used for a minority of functions (i.e., "plot" and "list_plot").  So maybe we ought to change the global default to aspect_ratio=1 and just set plot and list_plot to have default golden ratio aspect ratios.



---

archive/issue_comments_013566.json:
```json
{
    "body": "|                                 |                               |                                                                                                                                                         |             |\n|---------------------------------|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|\n| Matplotlib aspect ratio setting | Matplotlib adjustable setting | Mathematica [AspectRatio](http://trac.sagemath.org/sage_trac/search/opensearch?q=wiki%3AAspectRatio) setting | Explanation |\n| 'auto' | doesn't seem to matter | Full | Make the current data limits fill the available sized box |\n| 'equal' or 1 | 'box' | Automatic | Make each pixel be square (aspect ratio 1) |\n| | | | |\nIt appears that specifying a number in matplotlib ('box' adjustable) makes the *pixels* have a certain height-to-width ratio (e.g., a circle in the picture will appear to have the given aspect ratio), but in Mathematica, a number specifies the overall ratio of the *image* height-to-width.\u00a0 Thus the numbers are not directly comparable.\n\nPlus, in matplotlib, you can have the 'datalim' be adjustable, which changes the data limits on your plot to make the pixels have a certain aspect ratio.",
    "created_at": "2010-09-29T22:00:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13566",
    "user": "https://github.com/jasongrout"
}
```

|                                 |                               |                                                                                                                                                         |             |
|---------------------------------|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Matplotlib aspect ratio setting | Matplotlib adjustable setting | Mathematica [AspectRatio](http://trac.sagemath.org/sage_trac/search/opensearch?q=wiki%3AAspectRatio) setting | Explanation |
| 'auto' | doesn't seem to matter | Full | Make the current data limits fill the available sized box |
| 'equal' or 1 | 'box' | Automatic | Make each pixel be square (aspect ratio 1) |
| | | | |
It appears that specifying a number in matplotlib ('box' adjustable) makes the *pixels* have a certain height-to-width ratio (e.g., a circle in the picture will appear to have the given aspect ratio), but in Mathematica, a number specifies the overall ratio of the *image* height-to-width.  Thus the numbers are not directly comparable.

Plus, in matplotlib, you can have the 'datalim' be adjustable, which changes the data limits on your plot to make the pixels have a certain aspect ratio.



---

archive/issue_comments_013567.json:
```json
{
    "body": "Matplotlib's fig_aspect seems to do the sort of thing that mma's aspect ratio number setting does:\n\n!http://matplotlib.sourceforge.net/api/figure_api.html#matplotlib.figure.figaspect",
    "created_at": "2010-09-29T22:03:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13567",
    "user": "https://github.com/jasongrout"
}
```

Matplotlib's fig_aspect seems to do the sort of thing that mma's aspect ratio number setting does:

!http://matplotlib.sourceforge.net/api/figure_api.html#matplotlib.figure.figaspect



---

archive/issue_comments_013568.json:
```json
{
    "body": "One other note: setting bbox_inches='tight' in the savefig method seems to override the figure size specified.",
    "created_at": "2010-09-29T22:32:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13568",
    "user": "https://github.com/jasongrout"
}
```

One other note: setting bbox_inches='tight' in the savefig method seems to override the figure size specified.



---

archive/issue_comments_013569.json:
```json
{
    "body": "We have two concepts of \"aspect ratio\" that we'd like to expose to the user.\n\n* Figure aspect ratio -- controls the final image size, including any text labels, etc.\u00a0 This will be set using the following options:\n  * fig_aspect_ratio\n    * number - make an image with the specified aspect ratio (within reason) using the figaspect matplotlib function (which tries to be marginally smart, which actually may be a dumb thing to do...)\n    * 'auto' (default) - use bbox_inches='tight' to create a figure that holds the drawn objects\n  * figsize\n    * single number - use this as a base size for fig_aspect_ratio calculations (i.e., bigger numbers = bigger figures)\n    * two numbers - an actual figure size in inches\n* Pixel aspect ratio\n  * aspect_ratio -- the aspect ratio of a pixel in the image (or of a unit square in data coordinates, for example).\u00a0 The default here will change depending on the type of plot\n    * 'equal' or 1 -- square pixels.\u00a0 This will be the default for most things\n    * 'auto' -- plot the given data limits in the given (or computed) figsize, filling the figure\n    * number -- ratio of width to height (or height to width; I can't remember).\u00a0 For plot() and list_plot(), this will default to giving a golden ratio aspect ratio\n  * aspect_ratio_adjust -- what should we adjust to achieve the desired aspect ratio for the items drawn?\u00a0 Note that by default, the axes limits are enlarged slightly; to eliminate this, set axes_pad=0\n    * 'box' (default) -- the frame axes\n    * 'datalim' -- the data limits\n\nWhat do people think?",
    "created_at": "2010-09-30T02:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13569",
    "user": "https://github.com/jasongrout"
}
```

We have two concepts of "aspect ratio" that we'd like to expose to the user.

* Figure aspect ratio -- controls the final image size, including any text labels, etc.  This will be set using the following options:
  * fig_aspect_ratio
    * number - make an image with the specified aspect ratio (within reason) using the figaspect matplotlib function (which tries to be marginally smart, which actually may be a dumb thing to do...)
    * 'auto' (default) - use bbox_inches='tight' to create a figure that holds the drawn objects
  * figsize
    * single number - use this as a base size for fig_aspect_ratio calculations (i.e., bigger numbers = bigger figures)
    * two numbers - an actual figure size in inches
* Pixel aspect ratio
  * aspect_ratio -- the aspect ratio of a pixel in the image (or of a unit square in data coordinates, for example).  The default here will change depending on the type of plot
    * 'equal' or 1 -- square pixels.  This will be the default for most things
    * 'auto' -- plot the given data limits in the given (or computed) figsize, filling the figure
    * number -- ratio of width to height (or height to width; I can't remember).  For plot() and list_plot(), this will default to giving a golden ratio aspect ratio
  * aspect_ratio_adjust -- what should we adjust to achieve the desired aspect ratio for the items drawn?  Note that by default, the axes limits are enlarged slightly; to eliminate this, set axes_pad=0
    * 'box' (default) -- the frame axes
    * 'datalim' -- the data limits

What do people think?



---

archive/issue_comments_013570.json:
```json
{
    "body": "Helpful matplotlib mailing list post (read the thread): !http://www.mail-archive.com/matplotlib-users`@`lists.sourceforge.net/msg15623.html",
    "created_at": "2010-09-30T03:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13570",
    "user": "https://github.com/jasongrout"
}
```

Helpful matplotlib mailing list post (read the thread): !http://www.mail-archive.com/matplotlib-users`@`lists.sourceforge.net/msg15623.html



---

archive/issue_comments_013571.json:
```json
{
    "body": "Moving the proposal up to the description so we can edit it.  Ignore the proposal in the comments now.",
    "created_at": "2010-09-30T14:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13571",
    "user": "https://github.com/jasongrout"
}
```

Moving the proposal up to the description so we can edit it.  Ignore the proposal in the comments now.



---

archive/issue_comments_013572.json:
```json
{
    "body": "Update the proposal.",
    "created_at": "2010-10-01T02:01:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13572",
    "user": "https://github.com/jasongrout"
}
```

Update the proposal.



---

archive/issue_comments_013573.json:
```json
{
    "body": "I've attached two files.\u00a0 First, a work-in-progress rewrite of the aspect ratio stuff.\u00a0 Second, the plot.py file before this patch was applied.\u00a0 The plot.py file is the version from 4.6.alpha1 with tickets [#9740](http://trac.sagemath.org/sage_trac/search/opensearch?q=ticket%3A9740), [#9746](http://trac.sagemath.org/sage_trac/search/opensearch?q=ticket%3A9746), and [#4342](http://trac.sagemath.org/sage_trac/search/opensearch?q=ticket%3A4342) applied, in order.",
    "created_at": "2010-10-01T02:07:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13573",
    "user": "https://github.com/jasongrout"
}
```

I've attached two files.  First, a work-in-progress rewrite of the aspect ratio stuff.  Second, the plot.py file before this patch was applied.  The plot.py file is the version from 4.6.alpha1 with tickets [#9740](http://trac.sagemath.org/sage_trac/search/opensearch?q=ticket%3A9740), [#9746](http://trac.sagemath.org/sage_trac/search/opensearch?q=ticket%3A9746), and [#4342](http://trac.sagemath.org/sage_trac/search/opensearch?q=ticket%3A4342) applied, in order.



---

archive/issue_comments_013574.json:
```json
{
    "body": "This ticket is still needs_work.\u00a0 Remaining items include:\n\n* Updating docs to reflect changes, including\n  * Most aspect ratios now default to 1\n  * new/changed options:\n    * \u00a0fig_tight \n    * the new definition of aspect_ratio (= 1/old definition)\n    * aspect_ratio_adjustable\n* Make [GraphicsArray](http://trac.sagemath.org/sage_trac/search/opensearch?q=wiki%3AGraphicsArray) work (likely using the nice features of matplotlib in 1.0 for doing multiple subplots!)\n\nWarning: this patch changes the definition of aspect_ratio.\u00a0 Before, it was width/height, but now it is height/width.\u00a0 The new meaning is consistent with matplotlib and Mathematica.\n\nSince the patch now changes a very fundamental thing about Sage (the meaning of aspect ratio), it probably should be put off until a major release.",
    "created_at": "2010-10-01T02:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13574",
    "user": "https://github.com/jasongrout"
}
```

This ticket is still needs_work.  Remaining items include:

* Updating docs to reflect changes, including
  * Most aspect ratios now default to 1
  * new/changed options:
    *  fig_tight 
    * the new definition of aspect_ratio (= 1/old definition)
    * aspect_ratio_adjustable
* Make [GraphicsArray](http://trac.sagemath.org/sage_trac/search/opensearch?q=wiki%3AGraphicsArray) work (likely using the nice features of matplotlib in 1.0 for doing multiple subplots!)

Warning: this patch changes the definition of aspect_ratio.  Before, it was width/height, but now it is height/width.  The new meaning is consistent with matplotlib and Mathematica.

Since the patch now changes a very fundamental thing about Sage (the meaning of aspect ratio), it probably should be put off until a major release.



---

archive/issue_comments_013575.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-10-01T02:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13575",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_013576.json:
```json
{
    "body": "Also todo: set barchart and scatterplot to have default aspect ratios of 'auto'.",
    "created_at": "2010-10-01T03:31:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13576",
    "user": "https://github.com/jasongrout"
}
```

Also todo: set barchart and scatterplot to have default aspect ratios of 'auto'.



---

archive/issue_comments_013577.json:
```json
{
    "body": "Replying to [comment:14 jason]:\n\n> \n> Warning: this patch changes the definition of aspect_ratio.  Before, it was width/height, but now it is height/width.  The new meaning is consistent with matplotlib and Mathematica. Since the patch now changes a very fundamental thing about Sage (the meaning of aspect ratio), it probably should be put off until a major release.\n> \n\nApparently this statement isn't true.  The old aspect_ratio and new aspect_ratio mean the same thing.  I was basing the statement on reading the docs.  Either the current docs are backwards, or I was misreading them.\n\nSo, in short, things are good to go for finishing this patch and getting it into Sage as soon as possible.",
    "created_at": "2010-10-02T02:29:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13577",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:14 jason]:

> 
> Warning: this patch changes the definition of aspect_ratio.  Before, it was width/height, but now it is height/width.  The new meaning is consistent with matplotlib and Mathematica. Since the patch now changes a very fundamental thing about Sage (the meaning of aspect ratio), it probably should be put off until a major release.
> 

Apparently this statement isn't true.  The old aspect_ratio and new aspect_ratio mean the same thing.  I was basing the statement on reading the docs.  Either the current docs are backwards, or I was misreading them.

So, in short, things are good to go for finishing this patch and getting it into Sage as soon as possible.



---

archive/issue_comments_013578.json:
```json
{
    "body": "Attachment [2100-aspect_ratio.2.patch](tarball://root/attachments/some-uuid/ticket2100/2100-aspect_ratio.2.patch) by @jasongrout created at 2010-10-07 07:08:23\n\napply instead of previous patch",
    "created_at": "2010-10-07T07:08:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13578",
    "user": "https://github.com/jasongrout"
}
```

Attachment [2100-aspect_ratio.2.patch](tarball://root/attachments/some-uuid/ticket2100/2100-aspect_ratio.2.patch) by @jasongrout created at 2010-10-07 07:08:23

apply instead of previous patch



---

archive/issue_comments_013579.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-10-07T07:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13579",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_013580.json:
```json
{
    "body": "New patch revamping the aspect ratio calculations in Sage (and defaults!)",
    "created_at": "2010-10-07T07:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13580",
    "user": "https://github.com/jasongrout"
}
```

New patch revamping the aspect ratio calculations in Sage (and defaults!)



---

archive/issue_comments_013581.json:
```json
{
    "body": "Updating description to reflect changes in the patch.",
    "created_at": "2010-10-07T16:37:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13581",
    "user": "https://github.com/jasongrout"
}
```

Updating description to reflect changes in the patch.



---

archive/issue_comments_013582.json:
```json
{
    "body": "It seems to me that `set_aspect` ratio only accepts \"auto\" as a string input, while the proposal also lists \"equal\" as an option.\n\nWould it be possible to extend the functionality so that it is possible to specify either only width or only height of the final figure? I am thinking of using it in conjunction with SageTeX, where it would be natural to ask either for `width=\\textwidth` or `height=0.5\\texthight` and have the second dimension determined automatically based on the actual plot and aspect ratio.",
    "created_at": "2010-11-21T18:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13582",
    "user": "https://github.com/novoselt"
}
```

It seems to me that `set_aspect` ratio only accepts "auto" as a string input, while the proposal also lists "equal" as an option.

Would it be possible to extend the functionality so that it is possible to specify either only width or only height of the final figure? I am thinking of using it in conjunction with SageTeX, where it would be natural to ask either for `width=\textwidth` or `height=0.5\texthight` and have the second dimension determined automatically based on the actual plot and aspect ratio.



---

archive/issue_comments_013583.json:
```json
{
    "body": "New functions `pad_for_tick_labels` and `adjust_figure_to_contain_bbox` are not completely documented.\n\nAre #9740,  #9746, and  #4342 still prerequisites?",
    "created_at": "2010-11-21T18:24:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13583",
    "user": "https://github.com/novoselt"
}
```

New functions `pad_for_tick_labels` and `adjust_figure_to_contain_bbox` are not completely documented.

Are #9740,  #9746, and  #4342 still prerequisites?



---

archive/issue_comments_013584.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-21T18:24:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13584",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_013585.json:
```json
{
    "body": "Oops, got the answer to the last question already, for some reason they were not crossed in the above comment.",
    "created_at": "2010-11-21T18:25:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13585",
    "user": "https://github.com/novoselt"
}
```

Oops, got the answer to the last question already, for some reason they were not crossed in the above comment.



---

archive/issue_comments_013586.json:
```json
{
    "body": "This might be good bug-day fodder if people are already working on graphics code.",
    "created_at": "2011-01-12T21:43:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13586",
    "user": "https://github.com/jasongrout"
}
```

This might be good bug-day fodder if people are already working on graphics code.



---

archive/issue_comments_013587.json:
```json
{
    "body": "I hope to take care of novoselt's comments - 'equal' and the documentation - today.  This will depend on #7981, #8632, #10244, and #10143.\n\n> Would it be possible to extend the functionality so that it is possible to specify either only width or only height of the final figure? I am thinking of using it in conjunction with SageTeX, where it would be natural to ask either for `width=\\textwidth` or `height=0.5\\texthight` and have the second dimension determined automatically based on the actual plot and aspect ratio.\n\nI think this is a good idea, but I don't think the people who might work on this will have time for it before bitrot sets in even further.  I have opened ticket #10633 for this.",
    "created_at": "2011-01-14T13:26:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13587",
    "user": "https://github.com/kcrisman"
}
```

I hope to take care of novoselt's comments - 'equal' and the documentation - today.  This will depend on #7981, #8632, #10244, and #10143.

> Would it be possible to extend the functionality so that it is possible to specify either only width or only height of the final figure? I am thinking of using it in conjunction with SageTeX, where it would be natural to ask either for `width=\textwidth` or `height=0.5\texthight` and have the second dimension determined automatically based on the actual plot and aspect ratio.

I think this is a good idea, but I don't think the people who might work on this will have time for it before bitrot sets in even further.  I have opened ticket #10633 for this.



---

archive/issue_comments_013588.json:
```json
{
    "body": "Rather impressively, only one of seven hunks failed in contour_plot.py, and only 5 of 34 hunks failed on plot.py. So rebasing this to the other recent graphics patches should be no problem, as well as the other documentation comments.",
    "created_at": "2011-01-14T13:28:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13588",
    "user": "https://github.com/kcrisman"
}
```

Rather impressively, only one of seven hunks failed in contour_plot.py, and only 5 of 34 hunks failed on plot.py. So rebasing this to the other recent graphics patches should be no problem, as well as the other documentation comments.



---

archive/issue_comments_013589.json:
```json
{
    "body": "Let's just take the 'equal' option out of the proposal.  I think it's there just because that's what matplotlib does.",
    "created_at": "2011-01-14T16:06:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13589",
    "user": "https://github.com/jasongrout"
}
```

Let's just take the 'equal' option out of the proposal.  I think it's there just because that's what matplotlib does.



---

archive/issue_comments_013590.json:
```json
{
    "body": "I had to change a few things based on the new save() but otherwise nearly all is the same. It also turned out that fig_tight was never used in .matplotlib(), and in fact only can be passed to matplotlib's savefig(), so I treated it basically the same as transparent in .save().\n\nI can also remove 'equal' if you want, that's fine.\n\nBefore I go ahead and update this, though, I have a question. The two functions not documented (`pad_for_tick_labels` and `adjust_figure_to_contain_bbox`) only are used in a commented-out line\n\n```\n            # this messes up the aspect ratio!\n            #figure.canvas.mpl_connect('draw_event', pad_for_tick_labels)\n```\n\nSo... should they even be included at this time?",
    "created_at": "2011-01-14T16:09:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13590",
    "user": "https://github.com/kcrisman"
}
```

I had to change a few things based on the new save() but otherwise nearly all is the same. It also turned out that fig_tight was never used in .matplotlib(), and in fact only can be passed to matplotlib's savefig(), so I treated it basically the same as transparent in .save().

I can also remove 'equal' if you want, that's fine.

Before I go ahead and update this, though, I have a question. The two functions not documented (`pad_for_tick_labels` and `adjust_figure_to_contain_bbox`) only are used in a commented-out line

```
            # this messes up the aspect ratio!
            #figure.canvas.mpl_connect('draw_event', pad_for_tick_labels)
```

So... should they even be included at this time?



---

archive/issue_comments_013591.json:
```json
{
    "body": "Replying to [comment:26 kcrisman]:\n> I had to change a few things based on the new save() but otherwise nearly all is the same. It also turned out that fig_tight was never used in .matplotlib(), and in fact only can be passed to matplotlib's savefig(), so I treated it basically the same as transparent in .save().\n> \n> I can also remove 'equal' if you want, that's fine.\nDone as well.\n> Before I go ahead and update this, though, I have a question. The two functions not documented (`pad_for_tick_labels` and `adjust_figure_to_contain_bbox`) only are used in a commented-out line\n> {{{\n>             # this messes up the aspect ratio!\n>             #figure.canvas.mpl_connect('draw_event', pad_for_tick_labels)\n> }}}\n> So... should they even be included at this time?\nQuote from Jason: \"Feel free to move those functions to another ticket if they are really not called from anywhere.  I think they are leftovers from experimentation, so probably not strictly needed (especially if they really aren't called or used from anywhere).\"\n\nNew patch coming up relatively soon.",
    "created_at": "2011-01-17T17:25:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13591",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:26 kcrisman]:
> I had to change a few things based on the new save() but otherwise nearly all is the same. It also turned out that fig_tight was never used in .matplotlib(), and in fact only can be passed to matplotlib's savefig(), so I treated it basically the same as transparent in .save().
> 
> I can also remove 'equal' if you want, that's fine.
Done as well.
> Before I go ahead and update this, though, I have a question. The two functions not documented (`pad_for_tick_labels` and `adjust_figure_to_contain_bbox`) only are used in a commented-out line
> {{{
>             # this messes up the aspect ratio!
>             #figure.canvas.mpl_connect('draw_event', pad_for_tick_labels)
> }}}
> So... should they even be included at this time?
Quote from Jason: "Feel free to move those functions to another ticket if they are really not called from anywhere.  I think they are leftovers from experimentation, so probably not strictly needed (especially if they really aren't called or used from anywhere)."

New patch coming up relatively soon.



---

archive/issue_comments_013592.json:
```json
{
    "body": "> > So... should they even be included at this time?\n> Quote from Jason: \"Feel free to move those functions to another ticket if they are really not called from anywhere.  I think they are leftovers from experimentation, so probably not strictly needed (especially if they really aren't called or used from anywhere).\"\nSince I didn't really know where these should be used, or what the context was, I decided to just leave them in but fully commented out, with an admonition to add documentation if they ever get used again.  (This would also make it easier for a future developer to use them, inter alia.)\n\nGetting some doctest failures, though, related to this:\n\n```\nsage -t  devel/sage/sage/plot/plot3d/plot_field3d.py # 6 doctests failed\n```\n\nI doubt this will be hard to resolve.  Anyway, just status updates...",
    "created_at": "2011-01-17T19:03:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13592",
    "user": "https://github.com/kcrisman"
}
```

> > So... should they even be included at this time?
> Quote from Jason: "Feel free to move those functions to another ticket if they are really not called from anywhere.  I think they are leftovers from experimentation, so probably not strictly needed (especially if they really aren't called or used from anywhere)."
Since I didn't really know where these should be used, or what the context was, I decided to just leave them in but fully commented out, with an admonition to add documentation if they ever get used again.  (This would also make it easier for a future developer to use them, inter alia.)

Getting some doctest failures, though, related to this:

```
sage -t  devel/sage/sage/plot/plot3d/plot_field3d.py # 6 doctests failed
```

I doubt this will be hard to resolve.  Anyway, just status updates...



---

archive/issue_comments_013593.json:
```json
{
    "body": "Attachment [trac_2100-aspect-ratio-rebase.patch](tarball://root/attachments/some-uuid/ticket2100/trac_2100-aspect-ratio-rebase.patch) by @kcrisman created at 2011-01-17 20:06:30\n\nRebase to 4.6.1/4.6.2.alpha0",
    "created_at": "2011-01-17T20:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13593",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_2100-aspect-ratio-rebase.patch](tarball://root/attachments/some-uuid/ticket2100/trac_2100-aspect-ratio-rebase.patch) by @kcrisman created at 2011-01-17 20:06:30

Rebase to 4.6.1/4.6.2.alpha0



---

archive/issue_comments_013594.json:
```json
{
    "body": "The problem with the `plot_field3d` turns out to be the following very bad behavior of plotting vectors after this patch \n\n```\nsage: v = vector([1.,2.,3.])\nsage: v.plot() # all is well\nsage: plot(v) # passes in aspect_ratio to a 3d graphics, which already has such a thing, and get nasty traceback\n```\n\nThe culprit was telling `plot_vector_field3d` to do `plot(v)` for each vector instead of `v.plot()` as it should have.  However, this exposes something else really dumb - namely, that `plot.py` turns vectors into tuples before it plots them\n\n```\n    from sage.structure.element import is_Vector\n    if kwds.get('parametric',False) and is_Vector(funcs):\n        funcs = tuple(funcs)\n\n\n    if hasattr(funcs, 'plot'):\n        G = funcs.plot(*args, **original_opts)\n    # if we are using the generic plotting method\n    else:\n```\n\nthis presumably avoids the fact that\n\n```\nsage: w = vector([x^2,3,x^3])\nsage: plot(w,(x,0,1))\n---------------------------------------------------------------------------\nNotImplementedError                   \n```\n\nbut still this is a problem.  So after fixing this issue, I'm opening a ticket for making vector plotting more sensible. \n\nI think this change might need review (?) so I'm setting to 'needs review'.\n\nTo buildbot and reviewer: apply trac_2100-aspect-ratio-rebase.patch and trac_2100-3d-vector.patch.  Depends on #7981, #8632, #10244, and #10143.",
    "created_at": "2011-01-17T20:17:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13594",
    "user": "https://github.com/kcrisman"
}
```

The problem with the `plot_field3d` turns out to be the following very bad behavior of plotting vectors after this patch 

```
sage: v = vector([1.,2.,3.])
sage: v.plot() # all is well
sage: plot(v) # passes in aspect_ratio to a 3d graphics, which already has such a thing, and get nasty traceback
```

The culprit was telling `plot_vector_field3d` to do `plot(v)` for each vector instead of `v.plot()` as it should have.  However, this exposes something else really dumb - namely, that `plot.py` turns vectors into tuples before it plots them

```
    from sage.structure.element import is_Vector
    if kwds.get('parametric',False) and is_Vector(funcs):
        funcs = tuple(funcs)


    if hasattr(funcs, 'plot'):
        G = funcs.plot(*args, **original_opts)
    # if we are using the generic plotting method
    else:
```

this presumably avoids the fact that

```
sage: w = vector([x^2,3,x^3])
sage: plot(w,(x,0,1))
---------------------------------------------------------------------------
NotImplementedError                   
```

but still this is a problem.  So after fixing this issue, I'm opening a ticket for making vector plotting more sensible. 

I think this change might need review (?) so I'm setting to 'needs review'.

To buildbot and reviewer: apply trac_2100-aspect-ratio-rebase.patch and trac_2100-3d-vector.patch.  Depends on #7981, #8632, #10244, and #10143.



---

archive/issue_comments_013595.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-17T20:17:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13595",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_013596.json:
```json
{
    "body": "> I think this change might need review (?) so I'm setting to 'needs review'.\n\nOh yeah, and I never actually looked at very many of the plots.  Definitely still needs review ;) of the pictures and the (small) reviewer patch.",
    "created_at": "2011-01-18T15:45:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13596",
    "user": "https://github.com/kcrisman"
}
```

> I think this change might need review (?) so I'm setting to 'needs review'.

Oh yeah, and I never actually looked at very many of the plots.  Definitely still needs review ;) of the pictures and the (small) reviewer patch.



---

archive/issue_comments_013597.json:
```json
{
    "body": "Depends on #10143\n\n(others are \"inherited\")",
    "created_at": "2011-01-18T22:53:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13597",
    "user": "https://github.com/novoselt"
}
```

Depends on #10143

(others are "inherited")



---

archive/issue_comments_013598.json:
```json
{
    "body": "I'm setting this to positive review - it is a great improvement and it is a shame that it took us so long ;-)\n\nI am fine with the reviewer patch and I did take a look at a few (although definitely not all) plots in the documentation. Circles are finally circles!!!\n\nI have also discovered the following behaviour which may be a bug:\n\n```\nsage: x,y = var('x,y') \nsage: print x, y\nsage: f(x,y) = x^2 + y^2 - 2 \nsage: implicit_plot(f, (-3, 3), (-3, 3),fill=True).show(aspect_ratio=1) \nsage: implicit_plot(f, (-3, 3), (-3, 3),fill=False)\n```\n\nThe first line (with `fill=True`) completely fills the plot, not just the disk.",
    "created_at": "2011-01-19T03:45:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13598",
    "user": "https://github.com/novoselt"
}
```

I'm setting this to positive review - it is a great improvement and it is a shame that it took us so long ;-)

I am fine with the reviewer patch and I did take a look at a few (although definitely not all) plots in the documentation. Circles are finally circles!!!

I have also discovered the following behaviour which may be a bug:

```
sage: x,y = var('x,y') 
sage: print x, y
sage: f(x,y) = x^2 + y^2 - 2 
sage: implicit_plot(f, (-3, 3), (-3, 3),fill=True).show(aspect_ratio=1) 
sage: implicit_plot(f, (-3, 3), (-3, 3),fill=False)
```

The first line (with `fill=True`) completely fills the plot, not just the disk.



---

archive/issue_comments_013599.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-19T03:45:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13599",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_013600.json:
```json
{
    "body": "Thanks!\n> I have also discovered the following behaviour which may be a bug:\n> {{{\n> sage: x,y = var('x,y') \n> sage: print x, y\n> sage: f(x,y) = x^2 + y^2 - 2 \n> sage: implicit_plot(f, (-3, 3), (-3, 3),fill=True).show(aspect_ratio=1) \n> sage: implicit_plot(f, (-3, 3), (-3, 3),fill=False)\n> }}}\n> The first line (with `fill=True`) completely fills the plot, not just the disk.\nThis also happens with e.g. 4.6.1.alpha3, so this is definitely not related.   It sounds a LOT like #9744.  It'd be great if you could confirm that.  I thought we'd already taken care of this... unfortunately not, it seems.",
    "created_at": "2011-01-19T03:51:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13600",
    "user": "https://github.com/kcrisman"
}
```

Thanks!
> I have also discovered the following behaviour which may be a bug:
> {{{
> sage: x,y = var('x,y') 
> sage: print x, y
> sage: f(x,y) = x^2 + y^2 - 2 
> sage: implicit_plot(f, (-3, 3), (-3, 3),fill=True).show(aspect_ratio=1) 
> sage: implicit_plot(f, (-3, 3), (-3, 3),fill=False)
> }}}
> The first line (with `fill=True`) completely fills the plot, not just the disk.
This also happens with e.g. 4.6.1.alpha3, so this is definitely not related.   It sounds a LOT like #9744.  It'd be great if you could confirm that.  I thought we'd already taken care of this... unfortunately not, it seems.



---

archive/issue_comments_013601.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-19T04:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13601",
    "user": "https://github.com/novoselt"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_013602.json:
```json
{
    "body": "Actually, I was too hasty: \n\n```\nsage -t -long \"devel/sage-main/sage/modules/free_module_element.pyx\"\n**********************************************************************\nFile \"/mnt/usb1/scratch/novoselt/sage/devel/sage-main/sage/modules/free_module_element.pyx\", line 1390:\n    sage: plot(v) # defaults to an arrow plot\nException raised:\n    Traceback (most recent call last):\n      File \"/mnt/usb1/scratch/novoselt/sage/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/novoselt/sage/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/novoselt/sage/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_45[9]>\", line 1, in <module>\n        plot(v) # defaults to an arrow plot###line 1390:\n    sage: plot(v) # defaults to an arrow plot\n      File \"/mnt/usb1/scratch/novoselt/sage/local/lib/python/site-packages/sage/misc/displayhook.py\", line 174, in displayhook\n        print_obj(sys.stdout, obj)\n      File \"/mnt/usb1/scratch/novoselt/sage/local/lib/python/site-packages/sage/misc/displayhook.py\", line 142, in print_obj\n        print >>out_stream, `obj`\n      File \"base.pyx\", line 80, in sage.plot.plot3d.base.Graphics3d.__repr__ (sage/plot/plot3d/base.c:2453)\n        self.show()\n      File \"base.pyx\", line 1048, in sage.plot.plot3d.base.Graphics3d.show (sage/plot/plot3d/base.c:9375)\n        opts = self._process_viewing_options(kwds)\n      File \"base.pyx\", line 953, in sage.plot.plot3d.base.Graphics3d._process_viewing_options (sage/plot/plot3d/base.c:9174)\n        self._determine_frame_aspect_ratio(opts['aspect_ratio'])\n      File \"base.pyx\", line 199, in sage.plot.plot3d.base.Graphics3d._determine_frame_aspect_ratio (sage/plot/plot3d/base.c:3397)\n        return [(a_max[i] - a_min[i])*aspect_ratio[i] for i in range(3)]\n    TypeError: can't multiply sequence by non-int of type 'float'\n**********************************************************************\nFile \"/mnt/usb1/scratch/novoselt/sage/devel/sage-main/sage/modules/free_module_element.pyx\", line 1391:\n    sage: plot(v, plot_type='arrow')\nException raised:\n    Traceback (most recent call last):\n      File \"/mnt/usb1/scratch/novoselt/sage/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/novoselt/sage/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/novoselt/sage/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_45[10]>\", line 1, in <module>\n        plot(v, plot_type='arrow')###line 1391:\n    sage: plot(v, plot_type='arrow')\n      File \"/mnt/usb1/scratch/novoselt/sage/local/lib/python/site-packages/sage/misc/displayhook.py\", line 174, in displayhook\n        print_obj(sys.stdout, obj)\n      File \"/mnt/usb1/scratch/novoselt/sage/local/lib/python/site-packages/sage/misc/displayhook.py\", line 142, in print_obj\n        print >>out_stream, `obj`\n      File \"base.pyx\", line 80, in sage.plot.plot3d.base.Graphics3d.__repr__ (sage/plot/plot3d/base.c:2453)\n        self.show()\n      File \"base.pyx\", line 1048, in sage.plot.plot3d.base.Graphics3d.show (sage/plot/plot3d/base.c:9375)\n        opts = self._process_viewing_options(kwds)\n      File \"base.pyx\", line 953, in sage.plot.plot3d.base.Graphics3d._process_viewing_options (sage/plot/plot3d/base.c:9174)\n        self._determine_frame_aspect_ratio(opts['aspect_ratio'])\n      File \"base.pyx\", line 199, in sage.plot.plot3d.base.Graphics3d._determine_frame_aspect_ratio (sage/plot/plot3d/base.c:3397)\n        return [(a_max[i] - a_min[i])*aspect_ratio[i] for i in range(3)]\n    TypeError: can't multiply sequence by non-int of type 'float'\n**********************************************************************\nFile \"/mnt/usb1/scratch/novoselt/sage/devel/sage-main/sage/modules/free_module_element.pyx\", line 1393:\n    sage: plot(v, plot_type='point')+frame3d((0,0,0), v.list())\nException raised:\n    Traceback (most recent call last):\n      File \"/mnt/usb1/scratch/novoselt/sage/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/novoselt/sage/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/novoselt/sage/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_45[12]>\", line 1, in <module>\n        plot(v, plot_type='point')+frame3d((Integer(0),Integer(0),Integer(0)), v.list())###line 1393:\n    sage: plot(v, plot_type='point')+frame3d((0,0,0), v.list())\n      File \"/mnt/usb1/scratch/novoselt/sage/local/lib/python/site-packages/sage/misc/displayhook.py\", line 174, in displayhook\n        print_obj(sys.stdout, obj)\n      File \"/mnt/usb1/scratch/novoselt/sage/local/lib/python/site-packages/sage/misc/displayhook.py\", line 142, in print_obj\n        print >>out_stream, `obj`\n      File \"base.pyx\", line 80, in sage.plot.plot3d.base.Graphics3d.__repr__ (sage/plot/plot3d/base.c:2453)\n        self.show()\n      File \"base.pyx\", line 1048, in sage.plot.plot3d.base.Graphics3d.show (sage/plot/plot3d/base.c:9375)\n        opts = self._process_viewing_options(kwds)\n      File \"base.pyx\", line 953, in sage.plot.plot3d.base.Graphics3d._process_viewing_options (sage/plot/plot3d/base.c:9174)\n        self._determine_frame_aspect_ratio(opts['aspect_ratio'])\n      File \"base.pyx\", line 199, in sage.plot.plot3d.base.Graphics3d._determine_frame_aspect_ratio (sage/plot/plot3d/base.c:3397)\n        return [(a_max[i] - a_min[i])*aspect_ratio[i] for i in range(3)]\n    TypeError: can't multiply sequence by non-int of type 'float'\n**********************************************************************\n1 items had failures:\n   3 of  17 in __main__.example_45\n***Test Failed*** 3 failures.\n```\n\n\nThese are the only errors on the whole library. I guess they should be fixed in the same way as in the reviewer patch. Or maybe there should be a better fix?..",
    "created_at": "2011-01-19T04:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13602",
    "user": "https://github.com/novoselt"
}
```

Actually, I was too hasty: 

```
sage -t -long "devel/sage-main/sage/modules/free_module_element.pyx"
**********************************************************************
File "/mnt/usb1/scratch/novoselt/sage/devel/sage-main/sage/modules/free_module_element.pyx", line 1390:
    sage: plot(v) # defaults to an arrow plot
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/novoselt/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/novoselt/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/novoselt/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_45[9]>", line 1, in <module>
        plot(v) # defaults to an arrow plot###line 1390:
    sage: plot(v) # defaults to an arrow plot
      File "/mnt/usb1/scratch/novoselt/sage/local/lib/python/site-packages/sage/misc/displayhook.py", line 174, in displayhook
        print_obj(sys.stdout, obj)
      File "/mnt/usb1/scratch/novoselt/sage/local/lib/python/site-packages/sage/misc/displayhook.py", line 142, in print_obj
        print >>out_stream, `obj`
      File "base.pyx", line 80, in sage.plot.plot3d.base.Graphics3d.__repr__ (sage/plot/plot3d/base.c:2453)
        self.show()
      File "base.pyx", line 1048, in sage.plot.plot3d.base.Graphics3d.show (sage/plot/plot3d/base.c:9375)
        opts = self._process_viewing_options(kwds)
      File "base.pyx", line 953, in sage.plot.plot3d.base.Graphics3d._process_viewing_options (sage/plot/plot3d/base.c:9174)
        self._determine_frame_aspect_ratio(opts['aspect_ratio'])
      File "base.pyx", line 199, in sage.plot.plot3d.base.Graphics3d._determine_frame_aspect_ratio (sage/plot/plot3d/base.c:3397)
        return [(a_max[i] - a_min[i])*aspect_ratio[i] for i in range(3)]
    TypeError: can't multiply sequence by non-int of type 'float'
**********************************************************************
File "/mnt/usb1/scratch/novoselt/sage/devel/sage-main/sage/modules/free_module_element.pyx", line 1391:
    sage: plot(v, plot_type='arrow')
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/novoselt/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/novoselt/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/novoselt/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_45[10]>", line 1, in <module>
        plot(v, plot_type='arrow')###line 1391:
    sage: plot(v, plot_type='arrow')
      File "/mnt/usb1/scratch/novoselt/sage/local/lib/python/site-packages/sage/misc/displayhook.py", line 174, in displayhook
        print_obj(sys.stdout, obj)
      File "/mnt/usb1/scratch/novoselt/sage/local/lib/python/site-packages/sage/misc/displayhook.py", line 142, in print_obj
        print >>out_stream, `obj`
      File "base.pyx", line 80, in sage.plot.plot3d.base.Graphics3d.__repr__ (sage/plot/plot3d/base.c:2453)
        self.show()
      File "base.pyx", line 1048, in sage.plot.plot3d.base.Graphics3d.show (sage/plot/plot3d/base.c:9375)
        opts = self._process_viewing_options(kwds)
      File "base.pyx", line 953, in sage.plot.plot3d.base.Graphics3d._process_viewing_options (sage/plot/plot3d/base.c:9174)
        self._determine_frame_aspect_ratio(opts['aspect_ratio'])
      File "base.pyx", line 199, in sage.plot.plot3d.base.Graphics3d._determine_frame_aspect_ratio (sage/plot/plot3d/base.c:3397)
        return [(a_max[i] - a_min[i])*aspect_ratio[i] for i in range(3)]
    TypeError: can't multiply sequence by non-int of type 'float'
**********************************************************************
File "/mnt/usb1/scratch/novoselt/sage/devel/sage-main/sage/modules/free_module_element.pyx", line 1393:
    sage: plot(v, plot_type='point')+frame3d((0,0,0), v.list())
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/novoselt/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/novoselt/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/novoselt/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_45[12]>", line 1, in <module>
        plot(v, plot_type='point')+frame3d((Integer(0),Integer(0),Integer(0)), v.list())###line 1393:
    sage: plot(v, plot_type='point')+frame3d((0,0,0), v.list())
      File "/mnt/usb1/scratch/novoselt/sage/local/lib/python/site-packages/sage/misc/displayhook.py", line 174, in displayhook
        print_obj(sys.stdout, obj)
      File "/mnt/usb1/scratch/novoselt/sage/local/lib/python/site-packages/sage/misc/displayhook.py", line 142, in print_obj
        print >>out_stream, `obj`
      File "base.pyx", line 80, in sage.plot.plot3d.base.Graphics3d.__repr__ (sage/plot/plot3d/base.c:2453)
        self.show()
      File "base.pyx", line 1048, in sage.plot.plot3d.base.Graphics3d.show (sage/plot/plot3d/base.c:9375)
        opts = self._process_viewing_options(kwds)
      File "base.pyx", line 953, in sage.plot.plot3d.base.Graphics3d._process_viewing_options (sage/plot/plot3d/base.c:9174)
        self._determine_frame_aspect_ratio(opts['aspect_ratio'])
      File "base.pyx", line 199, in sage.plot.plot3d.base.Graphics3d._determine_frame_aspect_ratio (sage/plot/plot3d/base.c:3397)
        return [(a_max[i] - a_min[i])*aspect_ratio[i] for i in range(3)]
    TypeError: can't multiply sequence by non-int of type 'float'
**********************************************************************
1 items had failures:
   3 of  17 in __main__.example_45
***Test Failed*** 3 failures.
```


These are the only errors on the whole library. I guess they should be fixed in the same way as in the reviewer patch. Or maybe there should be a better fix?..



---

archive/issue_comments_013603.json:
```json
{
    "body": "Yes, the problem I hit is exactly #9744 (which actually mentions the same example from the documentation), thanks for pointing it out.",
    "created_at": "2011-01-19T04:29:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13603",
    "user": "https://github.com/novoselt"
}
```

Yes, the problem I hit is exactly #9744 (which actually mentions the same example from the documentation), thanks for pointing it out.



---

archive/issue_comments_013604.json:
```json
{
    "body": "Replying to [comment:36 novoselt]:\n> Actually, I was too hasty: \n> sage -t -long \"devel/sage-main/sage/modules/free_module_element.pyx\"\nAargh!  I'll try to fix this...\n> These are the only errors on the whole library. I guess they should be fixed in the same way as in the reviewer patch. Or maybe there should be a better fix?..\nNo, that is the correct fix for now.   An overarching ticket is #10638, which I forgot to mention before.",
    "created_at": "2011-01-19T13:30:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13604",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:36 novoselt]:
> Actually, I was too hasty: 
> sage -t -long "devel/sage-main/sage/modules/free_module_element.pyx"
Aargh!  I'll try to fix this...
> These are the only errors on the whole library. I guess they should be fixed in the same way as in the reviewer patch. Or maybe there should be a better fix?..
No, that is the correct fix for now.   An overarching ticket is #10638, which I forgot to mention before.



---

archive/issue_comments_013605.json:
```json
{
    "body": "Replying to [comment:38 kcrisman]:\n> Replying to [comment:36 novoselt]:\n> > Actually, I was too hasty: \n> > sage -t -long \"devel/sage-main/sage/modules/free_module_element.pyx\"\n> Aargh!  I'll try to fix this...\n> > These are the only errors on the whole library. I guess they should be fixed in the same way as in the reviewer patch. Or maybe there should be a better fix?..\n> No, that is the correct fix for now.   An overarching ticket is #10638, which I forgot to mention before.\nThe correct fix is to remove that kwd from the plot when \n\n```\n\n        if plot_type == 'arrow' or plot_type == 'point':\n            dimension = len(coords)\n            if dimension == 3:\n                from sage.plot.plot3d.shapes2 import line3d, point3d\n                \n                if plot_type == 'arrow':\n                    return line3d([(0,0,0), coords], arrow_head=True, **kwds)\n                else:\n                    return point3d(coords, **kwds)\n```\n\nthat should do it.  I will try this later.",
    "created_at": "2011-01-19T13:35:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13605",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:38 kcrisman]:
> Replying to [comment:36 novoselt]:
> > Actually, I was too hasty: 
> > sage -t -long "devel/sage-main/sage/modules/free_module_element.pyx"
> Aargh!  I'll try to fix this...
> > These are the only errors on the whole library. I guess they should be fixed in the same way as in the reviewer patch. Or maybe there should be a better fix?..
> No, that is the correct fix for now.   An overarching ticket is #10638, which I forgot to mention before.
The correct fix is to remove that kwd from the plot when 

```

        if plot_type == 'arrow' or plot_type == 'point':
            dimension = len(coords)
            if dimension == 3:
                from sage.plot.plot3d.shapes2 import line3d, point3d
                
                if plot_type == 'arrow':
                    return line3d([(0,0,0), coords], arrow_head=True, **kwds)
                else:
                    return point3d(coords, **kwds)
```

that should do it.  I will try this later.



---

archive/issue_comments_013606.json:
```json
{
    "body": "> > > These are the only errors on the whole library. I guess they should be fixed in the same way as in the reviewer patch. Or maybe there should be a better fix?..\n> > No, that is the correct fix for now.   An overarching ticket is #10638, which I forgot to mention before.\nOkay, now I am not rushing out the door and can think straight.  The problem is that this was never doctesting the thing in question in the first place because of the issues raised in #10638.  \n\nI *think* the issue is that `_extract_kwds_for_show` keeps the ``@`options` value of `aspect_ratio='auto') in play; when this gets passed to the `show()` method of `Line` (which is what `line3d` creates in this case), it refers to the one in `base.PrimitiveObject`, which unfortunately then puts this value of `aspect_ratio` in:\n\n```\n        opts = {}\n        opts.update(SHOW_DEFAULTS)\n        if self._extra_kwds is not None:\n            opts.update(self._extra_kwds)\n        opts.update(kwds)\n```\n\nand then doesn't realize it's a problem in\n\n```\n        if opts['frame_aspect_ratio'] == 'automatic':\n            if opts['aspect_ratio'] != 'automatic':\n                # Set the aspect_ratio of the frame to be the same as that of\n                # the object we are rendering given the aspect_ratio we'll use\n                # for it.\n                opts['frame_aspect_ratio'] = \\\n                    self._determine_frame_aspect_ratio(opts['aspect_ratio'])\n```\n\nWhich is where the problem happens.\n\nAlthough fixing this in the vector plotting didn't seem to work immediately.\n\nUnless we wanted to change all the 'auto' in this patch to 'automatic'.  I don't know if that is desirable either, though.  What do others think?",
    "created_at": "2011-01-19T19:24:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13606",
    "user": "https://github.com/kcrisman"
}
```

> > > These are the only errors on the whole library. I guess they should be fixed in the same way as in the reviewer patch. Or maybe there should be a better fix?..
> > No, that is the correct fix for now.   An overarching ticket is #10638, which I forgot to mention before.
Okay, now I am not rushing out the door and can think straight.  The problem is that this was never doctesting the thing in question in the first place because of the issues raised in #10638.  

I *think* the issue is that `_extract_kwds_for_show` keeps the ``@`options` value of `aspect_ratio='auto') in play; when this gets passed to the `show()` method of `Line` (which is what `line3d` creates in this case), it refers to the one in `base.PrimitiveObject`, which unfortunately then puts this value of `aspect_ratio` in:

```
        opts = {}
        opts.update(SHOW_DEFAULTS)
        if self._extra_kwds is not None:
            opts.update(self._extra_kwds)
        opts.update(kwds)
```

and then doesn't realize it's a problem in

```
        if opts['frame_aspect_ratio'] == 'automatic':
            if opts['aspect_ratio'] != 'automatic':
                # Set the aspect_ratio of the frame to be the same as that of
                # the object we are rendering given the aspect_ratio we'll use
                # for it.
                opts['frame_aspect_ratio'] = \
                    self._determine_frame_aspect_ratio(opts['aspect_ratio'])
```

Which is where the problem happens.

Although fixing this in the vector plotting didn't seem to work immediately.

Unless we wanted to change all the 'auto' in this patch to 'automatic'.  I don't know if that is desirable either, though.  What do others think?



---

archive/issue_comments_013607.json:
```json
{
    "body": "I like `auto` more than `automatic`, so I don't want to change it.\n\nCan we maybe change it the other way? Was `automatic` documented/used somewhere before?",
    "created_at": "2011-01-19T19:47:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13607",
    "user": "https://github.com/novoselt"
}
```

I like `auto` more than `automatic`, so I don't want to change it.

Can we maybe change it the other way? Was `automatic` documented/used somewhere before?



---

archive/issue_comments_013608.json:
```json
{
    "body": "> I like `auto` more than `automatic`, so I don't want to change it.\nAgreed, but...\n> Can we maybe change it the other way? Was `automatic` documented/used somewhere before?\nYes, this is the standard 3D option.  See [this reference manual page](http://www.sagemath.org/doc/reference/sage/plot/plot3d/base.html#sage.plot.plot3d.base.Graphics3d.show) for plot/plot3d/base.pyx.\n\nOf course, it would be possible to change the plot3d case to also accept 'auto' easily enough - in fact, that's essentially what I've done in my latest patch - and one could change the documentation accordingly.  But we couldn't remove it without a deprecation period - and in my mind it's pointless to go to the trouble, given that it's mostly a default so we could change things without even needing to deprecate that option.",
    "created_at": "2011-01-19T20:10:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13608",
    "user": "https://github.com/kcrisman"
}
```

> I like `auto` more than `automatic`, so I don't want to change it.
Agreed, but...
> Can we maybe change it the other way? Was `automatic` documented/used somewhere before?
Yes, this is the standard 3D option.  See [this reference manual page](http://www.sagemath.org/doc/reference/sage/plot/plot3d/base.html#sage.plot.plot3d.base.Graphics3d.show) for plot/plot3d/base.pyx.

Of course, it would be possible to change the plot3d case to also accept 'auto' easily enough - in fact, that's essentially what I've done in my latest patch - and one could change the documentation accordingly.  But we couldn't remove it without a deprecation period - and in my mind it's pointless to go to the trouble, given that it's mostly a default so we could change things without even needing to deprecate that option.



---

archive/issue_comments_013609.json:
```json
{
    "body": "I guess then changing to `automatic` is OK.\n\nFor consistency, it would be nice if the same variant was used throughout Sage, but then again the point is that this value should not be specified explicitly by the user.",
    "created_at": "2011-01-19T20:16:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13609",
    "user": "https://github.com/novoselt"
}
```

I guess then changing to `automatic` is OK.

For consistency, it would be nice if the same variant was used throughout Sage, but then again the point is that this value should not be specified explicitly by the user.



---

archive/issue_comments_013610.json:
```json
{
    "body": "Replying to [comment:43 novoselt]:\n> I guess then changing to `automatic` is OK.\nI'd want to run that by Jason (the original author) first, though - after all, the point below would suggest it doesn't matter (and it is a long process for me to rebase, sadly).\n> For consistency, it would be nice if the same variant was used throughout Sage, but then again the point is that this value should not be specified explicitly by the user.",
    "created_at": "2011-01-19T20:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13610",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:43 novoselt]:
> I guess then changing to `automatic` is OK.
I'd want to run that by Jason (the original author) first, though - after all, the point below would suggest it doesn't matter (and it is a long process for me to rebase, sadly).
> For consistency, it would be nice if the same variant was used throughout Sage, but then again the point is that this value should not be specified explicitly by the user.



---

archive/issue_comments_013611.json:
```json
{
    "body": "> > I guess then changing to `automatic` is OK.\n> I'd want to run that by Jason (the original author) first, though - after all, the point below would suggest it doesn't matter (and it is a long process for me to rebase, sadly).\nOne reason being that matplotlib uses 'auto', and consistency with that is nice as well.\n> > For consistency, it would be nice if the same variant was used throughout Sage, but then again the point is that this value should not be specified explicitly by the user.",
    "created_at": "2011-01-19T20:32:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13611",
    "user": "https://github.com/kcrisman"
}
```

> > I guess then changing to `automatic` is OK.
> I'd want to run that by Jason (the original author) first, though - after all, the point below would suggest it doesn't matter (and it is a long process for me to rebase, sadly).
One reason being that matplotlib uses 'auto', and consistency with that is nice as well.
> > For consistency, it would be nice if the same variant was used throughout Sage, but then again the point is that this value should not be specified explicitly by the user.



---

archive/issue_comments_013612.json:
```json
{
    "body": "Okay, this latest reviewer patch should fix the things we've talked about in a minimalist way.  It doesn't resolve the 'auto' versus 'automatic' issue.  No new instructions for applying patches.  Documentation also looks good with this change.",
    "created_at": "2011-01-19T20:36:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13612",
    "user": "https://github.com/kcrisman"
}
```

Okay, this latest reviewer patch should fix the things we've talked about in a minimalist way.  It doesn't resolve the 'auto' versus 'automatic' issue.  No new instructions for applying patches.  Documentation also looks good with this change.



---

archive/issue_comments_013613.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-19T20:36:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13613",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_013614.json:
```json
{
    "body": "Attachment [trac_2100-3d-vector.patch](tarball://root/attachments/some-uuid/ticket2100/trac_2100-3d-vector.patch) by @kcrisman created at 2011-01-19 20:38:49\n\nreviewer patch",
    "created_at": "2011-01-19T20:38:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13614",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_2100-3d-vector.patch](tarball://root/attachments/some-uuid/ticket2100/trac_2100-3d-vector.patch) by @kcrisman created at 2011-01-19 20:38:49

reviewer patch



---

archive/issue_comments_013615.json:
```json
{
    "body": "Wow, great job tracking down this subtle problem.  I personally slightly prefer `'auto'` over `'automatic'` because it's consistent with matplotlib and it's shorter.  However, I agree that users will probably not specify it too frequently, so `'automatic'` would probably be fine as well.  If we do make the default `'automatic'`, then I think we'll have to convert it to `'auto'` before passing it to matplotlib.\n\nAnother data point: mma uses Automatic (not Auto): http://reference.wolfram.com/mathematica/ref/Automatic.html",
    "created_at": "2011-01-19T21:24:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13615",
    "user": "https://github.com/jasongrout"
}
```

Wow, great job tracking down this subtle problem.  I personally slightly prefer `'auto'` over `'automatic'` because it's consistent with matplotlib and it's shorter.  However, I agree that users will probably not specify it too frequently, so `'automatic'` would probably be fine as well.  If we do make the default `'automatic'`, then I think we'll have to convert it to `'auto'` before passing it to matplotlib.

Another data point: mma uses Automatic (not Auto): http://reference.wolfram.com/mathematica/ref/Automatic.html



---

archive/issue_comments_013616.json:
```json
{
    "body": "Replying to [comment:48 jason]:\n> Wow, great job tracking down this subtle problem.  I personally slightly prefer `'auto'` over `'automatic'` because it's consistent with matplotlib and it's shorter.  However, I agree that users will probably not specify it too frequently, so `'automatic'` would probably be fine as well.  \nThanks.  I don't have any more time today to work on this, but I think then I vote for `'automatic'` for consistency, and having `'auto'` as one that secretly also works :) \n> If we do make the default `'automatic'`, then I think we'll have to convert it to `'auto'` before passing it to matplotlib.\nYes, I realize that.  I don't think that will be very difficult, since there seems to be only one place this is passed.",
    "created_at": "2011-01-19T21:31:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13616",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:48 jason]:
> Wow, great job tracking down this subtle problem.  I personally slightly prefer `'auto'` over `'automatic'` because it's consistent with matplotlib and it's shorter.  However, I agree that users will probably not specify it too frequently, so `'automatic'` would probably be fine as well.  
Thanks.  I don't have any more time today to work on this, but I think then I vote for `'automatic'` for consistency, and having `'auto'` as one that secretly also works :) 
> If we do make the default `'automatic'`, then I think we'll have to convert it to `'auto'` before passing it to matplotlib.
Yes, I realize that.  I don't think that will be very difficult, since there seems to be only one place this is passed.



---

archive/issue_comments_013617.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-21T13:28:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13617",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_013618.json:
```json
{
    "body": "Okay, putting this to 'needs work' in order to fix this.  Hopefully today or this weekend; it won't be hard, just have to do it.",
    "created_at": "2011-01-21T13:28:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13618",
    "user": "https://github.com/kcrisman"
}
```

Okay, putting this to 'needs work' in order to fix this.  Hopefully today or this weekend; it won't be hard, just have to do it.



---

archive/issue_comments_013619.json:
```json
{
    "body": "Oops... hmm, I gave myself one long weekend.  I'll try to see if this still applies to 4.6.2.alpha4 soon.",
    "created_at": "2011-02-08T18:01:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13619",
    "user": "https://github.com/kcrisman"
}
```

Oops... hmm, I gave myself one long weekend.  I'll try to see if this still applies to 4.6.2.alpha4 soon.



---

archive/issue_comments_013620.json:
```json
{
    "body": "All still applies to 4.6.2.alpha4.  I hope to conclude this adventure shortly, by replacing the reviewer patch with one that deals with the automatic/auto issue uniformly.",
    "created_at": "2011-02-14T19:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13620",
    "user": "https://github.com/kcrisman"
}
```

All still applies to 4.6.2.alpha4.  I hope to conclude this adventure shortly, by replacing the reviewer patch with one that deals with the automatic/auto issue uniformly.



---

archive/issue_comments_013621.json:
```json
{
    "body": "This should all work fine now.  I do want to point out that the standard plots seem to have increased somewhat in size.  The new reviewer patch is now different enough that it needs review.  Please do so now to avoid bitrot!",
    "created_at": "2011-02-15T03:01:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13621",
    "user": "https://github.com/kcrisman"
}
```

This should all work fine now.  I do want to point out that the standard plots seem to have increased somewhat in size.  The new reviewer patch is now different enough that it needs review.  Please do so now to avoid bitrot!



---

archive/issue_comments_013622.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-02-15T03:01:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13622",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_013623.json:
```json
{
    "body": "Replying to [comment:53 kcrisman]:\n> This should all work fine now.  I do want to point out that the standard plots seem to have increased somewhat in size.\n\nYes, I reverted things to the matplotlib defaults.  Before, we made the ratio of height/width the golden ratio, but now it is the standard matplotlib default (which I believe is 4:3, which matches computer screens better anyway).",
    "created_at": "2011-02-15T03:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13623",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:53 kcrisman]:
> This should all work fine now.  I do want to point out that the standard plots seem to have increased somewhat in size.

Yes, I reverted things to the matplotlib defaults.  Before, we made the ratio of height/width the golden ratio, but now it is the standard matplotlib default (which I believe is 4:3, which matches computer screens better anyway).



---

archive/issue_comments_013624.json:
```json
{
    "body": "Changing assignee from @williamstein to @jasongrout.",
    "created_at": "2011-02-15T03:09:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13624",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @williamstein to @jasongrout.



---

archive/issue_comments_013625.json:
```json
{
    "body": "Can you add instructions for reviewers/patchbot about which patches should be applied in what order?",
    "created_at": "2011-02-15T03:09:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13625",
    "user": "https://github.com/jasongrout"
}
```

Can you add instructions for reviewers/patchbot about which patches should be applied in what order?



---

archive/issue_comments_013626.json:
```json
{
    "body": "(and then I'll try to review this tonight or tomorrow)",
    "created_at": "2011-02-15T03:09:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13626",
    "user": "https://github.com/jasongrout"
}
```

(and then I'll try to review this tonight or tomorrow)



---

archive/issue_comments_013627.json:
```json
{
    "body": "See the description. I guess I didn't make it obvious enough :)\n\nApply [trac_2100-aspect-ratio-rebase.patch] and [trac_2100-auto-automatic-and-vector.patch] for this.",
    "created_at": "2011-02-15T03:11:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13627",
    "user": "https://github.com/kcrisman"
}
```

See the description. I guess I didn't make it obvious enough :)

Apply [trac_2100-aspect-ratio-rebase.patch] and [trac_2100-auto-automatic-and-vector.patch] for this.



---

archive/issue_comments_013628.json:
```json
{
    "body": "Apply [trac_2100-aspect-ratio-rebase.patch trac_2100-aspect-ratio-rebase.patch] and [trac_2100-auto-automatic-and-vector.patch trac_2100-auto-automatic-and-vector.patch] for this.",
    "created_at": "2011-02-15T03:12:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13628",
    "user": "https://github.com/kcrisman"
}
```

Apply [trac_2100-aspect-ratio-rebase.patch trac_2100-aspect-ratio-rebase.patch] and [trac_2100-auto-automatic-and-vector.patch trac_2100-auto-automatic-and-vector.patch] for this.



---

archive/issue_comments_013629.json:
```json
{
    "body": "I can't get the links to work for some reason - sorry.",
    "created_at": "2011-02-15T03:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13629",
    "user": "https://github.com/kcrisman"
}
```

I can't get the links to work for some reason - sorry.



---

archive/issue_comments_013630.json:
```json
{
    "body": "To patchbot/reviewers: Apply attachment:trac_2100-aspect-ratio-rebase.patch and attachment:trac_2100-auto-automatic-and-vector.patch",
    "created_at": "2011-02-16T17:17:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13630",
    "user": "https://github.com/kcrisman"
}
```

To patchbot/reviewers: Apply attachment:trac_2100-aspect-ratio-rebase.patch and attachment:trac_2100-auto-automatic-and-vector.patch



---

archive/issue_comments_013631.json:
```json
{
    "body": "Here is some code that looks less good with this patch than before.\n\n```\ndef my_eulers_method_plot(a_function,x0,y0,h,x1):\n    n=int((1.0)*(x1-x0)/h)\n    x00=x0; y00=y0\n    x01=x0; y01=y0\n    P=point((x00,y00),rgbcolor=hue(1)) # red    \n    Q=Graphics() # default is blue\n    f(x,y)=a_function(x,y) # Note that a_function should be a callable function of x, then y\n    for i in range(n+1):\n        y01 = y00+h*f(x00,y00)\n        x01 = x00+h\n        P=P+point((x01,y01),rgbcolor=hue(1))\n        Q=Q+line([(x00,y00),(x01,y01)])\n        x00=x01\n        y00=y01\n    return(P+Q)\n\nvar('x,y')\ndef euler_logistic_plot(parameter,y_start,end=15,step=1):\n    function(x,y)=parameter*y*(1-y)\n    my_eulers_method_plot(function,0,y_start,step,end).show(ymin=0)\n\neuler_logistic_plot(2,.7,97,.8)\n```\n\nI'll try to attach before and after.",
    "created_at": "2011-02-19T04:20:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13631",
    "user": "https://github.com/kcrisman"
}
```

Here is some code that looks less good with this patch than before.

```
def my_eulers_method_plot(a_function,x0,y0,h,x1):
    n=int((1.0)*(x1-x0)/h)
    x00=x0; y00=y0
    x01=x0; y01=y0
    P=point((x00,y00),rgbcolor=hue(1)) # red    
    Q=Graphics() # default is blue
    f(x,y)=a_function(x,y) # Note that a_function should be a callable function of x, then y
    for i in range(n+1):
        y01 = y00+h*f(x00,y00)
        x01 = x00+h
        P=P+point((x01,y01),rgbcolor=hue(1))
        Q=Q+line([(x00,y00),(x01,y01)])
        x00=x01
        y00=y01
    return(P+Q)

var('x,y')
def euler_logistic_plot(parameter,y_start,end=15,step=1):
    function(x,y)=parameter*y*(1-y)
    my_eulers_method_plot(function,0,y_start,step,end).show(ymin=0)

euler_logistic_plot(2,.7,97,.8)
```

I'll try to attach before and after.



---

archive/issue_comments_013632.json:
```json
{
    "body": "What this plot looks like before #2100",
    "created_at": "2011-02-19T04:21:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13632",
    "user": "https://github.com/kcrisman"
}
```

What this plot looks like before #2100



---

archive/issue_comments_013633.json:
```json
{
    "body": "Attachment [After.png](tarball://root/attachments/some-uuid/ticket2100/After.png) by @kcrisman created at 2011-02-19 04:21:54\n\nWhat this plot looks like after #2100",
    "created_at": "2011-02-19T04:21:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13633",
    "user": "https://github.com/kcrisman"
}
```

Attachment [After.png](tarball://root/attachments/some-uuid/ticket2100/After.png) by @kcrisman created at 2011-02-19 04:21:54

What this plot looks like after #2100



---

archive/issue_comments_013634.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2011-02-19T04:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13634",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_013635.json:
```json
{
    "body": "The issue is of course that I never used `plot()` to do this, but rather only `line()` and `point()` and `Graphics()`.  The default aspect ratio seems to have changed a lot, and so not only are the labels on the left totally squished, but it just looks bad.  Maybe mpl defaults aren't that great?  Or is this a pretty unusual scenario?\n\nAnyway, putting as needs info until I know what is happening here from someone who knows more about mpl (e.g., Jason).  So frustrating, too, because we should have this in!",
    "created_at": "2011-02-19T04:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13635",
    "user": "https://github.com/kcrisman"
}
```

The issue is of course that I never used `plot()` to do this, but rather only `line()` and `point()` and `Graphics()`.  The default aspect ratio seems to have changed a lot, and so not only are the labels on the left totally squished, but it just looks bad.  Maybe mpl defaults aren't that great?  Or is this a pretty unusual scenario?

Anyway, putting as needs info until I know what is happening here from someone who knows more about mpl (e.g., Jason).  So frustrating, too, because we should have this in!



---

archive/issue_comments_013636.json:
```json
{
    "body": "Yep, I think the problem here is that line and point now default to have aspect_ratio=1, so the y and x axis are drawn at equal scales.  Try setting the aspect_ratio to 'auto' (or whatever your patch does now).\n\nplot() defaults to 'auto' aspect ratio (e.g., fill the figure).  However, geometric figures like line and point default to aspect_ratio=1.",
    "created_at": "2011-02-19T04:54:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13636",
    "user": "https://github.com/jasongrout"
}
```

Yep, I think the problem here is that line and point now default to have aspect_ratio=1, so the y and x axis are drawn at equal scales.  Try setting the aspect_ratio to 'auto' (or whatever your patch does now).

plot() defaults to 'auto' aspect ratio (e.g., fill the figure).  However, geometric figures like line and point default to aspect_ratio=1.



---

archive/issue_comments_013637.json:
```json
{
    "body": "I think perhaps we should make line (and point?) default to 'auto'?  Because one is quite likely to have a line do a function, as opposed to other geometric figures.  And points are often used to shadow functions.\n\nAny other thoughts on this?  It would be really nice to finally get this in 4.7 - maybe you can take a quick look over spring break?",
    "created_at": "2011-03-05T02:52:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13637",
    "user": "https://github.com/kcrisman"
}
```

I think perhaps we should make line (and point?) default to 'auto'?  Because one is quite likely to have a line do a function, as opposed to other geometric figures.  And points are often used to shadow functions.

Any other thoughts on this?  It would be really nice to finally get this in 4.7 - maybe you can take a quick look over spring break?



---

archive/issue_comments_013638.json:
```json
{
    "body": "Putting needs review, though may need a minor change because of the thing in the last two comments.",
    "created_at": "2011-03-05T02:53:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13638",
    "user": "https://github.com/kcrisman"
}
```

Putting needs review, though may need a minor change because of the thing in the last two comments.



---

archive/issue_comments_013639.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-03-05T02:53:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13639",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_013640.json:
```json
{
    "body": "Okay, I'm going to refresh so that line and point still have 'auto'.  Needs review!",
    "created_at": "2011-06-15T19:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13640",
    "user": "https://github.com/kcrisman"
}
```

Okay, I'm going to refresh so that line and point still have 'auto'.  Needs review!



---

archive/issue_comments_013641.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd31\".",
    "created_at": "2011-06-15T19:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13641",
    "user": "https://github.com/kcrisman"
}
```

Changing keywords from "" to "sd31".



---

archive/issue_comments_013642.json:
```json
{
    "body": "FYI, I am currently reviewing this patch",
    "created_at": "2011-06-16T22:46:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13642",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

FYI, I am currently reviewing this patch



---

archive/issue_comments_013643.json:
```json
{
    "body": "Patch looks good.  Confirmed that kcrisman's code looks 'good' after the patch too :)  Positive Review. Great job guys.\n\nNote: I do get doctest failures on plot_field.py, but the failures are not caused by the patches to this ticket.",
    "created_at": "2011-06-16T23:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13643",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Patch looks good.  Confirmed that kcrisman's code looks 'good' after the patch too :)  Positive Review. Great job guys.

Note: I do get doctest failures on plot_field.py, but the failures are not caused by the patches to this ticket.



---

archive/issue_comments_013644.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-06-16T23:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13644",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_013645.json:
```json
{
    "body": "Replying to [comment:68 ryan]:\n> Note: I do get doctest failures on plot_field.py, but the failures are not caused by the patches to this ticket.\n\nWhat exactly do you mean by this? That a clean public release of Sage has doctest failures in `plot_field.py`?",
    "created_at": "2011-06-16T23:51:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13645",
    "user": "https://github.com/novoselt"
}
```

Replying to [comment:68 ryan]:
> Note: I do get doctest failures on plot_field.py, but the failures are not caused by the patches to this ticket.

What exactly do you mean by this? That a clean public release of Sage has doctest failures in `plot_field.py`?



---

archive/issue_comments_013646.json:
```json
{
    "body": "Correct - or to be more precise, warnings that do not cause the doctest to fail.  They are known, and not from Sage.",
    "created_at": "2011-06-17T00:13:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13646",
    "user": "https://github.com/kcrisman"
}
```

Correct - or to be more precise, warnings that do not cause the doctest to fail.  They are known, and not from Sage.



---

archive/issue_comments_013647.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-06-18T10:11:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13647",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_013648.json:
```json
{
    "body": "Please rebase this patch to be applied on top of #11491.",
    "created_at": "2011-06-18T10:11:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13648",
    "user": "https://github.com/jdemeyer"
}
```

Please rebase this patch to be applied on top of #11491.



---

archive/issue_comments_013649.json:
```json
{
    "body": "Replying to [comment:72 jdemeyer]:\n> Please rebase this patch to be applied on top of #11491.\n\nThanks - another rebase where a major improvement takes second rank to a trivial adjustment.  Especially since Ryan and I were involved on both tickets, it would have been nice to ask first.   Rebasing is not so trivial for the setups some of us have.\n\nBut no point crying over spilt milk.  Sigh... patches coming up.",
    "created_at": "2011-06-20T14:45:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13649",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:72 jdemeyer]:
> Please rebase this patch to be applied on top of #11491.

Thanks - another rebase where a major improvement takes second rank to a trivial adjustment.  Especially since Ryan and I were involved on both tickets, it would have been nice to ask first.   Rebasing is not so trivial for the setups some of us have.

But no point crying over spilt milk.  Sigh... patches coming up.



---

archive/issue_comments_013650.json:
```json
{
    "body": "Attachment [trac_2100-auto-automatic-and-vector.patch](tarball://root/attachments/some-uuid/ticket2100/trac_2100-auto-automatic-and-vector.patch) by @kcrisman created at 2011-06-20 14:45:44\n\nApply after rebase patch",
    "created_at": "2011-06-20T14:45:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13650",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_2100-auto-automatic-and-vector.patch](tarball://root/attachments/some-uuid/ticket2100/trac_2100-auto-automatic-and-vector.patch) by @kcrisman created at 2011-06-20 14:45:44

Apply after rebase patch



---

archive/issue_comments_013651.json:
```json
{
    "body": "Okay, *now* we should hopefully be at positive review!",
    "created_at": "2011-06-20T14:48:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13651",
    "user": "https://github.com/kcrisman"
}
```

Okay, *now* we should hopefully be at positive review!



---

archive/issue_comments_013652.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-06-20T14:48:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13652",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_013653.json:
```json
{
    "body": "Replying to [comment:73 kcrisman]:\n> Especially since Ryan and I were involved on both tickets, it would have been nice to ask first.\n\nI have done that in the past and **people complained**: [http://groups.google.com/group/sage-devel/browse_frm/thread/abd5fb944769e052/8e4057172b97f2e5](http://groups.google.com/group/sage-devel/browse_frm/thread/abd5fb944769e052/8e4057172b97f2e5)",
    "created_at": "2011-06-20T15:17:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13653",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:73 kcrisman]:
> Especially since Ryan and I were involved on both tickets, it would have been nice to ask first.

I have done that in the past and **people complained**: [http://groups.google.com/group/sage-devel/browse_frm/thread/abd5fb944769e052/8e4057172b97f2e5](http://groups.google.com/group/sage-devel/browse_frm/thread/abd5fb944769e052/8e4057172b97f2e5)



---

archive/issue_comments_013654.json:
```json
{
    "body": "Right, and my point is that this sort of feels the same way.   I am **not** suggesting unmerging something positively reviewed - definitely not the direction I'm going.\n\nWhat I'm suggesting (and only suggesting, because I can only imagine how much work release management is) is that perhaps sending a ping via Trac on two closely related tickets which have some overlap would be good *before* deciding which one to merge first.  Especially since in this case #11491 is so clearly much more trivial than this one, and also much older.    I'm sure Ryan and I would have agreed that this one was higher priority.\n\nAnyway, it turned out I had time for fixing it - it was a very small overlap, luckily.  Thanks for all the hard work; the final releases really are noticeably more polished nowadays, and it's a great thing.",
    "created_at": "2011-06-20T15:26:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13654",
    "user": "https://github.com/kcrisman"
}
```

Right, and my point is that this sort of feels the same way.   I am **not** suggesting unmerging something positively reviewed - definitely not the direction I'm going.

What I'm suggesting (and only suggesting, because I can only imagine how much work release management is) is that perhaps sending a ping via Trac on two closely related tickets which have some overlap would be good *before* deciding which one to merge first.  Especially since in this case #11491 is so clearly much more trivial than this one, and also much older.    I'm sure Ryan and I would have agreed that this one was higher priority.

Anyway, it turned out I had time for fixing it - it was a very small overlap, luckily.  Thanks for all the hard work; the final releases really are noticeably more polished nowadays, and it's a great thing.



---

archive/issue_comments_013655.json:
```json
{
    "body": "Replying to [comment:76 kcrisman]:\n> Right, and my point is that this sort of feels the same way.   I am **not** suggesting unmerging something positively reviewed - definitely not the direction I'm going.\n> \n> What I'm suggesting (and only suggesting, because I can only imagine how much work release management is) is that perhaps sending a ping via Trac on two closely related tickets which have some overlap would be good *before* deciding which one to merge first.  Especially since in this case #11491 is so clearly much more trivial than this one, and also much older.    I'm sure Ryan and I would have agreed that this one was higher priority.\n\nIt is not easy for me to determine a priori which patches conflict with eachother, so what you propose isn't really possible.  It's not that I looked at both patches and decided which one to merge.  What happened is that I already decided to merge #11491 before I even considered the patch here.\n\nSince the sage-devel discussion I mentioned, there is an agreement that once a patch is merged (even in a future alpha version), it should stay merged if possible.",
    "created_at": "2011-06-20T15:34:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13655",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:76 kcrisman]:
> Right, and my point is that this sort of feels the same way.   I am **not** suggesting unmerging something positively reviewed - definitely not the direction I'm going.
> 
> What I'm suggesting (and only suggesting, because I can only imagine how much work release management is) is that perhaps sending a ping via Trac on two closely related tickets which have some overlap would be good *before* deciding which one to merge first.  Especially since in this case #11491 is so clearly much more trivial than this one, and also much older.    I'm sure Ryan and I would have agreed that this one was higher priority.

It is not easy for me to determine a priori which patches conflict with eachother, so what you propose isn't really possible.  It's not that I looked at both patches and decided which one to merge.  What happened is that I already decided to merge #11491 before I even considered the patch here.

Since the sage-devel discussion I mentioned, there is an agreement that once a patch is merged (even in a future alpha version), it should stay merged if possible.



---

archive/issue_comments_013656.json:
```json
{
    "body": "Replying to [comment:76 kcrisman]:\n> Thanks for all the hard work; the final releases really are noticeably more polished nowadays, and it's a great thing.\nYou should really also thank Mitesh Patel for managing the [buildbot](http://build.sagemath.org/sage/waterfall).",
    "created_at": "2011-06-20T15:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13656",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:76 kcrisman]:
> Thanks for all the hard work; the final releases really are noticeably more polished nowadays, and it's a great thing.
You should really also thank Mitesh Patel for managing the [buildbot](http://build.sagemath.org/sage/waterfall).



---

archive/issue_comments_013657.json:
```json
{
    "body": "> It is not easy for me to determine a priori which patches conflict with eachother, so what you propose isn't really possible.  It's not that I looked at both patches and decided which one to merge.  What happened is that I already decided to merge #11491 before I even considered the patch here.\n\nUnderstood.\n\n> Since the sage-devel discussion I mentioned, there is an agreement that once a patch is merged (even in a future alpha version), it should stay merged if possible.\n\nYes, that definitely makes sense, as I hope I make clear above.  :)",
    "created_at": "2011-06-20T15:44:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13657",
    "user": "https://github.com/kcrisman"
}
```

> It is not easy for me to determine a priori which patches conflict with eachother, so what you propose isn't really possible.  It's not that I looked at both patches and decided which one to merge.  What happened is that I already decided to merge #11491 before I even considered the patch here.

Understood.

> Since the sage-devel discussion I mentioned, there is an agreement that once a patch is merged (even in a future alpha version), it should stay merged if possible.

Yes, that definitely makes sense, as I hope I make clear above.  :)



---

archive/issue_comments_013658.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-07-22T12:48:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2100#issuecomment-13658",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
