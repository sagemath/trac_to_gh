# Issue 8810: Implementation of Stanley symmetric functions

archive/issues_008810.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat\n\nThis patch implements (affine) Stanley symmetric functions for type A,B,C,D.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8810\n\n",
    "created_at": "2010-04-28T22:20:45Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Implementation of Stanley symmetric functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8810",
    "user": "@anneschilling"
}
```
Assignee: sage-combinat

CC:  sage-combinat

This patch implements (affine) Stanley symmetric functions for type A,B,C,D.

Issue created by migration from https://trac.sagemath.org/ticket/8810





---

archive/issue_comments_080856.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-14T20:57:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80856",
    "user": "stevenpon"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080857.json:
```json
{
    "body": "Depends on #8811, which needs review.",
    "created_at": "2010-05-14T20:57:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80857",
    "user": "stevenpon"
}
```

Depends on #8811, which needs review.



---

archive/issue_comments_080858.json:
```json
{
    "body": "There's no patch up at #8811, though.",
    "created_at": "2010-05-15T01:40:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80858",
    "user": "@jasongrout"
}
```

There's no patch up at #8811, though.



---

archive/issue_comments_080859.json:
```json
{
    "body": "I'm just starting this review, and I will probably have more to say, but here some initial issues.  In the file weyl_groups.py:\n* The methods `exp_poly_to_sym`, `pieri_factors`, and `is_pieri_factor` are missing doctests.\n* Do you think `exp_poly_to_sym` has general use?  If so, it should probably be placed in the symmetric function code somewhere.  If not, it should probably be made private (eg. `_exp_poly_to_sym`)\n* In `exp_poly_to_sym`, you should replace\n` R._from_dict(dict( ... ) `\nwith\n` R.sum_of_terms( ... ) `\n* In the doc for `pieri_factors`:  \"Those are used..\" should be \"These are used..\", \"For any types\" should be \"For any type\"\n* In each of the methods `pieri_factors`, `is_pieri_factor`, and `left_pieri_factorizations` a reference in the doc to the 'pieri_factors.py` file (where pieri factors are described in more detail) would be nice.\n* Some reference to a definition of a Stanley symmetric function should be given in the doc to the `stanley_symmetric_..` methods.\n* The latex in the doc for `left_pieri_factoriztions` is not properly marked up.\n* In the doc for `stanley_symmetric_function_as_polynomial`, I don't understand the phrase \"The results is given in the ring of symmetric functions in the elementary basis, each factorization having weight prod_i x_i\". Can you explain this more fully?\n\nThere is a lot of really cool new functionality here.  I'm looking forward to it getting in to sage.  I'll try to finish this review soon.",
    "created_at": "2010-06-03T14:44:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80859",
    "user": "@jbandlow"
}
```

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

archive/issue_comments_080860.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-03T14:44:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80860",
    "user": "@jbandlow"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_080861.json:
```json
{
    "body": "Another point--I'm concerned about the following doctest in `stanley_symmetric_function_as_polynomial`:\n\n```\n    sage: W = WeylGroup(['B',3,1]) \n    sage: W.from_reduced_word([3,2,1]).stanley_symmetric_function_as_polynomial() \n    2.0*x1^3 + x1*x2 + 0.5*x3\n```\n\nThe coefficients should be in QQ, I think.  Probably you can replace\n` return sum(...) ` with ` return R(sum( ... )) `.",
    "created_at": "2010-06-04T13:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80861",
    "user": "@jbandlow"
}
```

Another point--I'm concerned about the following doctest in `stanley_symmetric_function_as_polynomial`:

```
    sage: W = WeylGroup(['B',3,1]) 
    sage: W.from_reduced_word([3,2,1]).stanley_symmetric_function_as_polynomial() 
    2.0*x1^3 + x1*x2 + 0.5*x3
