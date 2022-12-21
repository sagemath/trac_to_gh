# Issue 7050: Make plotting single polar points or lines easy

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2009-09-28 12:24:48

Assignee: was

Keywords: plot, polar

See [http://groups.google.com/group/sage-support/browse_thread/thread/ad0294c057ddc462/6b9b4092034359c4?show_docid=6b9b4092034359c4](http://groups.google.com/group/sage-support/browse_thread/thread/ad0294c057ddc462/6b9b4092034359c4?show_docid=6b9b4092034359c4) for the original request.  

Probably the best thing to do is have both plotting of lines and individual points using polar coordinates as options.  This should not be too hard, but should be named consistently with other plotting functions.


---

Comment by kcrisman created at 2009-09-28 12:25:12

Changing type from defect to enhancement.


---

Comment by jason created at 2009-09-28 13:27:58

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
