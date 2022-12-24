# Issue 9259: Wrong markup on the documentation of CombinatorialClass.map

archive/issues_009259.json:
```json
{
    "body": "Assignee: @hivert\n\nCC:  @nthiery\n\nKeywords: CombinatorialClass map\n\nThe markup ``\\{f(x) x in self\\}`` looks bad in the html doc.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9259\n\n",
    "created_at": "2010-06-18T09:30:12Z",
    "labels": [
        "documentation",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Wrong markup on the documentation of CombinatorialClass.map",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9259",
    "user": "@hivert"
}
```
Assignee: @hivert

CC:  @nthiery

Keywords: CombinatorialClass map

The markup ``\{f(x) x in self\}`` looks bad in the html doc.

Issue created by migration from https://trac.sagemath.org/ticket/9259





---

archive/issue_comments_087124.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-18T09:49:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9259#issuecomment-87124",
    "user": "@hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087125.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-18T10:08:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9259#issuecomment-87125",
    "user": "@nthiery"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_087126.json:
```json
{
    "body": "Attachment [trac_9259-combinatorialclass_doc_fix-fh.patch](tarball://root/attachments/some-uuid/ticket9259/trac_9259-combinatorialclass_doc_fix-fh.patch) by @hivert created at 2010-06-18 10:12:18",
    "created_at": "2010-06-18T10:12:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9259#issuecomment-87126",
    "user": "@hivert"
}
```

Attachment [trac_9259-combinatorialclass_doc_fix-fh.patch](tarball://root/attachments/some-uuid/ticket9259/trac_9259-combinatorialclass_doc_fix-fh.patch) by @hivert created at 2010-06-18 10:12:18



---

archive/issue_comments_087127.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-19T15:53:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9259#issuecomment-87127",
    "user": "@hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_087128.json:
```json
{
    "body": "Trivial (yet useful) documentation improvement. Good to go!\n\nFor the record, all test pass on massena with 4.4.3 and the following applied:\n\n```\ntrac_8704-integer_range_print-fh.patch\ntrac_9104_freemod_name-fix-nt.patch\ntrac_8881-functorial_constructions-nt.patch\ntrac_8742-lazy_format-fh.patch\ntrac_8742-lazy_format-review-nt.patch\ntrac_8930-enumerated_set_deprecate-fh.patch\n8691_permutation_plainchange_tjb.patch\ntrac_8926_family_repr-fh.patch\ntrac_8902-subsets_call_fix-fh.patch\ntrac_8910-combinatorial_class_parent-fh.patch\ntrac_8910-subsets_an_element-fh.patch\ntrac_8888_partition_rim-fh.patch\ntrac_8888_reviewer_jb.patch\ntrac_8811_reduced_word_of_translations-nt.patch\ntrac_8500_transitive_groups-final.patch\ntrac_8549_cycle_enumerator-nb.patch\ntrac_8490_square_free-vd.patch\ntrac_8490_review-sl.patch\ntrac_9096_disj_union_sphinx_fix-fh.patch\ntrac_8890-free_module-cleanup-nt.patch\ntrac_8954-nilTemperley-as.patch\ntrac_8913-cayley_graph_twosided_labels-nt.patch\ntrac_8887-typo_monoid_prod-fh.patch\ntrac_9106-UniqueRep_sphinx_fix-fh.patch\ntrac_8876-triangular_morphisms_improve-fh.patch\ntrac_8876-reviewer_patch-jb.patch\ntrac_9178-attrcall_hash_fix-nt.patch\ntrac_8911_categorification_crystals-as.patch\ntrac_8380_gap3_interface.patch\ntrac_9056_semirings_category-nb.patch\ntrac_9056_semirings_category-review-nt.patch\ntrac_8747-testsuite-speedup-fh.patch\ntrac_9105-categories-primer-improvements-nt.patch\ntrac_9213-doc_poset_elements-sl.patch\ntrac_9214-doc_lyndon_word-sl.patch\nsage-4.4.5.patch\nsage-5.0.patch\ntrac_8984_crystals_alcove_path_model_bj.patch\ntrac_9215_doc_animate-sl.patch\ntrac_9216_doc_group_pyx-sl.patch\ntrac_8562-rebased.patch\ntrac_9259-combinatorialclass_doc_fix-fh.patch \n```\n",
    "created_at": "2010-06-21T23:00:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9259#issuecomment-87128",
    "user": "@nthiery"
}
```

Trivial (yet useful) documentation improvement. Good to go!

For the record, all test pass on massena with 4.4.3 and the following applied:

```
trac_8704-integer_range_print-fh.patch
trac_9104_freemod_name-fix-nt.patch
trac_8881-functorial_constructions-nt.patch
trac_8742-lazy_format-fh.patch
trac_8742-lazy_format-review-nt.patch
trac_8930-enumerated_set_deprecate-fh.patch
8691_permutation_plainchange_tjb.patch
trac_8926_family_repr-fh.patch
trac_8902-subsets_call_fix-fh.patch
trac_8910-combinatorial_class_parent-fh.patch
trac_8910-subsets_an_element-fh.patch
trac_8888_partition_rim-fh.patch
trac_8888_reviewer_jb.patch
trac_8811_reduced_word_of_translations-nt.patch
trac_8500_transitive_groups-final.patch
trac_8549_cycle_enumerator-nb.patch
trac_8490_square_free-vd.patch
trac_8490_review-sl.patch
trac_9096_disj_union_sphinx_fix-fh.patch
trac_8890-free_module-cleanup-nt.patch
trac_8954-nilTemperley-as.patch
trac_8913-cayley_graph_twosided_labels-nt.patch
trac_8887-typo_monoid_prod-fh.patch
trac_9106-UniqueRep_sphinx_fix-fh.patch
trac_8876-triangular_morphisms_improve-fh.patch
trac_8876-reviewer_patch-jb.patch
trac_9178-attrcall_hash_fix-nt.patch
trac_8911_categorification_crystals-as.patch
trac_8380_gap3_interface.patch
trac_9056_semirings_category-nb.patch
trac_9056_semirings_category-review-nt.patch
trac_8747-testsuite-speedup-fh.patch
trac_9105-categories-primer-improvements-nt.patch
trac_9213-doc_poset_elements-sl.patch
trac_9214-doc_lyndon_word-sl.patch
sage-4.4.5.patch
sage-5.0.patch
trac_8984_crystals_alcove_path_model_bj.patch
trac_9215_doc_animate-sl.patch
trac_9216_doc_group_pyx-sl.patch
trac_8562-rebased.patch
trac_9259-combinatorialclass_doc_fix-fh.patch 
```




---

archive/issue_comments_087129.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-21T23:00:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9259#issuecomment-87129",
    "user": "@nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087130.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T10:10:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9259#issuecomment-87130",
    "user": "@qed777"
}
```

Resolution: fixed
