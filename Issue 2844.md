# Issue 2844: Polyhedral improvements, round 2

Issue created by migration from https://trac.sagemath.org/ticket/2844

Original creator: mhampton

Original creation time: 2008-04-07 14:44:39

Assignee: somebody

Keywords: polytope, Minkowski sum

I have revamped my new polyhedra module so that it is much, much better.  Minkowski sums are now supported.  This required some minor changes to the 3D rendering in the gfan interface as well.  The module can do just about everything that sage could do through polymake previously - a few more particular polytopes could be predefined.
After this functionality is reviewed, it can be used for making Newton polytopes of multivariable polynomials (and eventually Laurent polynomials as well), but I will put that on a seperate ticket.
In the future, I would like to add more 3D support, better 2D rendering, face lattice computations, and more particular cases.


---

Attachment

adds many polyhedral functions not requiring polymake


---

Comment by mhansen created at 2008-04-07 22:28:22

Nice work!  Applies to 3.0.alpha2 and passes tests for me.


---

Attachment

I added 2844.patch which applies to the current 3.0.alpha3.  Apply it instead.


---

Comment by mabshoff created at 2008-04-08 00:28:50

Merged 2844.patch in Sage 3.0.alpha3


---

Comment by mabshoff created at 2008-04-08 00:28:50

Resolution: fixed
