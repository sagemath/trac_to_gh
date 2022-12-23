# Issue 3379: error in plotting 3d polytopes

Issue created by migration from https://trac.sagemath.org/ticket/3379

Original creator: mhansen

Original creation time: 2008-06-06 23:00:02

Assignee: mhampton

sage: p = LatticePolytope(m, compute_vertices=True)
sage: m = matrix([[0,0,0],[0,1,1],[1,0,1],[1,1,0]]).transpose()
sage: p = LatticePolytope(m, compute_vertices=True)
sage: p.plot3d()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/mike/temp/natalie/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/geometry/lattice_polytope.py in plot3d(self, show_facets, facet_opacity, facet_color, show_edges, edge_thickness, edge_color, show_vertices, vertex_size, vertex_color, show_points, point_size, point_color, show_vindices, vindex_color, show_pindices, pindex_color, index_shift)
   1447         if show_points:
   1448             pplot += point3d(self.points().columns(copy=False)[self.nvertices():],
-> 1449                         size=point_size, rgbcolor=point_color)
   1450         if show_pindices == None:
   1451             show_pindices = show_points

/opt/sage/local/lib/python2.5/site-packages/sage/plot/plot3d/shapes2.py in point3d(v, size, **kwds)
    506     else:
    507         A = sum([Point(z, size, **kwds) for z in v])
--> 508         A._set_extra_kwds(kwds)
    509         return A
    510     

AttributeError: 'int' object has no attribute '_set_extra_kwds'


---

Comment by mhansen created at 2008-06-06 23:01:46

This is occurs because it assumes that "self.points().columns(copy=False)[self.nvertices():]" does not return an empty list.

```
> /opt/sage/local/lib/python2.5/site-packages/sage/geometry/lattice_polytope.py(1449)plot3d()
   1448             pplot += point3d(self.points().columns(copy=False)[self.nvertices():],
-> 1449                         size=point_size, rgbcolor=point_color)
```

A workaround is to use p.plot3d(show_points=False) so that it doesn't hit that code.


---

Comment by mhampton created at 2008-06-08 12:51:48

Changing status from new to assigned.


---

Attachment

Addresses problem found by Mike Hansen


---

Comment by mhampton created at 2008-06-08 14:54:05

I did the simplest possible workaround, as suggested by Mike.  Other graphics components in this code are handled somewhat differently, so it did not appear that similar fixes were needed elsewhere.  Patch is attached.


---

Comment by mhampton created at 2008-06-08 14:54:05

Changing assignee from mhampton to mhansen.


---

Comment by mhampton created at 2008-06-08 14:54:05

Changing status from assigned to new.


---

Comment by craigcitro created at 2008-06-15 22:02:52

Changing keywords from "" to "editor_mhansen".


---

Attachment


---

Comment by mhansen created at 2008-06-19 20:24:02

Nick Alexander went over this with me and gave it positive review.


---

Comment by mabshoff created at 2008-06-23 12:24:18

Resolution: fixed


---

Comment by mabshoff created at 2008-06-23 12:24:18

Merged 3379.patch in Sage 3.0.4.alpha0
