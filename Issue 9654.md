# Issue 9654: implicit_plot does not accept color or rgbcolor as keywords

Issue created by migration from Trac.

Original creator: olazo

Original creation time: 2010-08-01 01:35:14

Assignee: olazo

CC:  kcrisman

Both

`implicit_plot(x^2 +  y^2-1,(x,-1,1),(y,-1,1),aspect_ratio=1,color='red')`

and

`implicit_plot(x^2 +  y^2-1,(x,-1,1),(y,-1,1),aspect_ratio=1,color='red')`

do not produce a red circle as would be expected. matplotlib's cmap options don't get it quite good.


---

Comment by olazo created at 2010-08-01 01:36:48

Changing keywords from "" to "implicit_plot".


---

Comment by jason created at 2010-08-14 08:41:06

Solved by #8529.


---

Comment by kcrisman created at 2011-04-20 03:01:25

Not quite.  `color` is ok, apparently not `rgbcolor`.

```
implicit_plot(x^2+y^2 == 2, (x,-3,3), (y,-3,3), rgbcolor=(0,1,0))
verbose 0 (138: primitive.py, options) WARNING: Ignoring option
'rgbcolor'=(0, 1, 0)
verbose 0 (138: primitive.py, options) 
The allowed options for ContourPlot defined by a 150 x 150 data grid
are:
    cmap           the name of a predefined colormap, 
                        a list of colors, or an instance of a 
                        matplotlib Colormap. Type: import matplotlib.cm;
matplotlib.cm.datad.keys()
                        for available colormap names.
    colorbar       Include a colorbar indicating the levels             

    colorbar_optionsa dictionary of options for colorbars               

    contours       Either an integer specifying the number of 
                        contour levels, or a sequence of numbers giving
                        the actual contours to use.
    fill           Fill contours or not                                 

    label_options  a dictionary of options for the labels               

    labels         show line labels or not                              

    legend_label   The label for this item in the legend.               

    linestyles     the style of the lines to be plotted                 

    linewidths     the width of the lines to be plotted                 

    plot_points    How many points to use for plotting precision        

    zorder         The layer level in which to draw   
```



---

Comment by kcrisman created at 2011-06-14 05:21:56

The right way to do this is to use `get_cmap`, but it's tricky to avoid some kind of weird circularity.


---

Comment by paulmasson created at 2016-07-04 20:47:04

This appears to be a simple fix for this issue. Do I need to add anything more than the doctest?
----
New commits:


---

Comment by paulmasson created at 2016-07-04 20:47:04

Changing status from new to needs_review.


---

Comment by tscrim created at 2016-07-05 06:42:51

You should raise an error if both `color` and `rgbcolor` are given akin to

```
sage: x,y = var('x,y')
sage: plot(x^2 - 2, rgbcolor=(0,1,0), color='red')
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
...
RuntimeError: Error in line(): option 'color' not valid.
```

Although I think `RuntimeError` is not the correct error, nor should `plot` go through so much to error out either. However that is a separate issue. The correct error is a `ValueError` in this situation.


---

Comment by paulmasson created at 2016-07-05 23:09:08

I've updated the branch to raise a `ValueError` for conflicting input, as well as added a doctest.

The error in `plot.py` appears to arise from this line:


```
`@`rename_keyword(color='rgbcolor')
```


Once we agree on how to handle the two arguments here, I can remove that line and update the code accordingly.


---

Comment by tscrim created at 2016-07-06 21:19:13

Replying to [comment:13 paulmasson]:
> I've updated the branch to raise a `ValueError` for conflicting input, as well as added a doctest.

Thanks. Looks good.

> The error in `plot.py` appears to arise from this line:
> 
> {{{
> `@`rename_keyword(color='rgbcolor')
> }}}
> 
> Once we agree on how to handle the two arguments here, I can remove that line and update the code accordingly.

Which error where? I don't see any doctest failures.
----
New commits:


---

Comment by paulmasson created at 2016-07-06 21:30:32

Replying to [comment:14 tscrim]:
> Which error where? I don't see any doctest failures.
I was unclear: I meant the `RunTime` error arising from specifying both `color` and `rgbcolor`. Presumably it arises from trying to rename a keyword argument with a name that already exists.


---

Comment by tscrim created at 2016-07-07 06:45:43

Replying to [comment:15 paulmasson]:
> Replying to [comment:14 tscrim]:
> > Which error where? I don't see any doctest failures.
> I was unclear: I meant the `RunTime` error arising from specifying both `color` and `rgbcolor`. Presumably it arises from trying to rename a keyword argument with a name that already exists.

Ah, the one coming from using `plot`. Yes, the failure is probably due to that. However, that is something for a separate ticket. If you could add a doctest checking that both inputs is invalid, then I will be happy to set a positive review.


---

Comment by git created at 2016-07-07 21:31:13

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by paulmasson created at 2016-07-07 21:34:10

Done.


---

Comment by tscrim created at 2016-07-08 04:30:19

Thanks.


---

Comment by tscrim created at 2016-07-08 04:30:19

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2016-07-08 12:37:24

Changing status from positive_review to needs_work.


---

Comment by vbraun created at 2016-07-08 12:37:24

Merge conflict


---

Comment by git created at 2016-07-08 19:49:27

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-07-08 20:49:05

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by paulmasson created at 2016-07-08 20:51:20

Fixed merge conflict. Doctests all pass.

What is the protocol for this situation? Do I reset the positive review or wait for someone else? Thanks.


---

Comment by paulmasson created at 2016-07-08 20:51:20

Changing status from needs_work to needs_review.


---

Comment by vbraun created at 2016-07-08 21:17:30

Just set it back to positive review if its just a straightforward merge fix


---

Comment by vbraun created at 2016-07-08 21:17:30

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2016-07-09 16:29:15

Resolution: fixed
