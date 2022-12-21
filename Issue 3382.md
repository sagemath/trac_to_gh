# Issue 3382: Compute Newton polytopes without polymake

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2008-06-08 12:50:15

Assignee: mhansen

Keywords: polytope, polyhedra, polynomials

Currently multivariable polynomials have a newton_polytope method which doesn't work without the optional polymake package installed.  This patch switches this method to using the Sage-native code in geometry/polyhedra.py, which only needs the default cddlib (in the future, this might optionally use lrs as well).  


---

Attachment


---

Comment by craigcitro created at 2008-06-15 22:03:48

Changing keywords from "polytope, polyhedra, polynomials" to "polytope, polyhedra, polynomials, editor_mhansen".


---

Comment by mhansen created at 2008-06-16 05:50:34

Looks good and passes tests for me.


---

Comment by mabshoff created at 2008-06-23 09:34:21

Merged in Sage 3.0.4.alpha0


---

Comment by mabshoff created at 2008-06-23 09:34:21

Resolution: fixed
