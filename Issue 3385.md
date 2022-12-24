# Issue 3385: plot_vector_field does not deal with aspect ratios correctly

archive/issues_003385.json:
```json
{
    "body": "Assignee: was\n\nAs [reported to sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/8f409c06fc3a291c), `plot_vector_field()` does not change the angle of the arrows as appropriate for the aspect ratio.\n\nTo see this, take [this `@`interact demo](http://wiki.sagemath.org/interact/diffeq#head-f79d3195e10d507bda57064c8b8d10d15e55a5e4) and change `xmin` to 1/4. The plotted solution is correct, but the angles of the arrows for the vector field aren't changed correctly. (Also see https://www.sagenb.org/home/pub/1794/, if it's actually loading.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/3385\n\n",
    "created_at": "2008-06-08T23:22:38Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "plot_vector_field does not deal with aspect ratios correctly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3385",
    "user": "ddrake"
}
```
Assignee: was

As [reported to sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/8f409c06fc3a291c), `plot_vector_field()` does not change the angle of the arrows as appropriate for the aspect ratio.

To see this, take [this `@`interact demo](http://wiki.sagemath.org/interact/diffeq#head-f79d3195e10d507bda57064c8b8d10d15e55a5e4) and change `xmin` to 1/4. The plotted solution is correct, but the angles of the arrows for the vector field aren't changed correctly. (Also see https://www.sagenb.org/home/pub/1794/, if it's actually loading.)

Issue created by migration from https://trac.sagemath.org/ticket/3385





---

archive/issue_comments_023690.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-03T01:05:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3385#issuecomment-23690",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_023691.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2008-09-03T01:05:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3385#issuecomment-23691",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_023692.json:
```json
{
    "body": "From the quiver documentation:\n\n```\n    In all cases the arrow aspect ratio is 1, so that if *U*==*V* the\n    angle of the arrow on the plot is 45 degrees CCW from the *x*-axis.\n```\n\n\nBasically, if you want the arrows to match up with the axes in the plot, you *must* have aspect_ratio=1. (that is, unless the arrows are horizontal or vertical :).",
    "created_at": "2008-09-12T05:08:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3385#issuecomment-23692",
    "user": "jason"
}
```

From the quiver documentation:

```
    In all cases the arrow aspect ratio is 1, so that if *U*==*V* the
    angle of the arrow on the plot is 45 degrees CCW from the *x*-axis.
```


Basically, if you want the arrows to match up with the axes in the plot, you *must* have aspect_ratio=1. (that is, unless the arrows are horizontal or vertical :).



---

archive/issue_comments_023693.json:
```json
{
    "body": "\n```\n[23:03] <jason> okay, so basically vector plots are junk unless you plot it with aspect_ratio=1\n[23:03] <jason> This is *very* good to know.\n[23:05] <mhansen> If I get bored, I may change it to use actual arrows.\n[23:06] <jason> You could use my new arrow class :)\n[23:06] <mhansen> Yep\n[23:06] <jason> well, you've probably got enough on your plate to not get bored for a while\n[23:06] <jason> for now, I think we ought to change the plot_vector_field and plot_slope_field documentation\n[23:06] <jason> to put a huge warning in there that these plots must be plotted with aspect_ratio=1 to make any sense\n[23:07] <jason> And maybe also to issue a warning when actually drawing a plot if it's not aspect_ratio=1\n```\n",
    "created_at": "2008-09-12T05:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3385#issuecomment-23693",
    "user": "jason"
}
```


```
[23:03] <jason> okay, so basically vector plots are junk unless you plot it with aspect_ratio=1
[23:03] <jason> This is *very* good to know.
[23:05] <mhansen> If I get bored, I may change it to use actual arrows.
[23:06] <jason> You could use my new arrow class :)
[23:06] <mhansen> Yep
[23:06] <jason> well, you've probably got enough on your plate to not get bored for a while
[23:06] <jason> for now, I think we ought to change the plot_vector_field and plot_slope_field documentation
[23:06] <jason> to put a huge warning in there that these plots must be plotted with aspect_ratio=1 to make any sense
[23:07] <jason> And maybe also to issue a warning when actually drawing a plot if it's not aspect_ratio=1
```




---

archive/issue_comments_023694.json:
```json
{
    "body": "Wow, ask and ye shall receive!  In response to a query on the matplotlib list, efiring (on the matplotlib team) added an 'angles' keyword that allows us to have arrows that are scaled to respect the aspect ratio:\n\nhttp://matplotlib.svn.sourceforge.net/viewvc/matplotlib/trunk/matplotlib/lib/matplotlib/quiver.py?r1=6067&r2=6112&pathrev=6112\n\nSo I guess the problem is pretty much solved if we update to matplotlib svn.",
    "created_at": "2008-09-19T01:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3385#issuecomment-23694",
    "user": "jason"
}
```

