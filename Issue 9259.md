# Issue 9259: Wrong markup on the documentation of CombinatorialClass.map

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2010-06-18 09:30:12

Assignee: hivert

CC:  nthiery

Keywords: CombinatorialClass map

The markup ``\{f(x) x in self\}`` looks bad in the html doc.


---

Comment by hivert created at 2010-06-18 09:49:16

Changing status from new to needs_review.


---

Comment by nthiery created at 2010-06-18 10:08:44

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by hivert created at 2010-06-19 15:53:07

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2010-06-21 23:00:00

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

Comment by nthiery created at 2010-06-21 23:00:00

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-21 10:10:55

Resolution: fixed
