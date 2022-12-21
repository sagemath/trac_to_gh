# Issue 9840: Make Qhull an optional package

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2010-08-30 16:52:38

Assignee: mhampton

CC:  novoselt vbraun mvngu schilly mhansen jdemeyer

Keywords: polyhedra, qhull, convex, Delaunay, Voronoi

From the README.txt of Qhull:

Qhull computes convex hulls, Delaunay triangulations, Voronoi diagrams,
furthest-site Voronoi diagrams, and halfspace intersections about a point.
It runs in 2-d, 3-d, 4-d, or higher.  It implements the Quickhull algorithm
for computing convex hulls.   Qhull handles round-off errors from floating
point arithmetic.  It can approximate a convex hull.

The program includes options for hull volume, facet area, partial hulls,
input transformations, randomization, tracing, multiple output formats, and
execution statistics.

First attempt at a spkg is at:

[http://sage.math.washington.edu/home/mhampton/qhull-2010.1.spkg](http://sage.math.washington.edu/home/mhampton/qhull-2010.1.spkg)


---

Comment by mhampton created at 2010-08-30 17:39:40

Changing status from new to needs_review.


---

Comment by mhampton created at 2010-10-20 01:54:59

This doesn't require much review - can someone take a look?
All this spkg does is install qhull.  I have tested on OS X 10.6 and 10.5 and linux.


---

Comment by vbraun created at 2010-10-20 11:51:32

Looks good to me! 

Its a bit odd that qhull uses no buildsystem except for a bare-bones makefile, but then they don't use any external library nor build a shared library. Still, there are a lot of #ifdef's strewn around the source code. In any case, I'm in favor of having it as an optional package.


---

Comment by vbraun created at 2010-10-20 11:51:32

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-11-01 10:39:50

Harald, Mike, or Minh, could you please add

 http://sage.math.washington.edu/home/mhampton/qhull-2010.1.spkg

as an optional package?


---

Comment by mvngu created at 2010-11-01 10:48:40

Replying to [comment:6 mpatel]:
> Harald, Mike, or Minh, could you please add
> 
>  http://sage.math.washington.edu/home/mhampton/qhull-2010.1.spkg
> 
> as an optional package?

Done. See the updated optional spkg page

http://www.sagemath.org/packages/optional/

The new package is now being mirrored.


---

Comment by jdemeyer created at 2010-11-01 11:21:53

Resolution: fixed
