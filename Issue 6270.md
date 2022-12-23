# Issue 6270: [with patch, needs review] add some files from the plot directory to the reference manual

Issue created by migration from https://trac.sagemath.org/ticket/6270

Original creator: jhpalmieri

Original creation time: 2009-06-12 18:20:59

Assignee: jhpalmieri

This adds the 8 files to the reference manual (since kcrisman has put so much work into getting them to 100% coverage).  It also adds a few cross-references to plot.py and makes one or two small changes (e.g., it removes a reference to `rgbcolor` at the beginning of plot.py, since that function isn't in the global name space, and its mention suggested that it might be).



---

Attachment

When applying the patch, I got the following hunk failures:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: 6270
sage: hg_sage.apply("../patch/6270/trac_6270.patch")
cd "/scratch/mvngu/sage-4.0.1/devel/sage" && hg status
cd "/scratch/mvngu/sage-4.0.1/devel/sage" && hg status
cd "/scratch/mvngu/sage-4.0.1/devel/sage" && hg import   "/scratch/mvngu/patch/6270/trac_6270.patch"
applying /scratch/mvngu/patch/6270/trac_6270.patch
patching file sage/plot/plot.py
Hunk #1 FAILED at 6
Hunk #2 FAILED at 1865
2 out of 2 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej
abort: patch failed to apply
```

The patch was applied on a fresh clone of Sage 4.0.1. Should there be a rebase?


---

Comment by jhpalmieri created at 2009-06-12 19:56:12

I'm sorry -- I forgot to say that this patch depends on #6257.  Please apply that one first and try again.


---

Comment by kcrisman created at 2009-06-13 03:49:12

You might want to look at # 6269 as well regarding the rgbcolor thing; I have potentially moved that and hue to a new file.


---

Comment by mvngu created at 2009-06-13 11:04:05

After applying the patch, the following modules are in the reference manual, but the ReST formatting need some polishing:

```
sage/plot/circle
sage/plot/disk
```

The following are referred to in the reference manual, but are not yet in the manual. So there's no hyperlink to any of them even if one is defined.

```
line()
implicit_plot()
region_plot()
scatter_plot()
bar_chart()
contour_plot()
density_plot()
plot_vector_field()
plot_slope_field()
matrix_plot()
complex_plot()
```

I can give the patch a positive review for adding files under the `sage/plot` directory to the reference manual. The formatting and referencing issues I mentioned above are *not* introduced by the patch, and should be addressed in another ticket. So patches should be applied in the following order:
 1. apply the patch at #6257
 1. then apply the patch on this ticket.


---

Comment by mvngu created at 2009-06-13 12:23:53

See #6274 for a follow-up to this ticket.


---

Comment by ncalexan created at 2009-06-13 21:42:53

Resolution: fixed
