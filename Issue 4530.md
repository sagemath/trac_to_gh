# Issue 4530: Implement plots with logarithmic scale

Issue created by migration from Trac.

Original creator: ronanpaixao

Original creation time: 2008-11-15 19:01:25

Assignee: somebody

Keywords: plot log scale

Currently plot() has no option to use logarithmic scales.

One workaround is to use matplotlib directly, with its semilogy(), semilogx() and loglog() functions, but that wouldn't produce plots with the customisations implemented in sage.
Another workaround is messing with the plot figure like:


```python
import pylab
p=plot(x,marker='.')
f=pylab.figure()
f.gca().set_xscale('log')
p.save(figure=f)
```


But that creates two problems:

 * The first problem is that the adaptive choosing of points just considers linear scale, so the points get too much spaced apart in the beginning of the plot and too close in the end.
 * The second problem relates to the axis, which, for the same reason, isn't located right.

Also, this requires the user to know how to deal with figures, which is not directly exposed by sage.

There are some possibilities to fix that:
 1. Make plot() detect if the figure changes the scales and modify the adaptive algorithm and the axis codes accordingly
 2. Create a kwarg to tell plot() to implement the scale-change internally
 3. Create other functions to use loglog(), semilogx() and semilogy()
 4. Many (or all) of the above together, since they aren't mutually exclusive

From what I noticed, Mathematica implements the separate functions way, but it may be better to fix the issue in plot() itself and if the other functions are wanted, just make it so that they call plot() with the correct arguments


---

Comment by ronanpaixao created at 2008-11-15 19:01:48

"Wrong" sage plot with log scale


---

Comment by ronanpaixao created at 2008-11-15 19:03:48

Resolution: duplicate


---

Attachment

Duplicate of bug #4529 (Submitted two times)
