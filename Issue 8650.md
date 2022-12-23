# Issue 8650: Extreme faces of Polyhedra are inconsistent

Issue created by migration from https://trac.sagemath.org/ticket/8650

Original creator: novoselt

Original creation time: 2010-04-04 19:23:02

Assignee: mhampton

Let's look at the first face of each dimension of a polyhedron:

```
for lset in polytopes.cross_polytope(2).face_lattice().level_sets():
    print lset[0]
```

The result is 

```
(None, None)
((0,), (1, 2))
((1, 2), (3,))
((0, 1, 2, 3), (0, 1, 2, 3))
```

where the first tuple (None, None) corresponds to the empty face of the polytope. The first element gives generating vertices of this face (there are None). The second one should give all facets that contain this face. This should be the set of all facets of the polytope, not None. Similarly, for the last face, i.e. the whole polytope, we need to list all vertices belonging to this face (they are correctly listed), and all facets containing the polytope - there should be None.

While it should be easy to fix, I don't quite understand the code of face_lattice, so maybe someone else can do this...


---

Comment by mhampton created at 2010-04-04 21:33:50

Oops.  I wrote face_lattice, so this is my fault.  Thanks for pointing it out.  I think I can fix it pretty soon (hopefully today).


---

Comment by mhampton created at 2010-04-04 22:20:54

Changing status from new to needs_review.


---

Attachment

OK, I think the attached patch corrects things.


---

Attachment

Apply this patch only


---

Comment by novoselt created at 2010-04-05 03:18:03

Changing status from needs_review to positive_review.


---

Comment by novoselt created at 2010-04-05 03:18:03

Thank you! I have added the code above to the TESTS section.


---

Comment by jhpalmieri created at 2010-04-16 18:56:29

Merged "trac_8650_fix_face_lattice_in_polyhedra.patch" in 4.4.alpha0.


---

Comment by jhpalmieri created at 2010-04-16 18:56:29

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-18 03:07:33

See #8709 for a followup.


---

Comment by novoselt created at 2010-04-18 04:10:26

And #8656.
