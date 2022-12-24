# Issue 3825: 2d-plots has no functionality for grid lines

archive/issues_003825.json:
```json
{
    "body": "Assignee: @saliola\n\nIt would be nice to be able to add grids to 2d plots in Sage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3825\n\n",
    "created_at": "2008-08-12T22:11:38Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "2d-plots has no functionality for grid lines",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3825",
    "user": "@saliola"
}
```
Assignee: @saliola

It would be nice to be able to add grids to 2d plots in Sage.

Issue created by migration from https://trac.sagemath.org/ticket/3825





---

archive/issue_comments_027204.json:
```json
{
    "body": "Attachment [trac_3825-gridlines.patch](tarball://root/attachments/some-uuid/ticket3825/trac_3825-gridlines.patch) by @saliola created at 2008-08-12 23:30:09",
    "created_at": "2008-08-12T23:30:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3825#issuecomment-27204",
    "user": "@saliola"
}
```

Attachment [trac_3825-gridlines.patch](tarball://root/attachments/some-uuid/ticket3825/trac_3825-gridlines.patch) by @saliola created at 2008-08-12 23:30:09



---

archive/issue_comments_027205.json:
```json
{
    "body": "Here is a patch. Based on code by S\u00e9bastien Labb\u00e9, so give him credit as well please.",
    "created_at": "2008-08-12T23:33:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3825#issuecomment-27205",
    "user": "@saliola"
}
```

Here is a patch. Based on code by Sébastien Labbé, so give him credit as well please.



---

archive/issue_comments_027206.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-08-13T01:55:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3825#issuecomment-27206",
    "user": "@saliola"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_027207.json:
```json
{
    "body": "REVIEW:\n\n* The gridlines option docstring in show is not nicely aligned like all the other ones; they also look like a mess in ClassGridLines:\n\n```\n...\n            axes         -- (default: True)\n            axes_labels  -- (default: None) list (or tuple) of two strings;\n                            the first is used as the label for the horizontal\n                            axis, and the second for the vertical axis.\n            fontsize     -- (default: current setting -- 10) positive\n                            integer; used for axes labels; if you make\n                            this very large, you may have to increase\n                            figsize to see all labels.\n            frame        -- (default: False) draw a frame around the image\n            gridlines -- (default: None) can be any one of the following:\n                None, False -- do not add grid lines\n                True, \"automatic\", \"major\" -- add grid at major ticks\n                    of axes\n                \"minor\" -- add grid at major and minor ticks of axes\n                [xlist,ylist] -- a tuple or list containing two elements,\n                    where xlist (or ylist) can be any of the following:\n                    None, False -- don't add horizontal (or vertical) lines\n                    True, \"automatic\", \"major\" -- add horizontal (or\n                        vertical) grid lines at the major ticks of axes\n                    \"minor\" -- add horizontal (or vertical) grid lines\n                        at major and minor ticks of axes\n                    iterable yielding numbers n or pairs (n,opts) where\n                        n is the coordinate of the line and opt is a\n                        dictionary of MATPLOTLIB options for rendering the\n                        line.\n```\n\n\n* This works:\n\n```\n            sage: f = lambda x,y: sin(x^2 + y^2)*cos(x)*sin(y)\n            sage: c = contour_plot(f, (-4, 4), (-4, 4), plot_points=15)\n            sage: c.show(gridlines=True, gridlinesstyle={'linestyle':'--','linewidth':1, 'color':'red'})\n```\n\nbut this doesn't:\n\n```\n            sage: f = lambda x,y: sin(x^2 + y^2)*cos(x)*sin(y)\n            sage: c = contour_plot(f, (-4, 4), (-4, 4), plot_points=15)\n            sage: c.show(gridlines=True, gridlinesstyle={'linestyle':'--','linewidth':1, 'rgbcolor':'red'})\n```\n\nBasically rgbcolor is annoyingly a synonym for color everywhere.  But it should be supported.\n\n* In fact, \n\n```\nline([(0,0), (1,2)], color='red')\n```\n\nlamely doesn't even work (though I hope somebody posts a patch to fix this).\n\n* For completeness can you add INPUT: and OUTPUT: blocks to\n\n```\n \t636\t    def add_gridlines(self, subplot, xmin, xmax, ymin, ymax, frame=False): \n \t637\t        # Process the input to get valid gridline data. \n \t638\t        r\"\"\" \n \t639\t        Add the grid lines to a subplot object. \n \t640\t \n```\n\n\nJust make the above very minor polish as a subsequent patch to yours and ... POSITIVE REVIEW.",
    "created_at": "2008-08-13T04:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3825#issuecomment-27207",
    "user": "@williamstein"
}
```

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

archive/issue_comments_027208.json:
```json
{
    "body": "Cleaned up the docstring (in both places).\n\n```\n            fontsize     -- (default: current setting -- 10) positive\n                            integer; used for axes labels; if you make\n                            this very large, you may have to increase\n                            figsize to see all labels.\n            frame        -- (default: False) draw a frame around the image\n            gridlines    -- (default: None) can be any of the following:\n                            1. None, False: do not add grid lines.\n                            2. True, \"automatic\", \"major\": add grid lines\n                               at major ticks of the axes.\n                            3. \"minor\": add grid at major and minor ticks.\n                            4. [xlist,ylist]: a tuple or list containing\n                               two elements, where xlist (or ylist) can be\n                               any of the following.\n                               4a. None, False: don't add horizontal (or\n                                   vertical) lines.\n                               4b. True, \"automatic\", \"major\": add\n                                   horizontal (or vertical) grid lines at\n                                   the major ticks of the axes.\n                               4c. \"minor\": add horizontal (or vertical)\n                                   grid lines at major and minor ticks of\n                                   axes.\n                               4d. an iterable yielding numbers n or pairs\n                                   (n,opts), where n is the coordinate of\n                                   the line and opt is a dictionary of\n                                   MATPLOTLIB options for rendering the\n                                   line.\n            gridlinesstyle,\n            hgridlinesstyle,\n            vgridlinesstyle \n                         -- (default: None) a dictionary of MATPLOTLIB\n                            options for the rendering of the grid lines,\n                            the horizontal grid lines or the vertical grid\n                            lines, respectively.\n```\n\n\nSupport for rgbcolor added; both examples work; changed some of the color keywords in the doctests to rgbcolor so it gets tested.\n\nAdded INPUT and OUTPUT blocks.",
    "created_at": "2008-08-13T06:52:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3825#issuecomment-27208",
    "user": "@saliola"
}
```

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

archive/issue_comments_027209.json:
```json
{
    "body": "patch with changes made after review",
    "created_at": "2008-08-13T06:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3825#issuecomment-27209",
    "user": "@saliola"
}
```

patch with changes made after review



---

archive/issue_comments_027210.json:
```json
{
    "body": "Attachment [trac_3825-gridlines-2.patch](tarball://root/attachments/some-uuid/ticket3825/trac_3825-gridlines-2.patch) by @saliola created at 2008-08-13 06:58:23",
    "created_at": "2008-08-13T06:58:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3825#issuecomment-27210",
    "user": "@saliola"
}
```

Attachment [trac_3825-gridlines-2.patch](tarball://root/attachments/some-uuid/ticket3825/trac_3825-gridlines-2.patch) by @saliola created at 2008-08-13 06:58:23



---

archive/issue_comments_027211.json:
```json
{
    "body": "Looks good now.",
    "created_at": "2008-08-14T03:34:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3825#issuecomment-27211",
    "user": "@williamstein"
}
```

Looks good now.



---

archive/issue_comments_027212.json:
```json
{
    "body": "Unfortunately this patch needs to be rebased against 3.1.rc0:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.rc0/devel/sage$ patch -p1 < trac_3813-anakha-adaptive-plot-v3.patch \npatching file sage/plot/plot.py\nHunk #1 succeeded at 3449 (offset 35 lines).\nHunk #2 succeeded at 3504 (offset 35 lines).\nHunk #3 succeeded at 3531 (offset 35 lines).\nHunk #4 succeeded at 3599 (offset 35 lines).\nHunk #5 succeeded at 3679 (offset 46 lines).\nHunk #6 FAILED at 3704.\nHunk #7 FAILED at 4536.\n2 out of 7 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej\n```\n",
    "created_at": "2008-08-15T06:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3825#issuecomment-27212",
    "user": "mabshoff"
}
```

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

archive/issue_comments_027213.json:
```json
{
    "body": "Opps, the above was meant for #3813. The two patches on this ticket do apply cleanly.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-15T06:26:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3825#issuecomment-27213",
    "user": "mabshoff"
}
```

Opps, the above was meant for #3813. The two patches on this ticket do apply cleanly.

Cheers,

Michael



---

archive/issue_comments_027214.json:
```json
{
    "body": "Merged trac_3825-gridlines.patch and trac_3825-gridlines-2.patch in Sage 3.1.rc0",
    "created_at": "2008-08-15T06:51:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3825#issuecomment-27214",
    "user": "mabshoff"
}
```

Merged trac_3825-gridlines.patch and trac_3825-gridlines-2.patch in Sage 3.1.rc0



---

archive/issue_comments_027215.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-15T06:51:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3825#issuecomment-27215",
    "user": "mabshoff"
}
```

Resolution: fixed
