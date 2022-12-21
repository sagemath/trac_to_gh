# Issue 8154: Enhencement for crystals

Issue created by migration from Trac.

Original creator: aschilling

Original creation time: 2010-02-02 16:31:40

Assignee: sage-combinat

CC:  sage-combinat

Keywords: combinatorics, crystals, KR crystals

New features for crystals:

- Started framework for general highest weight crystals in /combinat/crystals/highest_weight.py
  - Implementation of finite dimensional highest weight crystals for type E6 and E7
- Added new class for direct sums of crystals in /combinat/crystals/direct_sum.py
- Added a new crystal morphism function for acyclic crystals
- Added the Demazure operators on crystals
- Added Demazure characters for finite crystals in the ambient weight lattice
- Added _test_fast_iter method to compare two different ways of creating list of classical crystals

New features for Kirillov-Reshetikhin crystals:

- Implementation of Kirillov-Reshetikhin crystals B^{r,s} of type E_6^{(1)} for r=1,2,6
- Pointer to KirillovReshetikhin crystals given in /combinat/crystals/affine.py (as requested by Dan Bump)
- Added R-matrix for tensor product of two KR crystals

Bug fix:

- Fixed whitespace problems in
/combinat/crystals/crystals.py
/combinat/crystals/kirillov_reshetikhin.py
/combinat/crystals/affine.py
/combinat/crystals/spins.py
/combinat/crystals/tensor_products.py
/combinat/crystals/fast_crystals.py
/combinat/crystals/letters.py

Depends on trac ticket #7978 (trac_7978_crystal_cleanup-as.patch)


---

Comment by aschilling created at 2010-02-02 16:58:44

Changing status from new to needs_review.


---

Attachment


---

Comment by bump created at 2010-02-12 13:05:51

Changing status from needs_review to positive_review.


---

Comment by bump created at 2010-02-12 13:05:51

The patch (which goes on top of #7978) applies cleanly to Sage 4.3.2. It passes sage -testall.
I also tested various things to my satisfaction.

The Demazure operators can be described at two different levels: either as difference
operators on the weight space or (following Littelmann) as operators on the crystal.
Here they are implemented as operators on the crystal. They seem to work correctly.
Later it might be useful to implement them independently in 
sage.combinat.root_systems.weyl_characters in the WeightRing.

The direct sums of crystals are implemented.This is essentially just the disjoint
union. One point is that if two component crystals are equal, a "keepkey" can be
used to paint them different colors. Then the disjoint union produces a multiset.
This scheme is inherited from the parent class DisjointUnionEnumeratedSets where
it is noted that it is subject to future change. I suppose this could be improved
but that changes must first come in sage.sets.disjoint_union_enumerated_set.py.

The framework for general highest weight crystals is important. Currently one can
produce all finite highest weight crystals for types A,B,C,D and G2, but one must know how to do it.
For types A and C, the CrystalOfTableaux is sufficient but for types B and D one has half integral
weights and crystals with half-integral highest weight must be created by tensoring a spin crystal
with a CrystalOfTableaux. The framework in highest_weight.py is a step towards making this easier.
It should not be hard to implement this for the finite classical Cartan types.

Various other enhancements and fixes.

I tested the patch to my satisfaction and recommend merging it.


---

Comment by mvngu created at 2010-02-14 14:34:40

Resolution: fixed
