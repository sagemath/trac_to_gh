# Issue 9792: Make plot1d function

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2010-08-24 13:24:28

Assignee: jason, was

CC:  jason ppurka

Keywords: one-dimension, plot, graphics

Sometimes it would be nice to have the ability to plot one-dimensional things easily, like solutions to an inequality or something.  This would have just one (horizontal) axis and have options allowing plotting of individual points (perhaps if input is a list) or find a way to plot inequalities (maybe via thicker lines and/or tick marks at appropriate places).  

Ideally, this would add with a 2D `Graphics` object by putting it below it and have the axes align, but this might be too hard to do with matplotlib.


---

Comment by jason created at 2010-08-24 14:26:23

+1 to the idea.  It would be easy to have axes align in matplotlib (it's done all the time), but it might be slightly more difficult to expose that functionality in Sage, where each subplot doesn't know about other subplots.


---

Comment by kcrisman created at 2011-06-12 01:36:48

From a participant in a workshop:

```

Say, if I want to show the multiples of 5 on the number line. How should I do that in SAGE?

For example: points([(5*n,0) for n in [-3..3]]) gives me the y-axis which I don't want
```


jason says, regarding possible solutions,

```
I would just turn axes off and make your own line:

points([(5*n,0) for n in [-3..3]],axes=False)+line((-3,0),(3,0))

You'd have to do your own ticks, though.  You might also set ymin and ymax to something small (ymin=-.01,ymax=.01)

It would be pretty straightforward for us to make an option that turns off axes selectively.  I could imagine an interface like:

axes=False # turn off all axes
axes=True # turn on all axes
axes=[True,False] # turn on horizontal axis, turn off vertical axis

or maybe it should be:

axes='horizontal' # turn on only horizontal axis
axes='vertical' # turn on only vertical axis.
```



---

Comment by kcrisman created at 2011-09-07 12:47:19

#8085 is a duplicate.  See also [this sage-support thread](http://groups.google.com/group/sage-support/browse_thread/thread/ac5b5b42776ee09b/368976a362477233).


---

Comment by kcrisman created at 2012-07-16 13:26:01

Here is a contribution to this issue from user "jaia" at [this ask.sagemath.org question](http://ask.sagemath.org/question/1586/function-for-1-d-plotting):

```
def plot_1d(xmin, xmax, ymin=-1, ymax=1):
p=plot((ymax+ymin)/2, (xmin, xmax), color="black", axes=False) + point((0,ymax), color="white") + point((0,ymin), color="white")
return p
```

used

```
plot_1d(-1,1200,-1,1) + point((0,0), color="black", size=20) + text("0", (0,-0.05), color="black") + point((1000,0), color="black", size=20) + text("K", (1000,-0.05), color="black") + arrow((700, 0), (1000,0)) + arrow((0, 0), (300,0)) + arrow((350, 0), (650,0)) + arrow((1100, 0), (1000,0))
```

