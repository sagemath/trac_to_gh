# Issue 9188: lattice_polytope.facet_normal bug with polytopes of less that full dimension

Issue created by migration from https://trac.sagemath.org/ticket/9188

Original creator: vbraun

Original creation time: 2010-06-08 10:39:56

Assignee: mhampton

CC:  novoselt

In general, `lattice_polytope._embedding_matrix` is not orthogonal. But `facet_normal()` implicitly makes this assumption by embedding the normals (which live in the dual vector space) by the transpose of the `_embedding_matrix`. 

Here is an example of the incorrect result:

```
sage: lp = LatticePolytope(matrix([[1,1,-1,0],[1,-1,-1,0],[1,1,1,0],[3,3,3,0]]))
sage: lp.vertices()
[ 1  1 -1  0]
[ 1 -1 -1  0]
[ 1  1  1  0]
[ 3  3  3  0]
sage: lp.facet_normal(0)
(-1, 0, 1, 3)
sage: lp.vertices() * lp.facet_normal(0)
(-2, -2, 0, 0)
sage: lp.facet_constant(0)
-9
```

If `lp.facet_normal(0)` would define a facet then its equation would be satisfied at 3 out of 4 vertices. 

The attached patch fixes this issue. A scale factor for the dual embedding is introduced to keep the facet normal coordinates integral. Moreover, a suitable doctest is added.

NOTE: This bug impacts the toric variety code under development in #8986, #8987:

```
sage: c = Cone([(1,0,0,0),(0,1,0,0),(0,0,1,0)])
sage: c.faces()
((0-dimensional face of 3-dimensional cone,), (1-dimensional face of 3-dimensional cone, 1-dimensional face of 3-dimensional cone, 1-dimensional face of 3-dimensional cone), (2-dimensional face of 3-dimensional cone, 2-dimensional face of 3-dimensional cone, 2-dimensional face of 3-dimensional cone), (3-dimensional face of 3-dimensional cone,))
sage: c = Cone([(1,1,1,3),(1,-1,1,3),(-1,-1,1,3)])
sage: c.faces()
((0-dimensional face of 3-dimensional cone,), (2-dimensional face of 3-dimensional cone,), (3-dimensional face of 3-dimensional cone,))
```




---

Comment by vbraun created at 2010-06-08 10:51:43

Changing status from new to needs_review.


---

Comment by vbraun created at 2010-06-08 11:48:49

I missed two doctests that were failing; Some of the old doctests actually did give the wrong facet normals :-) Also, I improved my new doctest to also check the `facet_constant()`.


---

Comment by novoselt created at 2010-06-08 15:08:03

Changing assignee from mhampton to novoselt.


---

Comment by novoselt created at 2010-06-08 15:08:03

This is very embarrassing... Will look over and take care of propagated errors.


---

Comment by vbraun created at 2010-06-08 18:45:07

I forgot one more transposition of a matrix %-)  This version should be correct now. Added another doctest.


---

Attachment

Updated patch


---

Comment by novoselt created at 2010-06-08 18:49:23

Yeap, the first version was definitely wrong...


---

Comment by novoselt created at 2010-06-08 20:46:30

Apply on top of the original patch.


---

Attachment

OK, my patch looks big, but the only real change to the original is taking the absolute value of the dual scaling factor, so that normals remain inner.

In addition I (hopefully) made doctests more clear, since they do appear in the documentation. Polytopes are now created using coordinates of points with all the necessary transpositions after that. I also made doctest lines shorter for better looks of the documentation.

I have changed "parallel" to "orthogonal to integer kernel" in the description of normals (and now I do remember that I didn't like this "parallel" when I wrote it...).

If you are fine with all these changes, I will switch it to positive review. Thank you for catching this bug!


---

Comment by vbraun created at 2010-06-08 21:16:47

Good idea to make sure that the scaling factor is positive. I also like your work on the doctests. Looks good to me!

Note to release manager: apply both patches in order!


---

Comment by novoselt created at 2010-06-08 21:26:11

Changing status from needs_review to positive_review.


---

Comment by novoselt created at 2010-06-08 21:31:06

Patch at #8986 still applies fine and does not expose any errors in doctests, so let's leave it as is. I will add your example from this ticket into the next patch for #8987 which I am working on now.


---

Comment by mpatel created at 2010-07-20 08:47:31

Resolution: fixed
