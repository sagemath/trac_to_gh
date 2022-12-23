# Issue 2076: Inconsistent coloring of plotted points

Issue created by migration from https://trac.sagemath.org/ticket/2076

Original creator: jmitchell

Original creation time: 2008-02-06 20:04:23

Assignee: was

Keywords: color hue point plot 3

When I call, 

sage: point(((1,1), (2,2), (3,3)), rgbcolor=hue(1), pointsize=30)

I expect to get a plot of 3 red points, but (1,1) is plotted as dark red and the other two points are blue.  So far I've only been able to recreate this issue when only three points are in the tuple.  The rgbcolor value doesn't seem to affect the color of the three plotted points.

I hope to look at the code soon.


---

Comment by was created at 2008-02-07 02:52:43

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

Comment by was created at 2008-02-07 03:07:03

I propose the following:

 1. We upgrade from `matplotlib-0.91.1` to the latest verison, whatever it is.

 2. If this doesn't fix the problem, report it to the matplotlib list.

 3. If that doesn't work, fix the problem !?  Or program around it.


---

Comment by mhansen created at 2008-09-03 00:52:48

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2008-09-03 00:52:48

Changing status from new to assigned.


---

Attachment

This is actually a bug on our part according to the matplotlib 0.98 documentation for scatter.


---

Comment by jason created at 2008-09-04 04:09:19

I've read the matplotlib docs and this looks reasonable.  I don't have a current 3.1.2 tree to test it, though; so half of a positive review (the other half comes from applying it and checking the result of the doctest :).


---

Comment by mabshoff created at 2008-09-22 23:41:59

Jason,

since you now have a 3.1.2 can you do the final review on this? I can run doctests without a problem on 3.1.3.alpha1 to see if anything breaks. 

Cheers,

Michael


---

Comment by jason created at 2008-09-23 00:44:48

The example now works and doctests in plot/*.py pass with the patch applied.  So that's a full positive review, now.


---

Comment by mabshoff created at 2008-09-23 01:18:26

Resolution: fixed


---

Comment by mabshoff created at 2008-09-23 01:18:26

Merged in Sage 3.1.3.alpha1
