# Issue 5645: error in axis plotting with large values

Issue created by migration from https://trac.sagemath.org/ticket/5645

Original creator: robertwb

Original creation time: 2009-03-30 21:46:13

Assignee: was

CC:  mvngu


```
sage: plot(e^(x^-2), (x, -1, 1))
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/IPython/Prompts.py", line 551, in __call__
    manipulated_val = self.display(arg)
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/IPython/Prompts.py", line 577, in _display
    return self.shell.hooks.result_display(arg)
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/IPython/hooks.py", line 141, in __call__
    ret = cmd(*args, **kw)
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/IPython/hooks.py", line 171, in result_display
    out = pformat(arg)
  File "/Users/robert/sage/current/local/lib/python2.5/pprint.py", line 111, in pformat
    self._format(object, sio, 0, 0, {}, 0)
  File "/Users/robert/sage/current/local/lib/python2.5/pprint.py", line 129, in _format
    rep = self._repr(object, context, level - 1)
  File "/Users/robert/sage/current/local/lib/python2.5/pprint.py", line 195, in _repr
    self._depth, level)
  File "/Users/robert/sage/current/local/lib/python2.5/pprint.py", line 207, in format
    return _safe_repr(object, context, maxlevels, level)
  File "/Users/robert/sage/current/local/lib/python2.5/pprint.py", line 292, in _safe_repr
    rep = repr(object)
  File "sage_object.pyx", line 98, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1085)
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/plot/plot.py", line 861, in _repr_
    self.show()
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/plot/plot.py", line 1297, in show
    hgridlinesstyle=hgridlinesstyle)
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/plot/plot.py", line 1543, in save
    xmin, xmax, ymin, ymax = sage_axes.add_xy_axes(subplot, xmin, xmax, ymin, ymax)
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/plot/axes.py", line 325, in add_xy_axes
    x_axis_ypos, ystep, ytslminor, ytslmajor = self._find_axes(ymin, ymax)
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/plot/axes.py", line 241, in _find_axes
    tslmajor, oppaxis, step = self._tasteful_ticks(minval, maxval)
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/plot/axes.py", line 125, in _tasteful_ticks
    sl = [s for s in str(int(absmax))]
OverflowError: cannot convert float infinity to long

```



---

Comment by kcrisman created at 2009-09-15 17:24:38

To release manager: this ticket has been resolved by #5448.  The graph still looks terrible!  But that would be a different ticket.


---

Comment by jason created at 2009-09-29 15:58:31

This should be closed due to #5448


---

Comment by mvngu created at 2009-09-29 16:08:17

based on Sage 4.1.2.alpha4


---

Attachment

This has been fixed in Sage 4.1.2.alpha4. Closing this ticket as fixed by #5448:

```
[mvngu@darkstar sage-4.1.2.alpha4]$ ./sage -br main

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Time to execute 0 commands: 2.59876251221e-05 seconds
Finished compiling Cython code (time = 4.20651006699 seconds)
running install
running build
running build_py
running build_ext
Total time spent compiling C/C++ extensions:  0.156050920486 seconds.
running install_lib
running install_egg_info
Removing /home/mvngu/scratch/sandbox/sage-4.1.2.alpha4/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info
Writing /home/mvngu/scratch/sandbox/sage-4.1.2.alpha4/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: plot(e^(x^-2), (x, -1, 1))
```

The resulting plot is attached.


---

Comment by mvngu created at 2009-09-29 16:10:16

Resolution: fixed
