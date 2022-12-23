# Issue 3861: automatic line smoothing shouldn't be automatic, or should at least be documented

Issue created by migration from https://trac.sagemath.org/ticket/3861

Original creator: mclean

Original creation time: 2008-08-14 22:19:12

Assignee: was

CC:  kcrisman slelievre

Keywords: line3d, Line, smoothing, corner_cutoff

line3d for instance calls Line in 

/usr/local/sage/3.0.6/devel/sage/sage/plot/plot3d/shapes2.py

Which automatically applies some smoothing using corner_cutoff, which is buggy and poorly documented as in Ticket 3859:
http://trac.sagemath.org/sage_trac/ticket/3859

(See above Ticket for an example of how this can be bad.)

It is important that I plot lines directly, and automatic smoothing should either not be automatic, or should be documented,
even for functions that do not reference the smoothing directly like in Line3d.  Perhaps a 'smooth' keyword is more informative than the undocumented corner_cutoff.

The smoothing is done in the Line class object, and not in pmol, so it can (and should!) be selectively applied.

Fixing the referenced ticket is a workaround (set corner_cutoff = 1), but is very clunky, and currently does not even work.


---

Comment by robertwb created at 2008-08-16 01:23:46

I like the idea of a smoothnes parameter, 0=False meaning don't smooth at all, 1=True being some good default, and something higher (say 2) to forceable splite the whole thing. 

I agree it could be better documented, but I think smoothing is very useful when you are trying to visualize curves. Of course, if you're plotting stock data then it is really bad.


---

Comment by jason created at 2010-04-27 15:25:42

I also agree with Robert.  Notice also that:


```

sage: my_points=[[0,0,0],[1,0,0],[0,1,0]]
sage: my_points_tuples=map(tuple,my_points)
sage: sage.plot.plot3d.shapes2.Line(my_points,corner_cutoff=0)
Traceback (most recent call last):
...
TypeError: unhashable type: 'list'

sage.plot.plot3d.shapes2.Line(my_points_tuples,corner_cutoff=0) #works
sage: sage.plot.plot3d.shapes2.Line(my_points_tuples, corner_cutoff=1)
Traceback (most recent call last):
...
TypeError: 'NoneType' object is unsubscriptable
sage: sage.plot.plot3d.shapes2.Line(my_points_tuples, corner_cutoff=.999) # works

```



---

Comment by jason created at 2010-04-27 15:27:16

That last error is already #3859


---

Comment by slelievre created at 2021-04-27 22:07:44

Related:

- #3546: line3d with jmol draws curves instead of straight lines
