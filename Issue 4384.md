# Issue 4384: Axes computation for constant function causes division by zero

archive/issues_004384.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  anakha @jasongrout mvngu\n\nKeywords: plot contant ZeroDivisionError\n\nFor a function which is constant, but not obviously so, it would appear that some computation for laying out the axis creates a step size of 0 (tick marks on the vertical axis?).\n\n```\nsage: h=plot(sin(x)^2+cos(x)^2, -6, 6)\nsage: show(h)\n```\n\n```\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/home/rob/.sage/sage_notebook/worksheets/admin/48/code/6.py\", line 8, in <module>\n    show(h)\n  File \"/opt/sage-3.1.4/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/\", line 1, in <module>\n    \n  File \"/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/misc/functional.py\", line 882, in show\n    return x.show(*args, **kwds)\n  File \"/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/plot/plot.py\", line 1350, in show\n    hgridlinesstyle=hgridlinesstyle)\n  File \"/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/plot/plot.py\", line 1547, in save\n    xmin, xmax, ymin, ymax = sage_axes.add_xy_axes(subplot, xmin, xmax, ymin, ymax)\n  File \"/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/plot/axes.py\", line 325, in add_xy_axes\n    x_axis_ypos, ystep, ytslminor, ytslmajor = self._find_axes(ymin, ymax)\n  File \"/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/plot/axes.py\", line 239, in _find_axes\n    tslmajor, oppaxis, step = self._tasteless_ticks(minval, maxval, 10)\n  File \"/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/plot/axes.py\", line 217, in _tasteless_ticks\n    tslmajor = sage.misc.misc.srange(minval, minval+(num_pieces+1)*step, step)\n  File \"/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/misc/misc.py\", line 710, in srange\n    count = int(math.ceil((float((end-start)/step))))\nZeroDivisionError: float division\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/4384\n\n",
    "created_at": "2008-10-30T04:14:30Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Axes computation for constant function causes division by zero",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4384",
    "user": "https://github.com/rbeezer"
}
```
Assignee: somebody

CC:  anakha @jasongrout mvngu

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

Issue created by migration from https://trac.sagemath.org/ticket/4384





---

