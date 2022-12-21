# Issue 8810: Implementation of Stanley symmetric functions

Issue created by migration from Trac.

Original creator: aschilling

Original creation time: 2010-04-28 22:20:45

Assignee: sage-combinat

CC:  sage-combinat

This patch implements (affine) Stanley symmetric functions for type A,B,C,D.


---

Comment by stevenpon created at 2010-05-14 20:57:19

Changing status from new to needs_review.


---

Comment by stevenpon created at 2010-05-14 20:57:19

Depends on #8811, which needs review.


---

Comment by jason created at 2010-05-15 01:40:23

There's no patch up at #8811, though.


---

Comment by jbandlow created at 2010-06-03 14:44:52

I'm just starting this review, and I will probably have more to say, but here some initial issues.  In the file weyl_groups.py:
 * The methods `exp_poly_to_sym`, `pieri_factors`, and `is_pieri_factor` are missing doctests.
 * Do you think `exp_poly_to_sym` has general use?  If so, it should probably be placed in the symmetric function code somewhere.  If not, it should probably be made private (eg. `_exp_poly_to_sym`)
 * In `exp_poly_to_sym`, you should replace
` R._from_dict(dict( ... ) `
with
` R.sum_of_terms( ... ) `
 * In the doc for `pieri_factors`:  "Those are used.." should be "These are used..", "For any types" should be "For any type"
 * In each of the methods `pieri_factors`, `is_pieri_factor`, and `left_pieri_factorizations` a reference in the doc to the 'pieri_factors.py` file (where pieri factors are described in more detail) would be nice.
 * Some reference to a definition of a Stanley symmetric function should be given in the doc to the `stanley_symmetric_..` methods.
 * The latex in the doc for `left_pieri_factoriztions` is not properly marked up.
 * In the doc for `stanley_symmetric_function_as_polynomial`, I don't understand the phrase "The results is given in the ring of symmetric functions in the elementary basis, each factorization having weight prod_i x_i". Can you explain this more fully?

There is a lot of really cool new functionality here.  I'm looking forward to it getting in to sage.  I'll try to finish this review soon.


---

Comment by jbandlow created at 2010-06-03 14:44:52

Changing status from needs_review to needs_work.


---

Comment by jbandlow created at 2010-06-04 13:58:52

Another point--I'm concerned about the following doctest in `stanley_symmetric_function_as_polynomial`:

```
    sage: W = WeylGroup(['B',3,1]) 
    sage: W.from_reduced_word([3,2,1]).stanley_symmetric_function_as_polynomial() 
    2.0*x1^3 + x1*x2 + 0.5*x3
```

The coefficients should be in QQ, I think.  Probably you can replace
` return sum(...) ` with ` return R(sum( ... )) `.


---

Comment by stevenpon created at 2010-06-09 22:17:34

