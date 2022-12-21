# Issue 5134: Polyhedron: conversion from V-form to H-form fails if no extreme point is given

Issue created by migration from Trac.

Original creator: sbarthelemy

Original creation time: 2009-01-30 01:37:00

Assignee: mhampton

CC:  mhampton

Let's consider the first diagonal in `R^2` as a polyhedron. It has one extreme point (the origin) and one ray.
It can be defined in sage in V-form and converted to H-form as shown

```
sage: p1v1r = Polyhedron([This is the Trac macro *0,0* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#0,0-macro),[This is the Trac macro *1,1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1,1-macro))
sage: p1v1r
A Polyhedron with 1 vertex with 1 rays.
sage: p1v1r.ieqs()
[[1, 0, 0], [0, 1, 0]]
sage: p1v1r.linearities()
[This is the Trac macro *0, -1, 1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#0, -1, 1-macro)
```


the H-form can be read as

```
p1v1r = { (x,y) such that
1 + 0*x + 0*y >= 0 and 
1 + 1*x + 0*y >= 0 and
1 - 1*x + 1*y >= 0
```


Sage also allows us to define the polyhedron without the vertex

```
sage: p0v1r = Polyhedron([], [This is the Trac macro *1,1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1,1-macro))        
sage: p0v1r
A Polyhedron with 1 vertex.
sage: p0v1r.ieqs()                      
[]
sage: p0v1r.linearities()               
[]
```


However, then
 1. the _repr_() text is different
 2. the conversion to H-form failed

problem 2 comes from cdd which requires to be given the extreme point. We could fix it by adding the point before calling cdd.

However, from a theorical point of view, I think that it would also make sense to always require at least one vertex:

One can consider the polyhedron as a region of an euclidean space. In such a case, vertices are *points* and rays are * free vectors*. Then one would always require at least one point.

What do you think?


---

Comment by mabshoff created at 2009-01-30 01:50:44

Please remember to assign a milestone for each ticket opened.

Cheers,

Michael


---

Comment by mhampton created at 2009-11-13 03:16:18

I think this will be addressed by #7109 once it is done.  If a ray is entered without a vertex, the current behavior is to assume that the ray starts at the origin.  I think this is reasonable.


---

Comment by novoselt created at 2010-04-03 14:43:44

Changing status from new to needs_info.


---

Comment by novoselt created at 2010-04-03 14:43:44

Should this ticket be closed now that #7109 is merged? Current outputs are different from the ones described here and as I understand now both representations are computed during construction and are always correct.


---

Comment by mhampton created at 2010-04-03 19:12:43

Yes, I think it can be closed.


---

Comment by mhampton created at 2010-04-03 19:12:43

Resolution: fixed