archive/issue_comments_032201.json:
```json
{
    "body": "This is plotting related and has nothing to do with the notebook.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T01:11:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4384#issuecomment-32201",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is plotting related and has nothing to do with the notebook.

Cheers,

Michael



---

archive/issue_comments_032202.json:
```json
{
    "body": "Changing component from notebook to graphics.",
    "created_at": "2008-10-31T01:11:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4384#issuecomment-32202",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from notebook to graphics.



---

archive/issue_comments_032203.json:
```json
{
    "body": "This no longer causes an error, given #5448 being included, but has a different problem, in that matplotlib doesn't just extend the axes all the way to zero.  I don't know if there is a way to fix this, though.",
    "created_at": "2009-09-15T17:35:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4384#issuecomment-32203",
    "user": "https://github.com/kcrisman"
}
```

This no longer causes an error, given #5448 being included, but has a different problem, in that matplotlib doesn't just extend the axes all the way to zero.  I don't know if there is a way to fix this, though.



---

archive/issue_comments_032204.json:
```json
{
    "body": "There's *always* a way to fix it :).\n\nThis is odd, since `plot(1, -5, 5)` seems to give an okay axis range.  Even `plot(1+x-x,-1,1)` seems okay.",
    "created_at": "2009-09-15T17:44:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4384#issuecomment-32204",
    "user": "https://github.com/jasongrout"
}
```

There's *always* a way to fix it :).

This is odd, since `plot(1, -5, 5)` seems to give an okay axis range.  Even `plot(1+x-x,-1,1)` seems okay.



---

archive/issue_comments_032205.json:
```json
{
    "body": "Even weirder, for a second it did work on 4.1.2.alpha1 for me.  Then I exited and started again, and it went back to this weird behavior.\n\nAnyway, the problem is probably that we fixed something a while ago to catch constant function plotting, and 1+x-x evaluates to 1 in Sage, but the trig identity doesn't.",
    "created_at": "2009-09-15T18:25:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4384#issuecomment-32205",
    "user": "https://github.com/kcrisman"
}
```

Even weirder, for a second it did work on 4.1.2.alpha1 for me.  Then I exited and started again, and it went back to this weird behavior.

Anyway, the problem is probably that we fixed something a while ago to catch constant function plotting, and 1+x-x evaluates to 1 in Sage, but the trig identity doesn't.



---

archive/issue_comments_032206.json:
```json
{
    "body": "yes, it maybe has something to do with the fast_callable simplifying things or something.\n\nWe should probably add a special case for axes where the y-range is very small.",
    "created_at": "2009-09-15T18:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4384#issuecomment-32206",
    "user": "https://github.com/jasongrout"
}
```

yes, it maybe has something to do with the fast_callable simplifying things or something.

We should probably add a special case for axes where the y-range is very small.



---

archive/issue_comments_032207.json:
```json
{
    "body": "Okay, this shows problems: `plot(x^2-1-(x-1)*(x+1), -5, 5)`\n\nIn fact, it shows a lot of random noise.",
    "created_at": "2009-09-15T18:32:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4384#issuecomment-32207",
    "user": "https://github.com/jasongrout"
}
```

Okay, this shows problems: `plot(x^2-1-(x-1)*(x+1), -5, 5)`

In fact, it shows a lot of random noise.



---

archive/issue_comments_032208.json:
```json
{
    "body": "Replying to [comment:7 jason]:\n> Okay, this shows problems: `plot(x^2-1-(x-1)*(x+1), -5, 5)`\n> \n> In fact, it shows a lot of random noise.\n\nThe noise is to be expected, since it's impossible for these to evaluate exactly to zero as a float, don't you think?   But yes, the axes seems... weird.   Did the default [-1,1]x[-1,1] disappear?",
    "created_at": "2009-09-15T18:45:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4384#issuecomment-32208",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:7 jason]:
> Okay, this shows problems: `plot(x^2-1-(x-1)*(x+1), -5, 5)`
> 
> In fact, it shows a lot of random noise.

The noise is to be expected, since it's impossible for these to evaluate exactly to zero as a float, don't you think?   But yes, the axes seems... weird.   Did the default [-1,1]x[-1,1] disappear?



---

archive/issue_comments_032209.json:
```json
{
    "body": "Okay, the bug (the error) is fixed.  If we want to open another ticket that somehow figures out the user doesn't want a small window, and instead gives a much bigger range, then I think that should go on another ticket and this should be closed as fixed (due to #5448).",
    "created_at": "2009-09-29T16:03:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4384#issuecomment-32209",
    "user": "https://github.com/jasongrout"
}
```

Okay, the bug (the error) is fixed.  If we want to open another ticket that somehow figures out the user doesn't want a small window, and instead gives a much bigger range, then I think that should go on another ticket and this should be closed as fixed (due to #5448).



---

archive/issue_comments_032210.json:
```json
{
    "body": "Changing subject back to the original bug...",
    "created_at": "2009-09-29T16:04:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4384#issuecomment-32210",
    "user": "https://github.com/jasongrout"
}
```

Changing subject back to the original bug...



---

archive/issue_comments_032211.json:
```json
{
    "body": "Attachment [plot.png](tarball://root/attachments/some-uuid/ticket4384/plot.png) by mvngu created at 2009-09-29 16:15:39\n\nbased on Sage 4.1.2.alpha4",
    "created_at": "2009-09-29T16:15:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4384#issuecomment-32211",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [plot.png](tarball://root/attachments/some-uuid/ticket4384/plot.png) by mvngu created at 2009-09-29 16:15:39

based on Sage 4.1.2.alpha4



---

archive/issue_events_009906.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-29T16:17:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4384",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4384#event-9906"
}
```



---

archive/issue_comments_032212.json:
```json
{
    "body": "I can confirm this has been fixed:\n\n```\n[mvngu@darkstar sage-4.1.2.alpha4]$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage: h=plot(sin(x)^2+cos(x)^2, -6, 6)\nsage: show(h)\n```\nThe resulting plot is attached. Closing this ticket as being fixed by #5448.",
    "created_at": "2009-09-29T16:17:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4384#issuecomment-32212",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

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

archive/issue_comments_032213.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-29T16:17:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4384#issuecomment-32213",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
