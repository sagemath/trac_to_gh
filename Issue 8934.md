# Issue 8934: Trivial bug in computing faces of non-full-dimensional lattice polytopes

Issue created by migration from https://trac.sagemath.org/ticket/8934

Original creator: novoselt

Original creation time: 2010-05-08 22:11:05

Assignee: mhampton

CC:  vbraun

Currently computing faces of a non-full-dimensional lattice polytopes causes and exception, because when I was implementing support for such polytopes I missed a parameter in one place. The attached little patch fixes it and adds a doctest for the future.


---

Comment by novoselt created at 2010-05-08 22:18:04

Changing status from new to needs_review.


---

Comment by vbraun created at 2010-05-10 11:00:18

Changing status from needs_review to needs_work.


---

Comment by vbraun created at 2010-05-10 11:00:18

I'm pretty sure you need the double colon in 

```
line 545:"     Check that Trac 8934 is fixed::"
```

or the example will not be typeset correctly.

A special case of non-full-dimensional polytopes is the zero-dimensional case. This one is also broken, but in a slightly different way:

```
sage: p = LatticePolytope(matrix([[0]]))
sage: p.poly_x("i", reduce_dimension=True)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/vbraun/Sage/ToricVariety/<ipython console> in <module>()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/geometry/lattice_polytope.pyc in poly_x(self, keys, reduce_dimension)
   2223                1  -1     2
   2224         """
-> 2225         return self._palp("poly.x -f" + keys, reduce_dimension)
   2226 
   2227     def skeleton(self):

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/geometry/lattice_polytope.pyc in _palp(self, command, reduce_dimension)
    772         if self.dim() == 0:
    773             raise ValueError, ("Cannot run \"%s\" for the zero-dimensional "
--> 774                 + "polytope!\nPolytope: %s") % (command, self)
    775         if self.dim() < self.ambient_dim() and not reduce_dimension:
    776             raise ValueError(("Cannot run PALP for a %d-dimensional polytope " +

ValueError: Cannot run "poly.x -fi" for the zero-dimensional polytope!
Polytope: A lattice polytope: 0-dimensional, 1 vertices.
```

Also, `p.points()` fails for the same reason. It would be great if you could fix this case as well.


---

Attachment


---

Comment by novoselt created at 2010-05-10 19:22:20

I added ":" into the docstring and tried to address some of the issues with 0-dimensional polytopes, namely, it is now possible to ask for points and faces of them. The list of faces in this case is empty, since only proper faces are returned in the other dimensions. In particular, asking for any faces of the given dimension will cause an error, but that seems to be consistent and I have documented it. I also added a synonym "all_facet_equations" for "all_polars", since calling the second one does not make a lot of sense for non-reflexive polytopes (although it will do the job). Thanks a lot for quick reviews!


---

Comment by novoselt created at 2010-05-10 19:22:20

Changing status from needs_work to needs_review.


---

Comment by vbraun created at 2010-05-10 19:52:28

The new patch looks good! I've tried it and it works as expected. Should be committed to Sage asap.


---

Comment by vbraun created at 2010-05-10 19:52:28

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-06 19:32:28

Resolution: fixed
