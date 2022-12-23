# Issue 6309: miscellaneous additions to simplicial complex class; clique complex method for graphs

Issue created by migration from https://trac.sagemath.org/ticket/6309

Original creator: bantieau

Original creation time: 2009-06-16 06:37:33

Assignee: bantieau

First, I cached the graph() of a simplicial complex. These get very big and tedious to compute as the complexes get bigger.

I added the method clique_complex to the graph class. This returns the largest simplicial complex whose 1-skeleton is the given graph. Such simplicial complexes are called flag complexes.

I added is_flag_complex, is_connected, and remove_facet methods to the simplicial complex class.


---

Attachment


---

Comment by bantieau created at 2009-06-17 00:50:05

tweak to be compatibe with #6141, which changes facets to facets().


---

Attachment

The patch doesn't apply cleanly; does this depend on #6099?

The `remove_facet` method needs some doctests.  It also seems to have a line using self.facets, not self.facets().  Would it in fact make sense to just combine this with `remove_face`?  That is, rewrite `remove_face`: first check if the face being removed is a facet, in which case use your code.  Otherwise, use the old, presumably slower, code. I don't think we need two separate methods.  And before removing it, you should probably check that it's actually a facet: make sure it's not a face of any other facet.

Similarly, the `is_connected` method might fail if the complex was constructed with `maximality_check` False.

You might check your `is_connected` method for speed -- compare to this:

```
return self.graph().is_connected()
```

I expect that yours will be faster, even after the maximality check.  If you keep your code, you could put in a doctest like

```
sage: K = simplicial_complexes.RandomComplex(8,1)     [or some other simplicial complex]
sage: K.is_connected() == K.graph().is_connected()
True
```



---

Comment by bantieau created at 2009-06-17 19:06:42

It does not (shouldn't) rely on 6099. It applied cleanly for me to 4.0.2.rc1 once I created the second patch.

I agree with merging remove_facet() with remove_face(). And, I will try to make things robust with the maximality_check=False.

As for is_connected(), consider the following behavior:

```
sage: T = SimplicialComplex(5,[[1,2,3],[4]])
sage: T.graph().is_connected()
True
sage: T.is_connected()
False
```

Which should be correct?


---

Comment by jhpalmieri created at 2009-06-17 19:39:43

It looks like there's a bug in the graph method -- it shouldn't ignore isolated vertices.  I'll attach a patch for it.  

When I applied the patch, the last part didn't apply because it couldn't find the line

```
     return SimplicialComplex(sub_vertex_set,faces,maximality_check=True) 
```

which I think is added by #6099.


---

Attachment


---

Comment by bantieau created at 2009-11-06 19:13:40

Changing status from needs_work to needs_review.


---

Attachment

Added a hopefully final patch: 6309-merged. This contains the above patches, and merges well on a fresh branch of 4.2.

The methods graph() and remove_face() now both work correctly. My method for is_connected() was completely wrong. So, for the moment, is_connected() calls graph().is_connected(). This will not give the correct answer for simplicial complexes created with maximal_check=False.

I also updated the changes to graphs/graph.py to reflect the depreciation of the cliques() method.


---

Attachment

apply on top of 6309-merged.patch


---

Comment by jhpalmieri created at 2009-11-06 21:11:14

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2009-11-06 21:11:14

Looks good to me.  I'm attaching a referee's patch which fixes a few formatting issues.


---

Comment by jhpalmieri created at 2009-11-06 21:12:00

To the release manager: apply only "6309-merged.patch" and "trac_6309-referee.patch".


---

Attachment


---

Comment by mhansen created at 2009-11-07 06:13:09

I had to merge the above patch as well since the ordering between Simplex objects and Integer objects seems to vary from machine to machine.


---

Comment by mhansen created at 2009-11-07 06:13:09

Resolution: fixed
