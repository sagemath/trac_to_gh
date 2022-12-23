# Issue 3215: optional lrs package

Issue created by migration from https://trac.sagemath.org/ticket/3215

Original creator: mhampton

Original creation time: 2008-05-16 02:34:09

Assignee: somebody

Keywords: polyhedra, convex hull, polytope, geometry, lrs

lrs (linear reverse search) is an alternate algorithm to cddlib for changing from a vertex to facet/inequality description of a polyhedron.  For some polyhedra, lrs is much faster than cddlib, and for others cddlib is better.  It is difficult to determine in advance which will be better.  Since lrs is a small and easy to compile program, I think it should be included in sage.  Eventually there should be an option in polytope code to use lrs instead of cddlib.  This ticket is only concerned with making the functionality available, not in altering the polyhedral code.
A candidate spkg is available at: 
http://www.d.umn.edu/~mhampton/lrs-4.2b.p0.spkg


---

Comment by craigcitro created at 2008-06-15 22:00:08

Changing keywords from "polyhedra, convex hull, polytope, geometry, lrs" to "polyhedra, convex hull, polytope, geometry, lrs, editor_mhansen".


---

Comment by mhansen created at 2008-06-19 20:00:33

This builds fine for me in about a minute.


---

Comment by mabshoff created at 2008-06-25 09:19:00

Resolution: fixed


---

Comment by mabshoff created at 2008-06-25 09:19:00

Merged in Sage 3.0.4.alpha1
