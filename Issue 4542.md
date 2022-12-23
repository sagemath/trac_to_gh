# Issue 4542: polyhedra bug fix and improvments

Issue created by migration from https://trac.sagemath.org/ticket/4542

Original creator: mhampton

Original creation time: 2008-11-17 22:48:10

Assignee: mhampton

Keywords: polytopes

The attached patch fixes some big problems with defining polytopes through inequalities and linearities - defining via vertices has been tested a lot more.  I also added some new functionality for making prisms, pyramids, taking unions and intersections, and a standard 3D polytope, the small rhombicuboctahedron. 




---

Comment by mhampton created at 2008-11-17 22:48:50

patch for polyhedra.py, fixes linearity problem


---

Attachment


---

Comment by cwitty created at 2008-11-23 01:33:53

Looks good; doctests pass.

Positive review.


---

Comment by mabshoff created at 2008-11-23 06:43:06

Resolution: fixed


---

Comment by mabshoff created at 2008-11-23 06:43:06

Merged in Sage 3.2.1.alpha0
