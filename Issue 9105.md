# Issue 9105: Improve the category primer and tutorial

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2010-05-31 16:13:56

Assignee: nthiery

CC:  sage-algebra

Keywords: category primer

The attached patch improves the category primer and tutorial, based on feedback from Sage Days 20.

There is still much work to do, but since this patch tends to conflict with many others, let's get this in as is as a first step.


---

Comment by nthiery created at 2010-05-31 16:17:28

Patch under review on sage-combinat's patch server.


---

Comment by hivert created at 2010-05-31 21:33:06

Changing status from new to needs_review.


---

Attachment

As Nicolas said there is a lot of work to do on that doc but I think it's good to have those two draft into Sage's doc => Positive review.


---

Comment by hivert created at 2010-05-31 21:33:20

Changing status from needs_review to positive_review.


---

Attachment

The updated patch is refreshed w.t.r. 4.4.3, and rebased upon a trivial change (semirings in the list of categories) in #9056.

All test pass on massena with Sage 4.4.3 and the following patches applied:

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
trac_8888_partition_rim-fh.patch
trac_8888_reviewer_jb.patch
trac_8811_reduced_word_of_translations-nt.patch
trac_8500_transitive_groups-final.patch
trac_8549_cycle_enumerator-nb.patch
trac_8490_square_free-vd.patch
trac_9096_disj_union_sphinx_fix-fh.patch
trac_8954-nilTemperley-as.patch
trac_8913-cayley_graph_twosided_labels-nt.patch
trac_8887-typo_monoid_prod-fh.patch
trac_9106-UniqueRep_sphinx_fix-fh.patch
trac_8876-triangular_morphisms_improve-fh.patch
trac_8876-reviewer_patch-jb.patch
sage-5.0.patch
trac_9178-attrcall_hash_fix-nt.patch
gap3_interface_v4.3.3.patch
gap3_interface_patch2.patch
trac_8747-testsuite-speedup-fh.patch
trac_9056_semirings_category-nb.patch
trac_9056_semirings_category-review-nt.patch
trac_8911_categorification_crystals-as.patch
trac_9105-categories-primer-improvements-nt.patch
```


I therefore leave the positive review.


---

Comment by mhansen created at 2010-06-09 03:34:19

Resolution: fixed
