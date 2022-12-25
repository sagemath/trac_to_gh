# Issue 2076: Inconsistent coloring of plotted points

archive/issues_002076.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: color hue point plot 3\n\nWhen I call, \n\nsage: point(((1,1), (2,2), (3,3)), rgbcolor=hue(1), pointsize=30)\n\nI expect to get a plot of 3 red points, but (1,1) is plotted as dark red and the other two points are blue.  So far I've only been able to recreate this issue when only three points are in the tuple.  The rgbcolor value doesn't seem to affect the color of the three plotted points.\n\nI hope to look at the code soon.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2076\n\n",
    "created_at": "2008-02-06T20:04:23Z",
    "labels": [
        "component: graphics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "Inconsistent coloring of plotted points",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2076",
    "user": "https://trac.sagemath.org/admin/accounts/users/jmitchell"
}
```
Assignee: @williamstein

Keywords: color hue point plot 3

When I call, 

sage: point(((1,1), (2,2), (3,3)), rgbcolor=hue(1), pointsize=30)

I expect to get a plot of 3 red points, but (1,1) is plotted as dark red and the other two points are blue.  So far I've only been able to recreate this issue when only three points are in the tuple.  The rgbcolor value doesn't seem to affect the color of the three plotted points.

I hope to look at the code soon.

Issue created by migration from https://trac.sagemath.org/ticket/2076





---

archive/issue_comments_013402.json:
```json
{
    "body": "Amazingly, this is a bug in matplotlib itself!\n\n\n```\ndhcp46-72:~ was$ sage -ipython\nPython 2.5.1 (r251:54863, Feb  2 2008, 18:15:25) \nType \"copyright\", \"credits\" or \"license\" for more information.\n\nIPython 0.8.1 -- An enhanced Interactive Python.\n?       -> Introduction to IPython's features.\n%magic  -> Information about IPython's 'magic' % functions.\nhelp    -> Python's own help system.\nobject? -> Details about 'object'. ?object also works, ?? prints more.\n\nIn [1]: from matplotlib.backends.backend_agg import FigureCanvasAgg\n\nIn [2]: from pylab import Figure\n\nIn [3]:  f = Figure()\n   ...: \n\nIn [4]: g = f.add_subplot(111)\n\nIn [5]: g.scatter([2.0, 3.0, 0.0], [2.0, 3.0, 0.0], s=300, c=(0.0,0.0,1.0))\nOut[5]: <matplotlib.collections.RegularPolyCollection instance at 0x20f7878>\n\nIn [6]: canvas = FigureCanvasAgg(f)\n\nIn [7]: canvas.print_figure('foo.png')\n\nIn [8]: g.scatter([2.0, 3.0, 0.0, 1.0], [2.0, 3.0, 0.0, 1.0], s=300, c=(0.0,0.0,1.0))\nOut[8]: <matplotlib.collections.RegularPolyCollection instance at 0x20fa8c8>\n\nIn [9]: canvas = FigureCanvasAgg(f)\n\nIn [10]:  canvas.print_figure('foo2.png')\n   ....: \n\nIn [11]: \nDo you really want to exit ([y]/n)? y\ndhcp46-72:~ was$ open foo.png\ndhcp46-72:~ was$ open foo2.png\n```\n\n\nCleaner input in the Sage notebook:\n\n```\nsage: RealNumber = float; Integer=int\nsage: from matplotlib.backends.backend_agg import FigureCanvasAgg\nsage: from pylab import Figure\nsage: f = Figure()\nsage: g = f.add_subplot(111)\nsage: g.scatter([2.0, 3.0, 0.0], [2.0, 3.0, 0.0], s=300, c=(0.0,0.0,1.0))\n<matplotlib.collections.RegularPolyCollection instance at 0x7facfa8>\nsage: canvas = FigureCanvasAgg(f)\nsage: canvas.print_figure('foo.png')\nsage: g.scatter([2.0, 3.0, 0.0, 1.0], [2.0, 3.0, 0.0, 1.0], s=300, c=(0.0,0.0,1.0))\n<matplotlib.collections.RegularPolyCollection instance at 0x7fac328>\nsage: canvas = FigureCanvasAgg(f)\nsage: canvas.print_figure('foo.png')\n```\n",
    "created_at": "2008-02-07T02:52:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2076#issuecomment-13402",
    "user": "https://github.com/williamstein"
}
```

Amazingly, this is a bug in matplotlib itself!


```
dhcp46-72:~ was$ sage -ipython
Python 2.5.1 (r251:54863, Feb  2 2008, 18:15:25) 
Type "copyright", "credits" or "license" for more information.

IPython 0.8.1 -- An enhanced Interactive Python.
?       -> Introduction to IPython's features.
%magic  -> Information about IPython's 'magic' % functions.
help    -> Python's own help system.
object? -> Details about 'object'. ?object also works, ?? prints more.

In [1]: from matplotlib.backends.backend_agg import FigureCanvasAgg

In [2]: from pylab import Figure

In [3]:  f = Figure()
   ...: 

In [4]: g = f.add_subplot(111)

