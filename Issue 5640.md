# Issue 5640: no way to figure out list of colormaps from matrix plot's docstring

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-03-30 03:16:35

Assignee: was

This sentence, which is in the help for contour_plot, should also be in the help for the plot method on matrices:


```
                        cmap -- the name of
                        a predefined colormap, a list of colors
                        or an instance of a matplotlib Colormap.
                        Type: import matplotlib.cm; matplotlib.cm.datad.keys()
                        for available colormap names.
```


It should also be in the output here too:

```
sage: matrix(QQ,1,1).plot(cmap0=0)
          	

verbose 0 (84: primitive.py, options) WARNING: Ignoring option 'cmap0'=0
verbose 0 (84: primitive.py, options) 
The allowed options for MatrixPlot defined by a 1 x 1 data grid are:
    cmap           the name of a predefined colormap, 
                        a list of colors or an instance of a 
                        matplotlib Colormap.
    zorder         The layer level in which to draw                     
```



---

Comment by kcrisman created at 2009-06-20 01:10:04

Depends on #6269, at least potentially


---

Attachment

This should take care of the issue on the description.  Patch may depend on #6269; even though I can't find any specific instances where they overlap on code hunks, they do overlap in files, so better to be safe.  Note that this patch does not take care of #5083.  I have also added/improved documentation on the files in question.


---

Comment by kcrisman created at 2009-06-20 01:16:31

Changing assignee from was to kcrisman.


---

Comment by kcrisman created at 2009-06-20 01:16:31

Changing status from new to assigned.


---

Comment by mvngu created at 2009-06-24 22:15:57

Some hunk failures when applied against Sage 4.1.alpha0:

```
sage: hg_sage.apply("http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5640/trac_5640.patch")
Attempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5640/trac_5640.patch
Loading: [.....]
cd "/scratch/mvngu/sage-4.1.alpha0-sage.math-only-x86_64-Linux/devel/sage" && hg status
cd "/scratch/mvngu/sage-4.1.alpha0-sage.math-only-x86_64-Linux/devel/sage" && hg status
cd "/scratch/mvngu/sage-4.1.alpha0-sage.math-only-x86_64-Linux/devel/sage" && hg import   "/home/mvngu/.sage/temp/sage.math.washington.edu/23662/tmp_1.patch"
applying /home/mvngu/.sage/temp/sage.math.washington.edu/23662/tmp_1.patch
patching file sage/plot/contour_plot.py
Hunk #2 FAILED at 76
Hunk #3 FAILED at 84
Hunk #5 FAILED at 147
Hunk #6 FAILED at 223
Hunk #7 FAILED at 266
Hunk #8 FAILED at 287
Hunk #9 FAILED at 405
7 out of 9 hunks FAILED -- saving rejects to file sage/plot/contour_plot.py.rej
patching file sage/plot/density_plot.py
Hunk #2 FAILED at 78
Hunk #3 FAILED at 86
Hunk #4 FAILED at 121
3 out of 4 hunks FAILED -- saving rejects to file sage/plot/density_plot.py.rej
patching file sage/plot/matrix_plot.py
Hunk #2 FAILED at 81
Hunk #4 FAILED at 135
2 out of 4 hunks FAILED -- saving rejects to file sage/plot/matrix_plot.py.rej
abort: patch failed to apply
```



---

Comment by mvngu created at 2009-06-25 00:14:58

kcrisman: Can you rebase the patch?


---

Comment by mvngu created at 2009-06-26 00:05:13

rebased against Sage 4.1.alpha1


---

Attachment

The patch `trac_5640-rebased.patch` is rebased against Sage 4.1.alpha1 and depends on #6269. Thus patches should be applied in the following order:
 1. the rebased patch at #6269
 1. the rebased patch on this ticket


---

Comment by boothby created at 2009-06-26 23:11:50

Resolution: fixed
