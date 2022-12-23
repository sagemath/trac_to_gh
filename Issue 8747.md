# Issue 8747: Speedup testsuite using LazyFormat

Issue created by migration from https://trac.sagemath.org/ticket/8747

Original creator: hivert

Original creation time: 2010-04-22 19:58:57

Assignee: hivert

Thanks to #8742 one can speed up TestSuite by using `LazyFormat` to report failure. 


---

Attachment


---

Comment by hivert created at 2010-05-12 17:45:43

Changing status from new to needs_review.


---

Comment by hivert created at 2010-05-12 17:45:43

Private e-mail from Nicolas

```
- trac_8747-testsuite-speedup-fh.patch

   Ça m'a l'air bon! Est-ce que l'on veut systématiquement utiliser
   des lazy-format dans tous les tests, ou seulement ceux où il y a un
   impact de vitesse? Par exemple, Parent._test_category n'est
   probablement pas critique.
```


Translation: All looks good. Do we want to systematically use LazyFormat for all tests or only those impacting speed ? For example, Parent._test_category isn't critical.


Answer: I put them in parent to advertise the feature....


---

Comment by hivert created at 2010-05-12 17:45:43

Changing keywords from "" to "testsuite, lazy format strings".


---

Comment by nthiery created at 2010-06-07 17:57:39

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2010-06-07 17:57:39

All tests patch on Sage 4.4.3, with the following patches applied:

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
```


Except maybe on sage.misc.sagedoc, but that's most likely a glitch from building the doc previously with later patches applied.


---

Comment by mhansen created at 2010-06-09 02:22:44

Resolution: fixed
