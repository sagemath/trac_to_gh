# Issue 3825: 2d-plots has no functionality for grid lines

Issue created by migration from https://trac.sagemath.org/ticket/3825

Original creator: saliola

Original creation time: 2008-08-12 22:11:38

Assignee: saliola

It would be nice to be able to add grids to 2d plots in Sage.


---

Attachment


---

Comment by saliola created at 2008-08-12 23:33:32

Here is a patch. Based on code by Sébastien Labbé, so give him credit as well please.


---

Comment by saliola created at 2008-08-13 01:55:33

Changing type from defect to enhancement.


---

Comment by was created at 2008-08-13 04:22:15

REVIEW:

 * The gridlines option docstring in show is not nicely aligned like all the other ones; they also look like a mess in ClassGridLines:

```
...
            axes         -- (default: True)
            axes_labels  -- (default: None) list (or tuple) of two strings;
                            the first is used as the label for the horizontal
                            axis, and the second for the vertical axis.
            fontsize     -- (default: current setting -- 10) positive
                            integer; used for axes labels; if you make
                            this very large, you may have to increase
                            figsize to see all labels.
            frame        -- (default: False) draw a frame around the image
            gridlines -- (default: None) can be any one of the following:
                None, False -- do not add grid lines
                True, "automatic", "major" -- add grid at major ticks
                    of axes
                "minor" -- add grid at major and minor ticks of axes
                [xlist,ylist] -- a tuple or list containing two elements,
                    where xlist (or ylist) can be any of the following:
                    None, False -- don't add horizontal (or vertical) lines
                    True, "automatic", "major" -- add horizontal (or
                        vertical) grid lines at the major ticks of axes
                    "minor" -- add horizontal (or vertical) grid lines
                        at major and minor ticks of axes
                    iterable yielding numbers n or pairs (n,opts) where
                        n is the coordinate of the line and opt is a
                        dictionary of MATPLOTLIB options for rendering the
                        line.
```


 * This works:

```
            sage: f = lambda x,y: sin(x^2 + y^2)*cos(x)*sin(y)
            sage: c = contour_plot(f, (-4, 4), (-4, 4), plot_points=15)
            sage: c.show(gridlines=True, gridlinesstyle={'linestyle':'--','linewidth':1, 'color':'red'})
```

but this doesn't:

```
            sage: f = lambda x,y: sin(x^2 + y^2)*cos(x)*sin(y)
            sage: c = contour_plot(f, (-4, 4), (-4, 4), plot_points=15)
            sage: c.show(gridlines=True, gridlinesstyle={'linestyle':'--','linewidth':1, 'rgbcolor':'red'})
```

Basically rgbcolor is annoyingly a synonym for color everywhere.  But it should be supported.

 * In fact, 

```
line([(0,0), (1,2)], color='red')
```

lamely doesn't even work (though I hope somebody posts a patch to fix this).

 * For completeness can you add INPUT: and OUTPUT: blocks to

```
 	636	    def add_gridlines(self, subplot, xmin, xmax, ymin, ymax, frame=False): 
 	637	        # Process the input to get valid gridline data. 
 	638	        r""" 
 	639	        Add the grid lines to a subplot object. 
 	640	 
```


Just make the above very minor polish as a subsequent patch to yours and ... POSITIVE REVIEW.


---

Comment by saliola created at 2008-08-13 06:52:31

Cleaned up the docstring (in both places).

```
            fontsize     -- (default: current setting -- 10) positive
                            integer; used for axes labels; if you make
                            this very large, you may have to increase
                            figsize to see all labels.
            frame        -- (default: False) draw a frame around the image
            gridlines    -- (default: None) can be any of the following:
                            1. None, False: do not add grid lines.
                            2. True, "automatic", "major": add grid lines
                               at major ticks of the axes.
                            3. "minor": add grid at major and minor ticks.
                            4. [xlist,ylist]: a tuple or list containing
                               two elements, where xlist (or ylist) can be
                               any of the following.
                               4a. None, False: don't add horizontal (or
                                   vertical) lines.
                               4b. True, "automatic", "major": add
                                   horizontal (or vertical) grid lines at
                                   the major ticks of the axes.
                               4c. "minor": add horizontal (or vertical)
                                   grid lines at major and minor ticks of
                                   axes.
                               4d. an iterable yielding numbers n or pairs
                                   (n,opts), where n is the coordinate of
                                   the line and opt is a dictionary of
                                   MATPLOTLIB options for rendering the
                                   line.
            gridlinesstyle,
            hgridlinesstyle,
            vgridlinesstyle 
                         -- (default: None) a dictionary of MATPLOTLIB
                            options for the rendering of the grid lines,
                            the horizontal grid lines or the vertical grid
                            lines, respectively.
```


Support for rgbcolor added; both examples work; changed some of the color keywords in the doctests to rgbcolor so it gets tested.

Added INPUT and OUTPUT blocks.


---

Comment by saliola created at 2008-08-13 06:53:34

patch with changes made after review


---

Attachment


---

Comment by was created at 2008-08-14 03:34:23

Looks good now.


---

Comment by mabshoff created at 2008-08-15 06:21:14

Unfortunately this patch needs to be rebased against 3.1.rc0:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.rc0/devel/sage$ patch -p1 < trac_3813-anakha-adaptive-plot-v3.patch 
patching file sage/plot/plot.py
Hunk #1 succeeded at 3449 (offset 35 lines).
Hunk #2 succeeded at 3504 (offset 35 lines).
Hunk #3 succeeded at 3531 (offset 35 lines).
Hunk #4 succeeded at 3599 (offset 35 lines).
Hunk #5 succeeded at 3679 (offset 46 lines).
Hunk #6 FAILED at 3704.
Hunk #7 FAILED at 4536.
2 out of 7 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej
```



---

Comment by mabshoff created at 2008-08-15 06:26:12

Opps, the above was meant for #3813. The two patches on this ticket do apply cleanly.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-15 06:51:43

Merged trac_3825-gridlines.patch and trac_3825-gridlines-2.patch in Sage 3.1.rc0


---

Comment by mabshoff created at 2008-08-15 06:51:43

Resolution: fixed
