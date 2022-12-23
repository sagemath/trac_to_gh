# Issue 9917: triangulate point configurations

Issue created by migration from https://trac.sagemath.org/ticket/9918

Original creator: vbraun

Original creation time: 2010-09-16 11:22:09

Assignee: mhampton

CC:  mhampton novoselt

The attached patch implements triangulations of point configurations in arbitrary dimensions in Sage/Cython/C++ without relying on TOPCOM. 

```
sage: points = PointConfiguration([[0,0],[0,1],[1,0],[1,1],[-1,-1]]);
sage: points
A point configuration in QQ^2 consisting of 5 points. The 
triangulations of this point configuration are assumed to 
be connected, not necessarily fine, not necessarily regular.
sage: triang = points.triangulate()   # find one triangulation       
sage: triang
(<0,1,2>, <0,1,4>, <0,2,4>, <1,2,3>)
sage: triang[0]
(0, 1, 2)
sage: list( points.triangulations() )
[(<0,1,2>, <0,1,4>, <0,2,4>, <1,2,3>), 
 (<0,1,3>, <0,1,4>, <0,2,3>, <0,2,4>), 
 (<1,2,3>, <1,2,4>), 
 (<1,3,4>, <2,3,4>)]
sage: triang.plot(axes=False)                                        
```

The internal implementation covers finding a single triangulation as well as enumerating all triangulations connected to it by bistellar flips. TOPCOM is required to test for regularity and/or to find non-connected triangulations.

While not quite as fast, my limited testing shows the performance to be in the same order of magnitude as TOPCOM:

```
sage: U=matrix([
...      [ 0, 0, 0, 0, 0, 2, 4,-1, 1, 1, 0, 0, 1, 0],
...      [ 0, 0, 0, 1, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0],
...      [ 0, 2, 0, 0, 0, 0,-1, 0, 1, 0, 1, 0, 0, 1],
...      [ 0, 1, 1, 0, 0, 1, 0,-2, 1, 0, 0,-1, 1, 1],
...      [ 0, 0, 0, 0, 1, 0,-1, 0, 0, 0, 0, 0, 0, 0]
...   ])
sage: pc = PointConfiguration(U.columns())
sage: pc.set_engine('internal')
sage: time len(pc.triangulations_list())
CPU times: user 23.26 s, sys: 0.02 s, total: 23.29 s
Wall time: 23.32 s
9623
sage: pc.set_engine('TOPCOM')
sage: time len(pc.triangulations_list())
CPU times: user 7.80 s, sys: 0.13 s, total: 7.93 s
Wall time: 8.37 s
9623
```

See also #8169: include TOPCOM, where an optional spkg is being worked on.


---

Comment by vbraun created at 2010-09-16 11:24:54

Changing status from new to needs_review.


---

Comment by mhampton created at 2011-01-13 01:47:51

Passes tests, coverage, documentation looks good.  Nice work!  I haven't tested with TOPCOM but I don't think that's necessary since everything works without it.


---

Comment by mhampton created at 2011-01-13 01:47:51

Changing status from needs_review to positive_review.


---

Comment by novoselt created at 2011-01-22 21:15:04

For the record:

```
/disk/scratch/novoselt/sage/devel/sage/doc/en/reference/sage/geometry/triangulation/point_configuration.rst:638: WARNING: duplicate citation BSS, other instance in /disk/scratch/novoselt/sage/devel/sage/doc/en/reference/sage/geometry/polyhedra.rst
```

I am not sure what we are supposed to do with this (personally, I like to have references in the file where they are referenced), but the documentation does not build without warnings...


---

Comment by vbraun created at 2011-01-23 05:12:40

See also:

https://groups.google.com/d/topic/sage-devel/26YSkYOztus/discussion

Until there is a proper way of dealing with duplicate references, I think it is best to keep the warning around. The alternatives all suck...


---

Comment by jdemeyer created at 2011-01-26 17:04:11

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-01-26 17:04:11

Replying to [comment:4 novoselt]:
> For the record:
> {{{
> /disk/scratch/novoselt/sage/devel/sage/doc/en/reference/sage/geometry/triangulation/point_configuration.rst:638: WARNING: duplicate citation BSS, other instance in /disk/scratch/novoselt/sage/devel/sage/doc/en/reference/sage/geometry/polyhedra.rst
> }}}
> I am not sure what we are supposed to do with this (personally, I like to have references in the file where they are referenced), but the documentation does not build without warnings...

I'm afraid a Sphinx warning is sufficient reason for needs_work...


---

Attachment

Updated patch


---

Comment by vbraun created at 2011-01-26 22:46:41

Changing status from needs_work to positive_review.


---

Comment by vbraun created at 2011-01-26 22:46:41

Fine, if lack of warnings is more important than usefulness of the documentation. I removed the text of the citation, leaving only the link to the same citation a different module. Now Sphinx doesn't complain any more.


---

Comment by jdemeyer created at 2011-01-27 13:14:51

Resolution: fixed
