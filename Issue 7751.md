# Issue 7751: Kazhdan-Lusztig polynomials, Bruhat order, and related features [with patch, needs review]

Issue created by migration from https://trac.sagemath.org/ticket/7751

Original creator: bump

Original creation time: 2009-12-22 21:56:00

Assignee: AlexGhitza

CC:  sage-combinat

Keywords: Kazhdan-Lusztig, Bruhat order

This patch includes algorithms for the Bruhat order, Kazhdan-Lusztig polynomials, improvements to the `__repr__` method of WeylGroup elements, and other enhancements.

Some of the methods should be moved to `coxeter_group.py`.

Mike Hansen is working on an interface to coxeter3, which is be able to compute Kazhdan-Lusztig polynomials rather faster. However I think this patch still contains things that are needed.

For discussion see this thread:

http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/d324f6fcb6d2a436?hl=en


---

Comment by bump created at 2009-12-22 22:54:37

Changing component from algebra to combinatorics.


---

Comment by bump created at 2009-12-22 22:54:37

Changing assignee from AlexGhitza to bump.


---

Comment by bump created at 2009-12-23 15:02:03

I made a minor change so that the Kazhdan-Lusztig computation doesn't
hang in the affine case. I've only done much testing for finite Weyl groups
but I suppose it is correct in the affine case.


---

Comment by bump created at 2010-01-03 05:26:12

Changing status from new to needs_review.


---

Comment by bump created at 2010-01-03 05:26:12

I have revised the patch. It now depends on #7753 and #7754. The revised patch makes use of the Bruhat order as implemented in #7753 and makes the Kazhdan-Lusztig polynomials using ``@`cached_method`. Other changes allow the base ring to be a `LaurentPolynomialRing`.

The patch is much faster now, something like 50% faster.


---

Comment by bump created at 2010-01-23 12:49:37

Rebased to Sage 4.3.1.


---

Comment by roed created at 2010-02-09 04:27:37

Changing status from needs_review to needs_work.


---

Comment by roed created at 2010-02-09 04:27:37

Looks good.  Here are a few comments.  After these are addressed, I'll be happy to give this a positive review.

 * `sage/combinat/kazhdan_lusztig.py`
  * typo in your e-mail address.
  * the method of determining KL._base_ring_type seems a little strange.  Why not use is_Polynomial and isinstance(q, LaurentPolynomial)?
  * KazhdanLusztigPolynomial should inherit from SageObject.  That allows pickling, etc.

 * `sage/combinat/root_system/weyl_group.py`
  *In `WeylGroup_gens`, `__classcall_` needs another trailing underscore.  Include a doctest to make sure that this feature works!
  * Can you include a doctest in `WeylGroupElement.__repr__`?  I know it's tested elsewhere, but...

In general, do you have a reason to use `__call__` explicitly, rather than parentheses?  Similarly, you don't need to explicitly call __repr__: using %s in a string will do that for you automatically.


---

Comment by bump created at 2010-02-11 01:45:20

Changing status from needs_work to needs_review.


---

Comment by bump created at 2010-02-11 01:45:20

I addressed most of David Roe's comments.

But the email address is not a typo.

Brant Jones is also looking at the patch.


---

Comment by brant.c.jones created at 2010-02-11 03:40:55

Changing status from needs_review to positive_review.


---

Comment by brant.c.jones created at 2010-02-11 03:40:55

Patch review: trac_7751

This patch implements Kazhdan--Lusztig polynomials and R-polynomials associated to pairs of Weyl group elements in arbitrary type using standard recursive formulas.  I have verified the results of this code against the Kazhdan--Lusztig polynomials produced by GAP/Chevie for all pairs of elements in finite type A_4.  I also verified this code against GAP/Chevie for all pairs in affine type A_2 (having 3 generators) for all pairs of elements with Coxeter length less than or equal to 5.  This patch correctly implements useful mathematics and the documentation includes references to relevant mathematical literature.  

-- Brant Jones


---

Comment by roed created at 2010-02-11 06:37:27

Remove assignee bump.


---

Comment by roed created at 2010-02-11 06:37:27

I agree.  Positive review.


---

Comment by mpatel created at 2010-02-11 13:38:57

Applying the patch to [this hierarchy](http://trac.sagemath.org/sage_trac/ticket/8186#comment:8) (minus #8232), I get

```
patching file sage/combinat/root_system/weyl_group.py
Hunk #5 FAILED at 145
1 out of 13 hunks FAILED -- saving rejects to file sage/combinat/root_system/weyl_group.py.rej
```

The reject:

```diff
--- weyl_group.py
+++ weyl_group.py
@@ -138,6 +146,7 @@
         self.n = lattice.dimension() # Really needed?
         # MatrixGroup_gens takes plain matrices as input. So we can't do:
         #MatrixGroup_gens.__init__(self, list(self.simple_reflections()))
+        self._prefix = prefix
         MatrixGroup_gens.__init__(self, [self.morphism_matrix(self.lattice().si
mple_reflection(i)) for i in self.index_set()])
 
     @cached_method
```



---

Comment by bump created at 2010-02-12 13:23:38

If this conflict occurs, you may resolve just making sure the line
`self._prefix = prefix` occurs somewhere in the __init__ method of
WeylGroup.


---

Comment by bump created at 2010-02-12 14:20:56

Correction: the line self._prefix = prefix should be somewhere in the init method of `WeylGroup_gens`
(not `WeylGroup`).


---

Comment by bump created at 2010-02-13 01:25:36

Kazhdan-Lusztig polynomials, Bruhat order, improved `__repr__` for WeylGroups.


---

Attachment

Patch rebased to sage-4.3.3.alpha0. This fixes the conflict
reported by mpatel with no other changes.


---

Comment by mvngu created at 2010-02-14 14:33:11

Daniel, I have committed the attachment [kazhdan_lusztig.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7751/kazhdan_lusztig.patch) in your name, since the patch doesn't contain your full name.


---

Comment by mvngu created at 2010-02-14 14:33:11

Resolution: fixed
