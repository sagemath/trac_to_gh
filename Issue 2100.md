# Issue 2100: sensible defaults for aspect ratio

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-02-08 04:49:50

Assignee: was

CC:  kcrisman mhampton mpatel

If we are plotting a circle or sphere with circle.show(), we ought to see a circle and not have to manually specify the aspect ratio.  The aspect ratio should have sensible defaults that depend on the thing that is being plotted.


---

Comment by jason created at 2008-03-30 05:03:22

For reference, in Mathematica (see http://reference.wolfram.com/mathematica/ref/AspectRatio.html?q=AspectRatio&lang=en )

 * Graphics objects use Automatic aspect ratio
 * plot and listplot use 1/golden ratio
 * parametric plot uses automatic
 * contour plot uses aspect ratio of 1

Automatic is an aspect ratio determined by the pixels in the plot.  It does not distort the plot (i.e., circles are still circles).


---

Comment by mabshoff created at 2008-10-31 05:41:57

Jason,

didn't we fix this recently?

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-01-22 18:28:03

Changing type from defect to enhancement.


---

Comment by jason created at 2010-09-07 03:34:21

#9813 takes care of two cases of these.

Interestingly, from the above list, it seems like the golden ratio is only used for a minority of functions (i.e., "plot" and "list_plot").  So maybe we ought to change the global default to aspect_ratio=1 and just set plot and list_plot to have default golden ratio aspect ratios.


---

Comment by jason created at 2010-09-29 22:00:12

|                                 |                               |                                                                                                              |             |
|---------------------------------|-------------------------------|--------------------------------------------------------------------------------------------------------------|-------------|
| Matplotlib aspect ratio setting | Matplotlib adjustable setting | Mathematica [AspectRatio](http://trac.sagemath.org/sage_trac/search/opensearch?q=wiki%3AAspectRatio) setting | Explanation |
| 'auto' | doesn't seem to matter | Full | Make the current data limits fill the available sized box |
| 'equal' or 1 | 'box' | Automatic | Make each pixel be square (aspect ratio 1) |
| | | | |
It appears that specifying a number in matplotlib ('box' adjustable) makes the *pixels* have a certain height-to-width ratio (e.g., a circle in the picture will appear to have the given aspect ratio), but in Mathematica, a number specifies the overall ratio of the *image* height-to-width.  Thus the numbers are not directly comparable.

Plus, in matplotlib, you can have the 'datalim' be adjustable, which changes the data limits on your plot to make the pixels have a certain aspect ratio.


---

Comment by jason created at 2010-09-29 22:03:27

Matplotlib's fig_aspect seems to do the sort of thing that mma's aspect ratio number setting does:

!http://matplotlib.sourceforge.net/api/figure_api.html#matplotlib.figure.figaspect


---

Comment by jason created at 2010-09-29 22:32:14

One other note: setting bbox_inches='tight' in the savefig method seems to override the figure size specified.


---

Comment by jason created at 2010-09-30 02:46:58

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

Comment by jason created at 2010-09-30 03:09:38

Helpful matplotlib mailing list post (read the thread): !http://www.mail-archive.com/matplotlib-users`@`lists.sourceforge.net/msg15623.html


---

Comment by jason created at 2010-09-30 14:23:09

Moving the proposal up to the description so we can edit it.  Ignore the proposal in the comments now.


---

Comment by jason created at 2010-10-01 02:01:28

Update the proposal.


---

Comment by jason created at 2010-10-01 02:07:06

I've attached two files.  First, a work-in-progress rewrite of the aspect ratio stuff.  Second, the plot.py file before this patch was applied.  The plot.py file is the version from 4.6.alpha1 with tickets [#9740](http://trac.sagemath.org/sage_trac/search/opensearch?q=ticket%3A9740), [#9746](http://trac.sagemath.org/sage_trac/search/opensearch?q=ticket%3A9746), and [#4342](http://trac.sagemath.org/sage_trac/search/opensearch?q=ticket%3A4342) applied, in order.


---

Comment by jason created at 2010-10-01 02:11:15

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

Comment by jason created at 2010-10-01 02:11:15

Changing status from new to needs_work.


---

Comment by jason created at 2010-10-01 03:31:57

Also todo: set barchart and scatterplot to have default aspect ratios of 'auto'.


---

Comment by jason created at 2010-10-02 02:29:43

Replying to [comment:14 jason]:

> 
> Warning: this patch changes the definition of aspect_ratio.  Before, it was width/height, but now it is height/width.  The new meaning is consistent with matplotlib and Mathematica. Since the patch now changes a very fundamental thing about Sage (the meaning of aspect ratio), it probably should be put off until a major release.
> 

Apparently this statement isn't true.  The old aspect_ratio and new aspect_ratio mean the same thing.  I was basing the statement on reading the docs.  Either the current docs are backwards, or I was misreading them.

So, in short, things are good to go for finishing this patch and getting it into Sage as soon as possible.


---

Attachment

apply instead of previous patch


---

Comment by jason created at 2010-10-07 07:10:20

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-10-07 07:10:20

New patch revamping the aspect ratio calculations in Sage (and defaults!)


---

Comment by jason created at 2010-10-07 16:37:57

Updating description to reflect changes in the patch.


---

Comment by novoselt created at 2010-11-21 18:15:51

It seems to me that `set_aspect` ratio only accepts "auto" as a string input, while the proposal also lists "equal" as an option.

Would it be possible to extend the functionality so that it is possible to specify either only width or only height of the final figure? I am thinking of using it in conjunction with SageTeX, where it would be natural to ask either for `width=\textwidth` or `height=0.5\texthight` and have the second dimension determined automatically based on the actual plot and aspect ratio.


---

Comment by novoselt created at 2010-11-21 18:24:06

New functions `pad_for_tick_labels` and `adjust_figure_to_contain_bbox` are not completely documented.

Are #9740,  #9746, and  #4342 still prerequisites?


---

Comment by novoselt created at 2010-11-21 18:24:06

Changing status from needs_review to needs_work.


---

Comment by novoselt created at 2010-11-21 18:25:05

Oops, got the answer to the last question already, for some reason they were not crossed in the above comment.


---

Comment by jason created at 2011-01-12 21:43:56

This might be good bug-day fodder if people are already working on graphics code.


---

Comment by kcrisman created at 2011-01-14 13:26:08

I hope to take care of novoselt's comments - 'equal' and the documentation - today.  This will depend on #7981, #8632, #10244, and #10143.

> Would it be possible to extend the functionality so that it is possible to specify either only width or only height of the final figure? I am thinking of using it in conjunction with SageTeX, where it would be natural to ask either for `width=\textwidth` or `height=0.5\texthight` and have the second dimension determined automatically based on the actual plot and aspect ratio.

I think this is a good idea, but I don't think the people who might work on this will have time for it before bitrot sets in even further.  I have opened ticket #10633 for this.


---

Comment by kcrisman created at 2011-01-14 13:28:45

Rather impressively, only one of seven hunks failed in contour_plot.py, and only 5 of 34 hunks failed on plot.py. So rebasing this to the other recent graphics patches should be no problem, as well as the other documentation comments.


---

Comment by jason created at 2011-01-14 16:06:29

Let's just take the 'equal' option out of the proposal.  I think it's there just because that's what matplotlib does.


---

Comment by kcrisman created at 2011-01-14 16:09:12

I had to change a few things based on the new save() but otherwise nearly all is the same. It also turned out that fig_tight was never used in .matplotlib(), and in fact only can be passed to matplotlib's savefig(), so I treated it basically the same as transparent in .save().

I can also remove 'equal' if you want, that's fine.

Before I go ahead and update this, though, I have a question. The two functions not documented (`pad_for_tick_labels` and `adjust_figure_to_contain_bbox`) only are used in a commented-out line

```
            # this messes up the aspect ratio!
            #figure.canvas.mpl_connect('draw_event', pad_for_tick_labels)
```

So... should they even be included at this time?


---

Comment by kcrisman created at 2011-01-17 17:25:15

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

Comment by kcrisman created at 2011-01-17 19:03:27

> > So... should they even be included at this time?
> Quote from Jason: "Feel free to move those functions to another ticket if they are really not called from anywhere.  I think they are leftovers from experimentation, so probably not strictly needed (especially if they really aren't called or used from anywhere)."
Since I didn't really know where these should be used, or what the context was, I decided to just leave them in but fully commented out, with an admonition to add documentation if they ever get used again.  (This would also make it easier for a future developer to use them, inter alia.)

Getting some doctest failures, though, related to this:

```
sage -t  devel/sage/sage/plot/plot3d/plot_field3d.py # 6 doctests failed
```

I doubt this will be hard to resolve.  Anyway, just status updates...


---

Attachment

Rebase to 4.6.1/4.6.2.alpha0


---

Comment by kcrisman created at 2011-01-17 20:17:54

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

Comment by kcrisman created at 2011-01-17 20:17:54

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2011-01-18 15:45:37

> I think this change might need review (?) so I'm setting to 'needs review'.

Oh yeah, and I never actually looked at very many of the plots.  Definitely still needs review ;) of the pictures and the (small) reviewer patch.


---

Comment by novoselt created at 2011-01-18 22:53:00

Depends on #10143

(others are "inherited")


---

Comment by novoselt created at 2011-01-19 03:45:25

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

Comment by novoselt created at 2011-01-19 03:45:25

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-01-19 03:51:59

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

Comment by novoselt created at 2011-01-19 04:01:36

Changing status from positive_review to needs_work.


---

Comment by novoselt created at 2011-01-19 04:01:36

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

Comment by novoselt created at 2011-01-19 04:29:05

Yes, the problem I hit is exactly #9744 (which actually mentions the same example from the documentation), thanks for pointing it out.


---

Comment by kcrisman created at 2011-01-19 13:30:15

Replying to [comment:36 novoselt]:
> Actually, I was too hasty: 
> sage -t -long "devel/sage-main/sage/modules/free_module_element.pyx"
Aargh!  I'll try to fix this...
> These are the only errors on the whole library. I guess they should be fixed in the same way as in the reviewer patch. Or maybe there should be a better fix?..
No, that is the correct fix for now.   An overarching ticket is #10638, which I forgot to mention before.


---

Comment by kcrisman created at 2011-01-19 13:35:18

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

Comment by kcrisman created at 2011-01-19 19:24:36

> > > These are the only errors on the whole library. I guess they should be fixed in the same way as in the reviewer patch. Or maybe there should be a better fix?..
> > No, that is the correct fix for now.   An overarching ticket is #10638, which I forgot to mention before.
Okay, now I am not rushing out the door and can think straight.  The problem is that this was never doctesting the thing in question in the first place because of the issues raised in #10638.  

I _think_ the issue is that `_extract_kwds_for_show` keeps the ``@`options` value of `aspect_ratio='auto') in play; when this gets passed to the `show()` method of `Line` (which is what `line3d` creates in this case), it refers to the one in `base.PrimitiveObject`, which unfortunately then puts this value of `aspect_ratio` in:

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

Comment by novoselt created at 2011-01-19 19:47:05

I like `auto` more than `automatic`, so I don't want to change it.

Can we maybe change it the other way? Was `automatic` documented/used somewhere before?


---

Comment by kcrisman created at 2011-01-19 20:10:19

> I like `auto` more than `automatic`, so I don't want to change it.
Agreed, but...
> Can we maybe change it the other way? Was `automatic` documented/used somewhere before?
Yes, this is the standard 3D option.  See [this reference manual page](http://www.sagemath.org/doc/reference/sage/plot/plot3d/base.html#sage.plot.plot3d.base.Graphics3d.show) for plot/plot3d/base.pyx.

Of course, it would be possible to change the plot3d case to also accept 'auto' easily enough - in fact, that's essentially what I've done in my latest patch - and one could change the documentation accordingly.  But we couldn't remove it without a deprecation period - and in my mind it's pointless to go to the trouble, given that it's mostly a default so we could change things without even needing to deprecate that option.


---

Comment by novoselt created at 2011-01-19 20:16:16

I guess then changing to `automatic` is OK.

For consistency, it would be nice if the same variant was used throughout Sage, but then again the point is that this value should not be specified explicitly by the user.


---

Comment by kcrisman created at 2011-01-19 20:21:13

Replying to [comment:43 novoselt]:
> I guess then changing to `automatic` is OK.
I'd want to run that by Jason (the original author) first, though - after all, the point below would suggest it doesn't matter (and it is a long process for me to rebase, sadly).
> For consistency, it would be nice if the same variant was used throughout Sage, but then again the point is that this value should not be specified explicitly by the user.


---

Comment by kcrisman created at 2011-01-19 20:32:26

> > I guess then changing to `automatic` is OK.
> I'd want to run that by Jason (the original author) first, though - after all, the point below would suggest it doesn't matter (and it is a long process for me to rebase, sadly).
One reason being that matplotlib uses 'auto', and consistency with that is nice as well.
> > For consistency, it would be nice if the same variant was used throughout Sage, but then again the point is that this value should not be specified explicitly by the user.


---

Comment by kcrisman created at 2011-01-19 20:36:07

Okay, this latest reviewer patch should fix the things we've talked about in a minimalist way.  It doesn't resolve the 'auto' versus 'automatic' issue.  No new instructions for applying patches.  Documentation also looks good with this change.


---

Comment by kcrisman created at 2011-01-19 20:36:07

Changing status from needs_work to needs_review.


---

Attachment

reviewer patch


---

Comment by jason created at 2011-01-19 21:24:13

Wow, great job tracking down this subtle problem.  I personally slightly prefer `'auto'` over `'automatic'` because it's consistent with matplotlib and it's shorter.  However, I agree that users will probably not specify it too frequently, so `'automatic'` would probably be fine as well.  If we do make the default `'automatic'`, then I think we'll have to convert it to `'auto'` before passing it to matplotlib.

Another data point: mma uses Automatic (not Auto): http://reference.wolfram.com/mathematica/ref/Automatic.html


---

Comment by kcrisman created at 2011-01-19 21:31:43

Replying to [comment:48 jason]:
> Wow, great job tracking down this subtle problem.  I personally slightly prefer `'auto'` over `'automatic'` because it's consistent with matplotlib and it's shorter.  However, I agree that users will probably not specify it too frequently, so `'automatic'` would probably be fine as well.  
Thanks.  I don't have any more time today to work on this, but I think then I vote for `'automatic'` for consistency, and having `'auto'` as one that secretly also works :) 
> If we do make the default `'automatic'`, then I think we'll have to convert it to `'auto'` before passing it to matplotlib.
Yes, I realize that.  I don't think that will be very difficult, since there seems to be only one place this is passed.


---

Comment by kcrisman created at 2011-01-21 13:28:06

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2011-01-21 13:28:06

Okay, putting this to 'needs work' in order to fix this.  Hopefully today or this weekend; it won't be hard, just have to do it.


---

Comment by kcrisman created at 2011-02-08 18:01:18

Oops... hmm, I gave myself one long weekend.  I'll try to see if this still applies to 4.6.2.alpha4 soon.


---

Comment by kcrisman created at 2011-02-14 19:47:27

All still applies to 4.6.2.alpha4.  I hope to conclude this adventure shortly, by replacing the reviewer patch with one that deals with the automatic/auto issue uniformly.


---

Comment by kcrisman created at 2011-02-15 03:01:20

This should all work fine now.  I do want to point out that the standard plots seem to have increased somewhat in size.  The new reviewer patch is now different enough that it needs review.  Please do so now to avoid bitrot!


---

Comment by kcrisman created at 2011-02-15 03:01:20

Changing status from needs_work to needs_review.


---

Comment by jason created at 2011-02-15 03:08:24

Replying to [comment:53 kcrisman]:
> This should all work fine now.  I do want to point out that the standard plots seem to have increased somewhat in size.

Yes, I reverted things to the matplotlib defaults.  Before, we made the ratio of height/width the golden ratio, but now it is the standard matplotlib default (which I believe is 4:3, which matches computer screens better anyway).


---

Comment by jason created at 2011-02-15 03:09:25

Changing assignee from was to jason.


---

Comment by jason created at 2011-02-15 03:09:25

Can you add instructions for reviewers/patchbot about which patches should be applied in what order?


---

Comment by jason created at 2011-02-15 03:09:59

(and then I'll try to review this tonight or tomorrow)


---

Comment by kcrisman created at 2011-02-15 03:11:22

See the description. I guess I didn't make it obvious enough :)

Apply [trac_2100-aspect-ratio-rebase.patch] and [trac_2100-auto-automatic-and-vector.patch] for this.


---

Comment by kcrisman created at 2011-02-15 03:12:12

Apply [trac_2100-aspect-ratio-rebase.patch trac_2100-aspect-ratio-rebase.patch] and [trac_2100-auto-automatic-and-vector.patch trac_2100-auto-automatic-and-vector.patch] for this.


---

Comment by kcrisman created at 2011-02-15 03:12:31

I can't get the links to work for some reason - sorry.


---

Comment by kcrisman created at 2011-02-16 17:17:43

To patchbot/reviewers: Apply attachment:trac_2100-aspect-ratio-rebase.patch and attachment:trac_2100-auto-automatic-and-vector.patch


---

Comment by kcrisman created at 2011-02-19 04:20:10

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

Comment by kcrisman created at 2011-02-19 04:21:35

What this plot looks like before #2100


---

Attachment

What this plot looks like after #2100


---

Comment by kcrisman created at 2011-02-19 04:24:04

Changing status from needs_review to needs_info.


---

Comment by kcrisman created at 2011-02-19 04:24:04

The issue is of course that I never used `plot()` to do this, but rather only `line()` and `point()` and `Graphics()`.  The default aspect ratio seems to have changed a lot, and so not only are the labels on the left totally squished, but it just looks bad.  Maybe mpl defaults aren't that great?  Or is this a pretty unusual scenario?

Anyway, putting as needs info until I know what is happening here from someone who knows more about mpl (e.g., Jason).  So frustrating, too, because we should have this in!


---

Comment by jason created at 2011-02-19 04:54:43

Yep, I think the problem here is that line and point now default to have aspect_ratio=1, so the y and x axis are drawn at equal scales.  Try setting the aspect_ratio to 'auto' (or whatever your patch does now).

plot() defaults to 'auto' aspect ratio (e.g., fill the figure).  However, geometric figures like line and point default to aspect_ratio=1.


---

Comment by kcrisman created at 2011-03-05 02:52:15

I think perhaps we should make line (and point?) default to 'auto'?  Because one is quite likely to have a line do a function, as opposed to other geometric figures.  And points are often used to shadow functions.

Any other thoughts on this?  It would be really nice to finally get this in 4.7 - maybe you can take a quick look over spring break?


---

Comment by kcrisman created at 2011-03-05 02:53:01

Putting needs review, though may need a minor change because of the thing in the last two comments.


---

Comment by kcrisman created at 2011-03-05 02:53:01

Changing status from needs_info to needs_review.


---

Comment by kcrisman created at 2011-06-15 19:34:36

Okay, I'm going to refresh so that line and point still have 'auto'.  Needs review!


---

Comment by kcrisman created at 2011-06-15 19:34:36

Changing keywords from "" to "sd31".


---

Comment by ryan created at 2011-06-16 22:46:49

FYI, I am currently reviewing this patch


---

Comment by ryan created at 2011-06-16 23:47:35

Patch looks good.  Confirmed that kcrisman's code looks 'good' after the patch too :)  Positive Review. Great job guys.

Note: I do get doctest failures on plot_field.py, but the failures are not caused by the patches to this ticket.


---

Comment by ryan created at 2011-06-16 23:47:35

Changing status from needs_review to positive_review.


---

Comment by novoselt created at 2011-06-16 23:51:30

Replying to [comment:68 ryan]:
> Note: I do get doctest failures on plot_field.py, but the failures are not caused by the patches to this ticket.

What exactly do you mean by this? That a clean public release of Sage has doctest failures in `plot_field.py`?


---

Comment by kcrisman created at 2011-06-17 00:13:02

Correct - or to be more precise, warnings that do not cause the doctest to fail.  They are known, and not from Sage.


---

Comment by jdemeyer created at 2011-06-18 10:11:54

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-06-18 10:11:54

Please rebase this patch to be applied on top of #11491.


---

Comment by kcrisman created at 2011-06-20 14:45:19

Replying to [comment:72 jdemeyer]:
> Please rebase this patch to be applied on top of #11491.

Thanks - another rebase where a major improvement takes second rank to a trivial adjustment.  Especially since Ryan and I were involved on both tickets, it would have been nice to ask first.   Rebasing is not so trivial for the setups some of us have.

But no point crying over spilt milk.  Sigh... patches coming up.


---

Attachment

Apply after rebase patch


---

Comment by kcrisman created at 2011-06-20 14:48:42

Okay, _now_ we should hopefully be at positive review!


---

Comment by kcrisman created at 2011-06-20 14:48:42

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2011-06-20 15:17:41

Replying to [comment:73 kcrisman]:
> Especially since Ryan and I were involved on both tickets, it would have been nice to ask first.

I have done that in the past and *people complained*: [http://groups.google.com/group/sage-devel/browse_frm/thread/abd5fb944769e052/8e4057172b97f2e5](http://groups.google.com/group/sage-devel/browse_frm/thread/abd5fb944769e052/8e4057172b97f2e5)


---

Comment by kcrisman created at 2011-06-20 15:26:04

Right, and my point is that this sort of feels the same way.   I am *not* suggesting unmerging something positively reviewed - definitely not the direction I'm going.

What I'm suggesting (and only suggesting, because I can only imagine how much work release management is) is that perhaps sending a ping via Trac on two closely related tickets which have some overlap would be good _before_ deciding which one to merge first.  Especially since in this case #11491 is so clearly much more trivial than this one, and also much older.    I'm sure Ryan and I would have agreed that this one was higher priority.

Anyway, it turned out I had time for fixing it - it was a very small overlap, luckily.  Thanks for all the hard work; the final releases really are noticeably more polished nowadays, and it's a great thing.


---

Comment by jdemeyer created at 2011-06-20 15:34:25

Replying to [comment:76 kcrisman]:
> Right, and my point is that this sort of feels the same way.   I am *not* suggesting unmerging something positively reviewed - definitely not the direction I'm going.
> 
> What I'm suggesting (and only suggesting, because I can only imagine how much work release management is) is that perhaps sending a ping via Trac on two closely related tickets which have some overlap would be good _before_ deciding which one to merge first.  Especially since in this case #11491 is so clearly much more trivial than this one, and also much older.    I'm sure Ryan and I would have agreed that this one was higher priority.

It is not easy for me to determine a priori which patches conflict with eachother, so what you propose isn't really possible.  It's not that I looked at both patches and decided which one to merge.  What happened is that I already decided to merge #11491 before I even considered the patch here.

Since the sage-devel discussion I mentioned, there is an agreement that once a patch is merged (even in a future alpha version), it should stay merged if possible.


---

Comment by jdemeyer created at 2011-06-20 15:35:27

Replying to [comment:76 kcrisman]:
> Thanks for all the hard work; the final releases really are noticeably more polished nowadays, and it's a great thing.
You should really also thank Mitesh Patel for managing the [buildbot](http://build.sagemath.org/sage/waterfall).


---

Comment by kcrisman created at 2011-06-20 15:44:33

> It is not easy for me to determine a priori which patches conflict with eachother, so what you propose isn't really possible.  It's not that I looked at both patches and decided which one to merge.  What happened is that I already decided to merge #11491 before I even considered the patch here.

Understood.

> Since the sage-devel discussion I mentioned, there is an agreement that once a patch is merged (even in a future alpha version), it should stay merged if possible.

Yes, that definitely makes sense, as I hope I make clear above.  :)


---

Comment by jdemeyer created at 2011-07-22 12:48:14

Resolution: fixed
