# Issue 3806: improvements to plot.py

Issue created by migration from https://trac.sagemath.org/ticket/3806

Original creator: mhansen

Original creation time: 2008-08-11 19:57:07

Assignee: was

If you do


```
sage: plot(sin(x), 100, 120))
```


you get a plot which goes from -1 to 120 which is mostly empty space.  The is due to the behavior of Graphics() and _extend_axes.  Many of the other graphics objects suffer this same problem.  This patch fixes that and cleans up some of the useless code factoring in plot.py which hopefully makes it easier to understand.


---

Attachment


---

Attachment


---

Comment by ekirkman created at 2008-08-12 01:52:26

mabshoff is going to test it, but super-dooper +1 on style!


---

Comment by mabshoff created at 2008-08-12 02:08:19

The following test fails:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.alpha2$ ./sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py
sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/tmp/ell_point.py", line 392:
    sage: P.plot(pointsize=30, rgbcolor=(1,0,0))
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_18[3]>", line 1, in <module>
        P.plot(pointsize=Integer(30), rgbcolor=(Integer(1),Integer(0),Integer(0)))###line 392:
    sage: P.plot(pointsize=30, rgbcolor=(1,0,0))
      File "sage_object.pyx", line 92, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:795)
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/local/lib/python2.5/site-packages/sage/plot/plot.py", line 740, in _repr_
        self.show()
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/local/lib/python2.5/site-packages/sage/plot/plot.py", line 1242, in show
        aspect_ratio=aspect_ratio)
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/local/lib/python2.5/site-packages/sage/plot/plot.py", line 1421, in save
        xmin, xmax, ymin, ymax = sage_axes.add_xy_axes(subplot, xmin, xmax, ymin, ymax)
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/local/lib/python2.5/site-packages/sage/plot/axes.py", line 320, in add_xy_axes
        y_axis_xpos, xstep, xtslminor, xtslmajor = self._find_axes(xmin, xmax)
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/local/lib/python2.5/site-packages/sage/plot/axes.py", line 234, in _find_axes
        raise ValueError, "maxval >= minval is required"
    ValueError: maxval >= minval is required
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_18
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.alpha2/tmp/.doctest_ell_point.py
         [11.0 s]
exit code: 1024
```



---

Comment by rlm created at 2008-08-12 05:46:35

Equivalently,

```
sage: point((-1,1),pointsize=30, rgbcolor=(1,0,0))
<boom>
```



---

Attachment

+1 to rlm's patch


---

Comment by mabshoff created at 2008-08-12 06:30:51

Resolution: fixed


---

Comment by mabshoff created at 2008-08-12 06:30:51

Merged all three patches in Sage 3.1.alpha2
