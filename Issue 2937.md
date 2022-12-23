# Issue 2937: defects in polyhedra, 3d-gfan rendering

Issue created by migration from https://trac.sagemath.org/ticket/2937

Original creator: mhampton

Original creation time: 2008-04-15 23:01:07

Assignee: mhampton

Keywords: polyhedra, convex hull, polytope, gfan

Currently there are major issues in polyhedra.py (see #2844), which also affect 3d rendering of Groebner gfans - for example, the following doesn't work:

sage: R4.<x,y,z,w> = PolynomialRing(QQ,4)
sage: idnp = R4.ideal([x*y*z+x<sup>2*z-x*y,x*w</sup>2-z,x*w^4+x*z])
sage: gfnp = idnp.groebner_fan()
sage: a = gfnp.render3d()

I (Marshall Hampton) am actively fixing these issues but I don't have a patch yet.  There are two main problems: 1) I didn't handle unbounded polyhedra well (which is what causes the above problem) and 2) properties such as facial_incidences can be wrong because of vertex reordering by cddlib.  I should have a patch that fixes those problems and adds some rendering enhancements by 5/1/2008 (or earlier).


---

Comment by mhampton created at 2008-04-15 23:04:40

Changing status from new to assigned.


---

Comment by mhampton created at 2008-04-15 23:04:40

Once again, this time with feeling!:

Currently there are major issues in polyhedra.py (see #2844), which also affect 3d rendering of Groebner gfans - for example, the following doesn't work:


```
sage: R4.<x,y,z,w> = PolynomialRing(QQ,4) 
sage: idnp = R4.ideal([x*y*z+x2*z-x*y,x*w2-z,x*w4+x*z]) 
sage: gfnp = idnp.groebner_fan() 
sage: a = gfnp.render3d()
```


I (Marshall Hampton) am actively fixing these issues but I don't have a patch yet. There are two main problems: 1) I didn't handle unbounded polyhedra well (which is what causes the above problem) and 2) properties such as facial_incidences can be wrong because of vertex reordering by cddlib. I should have a patch that fixes those problems and adds some rendering enhancements by 5/1/2008 (or earlier).


---

Comment by mabshoff created at 2008-05-17 21:36:33

Resolution: fixed


---

Comment by mabshoff created at 2008-05-17 21:36:33

This issue has been fixed by merging #2716:

```
[22:34] <mhampton> mabshoff: I just figured out why I was confused.  #2716 took long 
enough to get in that you had me rebase it, and I put in stuff that I had meant for #2937
[22:34] <-- roed has left this server (Read error: 110 (Connection timed out)).
[22:34] <mhampton> So #2937 can be closed
```


Cheers,

Michael