I updated the docs and addressed your concerns about exp_poly_to_sym (it's now included with symmetric functions), as well as putting coefficients in QQ.  The patch is also in the combinat queue but currently disabled until Nicolas takes a quick look at my work.  It should be back soon, though.


---

Comment by stevenpon created at 2010-06-09 22:17:34

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2010-06-10 08:22:04

Hi!

I am currently going through the patch, and will post shortly a reviewer's patch.


---

Comment by nthiery created at 2010-06-10 17:27:06

Changing status from needs_review to needs_work.


---

Comment by nthiery created at 2010-06-10 17:27:06

Hi Steve!

I pushed a reviewers patch on the Sage-Combinat server. It fixes a bug
or two, improves doctests, removes some unneeded imports, and removes
some unneeded code. By the way, I have rebased the Grothendieck patch.

There are still quite a few missing doctests:


```
> sage -coverage combinat/root_system/pieri_factors.py                          
----------------------------------------------------------------------
combinat/root_system/pieri_factors.py
SCORE combinat/root_system/pieri_factors.py: 77% (28 of 36)
Missing documentation:
	 * elements(self):
	 * __classcall__(cls, W, min_length = 0, max_length = infinity, min_support = frozenset([]), max_support = None):
	 * maximal_elements_combinatorial(self):
Missing doctests:
	 * __iter__(self):
	 * __iter__(self):
	 * stanley_symm_poly_weight(self,w):
	 * maximal_elements_combinatorial(self):
	 * stanley_symm_poly_weight(self, w):
```


Please fix them, and look for TODO's in the file!


---

Attachment

Thanks Nicolas!

I was not sure how one usually goes about incorporating modifications from a reviewer's patch, so I hope what I did was alright.  I incorporated your changes into my patch, added documentation and fixed the TODO's, and then disabled your reviewer patch in the combinat queue.  The latest patch is now in the combinat queue and on the trac server.


---

Comment by stevenpon created at 2010-06-20 01:02:45

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2010-06-21 23:05:12

Replying to [comment:9 stevenpon]:
> Thanks Nicolas!
> 
> I was not sure how one usually goes about incorporating modifications from a reviewer's patch, so I hope what I did was alright.  I incorporated your changes into my patch, added documentation and fixed the TODO's, and then disabled your reviewer patch in the combinat queue.  The latest patch is now in the combinat queue and on the trac server.

See `hg qfold`, in the patch server documentation.

I have just added a new reviewer's patch, fixing the lack of tests for `__classcall__`, and a couple other small issues. Please review, fold, and reupload here. With that, this patch is good to go from a technical view point. I am now running all tests.

Anne: do you think we need further review from the mathematical view point? If yes, do you have suggestions for a reviewer?


---

Comment by nthiery created at 2010-06-21 23:19:13

For the record, all test pass on 4.4.3 on ubuntu linux with the following patches applied:

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
trac_8984_crystals_alcove_path_model_bj.patch
trac_9215_doc_animate-sl.patch
trac_9216_doc_group_pyx-sl.patch
trac_8562-rebased.patch
trac_9259-combinatorialclass_doc_fix-fh.patch
trac_8810_stanley_symmetric_functions-sp-as.patch
trac_8810_stanley_symmetric_functions-review-nt.patch
```



---

Comment by aschilling created at 2010-06-22 08:00:07

> Anne: do you think we need further review from the mathematical view point? If yes, do you have suggestions for a reviewer?

If a mathematical review is needed, then Mark Shimozono or Jason Bandlow might be good candidates.


---

Comment by nthiery created at 2010-06-22 08:06:48

Replying to [comment:12 aschilling]:
> > Anne: do you think we need further review from the mathematical view point? If yes, do you have suggestions for a reviewer?
> 
> If a mathematical review is needed, then Mark Shimozono or Jason Bandlow might be good candidates.

Good idea. Let's try to save Jason some time for other reviews. Can you please send a quick e-mail to Mark?


---

Comment by aschilling created at 2010-06-25 03:14:33

Changing status from needs_review to positive_review.


---

Attachment

Nicolas Thiery did the technical review of this patch.
Thomas Lam did the mathematical review of this patch. His comments are:

Anne,

I dont really know with the code, but I looked at some of the examples
and I could not find any problem.

Thomas

Hence I am setting a positive review on this patch.

Release manager, please merge only:

trac_8810_stanley_symmetric_functions-sp-as.2.patch


---

Attachment

Version without tabs - apply only this patch


---

Comment by davidloeffler created at 2010-06-30 17:18:08

The patch `trac_8810_stanley_symmetric_functions-sp-as.2.patch` uses tabs for indentation, which is against sage library coding conventions. I have uploaded a version using spaces instead of tabs.


---

Comment by nthiery created at 2010-07-01 09:23:10

Thanks for spotting this!

Steve: please update the patch on the queue!


---

Comment by davidloeffler created at 2010-07-01 09:33:14

You might want to go through your combinat queue and check that none of the other patches introduce tabs, because rlm is going to merge #8680 in the next alpha, after which the doctest script will reject any source file that contains a tab character.


---

Comment by nthiery created at 2010-07-01 10:17:52

Replying to [comment:17 davidloeffler]:
> You might want to go through your combinat queue and check that none of the other patches introduce tabs, because rlm is going to merge #8680 in the next alpha, after which the doctest script will reject any source file that contains a tab character.

Great, I can't wait until #8680 is merged and our devs get early notices about tabs!


---

Comment by mpatel created at 2010-07-21 01:39:22

Changing status from positive_review to needs_work.


---

Comment by mpatel created at 2010-07-21 01:39:22

With [attachment:trac_8810_stanley_symmetric_functions-untabified.patch], I get one docbuild warning:

```
/mnt/usb1/scratch/mpatel/tmp/sage-4.5.1-rm/local/lib/python2.6/site-packages/sage/combinat/sf/monomial.py:docstring of sage.combinat.sf.monomial.SymmetricFunctionAlgebra_monomial.from_polynomial_exp:36: (ERROR/3) Unknown interpreted text role "function".
```

I'm about to attach a small patch that should fix this.


---

Comment by mpatel created at 2010-07-21 01:39:51

Small doc fix.  Apply on top of "untabified" patch.


---

Comment by mpatel created at 2010-07-21 01:40:08

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by nthiery created at 2010-07-21 03:55:54

Thanks for the fix! I did not rerun the test, but I don't see how the changes could break them either. Positive review!


---

Comment by nthiery created at 2010-07-21 03:55:54

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-21 10:27:51

Resolution: fixed
