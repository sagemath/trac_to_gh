# Issue 2730: matplotlib in Debian is (probably) too old

Issue created by migration from https://trac.sagemath.org/ticket/2730

Original creator: tabbott

Original creation time: 2008-03-30 00:02:01

Assignee: tabbott

I get the following doctest errors in the Debian build of SAGE 2.10.4.  I think the problem is that matplotlib.patches got changed to add "from matplotlib.lines as lines" since matplotlib 0.90.1 (the version in debian).  

**********************************************************************
File "tut.py", line 1818:
    : p.save()
Exception raised:
    Traceback (most recent call last):
      File "/usr/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_72[2]>", line 1, in <module>
        p.save()###line 1818:
    : p.save()
      File "/usr/lib/python2.5/site-packages/sage/plot/plot.py", line 1419, in save
        xmin, xmax, ymin, ymax = sage_axes.add_xy_axes(subplot, xmin, xmax, ymin, ymax)
      File "/usr/lib/python2.5/site-packages/sage/plot/axes.py", line 332, in add_xy_axes
        self._draw_axes(subplot, axes, xmin, xmax, ymin, ymax, x_axis_ypos, y_axis_xpos)
      File "/usr/lib/python2.5/site-packages/sage/plot/axes.py", line 263, in _draw_axes
        subplot.add_line(patches.lines.Line2D([xmin, xmax], [x_axis_ypos, x_axis_ypos],
    AttributeError: 'module' object has no attribute 'lines'



---

Comment by tabbott created at 2008-03-30 02:19:58

I did the most trivial forward-port of a newer matplotlib for Debian and uploaded to the testing repository at http://web.mit.edu/sage/apt/.

It seems to work.


---

Comment by mabshoff created at 2008-03-30 09:54:42

Resolution: wontfix


---

Comment by mabshoff created at 2008-03-30 09:54:42

This is not _#Sage Specific_': Please file a bug report with Debian or alternatively package the Sage version of matplotlib.

Cheers,

Michael
