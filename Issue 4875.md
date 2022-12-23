# Issue 4875: Polyhedron.show(fill=True) fails

Issue created by migration from https://trac.sagemath.org/ticket/4875

Original creator: abergeron

Original creation time: 2008-12-24 18:51:50

Assignee: was

CC:  wcauchois abergeron mhampton

This is what I get:


```
sage: Polyhedron(vertices = [[1, 2, 3], [0,1,0], [1,1,1]]).show(fill=True)
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

[snip IPython layers ...]

/Volumes/Place/anakha/Applications/sage-3.2.2/local/lib/python2.5/site-packages/sage/plot/plot3d/base.so in sage.plot.plot3d.base.Graphics3d.__repr__ (sage/plot/plot3d/base.c:1976)()

/Volumes/Place/anakha/Applications/sage-3.2.2/local/lib/python2.5/site-packages/sage/plot/plot3d/base.so in sage.plot.plot3d.base.Graphics3d.show (sage/plot/plot3d/base.c:8919)()

/Volumes/Place/anakha/Applications/sage-3.2.2/local/lib/python2.5/site-packages/sage/plot/plot3d/base.so in sage.plot.plot3d.base.Graphics3d.export_jmol (sage/plot/plot3d/base.c:4230)()

/Volumes/Place/anakha/Applications/sage-3.2.2/local/lib/python2.5/site-packages/sage/plot/plot3d/base.so in sage.plot.plot3d.base.Graphics3dGroup.jmol_repr (sage/plot/plot3d/base.c:10166)()

/Volumes/Place/anakha/Applications/sage-3.2.2/local/lib/python2.5/site-packages/sage/plot/plot3d/base.so in sage.plot.plot3d.base.TransformGroup.jmol_repr (sage/plot/plot3d/base.c:11940)()

/Volumes/Place/anakha/Applications/sage-3.2.2/local/lib/python2.5/site-packages/sage/plot/plot3d/base.so in sage.plot.plot3d.base.TransformGroup.jmol_repr (sage/plot/plot3d/base.c:11940)()

/Volumes/Place/anakha/Applications/sage-3.2.2/local/lib/python2.5/site-packages/sage/plot/plot3d/index_face_set.so in sage.plot.plot3d.index_face_set.IndexFaceSet.jmol_repr (sage/plot/plot3d/index_face_set.c:6298)()

RuntimeError: 

```


I will investigate after Christmas, unless someone fixes this by then.


---

Comment by abergeron created at 2008-12-24 19:41:19

Turns out I need this sooner, so here I go.

It seems this is a really weird cython bug.

The last function shown in the traceback (jmol_repr) call _seperate_creases.  But that call sometimes returns NULL (signaling an error) without passing through the error path (and adding itself to the traceback).  

I suspect a macro doing a return since there are no other returns than the last one in the code.  I have verified the control flow does not pass through the final block by adding a printf() just before the return but when the bug is triggered, it does not print anything.

Also this bug seems intermittent.  I often have to repeat the offending line 3 or 4 times until it triggers.


---

Comment by wcauchois created at 2009-03-04 07:04:55

This bug was hard to track down! But I believe the root cause is in Polyhedron.render_solid(), when the method gives invalid faces to IndexFaceSet. This causes issues later on, inside IndexFaceSet, when certain CPython methods with little to no error checking index into those faces.

These faces are incorrect because Polyhedron.triangulated_facial_incidences() does not properly triangulate the facial incidences. Look at this:


```
sage: Polyhedron(vertices = [[1, 2, 3], [0,1,0], [1,1,1]]).triangulated_facial_incidences()
[[0, [0, 2]], [1, [0, 1]], [2, [1, 2]]]
```


Triangles in 3-space should consist of 3 vertices, not 2!

triangulated_facial_incidences() naively handles the case where `vert_number != self.dim()` (see polyhedra.py:678) by simply appending the original facial incidence.

The output from facial_incidences() looks like this:


```
sage: Polyhedron(vertices = [[1, 2, 3], [0,1,0], [1,1,1]]).facial_incidences()
[[0, [0, 2]], [1, [0, 1]], [2, [1, 2]]]
```


Just FYI, the facial incidences are computed using cddlib. Here's a log of Sage's interaction with cddlib:


```
sage: P = Polyhedron(vertices = [[1, 2, 3], [0,1,0], [1,1,1]])
sage: vert_to_ieq(P._vertices, rays=P._rays, cdd_type=P._cdd_type, verbose=True)
V-representation
begin
3 4 rational
1 1 2 3 
1 0 1 0 
1 1 1 1 
end


Input is a V-representation
H-representation
linearity 1  4
begin
 4 4 rational
 1 -1 0 0
 1 1 -1 0
 -1 0 1 0
 2 -1 -2 1
end

V-representation
begin
 3 4 rational
 1 1 2 3
 1 0 1 0
 1 1 1 1
end

Here is the incidence list:
begin
  4    3
 1 2 : 1 3 
 2 2 : 1 2 
 3 2 : 2 3 
 4 3 : 1 2 3 
end

Here is the adjacency list:
begin
  4    4
 1 2 : 2 3 
 2 2 : 1 3 
 3 2 : 1 2 
 4 0 : 
end

A Polyhedron with 3 vertices.
```


I would love to fix this bug, but unfortunately I don't have the mathematical knowledge to improve triangulated_facial_incidences(). Hopefully now that the source of the bug is clear, someone with more intimate knowledge of polyhedra can fix it!


---

Comment by wcauchois created at 2009-03-04 07:08:26

Oh, here's an example of manually altering triangulated_facial_incidences() so that show(fill=True) works:

```
P = Polyhedron(vertices = [[1, 2, 3], [0,1,0], [1,1,1]])
P.triangulated_facial_incidences()
# the method caches its result in this private variable
P._triangulated_facial_incidences = [[0, [0, 1, 2]]]
P.show(fill=True)
```



---

Comment by mhampton created at 2009-03-05 13:38:22

The problem is really that 2D polyhedra in 3D are not being handled well.  The triangulation is correct - you are constructing a 2D object, whose "faces" are its edges.  But for rendering, we should special-case this, and if the intrinsic dimension is 2 then we need to triangulate differently.

I will try to fix this today if I can find the time.
-M. Hampton


---

Attachment

special casing of 2d polytopes in 3d


---

Comment by mhampton created at 2009-03-21 04:14:50

Attached patch should fix the problem.  This issue is simpler than it first appeared, I think.


---

Comment by mhampton created at 2009-03-21 17:17:38

Changing assignee from was to mhampton.


---

Comment by mhampton created at 2009-03-21 17:17:38

Changing status from new to assigned.


---

Comment by dperkinson created at 2009-05-20 19:14:12

I applied the patch to Sage Version 4.0.alpha0, Release Date: 2009-05-15.  It passes all the doctests in sage/geometry/, and works with several other examples I tried.  So the show method now works with 2d polyhedra in 3d.  There is still a problem with displaying 1d polyhedra in 3d, but that wasn't the purpose of this patch.

By the way, this patch plays well with trac_5581_rebase.patch, i.e., applying these patches in either order, the doctests in sage/geometry all pass.


---

Comment by mabshoff created at 2009-05-21 02:06:59

Merged in Sage 4.0.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-21 02:06:59

Resolution: fixed
