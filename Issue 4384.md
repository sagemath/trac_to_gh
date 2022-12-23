# Issue 4384: Axes computation for constant function causes division by zero

Issue created by migration from https://trac.sagemath.org/ticket/4384

Original creator: rbeezer

Original creation time: 2008-10-30 04:14:30

Assignee: somebody

CC:  anakha jason mvngu

Keywords: plot contant ZeroDivisionError

For a function which is constant, but not obviously so, it would appear that some computation for laying out the axis creates a step size of 0 (tick marks on the vertical axis?).


```
sage: h=plot(sin(x)^2+cos(x)^2, -6, 6)
sage: show(h)
```



```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/rob/.sage/sage_notebook/worksheets/admin/48/code/6.py", line 8, in <module>
    show(h)
  File "/opt/sage-3.1.4/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/", line 1, in <module>
    
  File "/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/misc/functional.py", line 882, in show
    return x.show(*args, **kwds)
  File "/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/plot/plot.py", line 1350, in show
    hgridlinesstyle=hgridlinesstyle)
  File "/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/plot/plot.py", line 1547, in save
    xmin, xmax, ymin, ymax = sage_axes.add_xy_axes(subplot, xmin, xmax, ymin, ymax)
  File "/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/plot/axes.py", line 325, in add_xy_axes
    x_axis_ypos, ystep, ytslminor, ytslmajor = self._find_axes(ymin, ymax)
  File "/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/plot/axes.py", line 239, in _find_axes
    tslmajor, oppaxis, step = self._tasteless_ticks(minval, maxval, 10)
  File "/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/plot/axes.py", line 217, in _tasteless_ticks
    tslmajor = sage.misc.misc.srange(minval, minval+(num_pieces+1)*step, step)
  File "/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/misc/misc.py", line 710, in srange
    count = int(math.ceil((float((end-start)/step))))
ZeroDivisionError: float division
```



---

Comment by mabshoff created at 2008-10-31 01:11:10

This is plotting related and has nothing to do with the notebook.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-31 01:11:10

Changing component from notebook to graphics.


---

Comment by kcrisman created at 2009-09-15 17:35:35

This no longer causes an error, given #5448 being included, but has a different problem, in that matplotlib doesn't just extend the axes all the way to zero.  I don't know if there is a way to fix this, though.


---

Comment by jason created at 2009-09-15 17:44:10

There's *always* a way to fix it :).

This is odd, since `plot(1, -5, 5)` seems to give an okay axis range.  Even `plot(1+x-x,-1,1)` seems okay.


---

Comment by kcrisman created at 2009-09-15 18:25:05

Even weirder, for a second it did work on 4.1.2.alpha1 for me.  Then I exited and started again, and it went back to this weird behavior.

Anyway, the problem is probably that we fixed something a while ago to catch constant function plotting, and 1+x-x evaluates to 1 in Sage, but the trig identity doesn't.


---

Comment by jason created at 2009-09-15 18:26:45

yes, it maybe has something to do with the fast_callable simplifying things or something.

We should probably add a special case for axes where the y-range is very small.


---

Comment by jason created at 2009-09-15 18:32:53

Okay, this shows problems: `plot(x^2-1-(x-1)*(x+1), -5, 5)`

In fact, it shows a lot of random noise.


---

Comment by kcrisman created at 2009-09-15 18:45:10

Replying to [comment:7 jason]:
> Okay, this shows problems: `plot(x^2-1-(x-1)*(x+1), -5, 5)`
> 
> In fact, it shows a lot of random noise.
The noise is to be expected, since it's impossible for these to evaluate exactly to zero as a float, don't you think?   But yes, the axes seems... weird.   Did the default [-1,1]x[-1,1] disappear?


---

Comment by jason created at 2009-09-29 16:03:38

Okay, the bug (the error) is fixed.  If we want to open another ticket that somehow figures out the user doesn't want a small window, and instead gives a much bigger range, then I think that should go on another ticket and this should be closed as fixed (due to #5448).


---

Comment by jason created at 2009-09-29 16:04:26

Changing subject back to the original bug...


---

Attachment

based on Sage 4.1.2.alpha4


---

Comment by mvngu created at 2009-09-29 16:17:34

I can confirm this has been fixed:

```
[mvngu@darkstar sage-4.1.2.alpha4]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: h=plot(sin(x)^2+cos(x)^2, -6, 6)
sage: show(h)
```

The resulting plot is attached. Closing this ticket as being fixed by #5448.


---

Comment by mvngu created at 2009-09-29 16:17:34

Resolution: fixed
