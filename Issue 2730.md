# Issue 2730: matplotlib in Debian is (probably) too old

archive/issues_002730.json:
```json
{
    "body": "Assignee: @timabbott\n\nI get the following doctest errors in the Debian build of SAGE 2.10.4.  I think the problem is that matplotlib.patches got changed to add \"from matplotlib.lines as lines\" since matplotlib 0.90.1 (the version in debian).  \n\n**********************************************************************\nFile \"tut.py\", line 1818:\n    : p.save()\nException raised:\n    Traceback (most recent call last):\n      File \"/usr/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_72[2]>\", line 1, in <module>\n        p.save()###line 1818:\n    : p.save()\n      File \"/usr/lib/python2.5/site-packages/sage/plot/plot.py\", line 1419, in save\n        xmin, xmax, ymin, ymax = sage_axes.add_xy_axes(subplot, xmin, xmax, ymin, ymax)\n      File \"/usr/lib/python2.5/site-packages/sage/plot/axes.py\", line 332, in add_xy_axes\n        self._draw_axes(subplot, axes, xmin, xmax, ymin, ymax, x_axis_ypos, y_axis_xpos)\n      File \"/usr/lib/python2.5/site-packages/sage/plot/axes.py\", line 263, in _draw_axes\n        subplot.add_line(patches.lines.Line2D([xmin, xmax], [x_axis_ypos, x_axis_ypos],\n    AttributeError: 'module' object has no attribute 'lines'\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2730\n\n",
    "created_at": "2008-03-30T00:02:01Z",
    "labels": [
        "debian-package",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "matplotlib in Debian is (probably) too old",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2730",
    "user": "@timabbott"
}
```
Assignee: @timabbott

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


Issue created by migration from https://trac.sagemath.org/ticket/2730





---

archive/issue_comments_018796.json:
```json
{
    "body": "I did the most trivial forward-port of a newer matplotlib for Debian and uploaded to the testing repository at http://web.mit.edu/sage/apt/.\n\nIt seems to work.",
    "created_at": "2008-03-30T02:19:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2730#issuecomment-18796",
    "user": "@timabbott"
}
```

I did the most trivial forward-port of a newer matplotlib for Debian and uploaded to the testing repository at http://web.mit.edu/sage/apt/.

It seems to work.



---

archive/issue_comments_018797.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-03-30T09:54:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2730#issuecomment-18797",
    "user": "mabshoff"
}
```

Resolution: wontfix



---

archive/issue_comments_018798.json:
```json
{
    "body": "This is not *#Sage Specific*': Please file a bug report with Debian or alternatively package the Sage version of matplotlib.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-30T09:54:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2730#issuecomment-18798",
    "user": "mabshoff"
}
```

This is not *#Sage Specific*': Please file a bug report with Debian or alternatively package the Sage version of matplotlib.

Cheers,

Michael
