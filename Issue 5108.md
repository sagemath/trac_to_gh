# Issue 5108: Add infinite planes to Sage 3d graphics

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-01-26 21:37:51

Assignee: was


```
> Is there an easy way to draw infinite planes in Sage, given, say, the
> > normal vector and a point on the plane?  Of course, you can draw them
> > using parametric_plot3d, but that requires me specifying a range, etc.
> > It also seems like it wouldn't be terribly efficient, since the infinite
> > plane could be represented with a jmol plane primitive or a Tachyon
> > plane primitive, which is presumably more efficient than a bunch of
> > triangles.  It seems like it would be handy to have a primitive for an
> > infinite plane.
> >
> > I'm posting to sage-devel because I suspect there is not a primitive for
> > an infinite plane.
> >
> > I imagine that such a primitive would look something like:
> >
> > plane(normal, point=(0,0,0))
> >
> > If it was drawn by itself, it would pick some default bounding box,
> > centered around the point.  If it wasn't drawn by itself, it would just
> > fit itself inside of whatever the current bounding box for everything
> > else was.  Or maybe it would still specify a bounding box around the
> > point, since that is likely to be a point of interest to the viewers,
> > but the plane would grow to fill the entire bounding box constructed in
> > a composite graphic.

This isn't in Sage, and it would be very useful if somebody (=you, of
course) were to add it.  You would want to look at the
plot3d/platonic.py file to get an idea how to make index_face_set.pyx
do what you want.
```



---

Comment by jason created at 2009-01-26 21:38:47

Changing assignee from was to jason.


---

Comment by jason created at 2009-01-26 21:38:47

Changing status from new to assigned.
