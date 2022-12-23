# Issue 8368: add colorbar option to contour_plots

Issue created by migration from https://trac.sagemath.org/ticket/8368

Original creator: jason

Original creation time: 2010-02-25 19:15:12

Assignee: was

CC:  kcrisman wcauchois robert.marik

This patch adds the option of creating a color bar on a filled contour plot.  See the doctests in the patch for examples.


---

Comment by jason created at 2010-02-25 19:17:17

This ticket depends on #8366.


---

Comment by jason created at 2010-02-25 19:17:17

Changing status from new to needs_review.


---

Comment by jason created at 2010-02-25 19:43:37

(update makes colorbars work even when fill=False)


---

Comment by mhampton created at 2010-04-04 04:05:44

One thing I don't like about this is that you can't easily get a 1:1 aspect ratio plot - using figsize = [a,a] makes the overall figure square but not the plotted region.


---

Comment by jason created at 2010-04-15 03:34:02

Replying to [comment:4 mhampton]:
> One thing I don't like about this is that you can't easily get a 1:1 aspect ratio plot - using figsize = [a,a] makes the overall figure square but not the plotted region.

Of course.  If you want the aspect ratio to be 1, then use the aspect_ratio=1 argument, which controls the aspect ratio.  The figsize option controls the "figure size", i.e., the size of the entire figure.


---

Comment by jason created at 2010-04-15 03:35:52

apply instead of previous patch (rebased for the new #8366)


---

Attachment

Replying to [comment:5 jason]:
> Replying to [comment:4 mhampton]:
> > One thing I don't like about this is that you can't easily get a 1:1 aspect ratio plot - using figsize = [a,a] makes the overall figure square but not the plotted region.
> 
> Of course.  If you want the aspect ratio to be 1, then use the aspect_ratio=1 argument, which controls the aspect ratio.  The figsize option controls the "figure size", i.e., the size of the entire figure.

OK.  I think I got into the habit of using figsize before aspect_ratio worked.  I will check the rebased version as soon as I can.


---

Comment by robert.marik created at 2010-04-16 11:02:52

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

Comment by jason created at 2010-04-16 11:56:09

apply on top of previous patch


---

Attachment

I fixed both issues in the above patch.

I also doctested contour_plot.py this time!  Things should work now.


---

Comment by robert.marik created at 2010-04-21 17:23:11

Changing status from needs_review to positive_review.


---

Comment by robert.marik created at 2010-04-21 17:23:11

Installs fine, works as excpected, tests passed now, documentation builds fine, positive review and thanks for adding this feature, as well as including my comments.

Positive review.

Release manager: Apply both trac-8368-colorbars.patch and trac-8368-fix-options.patch patches.


---

Comment by jhpalmieri created at 2010-04-23 17:11:16

Merged into 4.4.alpha2:
 - trac-8368-colorbars.patch
 - trac-8368-fix-options.patch


---

Comment by jhpalmieri created at 2010-04-23 17:11:16

Resolution: fixed
