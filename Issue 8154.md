# Issue 8154: Enhencement for crystals

archive/issues_008154.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat\n\nKeywords: combinatorics, crystals, KR crystals\n\nNew features for crystals:\n\n- Started framework for general highest weight crystals in /combinat/crystals/highest_weight.py\n  - Implementation of finite dimensional highest weight crystals for type E6 and E7\n- Added new class for direct sums of crystals in /combinat/crystals/direct_sum.py\n- Added a new crystal morphism function for acyclic crystals\n- Added the Demazure operators on crystals\n- Added Demazure characters for finite crystals in the ambient weight lattice\n- Added _test_fast_iter method to compare two different ways of creating list of classical crystals\n\nNew features for Kirillov-Reshetikhin crystals:\n\n- Implementation of Kirillov-Reshetikhin crystals B^{r,s} of type E_6^{(1)} for r=1,2,6\n- Pointer to KirillovReshetikhin crystals given in /combinat/crystals/affine.py (as requested by Dan Bump)\n- Added R-matrix for tensor product of two KR crystals\n\nBug fix:\n\n- Fixed whitespace problems in\n/combinat/crystals/crystals.py\n/combinat/crystals/kirillov_reshetikhin.py\n/combinat/crystals/affine.py\n/combinat/crystals/spins.py\n/combinat/crystals/tensor_products.py\n/combinat/crystals/fast_crystals.py\n/combinat/crystals/letters.py\n\nDepends on trac ticket #7978 (trac_7978_crystal_cleanup-as.patch)\n\nIssue created by migration from https://trac.sagemath.org/ticket/8154\n\n",
    "created_at": "2010-02-02T16:31:40Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "Enhencement for crystals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8154",
    "user": "aschilling"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/8154





---

archive/issue_comments_071692.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-02T16:58:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8154#issuecomment-71692",
    "user": "aschilling"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071693.json:
```json
{
    "body": "Attachment [trac_8154_affine-E-as.patch](tarball://root/attachments/some-uuid/ticket8154/trac_8154_affine-E-as.patch) by aschilling created at 2010-02-02 22:51:35",
    "created_at": "2010-02-02T22:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8154#issuecomment-71693",
    "user": "aschilling"
}
```

Attachment [trac_8154_affine-E-as.patch](tarball://root/attachments/some-uuid/ticket8154/trac_8154_affine-E-as.patch) by aschilling created at 2010-02-02 22:51:35



---

archive/issue_comments_071694.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-12T13:05:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8154#issuecomment-71694",
    "user": "bump"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071695.json:
```json
{
    "body": "The patch (which goes on top of #7978) applies cleanly to Sage 4.3.2. It passes sage -testall.\nI also tested various things to my satisfaction.\n\nThe Demazure operators can be described at two different levels: either as difference\noperators on the weight space or (following Littelmann) as operators on the crystal.\nHere they are implemented as operators on the crystal. They seem to work correctly.\nLater it might be useful to implement them independently in \nsage.combinat.root_systems.weyl_characters in the WeightRing.\n\nThe direct sums of crystals are implemented.This is essentially just the disjoint\nunion. One point is that if two component crystals are equal, a \"keepkey\" can be\nused to paint them different colors. Then the disjoint union produces a multiset.\nThis scheme is inherited from the parent class DisjointUnionEnumeratedSets where\nit is noted that it is subject to future change. I suppose this could be improved\nbut that changes must first come in sage.sets.disjoint_union_enumerated_set.py.\n\nThe framework for general highest weight crystals is important. Currently one can\nproduce all finite highest weight crystals for types A,B,C,D and G2, but one must know how to do it.\nFor types A and C, the CrystalOfTableaux is sufficient but for types B and D one has half integral\nweights and crystals with half-integral highest weight must be created by tensoring a spin crystal\nwith a CrystalOfTableaux. The framework in highest_weight.py is a step towards making this easier.\nIt should not be hard to implement this for the finite classical Cartan types.\n\nVarious other enhancements and fixes.\n\nI tested the patch to my satisfaction and recommend merging it.",
    "created_at": "2010-02-12T13:05:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8154#issuecomment-71695",
    "user": "bump"
}
```

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

archive/issue_comments_071696.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-14T14:34:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8154#issuecomment-71696",
    "user": "mvngu"
}
```

Resolution: fixed
