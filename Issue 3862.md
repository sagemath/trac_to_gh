# Issue 3862: axes in plot3d broken

Issue created by migration from Trac.

Original creator: mclean

Original creation time: 2008-08-14 22:27:04

Assignee: was

CC:  kcrisman

Keywords: plot3d, axes

Example:

```
var('x')
var('y')
plot3d(cos(x) + sin(y), (x, -2,1), (y, -2,1), axes = True)
```


At least one axis is in the right location, the other two...

Translating coordinates into jmol seems to be difficult, so maybe this is the reason?



---

Comment by jason created at 2009-02-10 19:40:51

The fix is to put `axes molecular` in the jmol script.  You can see the fix by right-clicking, selecting "console", and then entering the `axes molecular` command.


---

Comment by jason created at 2009-02-10 19:54:49

The attached patch makes the axes centered at the origin.


---

Comment by jason created at 2009-02-10 19:57:39

Assigning this to sage-3.3 will get mabshoff's attention, probably before he comes back on IRC :).  Is this trivial enough to get in?  It corrects a very annoying thing that bothers me when trying to teach calculus and graphing things in 3d.


---

Comment by jason created at 2009-02-10 21:19:21

Okay, never mind.  Carl Witty pointed out that this ticket deals with the *Sage* axes, not the jmol axes.  I'm posting this patch up at #5229 and retracting my claim of a fix here.
