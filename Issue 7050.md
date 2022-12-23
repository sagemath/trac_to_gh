# Issue 7050: Make plotting single polar points or lines easy

archive/issues_007050.json:
```json
{
    "body": "Assignee: was\n\nKeywords: plot, polar\n\nSee [http://groups.google.com/group/sage-support/browse_thread/thread/ad0294c057ddc462/6b9b4092034359c4?show_docid=6b9b4092034359c4](http://groups.google.com/group/sage-support/browse_thread/thread/ad0294c057ddc462/6b9b4092034359c4?show_docid=6b9b4092034359c4) for the original request.  \n\nProbably the best thing to do is have both plotting of lines and individual points using polar coordinates as options.  This should not be too hard, but should be named consistently with other plotting functions.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7050\n\n",
    "created_at": "2009-09-28T12:24:48Z",
    "labels": [
        "graphics",
        "minor",
        "bug"
    ],
    "title": "Make plotting single polar points or lines easy",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7050",
    "user": "kcrisman"
}
```
Assignee: was

Keywords: plot, polar

See [http://groups.google.com/group/sage-support/browse_thread/thread/ad0294c057ddc462/6b9b4092034359c4?show_docid=6b9b4092034359c4](http://groups.google.com/group/sage-support/browse_thread/thread/ad0294c057ddc462/6b9b4092034359c4?show_docid=6b9b4092034359c4) for the original request.  

Probably the best thing to do is have both plotting of lines and individual points using polar coordinates as options.  This should not be too hard, but should be named consistently with other plotting functions.

Issue created by migration from https://trac.sagemath.org/ticket/7050





---

archive/issue_comments_058358.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-09-28T12:25:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7050#issuecomment-58358",
    "user": "kcrisman"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_058359.json:
```json
{
    "body": "Please note that matplotlib already addresses these issues.  See, for example, this discussion: \n\nhttp://www.mail-archive.com/matplotlib-devel`@`lists.sourceforge.net/msg04785.html\n\nWe just have to change our polar plots to use the matplotlib polar plotting mechanism.  That's something I've been meaning to do anyway, especially now that we use the matplotlib axes instead of our own.  I probably won't get to it in the near future, though.  Someone else is more than welcome to do it.\n\nBasically, right now, our \"polar plots\" are just normal plots with the coordinates undergoing the polar transformation on each point.  I think it might be good to change this so that our polar plots actually use the polar projection to give matplotlib polar plots.  See \n\n\nExamples of matplotlib polar plots:\n\nhttp://matplotlib.sourceforge.net/examples/pylab_examples/polar_bar.html\nhttp://matplotlib.sourceforge.net/examples/pylab_examples/polar_demo.html\nhttp://matplotlib.sourceforge.net/examples/pylab_examples/polar_scatter.html\n\nor more exciting stuff that is currently in matplotlib and being refined:\n\nhttp://matplotlib.sourceforge.net/examples/axes_grid/demo_curvelinear_grid.html\n\nhttp://matplotlib.sourceforge.net/examples/axes_grid/demo_floating_axis.html\n\nThanks,\n\nJason",
    "created_at": "2009-09-28T13:27:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7050#issuecomment-58359",
    "user": "jason"
}
```

Please note that matplotlib already addresses these issues.  See, for example, this discussion: 

http://www.mail-archive.com/matplotlib-devel`@`lists.sourceforge.net/msg04785.html

We just have to change our polar plots to use the matplotlib polar plotting mechanism.  That's something I've been meaning to do anyway, especially now that we use the matplotlib axes instead of our own.  I probably won't get to it in the near future, though.  Someone else is more than welcome to do it.

Basically, right now, our "polar plots" are just normal plots with the coordinates undergoing the polar transformation on each point.  I think it might be good to change this so that our polar plots actually use the polar projection to give matplotlib polar plots.  See 


Examples of matplotlib polar plots:

http://matplotlib.sourceforge.net/examples/pylab_examples/polar_bar.html
http://matplotlib.sourceforge.net/examples/pylab_examples/polar_demo.html
http://matplotlib.sourceforge.net/examples/pylab_examples/polar_scatter.html

or more exciting stuff that is currently in matplotlib and being refined:

http://matplotlib.sourceforge.net/examples/axes_grid/demo_curvelinear_grid.html

http://matplotlib.sourceforge.net/examples/axes_grid/demo_floating_axis.html

Thanks,

Jason
