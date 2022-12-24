# Issue 5645: error in axis plotting with large values

archive/issues_005645.json:
```json
{
    "body": "Assignee: was\n\nCC:  mvngu\n\n\n```\nsage: plot(e^(x^-2), (x, -1, 1))\n------------------------------------------------------------\nTraceback (most recent call last):\n  File \"<ipython console>\", line 1, in <module>\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/IPython/Prompts.py\", line 551, in __call__\n    manipulated_val = self.display(arg)\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/IPython/Prompts.py\", line 577, in _display\n    return self.shell.hooks.result_display(arg)\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/IPython/hooks.py\", line 141, in __call__\n    ret = cmd(*args, **kw)\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/IPython/hooks.py\", line 171, in result_display\n    out = pformat(arg)\n  File \"/Users/robert/sage/current/local/lib/python2.5/pprint.py\", line 111, in pformat\n    self._format(object, sio, 0, 0, {}, 0)\n  File \"/Users/robert/sage/current/local/lib/python2.5/pprint.py\", line 129, in _format\n    rep = self._repr(object, context, level - 1)\n  File \"/Users/robert/sage/current/local/lib/python2.5/pprint.py\", line 195, in _repr\n    self._depth, level)\n  File \"/Users/robert/sage/current/local/lib/python2.5/pprint.py\", line 207, in format\n    return _safe_repr(object, context, maxlevels, level)\n  File \"/Users/robert/sage/current/local/lib/python2.5/pprint.py\", line 292, in _safe_repr\n    rep = repr(object)\n  File \"sage_object.pyx\", line 98, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1085)\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/plot/plot.py\", line 861, in _repr_\n    self.show()\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/plot/plot.py\", line 1297, in show\n    hgridlinesstyle=hgridlinesstyle)\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/plot/plot.py\", line 1543, in save\n    xmin, xmax, ymin, ymax = sage_axes.add_xy_axes(subplot, xmin, xmax, ymin, ymax)\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/plot/axes.py\", line 325, in add_xy_axes\n    x_axis_ypos, ystep, ytslminor, ytslmajor = self._find_axes(ymin, ymax)\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/plot/axes.py\", line 241, in _find_axes\n    tslmajor, oppaxis, step = self._tasteful_ticks(minval, maxval)\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/plot/axes.py\", line 125, in _tasteful_ticks\n    sl = [s for s in str(int(absmax))]\nOverflowError: cannot convert float infinity to long\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5645\n\n",
    "created_at": "2009-03-30T21:46:13Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "error in axis plotting with large values",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5645",
    "user": "robertwb"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/5645





---

archive/issue_comments_044086.json:
```json
{
    "body": "To release manager: this ticket has been resolved by #5448.  The graph still looks terrible!  But that would be a different ticket.",
    "created_at": "2009-09-15T17:24:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5645#issuecomment-44086",
    "user": "kcrisman"
}
```

To release manager: this ticket has been resolved by #5448.  The graph still looks terrible!  But that would be a different ticket.



---

archive/issue_comments_044087.json:
```json
{
    "body": "This should be closed due to #5448",
    "created_at": "2009-09-29T15:58:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5645#issuecomment-44087",
    "user": "jason"
}
```

This should be closed due to #5448



---

archive/issue_comments_044088.json:
```json
{
    "body": "based on Sage 4.1.2.alpha4",
    "created_at": "2009-09-29T16:08:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5645#issuecomment-44088",
    "user": "mvngu"
}
```

based on Sage 4.1.2.alpha4



---

archive/issue_comments_044089.json:
```json
{
    "body": "Attachment [plot.png](tarball://root/attachments/some-uuid/ticket5645/plot.png) by mvngu created at 2009-09-29 16:10:16\n\nThis has been fixed in Sage 4.1.2.alpha4. Closing this ticket as fixed by #5448:\n\n```\n[mvngu@darkstar sage-4.1.2.alpha4]$ ./sage -br main\n\n----------------------------------------------------------\nsage: Building and installing modified Sage library files.\n\n\nInstalling c_lib\nscons: `install' is up to date.\nUpdating Cython code....\nTime to execute 0 commands: 2.59876251221e-05 seconds\nFinished compiling Cython code (time = 4.20651006699 seconds)\nrunning install\nrunning build\nrunning build_py\nrunning build_ext\nTotal time spent compiling C/C++ extensions:  0.156050920486 seconds.\nrunning install_lib\nrunning install_egg_info\nRemoving /home/mvngu/scratch/sandbox/sage-4.1.2.alpha4/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info\nWriting /home/mvngu/scratch/sandbox/sage-4.1.2.alpha4/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage: plot(e^(x^-2), (x, -1, 1))\n```\n\nThe resulting plot is attached.",
    "created_at": "2009-09-29T16:10:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5645#issuecomment-44089",
    "user": "mvngu"
}
```

Attachment [plot.png](tarball://root/attachments/some-uuid/ticket5645/plot.png) by mvngu created at 2009-09-29 16:10:16

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

archive/issue_comments_044090.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-29T16:10:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5645#issuecomment-44090",
    "user": "mvngu"
}
```

Resolution: fixed
