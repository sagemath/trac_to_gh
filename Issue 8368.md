# Issue 8368: add colorbar option to contour_plots

archive/issues_008368.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @kcrisman wcauchois @robert-marik\n\nThis patch adds the option of creating a color bar on a filled contour plot.  See the doctests in the patch for examples.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8368\n\n",
    "created_at": "2010-02-25T19:15:12Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "add colorbar option to contour_plots",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8368",
    "user": "@jasongrout"
}
```
Assignee: @williamstein

CC:  @kcrisman wcauchois @robert-marik

This patch adds the option of creating a color bar on a filled contour plot.  See the doctests in the patch for examples.

Issue created by migration from https://trac.sagemath.org/ticket/8368





---

archive/issue_comments_074796.json:
```json
{
    "body": "This ticket depends on #8366.",
    "created_at": "2010-02-25T19:17:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8368#issuecomment-74796",
    "user": "@jasongrout"
}
```

This ticket depends on #8366.



---

archive/issue_comments_074797.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-25T19:17:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8368#issuecomment-74797",
    "user": "@jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074798.json:
```json
{
    "body": "(update makes colorbars work even when fill=False)",
    "created_at": "2010-02-25T19:43:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8368#issuecomment-74798",
    "user": "@jasongrout"
}
```

(update makes colorbars work even when fill=False)



---

archive/issue_comments_074799.json:
```json
{
    "body": "One thing I don't like about this is that you can't easily get a 1:1 aspect ratio plot - using figsize = [a,a] makes the overall figure square but not the plotted region.",
    "created_at": "2010-04-04T04:05:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8368#issuecomment-74799",
    "user": "mhampton"
}
```

One thing I don't like about this is that you can't easily get a 1:1 aspect ratio plot - using figsize = [a,a] makes the overall figure square but not the plotted region.



---

archive/issue_comments_074800.json:
```json
{
    "body": "Replying to [comment:4 mhampton]:\n> One thing I don't like about this is that you can't easily get a 1:1 aspect ratio plot - using figsize = [a,a] makes the overall figure square but not the plotted region.\n\nOf course.  If you want the aspect ratio to be 1, then use the aspect_ratio=1 argument, which controls the aspect ratio.  The figsize option controls the \"figure size\", i.e., the size of the entire figure.",
    "created_at": "2010-04-15T03:34:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8368#issuecomment-74800",
    "user": "@jasongrout"
}
```

Replying to [comment:4 mhampton]:
> One thing I don't like about this is that you can't easily get a 1:1 aspect ratio plot - using figsize = [a,a] makes the overall figure square but not the plotted region.

Of course.  If you want the aspect ratio to be 1, then use the aspect_ratio=1 argument, which controls the aspect ratio.  The figsize option controls the "figure size", i.e., the size of the entire figure.



---

archive/issue_comments_074801.json:
```json
{
    "body": "apply instead of previous patch (rebased for the new #8366)",
    "created_at": "2010-04-15T03:35:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8368#issuecomment-74801",
    "user": "@jasongrout"
}
```

apply instead of previous patch (rebased for the new #8366)



---

archive/issue_comments_074802.json:
```json
{
    "body": "Attachment [trac-8368-colorbars.patch](tarball://root/attachments/some-uuid/ticket8368/trac-8368-colorbars.patch) by mhampton created at 2010-04-15 15:14:56\n\nReplying to [comment:5 jason]:\n> Replying to [comment:4 mhampton]:\n> > One thing I don't like about this is that you can't easily get a 1:1 aspect ratio plot - using figsize = [a,a] makes the overall figure square but not the plotted region.\n> \n> Of course.  If you want the aspect ratio to be 1, then use the aspect_ratio=1 argument, which controls the aspect ratio.  The figsize option controls the \"figure size\", i.e., the size of the entire figure.\n\nOK.  I think I got into the habit of using figsize before aspect_ratio worked.  I will check the rebased version as soon as I can.",
    "created_at": "2010-04-15T15:14:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8368#issuecomment-74802",
    "user": "mhampton"
}
```

Attachment [trac-8368-colorbars.patch](tarball://root/attachments/some-uuid/ticket8368/trac-8368-colorbars.patch) by mhampton created at 2010-04-15 15:14:56

Replying to [comment:5 jason]:
> Replying to [comment:4 mhampton]:
> > One thing I don't like about this is that you can't easily get a 1:1 aspect ratio plot - using figsize = [a,a] makes the overall figure square but not the plotted region.
> 
> Of course.  If you want the aspect ratio to be 1, then use the aspect_ratio=1 argument, which controls the aspect ratio.  The figsize option controls the "figure size", i.e., the size of the entire figure.

OK.  I think I got into the habit of using figsize before aspect_ratio worked.  I will check the rebased version as soon as I can.



---

archive/issue_comments_074803.json:
```json
{
    "body": "Thanks for rebasing, I got the following errors. (But I do not switch the 'needs_review' flag unless somebody confirms this issue.)\n\n```\n...\n      File \"/mnt/usb1/scratch/marik/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/lib/python/site-packages/sage/plot/contour_plot.py\", line 193, in _render_on_subplot\n        if options['colorbar']:\n    KeyError: 'colorbar'\n**********************************************************************\n...\n----------------------------------------------------------------------\nThe following tests failed:\n\n        sage -t  \"devel/sage/sage/plot/contour_plot.py\"\nTotal time for all tests: 25.0 seconds\n```\n\n\nIt would be also nice to add :: in between each pair of different examples - this allows to run any of the examples provided in this patch immediately from reference guide.\nRobert",
    "created_at": "2010-04-16T11:02:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8368#issuecomment-74803",
    "user": "@robert-marik"
}
```

Thanks for rebasing, I got the following errors. (But I do not switch the 'needs_review' flag unless somebody confirms this issue.)

```
...
      File "/mnt/usb1/scratch/marik/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/lib/python/site-packages/sage/plot/contour_plot.py", line 193, in _render_on_subplot
        if options['colorbar']:
    KeyError: 'colorbar'