In [5]: g.scatter([2.0, 3.0, 0.0], [2.0, 3.0, 0.0], s=300, c=(0.0,0.0,1.0))
Out[5]: <matplotlib.collections.RegularPolyCollection instance at 0x20f7878>

In [6]: canvas = FigureCanvasAgg(f)

In [7]: canvas.print_figure('foo.png')

In [8]: g.scatter([2.0, 3.0, 0.0, 1.0], [2.0, 3.0, 0.0, 1.0], s=300, c=(0.0,0.0,1.0))
Out[8]: <matplotlib.collections.RegularPolyCollection instance at 0x20fa8c8>

In [9]: canvas = FigureCanvasAgg(f)

In [10]:  canvas.print_figure('foo2.png')
   ....: 

In [11]: 
Do you really want to exit ([y]/n)? y
dhcp46-72:~ was$ open foo.png
dhcp46-72:~ was$ open foo2.png
```


Cleaner input in the Sage notebook:

```
sage: RealNumber = float; Integer=int
sage: from matplotlib.backends.backend_agg import FigureCanvasAgg
sage: from pylab import Figure
sage: f = Figure()
sage: g = f.add_subplot(111)
sage: g.scatter([2.0, 3.0, 0.0], [2.0, 3.0, 0.0], s=300, c=(0.0,0.0,1.0))
<matplotlib.collections.RegularPolyCollection instance at 0x7facfa8>
sage: canvas = FigureCanvasAgg(f)
sage: canvas.print_figure('foo.png')
sage: g.scatter([2.0, 3.0, 0.0, 1.0], [2.0, 3.0, 0.0, 1.0], s=300, c=(0.0,0.0,1.0))
<matplotlib.collections.RegularPolyCollection instance at 0x7fac328>
sage: canvas = FigureCanvasAgg(f)
sage: canvas.print_figure('foo.png')
```




---

archive/issue_comments_013403.json:
```json
{
    "body": "I propose the following:\n\n1. We upgrade from `matplotlib-0.91.1` to the latest verison, whatever it is.\n\n2. If this doesn't fix the problem, report it to the matplotlib list.\n\n3. If that doesn't work, fix the problem !?  Or program around it.",
    "created_at": "2008-02-07T03:07:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2076#issuecomment-13403",
    "user": "https://github.com/williamstein"
}
```

I propose the following:

1. We upgrade from `matplotlib-0.91.1` to the latest verison, whatever it is.

2. If this doesn't fix the problem, report it to the matplotlib list.

3. If that doesn't work, fix the problem !?  Or program around it.



---

archive/issue_comments_013404.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2008-09-03T00:52:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2076#issuecomment-13404",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_013405.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-03T00:52:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2076#issuecomment-13405",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_013406.json:
```json
{
    "body": "Attachment [trac_2076.patch](tarball://root/attachments/some-uuid/ticket2076/trac_2076.patch) by @mwhansen created at 2008-09-04 03:43:45\n\nThis is actually a bug on our part according to the matplotlib 0.98 documentation for scatter.",
    "created_at": "2008-09-04T03:43:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2076#issuecomment-13406",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_2076.patch](tarball://root/attachments/some-uuid/ticket2076/trac_2076.patch) by @mwhansen created at 2008-09-04 03:43:45

This is actually a bug on our part according to the matplotlib 0.98 documentation for scatter.



---

archive/issue_comments_013407.json:
```json
{
    "body": "I've read the matplotlib docs and this looks reasonable.  I don't have a current 3.1.2 tree to test it, though; so half of a positive review (the other half comes from applying it and checking the result of the doctest :).",
    "created_at": "2008-09-04T04:09:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2076#issuecomment-13407",
    "user": "https://github.com/jasongrout"
}
```

I've read the matplotlib docs and this looks reasonable.  I don't have a current 3.1.2 tree to test it, though; so half of a positive review (the other half comes from applying it and checking the result of the doctest :).



---

archive/issue_comments_013408.json:
```json
{
    "body": "Jason,\n\nsince you now have a 3.1.2 can you do the final review on this? I can run doctests without a problem on 3.1.3.alpha1 to see if anything breaks. \n\nCheers,\n\nMichael",
    "created_at": "2008-09-22T23:41:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2076#issuecomment-13408",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Jason,

since you now have a 3.1.2 can you do the final review on this? I can run doctests without a problem on 3.1.3.alpha1 to see if anything breaks. 

Cheers,

Michael



---

archive/issue_comments_013409.json:
```json
{
    "body": "The example now works and doctests in plot/*.py pass with the patch applied.  So that's a full positive review, now.",
    "created_at": "2008-09-23T00:44:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2076#issuecomment-13409",
    "user": "https://github.com/jasongrout"
}
```

The example now works and doctests in plot/*.py pass with the patch applied.  So that's a full positive review, now.



---

archive/issue_comments_013410.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-23T01:18:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2076#issuecomment-13410",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013411.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha1",
    "created_at": "2008-09-23T01:18:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2076#issuecomment-13411",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.alpha1



---

archive/issue_events_002237.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-23T01:18:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2076",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2076#event-2237"
}
```