Wow, ask and ye shall receive!  In response to a query on the matplotlib list, efiring (on the matplotlib team) added an 'angles' keyword that allows us to have arrows that are scaled to respect the aspect ratio:

http://matplotlib.svn.sourceforge.net/viewvc/matplotlib/trunk/matplotlib/lib/matplotlib/quiver.py?r1=6067&r2=6112&pathrev=6112

So I guess the problem is pretty much solved if we update to matplotlib svn.



---

archive/issue_comments_023695.json:
```json
{
    "body": "That is a keyword argument to the matplotlib quiver command.",
    "created_at": "2008-09-19T01:18:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3385#issuecomment-23695",
    "user": "jason"
}
```

That is a keyword argument to the matplotlib quiver command.



---

archive/issue_comments_023696.json:
```json
{
    "body": "I updated the matplotlib spkg to matplotlib-0.98.3.p2.spkg to include the SVN version of quiver.py that adds this keyword.  Everything seems to work great and tests pass in the plot directory.\n\nThe new spkg is at http://sage.math.washington.edu/home/jason/matplotlib-0.98.3.p2.spkg\n\nThis spkg needs to be installed before the attached patch is applied.",
    "created_at": "2008-09-20T19:20:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3385#issuecomment-23696",
    "user": "jason"
}
```

I updated the matplotlib spkg to matplotlib-0.98.3.p2.spkg to include the SVN version of quiver.py that adds this keyword.  Everything seems to work great and tests pass in the plot directory.

The new spkg is at http://sage.math.washington.edu/home/jason/matplotlib-0.98.3.p2.spkg

This spkg needs to be installed before the attached patch is applied.



---

archive/issue_comments_023697.json:
```json
{
    "body": "Attachment [plot_vector_field_aspect_ratio.patch](tarball://root/attachments/some-uuid/ticket3385/plot_vector_field_aspect_ratio.patch) by jason created at 2008-09-20 19:21:58",
    "created_at": "2008-09-20T19:21:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3385#issuecomment-23697",
    "user": "jason"
}
```

Attachment [plot_vector_field_aspect_ratio.patch](tarball://root/attachments/some-uuid/ticket3385/plot_vector_field_aspect_ratio.patch) by jason created at 2008-09-20 19:21:58



---

archive/issue_comments_023698.json:
```json
{
    "body": "Nice work Jason! +1",
    "created_at": "2008-10-02T02:10:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3385#issuecomment-23698",
    "user": "mhansen"
}
```

Nice work Jason! +1



---

archive/issue_comments_023699.json:
```json
{
    "body": "Thanks!  efiring on the matplotlib team did the real work, though; he deserves the thanks.",
    "created_at": "2008-10-02T02:13:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3385#issuecomment-23699",
    "user": "jason"
}
```

Thanks!  efiring on the matplotlib team did the real work, though; he deserves the thanks.



---

archive/issue_comments_023700.json:
```json
{
    "body": "I see mhansen already reviewed this, but as I was the first to complain, I feel like I should too. :)\n\nI am embarrassed to admit, though, that I don't know how to install the manually-downloaded `.spkg` file. I know it's just a `tar.bz2` file and so on, but what's the proper way to install it?",
    "created_at": "2008-10-02T02:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3385#issuecomment-23700",
    "user": "ddrake"
}
```

I see mhansen already reviewed this, but as I was the first to complain, I feel like I should too. :)

I am embarrassed to admit, though, that I don't know how to install the manually-downloaded `.spkg` file. I know it's just a `tar.bz2` file and so on, but what's the proper way to install it?



---

archive/issue_comments_023701.json:
```json
{
    "body": "Dan,\n\nJust do \"sage -f <file-name>.spkg\"\n\nThat forces an install of the spkg.",
    "created_at": "2008-10-02T02:20:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3385#issuecomment-23701",
    "user": "jason"
}
```

Dan,

Just do "sage -f <file-name>.spkg"

That forces an install of the spkg.



---

archive/issue_comments_023702.json:
```json
{
    "body": "To answer some inquiries about patch conflicts, this patch depends on #4103 (in 3.1.3alpha0) and #4104 (in 3.1.3alpha0), in that order.\n\nSorry for not noting that.",
    "created_at": "2008-10-02T02:36:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3385#issuecomment-23702",
    "user": "jason"
}
```

To answer some inquiries about patch conflicts, this patch depends on #4103 (in 3.1.3alpha0) and #4104 (in 3.1.3alpha0), in that order.

Sorry for not noting that.



---

archive/issue_comments_023703.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-02T08:32:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3385#issuecomment-23703",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_023704.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha3",
    "created_at": "2008-10-02T08:32:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3385#issuecomment-23704",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.alpha3
