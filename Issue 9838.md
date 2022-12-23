# Issue 9838: Add dual cone computation

Issue created by migration from https://trac.sagemath.org/ticket/9839

Original creator: novoselt

Original creation time: 2010-08-30 05:49:07

Assignee: mhampton

CC:  vbraun

This patch allows computing dual cones, including non-strictly convex and non-full-dimensional cases. 

The actual work is done in `facet_normals` which now works for non-strictly convex cones as well. The method `base_extend` for quotient lattices was added during one of the implementation attempts and I left it for future use as well (the hope was to create cones in quotient lattices, but it does not work yet).

There is still a dimension 6 limitation stemming from PALP for computing duals and facet normals. This is still our best option for low dimension, but perhaps it would be nice if `facet_normals` caught the exception when PALP does not work and used polyhedra module in this case. Then computing the dual cone and face lattices should work automatically.


---

Attachment


---

Comment by novoselt created at 2010-08-30 05:53:15

Changing status from new to needs_review.


---

Comment by vbraun created at 2010-08-30 12:23:49

I don't like that your lattice now needs to have `self.dual()` implemented:

```
sage: c = Cone([(1,0), [0,1]], lattice = ZZ^2)
sage: c.facet_normals()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/vbraun/opt/sage-4.5.2/devel/sage-main/<ipython console> in <module>()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/geometry/cone.pyc in facet_normals(self)
   1808         """
   1809         if "_facet_normals" not in self.__dict__:
-> 1810             M = self.lattice().dual()
   1811             P = self.lattice_polytope()
   1812             rotate_lifts = not self.is_strictly_convex()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__getattr__ (sage/structure/parent.c:5311)()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2757)()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2629)()

AttributeError: 'FreeModule_ambient_pid_with_category' object has no attribute 'dual'
```

This essentially limits you to `ToricLattice`s now. I think it would be good for `factet_normals()` to use the same lattice otherwise, so `ZZ^n` works as well. 

The rest looks good!


---

Comment by vbraun created at 2010-08-30 15:19:10

The absence of `dual()` also annoyed me in the divisor class stuff which is built on top of `ZZ^n`... So here is a patch. I added a new `cone.lattice_dual()` method which returns the dual toric lattice (if possible) or the original lattice (if not possible).

I'm fine with the current state of affairs, so feel free to set positive review if its ok with you.


---

Comment by novoselt created at 2010-08-30 18:59:15

Great additions for the dual lattice and documentation clarifications!

Just a couple of suggestions: can we
 * name the method `dual_lattice` instead of `lattice_dual` and
 * add to the documentation of this method itself an explanation that "dual lattice" is the same as "just lattice" if it does not have `dual()` method?


---

Comment by vbraun created at 2010-08-30 21:01:43

Updated patch


---

Attachment

Renamed to `dual_lattice` and added documentation.


---

Comment by novoselt created at 2010-08-31 00:27:14

Adjusted version


---

Attachment

Thank you! I caught a broken link and changed a little bit documentation in lines 1743-1749 of the new patch. If it looks OK, please switch to positive review!


---

Comment by vbraun created at 2010-08-31 19:10:46

Looks good. Positive review.

For the release coordinator: Apply 

  1. `trac_9839_add_dual_cone_computation.patch`
  2. `trac_9839_reviewer.2.patch`


---

Comment by vbraun created at 2010-08-31 19:10:46

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-15 09:57:50

Resolution: fixed