**********************************************************************
...
----------------------------------------------------------------------
The following tests failed:

        sage -t  "devel/sage/sage/plot/contour_plot.py"
Total time for all tests: 25.0 seconds
```


It would be also nice to add :: in between each pair of different examples - this allows to run any of the examples provided in this patch immediately from reference guide.
Robert



---

archive/issue_comments_074804.json:
```json
{
    "body": "apply on top of previous patch",
    "created_at": "2010-04-16T11:56:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8368#issuecomment-74804",
    "user": "@jasongrout"
}
```

apply on top of previous patch



---

archive/issue_comments_074805.json:
```json
{
    "body": "Attachment [trac-8368-fix-options.patch](tarball://root/attachments/some-uuid/ticket8368/trac-8368-fix-options.patch) by @jasongrout created at 2010-04-16 11:57:06\n\nI fixed both issues in the above patch.\n\nI also doctested contour_plot.py this time!\u00a0 Things should work now.",
    "created_at": "2010-04-16T11:57:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8368#issuecomment-74805",
    "user": "@jasongrout"
}
```

Attachment [trac-8368-fix-options.patch](tarball://root/attachments/some-uuid/ticket8368/trac-8368-fix-options.patch) by @jasongrout created at 2010-04-16 11:57:06

I fixed both issues in the above patch.

I also doctested contour_plot.py this time!  Things should work now.



---

archive/issue_comments_074806.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-21T17:23:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8368#issuecomment-74806",
    "user": "@robert-marik"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074807.json:
```json
{
    "body": "Installs fine, works as excpected, tests passed now, documentation builds fine, positive review and thanks for adding this feature, as well as including my comments.\n\nPositive review.\n\nRelease manager: Apply both trac-8368-colorbars.patch and trac-8368-fix-options.patch patches.",
    "created_at": "2010-04-21T17:23:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8368#issuecomment-74807",
    "user": "@robert-marik"
}
```

Installs fine, works as excpected, tests passed now, documentation builds fine, positive review and thanks for adding this feature, as well as including my comments.

Positive review.

Release manager: Apply both trac-8368-colorbars.patch and trac-8368-fix-options.patch patches.



---

archive/issue_comments_074808.json:
```json
{
    "body": "Merged into 4.4.alpha2:\n- trac-8368-colorbars.patch\n- trac-8368-fix-options.patch",
    "created_at": "2010-04-23T17:11:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8368#issuecomment-74808",
    "user": "@jhpalmieri"
}
```

Merged into 4.4.alpha2:
- trac-8368-colorbars.patch
- trac-8368-fix-options.patch



---

archive/issue_comments_074809.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-23T17:11:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8368#issuecomment-74809",
    "user": "@jhpalmieri"
}
```

Resolution: fixed