```

The coefficients should be in QQ, I think.  Probably you can replace
` return sum(...) ` with ` return R(sum( ... )) `.



---

archive/issue_comments_080862.json:
```json
{
    "body": "I updated the docs and addressed your concerns about exp_poly_to_sym (it's now included with symmetric functions), as well as putting coefficients in QQ.  The patch is also in the combinat queue but currently disabled until Nicolas takes a quick look at my work.  It should be back soon, though.",
    "created_at": "2010-06-09T22:17:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80862",
    "user": "stevenpon"
}
```

I updated the docs and addressed your concerns about exp_poly_to_sym (it's now included with symmetric functions), as well as putting coefficients in QQ.  The patch is also in the combinat queue but currently disabled until Nicolas takes a quick look at my work.  It should be back soon, though.



---

archive/issue_comments_080863.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-09T22:17:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80863",
    "user": "stevenpon"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_080864.json:
```json
{
    "body": "Hi!\n\nI am currently going through the patch, and will post shortly a reviewer's patch.",
    "created_at": "2010-06-10T08:22:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80864",
    "user": "@nthiery"
}
```

Hi!

I am currently going through the patch, and will post shortly a reviewer's patch.



---

archive/issue_comments_080865.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-10T17:27:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80865",
    "user": "@nthiery"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_080866.json:
```json
{
    "body": "Hi Steve!\n\nI pushed a reviewers patch on the Sage-Combinat server. It fixes a bug\nor two, improves doctests, removes some unneeded imports, and removes\nsome unneeded code. By the way, I have rebased the Grothendieck patch.\n\nThere are still quite a few missing doctests:\n\n\n```\n> sage -coverage combinat/root_system/pieri_factors.py                          \n----------------------------------------------------------------------\ncombinat/root_system/pieri_factors.py\nSCORE combinat/root_system/pieri_factors.py: 77% (28 of 36)\nMissing documentation:\n\t * elements(self):\n\t * __classcall__(cls, W, min_length = 0, max_length = infinity, min_support = frozenset([]), max_support = None):\n\t * maximal_elements_combinatorial(self):\nMissing doctests:\n\t * __iter__(self):\n\t * __iter__(self):\n\t * stanley_symm_poly_weight(self,w):\n\t * maximal_elements_combinatorial(self):\n\t * stanley_symm_poly_weight(self, w):\n```\n\n\nPlease fix them, and look for TODO's in the file!",
    "created_at": "2010-06-10T17:27:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80866",
    "user": "@nthiery"
}
```

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

archive/issue_comments_080867.json:
```json
{
    "body": "Attachment [trac_8810_stanley_symmetric_functions-sp-as.patch](tarball://root/attachments/some-uuid/ticket8810/trac_8810_stanley_symmetric_functions-sp-as.patch) by stevenpon created at 2010-06-20 01:02:45\n\nThanks Nicolas!\n\nI was not sure how one usually goes about incorporating modifications from a reviewer's patch, so I hope what I did was alright.  I incorporated your changes into my patch, added documentation and fixed the TODO's, and then disabled your reviewer patch in the combinat queue.  The latest patch is now in the combinat queue and on the trac server.",
    "created_at": "2010-06-20T01:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80867",
    "user": "stevenpon"
}
```

Attachment [trac_8810_stanley_symmetric_functions-sp-as.patch](tarball://root/attachments/some-uuid/ticket8810/trac_8810_stanley_symmetric_functions-sp-as.patch) by stevenpon created at 2010-06-20 01:02:45

Thanks Nicolas!

I was not sure how one usually goes about incorporating modifications from a reviewer's patch, so I hope what I did was alright.  I incorporated your changes into my patch, added documentation and fixed the TODO's, and then disabled your reviewer patch in the combinat queue.  The latest patch is now in the combinat queue and on the trac server.



---

archive/issue_comments_080868.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-20T01:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80868",
    "user": "stevenpon"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_080869.json:
```json
{
    "body": "Replying to [comment:9 stevenpon]:\n> Thanks Nicolas!\n> \n> I was not sure how one usually goes about incorporating modifications from a reviewer's patch, so I hope what I did was alright.  I incorporated your changes into my patch, added documentation and fixed the TODO's, and then disabled your reviewer patch in the combinat queue.  The latest patch is now in the combinat queue and on the trac server.\n\nSee `hg qfold`, in the patch server documentation.\n\nI have just added a new reviewer's patch, fixing the lack of tests for `__classcall__`, and a couple other small issues. Please review, fold, and reupload here. With that, this patch is good to go from a technical view point. I am now running all tests.\n\nAnne: do you think we need further review from the mathematical view point? If yes, do you have suggestions for a reviewer?",
    "created_at": "2010-06-21T23:05:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80869",
    "user": "@nthiery"
}
```

Replying to [comment:9 stevenpon]:
> Thanks Nicolas!
> 
> I was not sure how one usually goes about incorporating modifications from a reviewer's patch, so I hope what I did was alright.  I incorporated your changes into my patch, added documentation and fixed the TODO's, and then disabled your reviewer patch in the combinat queue.  The latest patch is now in the combinat queue and on the trac server.

See `hg qfold`, in the patch server documentation.

I have just added a new reviewer's patch, fixing the lack of tests for `__classcall__`, and a couple other small issues. Please review, fold, and reupload here. With that, this patch is good to go from a technical view point. I am now running all tests.

Anne: do you think we need further review from the mathematical view point? If yes, do you have suggestions for a reviewer?



---

archive/issue_comments_080870.json:
```json
{
    "body": "For the record, all test pass on 4.4.3 on ubuntu linux with the following patches applied:\n\n```\ntrac_8704-integer_range_print-fh.patch\ntrac_9104_freemod_name-fix-nt.patch\ntrac_8881-functorial_constructions-nt.patch\ntrac_8742-lazy_format-fh.patch\ntrac_8742-lazy_format-review-nt.patch\ntrac_8930-enumerated_set_deprecate-fh.patch\n8691_permutation_plainchange_tjb.patch\ntrac_8926_family_repr-fh.patch\ntrac_8902-subsets_call_fix-fh.patch\ntrac_8910-combinatorial_class_parent-fh.patch\ntrac_8910-subsets_an_element-fh.patch\ntrac_8888_partition_rim-fh.patch\ntrac_8888_reviewer_jb.patch\ntrac_8811_reduced_word_of_translations-nt.patch\ntrac_8500_transitive_groups-final.patch\ntrac_8549_cycle_enumerator-nb.patch\ntrac_8490_square_free-vd.patch\ntrac_8490_review-sl.patch\ntrac_9096_disj_union_sphinx_fix-fh.patch\ntrac_8890-free_module-cleanup-nt.patch\ntrac_8954-nilTemperley-as.patch\ntrac_8913-cayley_graph_twosided_labels-nt.patch\ntrac_8887-typo_monoid_prod-fh.patch\ntrac_9106-UniqueRep_sphinx_fix-fh.patch\ntrac_8876-triangular_morphisms_improve-fh.patch\ntrac_8876-reviewer_patch-jb.patch\ntrac_9178-attrcall_hash_fix-nt.patch\ntrac_8911_categorification_crystals-as.patch\ntrac_8380_gap3_interface.patch\ntrac_9056_semirings_category-nb.patch\ntrac_9056_semirings_category-review-nt.patch\ntrac_8747-testsuite-speedup-fh.patch\ntrac_9105-categories-primer-improvements-nt.patch\ntrac_9213-doc_poset_elements-sl.patch\ntrac_9214-doc_lyndon_word-sl.patch\ntrac_8984_crystals_alcove_path_model_bj.patch\ntrac_9215_doc_animate-sl.patch\ntrac_9216_doc_group_pyx-sl.patch\ntrac_8562-rebased.patch\ntrac_9259-combinatorialclass_doc_fix-fh.patch\ntrac_8810_stanley_symmetric_functions-sp-as.patch\ntrac_8810_stanley_symmetric_functions-review-nt.patch\n```\n",
    "created_at": "2010-06-21T23:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80870",
    "user": "@nthiery"
}
```

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

archive/issue_comments_080871.json:
```json
{
    "body": "> Anne: do you think we need further review from the mathematical view point? If yes, do you have suggestions for a reviewer?\n\nIf a mathematical review is needed, then Mark Shimozono or Jason Bandlow might be good candidates.",
    "created_at": "2010-06-22T08:00:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80871",
    "user": "@anneschilling"
}
```

> Anne: do you think we need further review from the mathematical view point? If yes, do you have suggestions for a reviewer?

If a mathematical review is needed, then Mark Shimozono or Jason Bandlow might be good candidates.



---

archive/issue_comments_080872.json:
```json
{
    "body": "Replying to [comment:12 aschilling]:\n> > Anne: do you think we need further review from the mathematical view point? If yes, do you have suggestions for a reviewer?\n> \n> If a mathematical review is needed, then Mark Shimozono or Jason Bandlow might be good candidates.\n\nGood idea. Let's try to save Jason some time for other reviews. Can you please send a quick e-mail to Mark?",
    "created_at": "2010-06-22T08:06:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80872",
    "user": "@nthiery"
}
```

Replying to [comment:12 aschilling]:
> > Anne: do you think we need further review from the mathematical view point? If yes, do you have suggestions for a reviewer?
> 
> If a mathematical review is needed, then Mark Shimozono or Jason Bandlow might be good candidates.

Good idea. Let's try to save Jason some time for other reviews. Can you please send a quick e-mail to Mark?



---

archive/issue_comments_080873.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-25T03:14:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80873",
    "user": "@anneschilling"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080874.json:
```json
{
    "body": "Attachment [trac_8810_stanley_symmetric_functions-sp-as.2.patch](tarball://root/attachments/some-uuid/ticket8810/trac_8810_stanley_symmetric_functions-sp-as.2.patch) by @anneschilling created at 2010-06-25 03:14:33\n\nNicolas Thiery did the technical review of this patch.\nThomas Lam did the mathematical review of this patch. His comments are:\n\nAnne,\n\nI dont really know with the code, but I looked at some of the examples\nand I could not find any problem.\n\nThomas\n\nHence I am setting a positive review on this patch.\n\nRelease manager, please merge only:\n\ntrac_8810_stanley_symmetric_functions-sp-as.2.patch",
    "created_at": "2010-06-25T03:14:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80874",
    "user": "@anneschilling"
}
```

Attachment [trac_8810_stanley_symmetric_functions-sp-as.2.patch](tarball://root/attachments/some-uuid/ticket8810/trac_8810_stanley_symmetric_functions-sp-as.2.patch) by @anneschilling created at 2010-06-25 03:14:33

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

archive/issue_comments_080875.json:
```json
{
    "body": "Attachment [trac_8810_stanley_symmetric_functions-untabified.patch](tarball://root/attachments/some-uuid/ticket8810/trac_8810_stanley_symmetric_functions-untabified.patch) by @loefflerd created at 2010-06-30 17:16:43\n\nVersion without tabs - apply only this patch",
    "created_at": "2010-06-30T17:16:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80875",
    "user": "@loefflerd"
}
```

Attachment [trac_8810_stanley_symmetric_functions-untabified.patch](tarball://root/attachments/some-uuid/ticket8810/trac_8810_stanley_symmetric_functions-untabified.patch) by @loefflerd created at 2010-06-30 17:16:43

Version without tabs - apply only this patch



---

archive/issue_comments_080876.json:
```json
{
    "body": "The patch `trac_8810_stanley_symmetric_functions-sp-as.2.patch` uses tabs for indentation, which is against sage library coding conventions. I have uploaded a version using spaces instead of tabs.",
    "created_at": "2010-06-30T17:18:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80876",
    "user": "@loefflerd"
}
```

The patch `trac_8810_stanley_symmetric_functions-sp-as.2.patch` uses tabs for indentation, which is against sage library coding conventions. I have uploaded a version using spaces instead of tabs.



---

archive/issue_comments_080877.json:
```json
{
    "body": "Thanks for spotting this!\n\nSteve: please update the patch on the queue!",
    "created_at": "2010-07-01T09:23:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80877",
    "user": "@nthiery"
}
```

Thanks for spotting this!

Steve: please update the patch on the queue!



---

archive/issue_comments_080878.json:
```json
{
    "body": "You might want to go through your combinat queue and check that none of the other patches introduce tabs, because rlm is going to merge #8680 in the next alpha, after which the doctest script will reject any source file that contains a tab character.",
    "created_at": "2010-07-01T09:33:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80878",
    "user": "@loefflerd"
}
```

You might want to go through your combinat queue and check that none of the other patches introduce tabs, because rlm is going to merge #8680 in the next alpha, after which the doctest script will reject any source file that contains a tab character.



---

archive/issue_comments_080879.json:
```json
{
    "body": "Replying to [comment:17 davidloeffler]:\n> You might want to go through your combinat queue and check that none of the other patches introduce tabs, because rlm is going to merge #8680 in the next alpha, after which the doctest script will reject any source file that contains a tab character.\n\nGreat, I can't wait until #8680 is merged and our devs get early notices about tabs!",
    "created_at": "2010-07-01T10:17:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80879",
    "user": "@nthiery"
}
```

Replying to [comment:17 davidloeffler]:
> You might want to go through your combinat queue and check that none of the other patches introduce tabs, because rlm is going to merge #8680 in the next alpha, after which the doctest script will reject any source file that contains a tab character.

Great, I can't wait until #8680 is merged and our devs get early notices about tabs!



---

archive/issue_comments_080880.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-21T01:39:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80880",
    "user": "@qed777"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_080881.json:
```json
{
    "body": "With [attachment:trac_8810_stanley_symmetric_functions-untabified.patch], I get one docbuild warning:\n\n```\n/mnt/usb1/scratch/mpatel/tmp/sage-4.5.1-rm/local/lib/python2.6/site-packages/sage/combinat/sf/monomial.py:docstring of sage.combinat.sf.monomial.SymmetricFunctionAlgebra_monomial.from_polynomial_exp:36: (ERROR/3) Unknown interpreted text role \"function\".\n```\n\nI'm about to attach a small patch that should fix this.",
    "created_at": "2010-07-21T01:39:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80881",
    "user": "@qed777"
}
```

With [attachment:trac_8810_stanley_symmetric_functions-untabified.patch], I get one docbuild warning:

```
/mnt/usb1/scratch/mpatel/tmp/sage-4.5.1-rm/local/lib/python2.6/site-packages/sage/combinat/sf/monomial.py:docstring of sage.combinat.sf.monomial.SymmetricFunctionAlgebra_monomial.from_polynomial_exp:36: (ERROR/3) Unknown interpreted text role "function".
```

I'm about to attach a small patch that should fix this.



---

archive/issue_comments_080882.json:
```json
{
    "body": "Small doc fix.  Apply on top of \"untabified\" patch.",
    "created_at": "2010-07-21T01:39:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80882",
    "user": "@qed777"
}
```

Small doc fix.  Apply on top of "untabified" patch.



---

archive/issue_comments_080883.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-21T01:40:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80883",
    "user": "@qed777"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_080884.json:
```json
{
    "body": "Attachment [trac_8810_stanley_symmetric_functions-docfix.patch](tarball://root/attachments/some-uuid/ticket8810/trac_8810_stanley_symmetric_functions-docfix.patch) by @qed777 created at 2010-07-21 01:40:08",
    "created_at": "2010-07-21T01:40:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80884",
    "user": "@qed777"
}
```

Attachment [trac_8810_stanley_symmetric_functions-docfix.patch](tarball://root/attachments/some-uuid/ticket8810/trac_8810_stanley_symmetric_functions-docfix.patch) by @qed777 created at 2010-07-21 01:40:08



---

archive/issue_comments_080885.json:
```json
{
    "body": "Thanks for the fix! I did not rerun the test, but I don't see how the changes could break them either. Positive review!",
    "created_at": "2010-07-21T03:55:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80885",
    "user": "@nthiery"
}
```

Thanks for the fix! I did not rerun the test, but I don't see how the changes could break them either. Positive review!



---

archive/issue_comments_080886.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-21T03:55:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80886",
    "user": "@nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080887.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T10:27:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8810#issuecomment-80887",
    "user": "@qed777"
}
```

Resolution: fixed
