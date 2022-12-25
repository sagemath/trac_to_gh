# Issue 9105: Improve the category primer and tutorial

archive/issues_009105.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-algebra\n\nKeywords: category primer\n\nThe attached patch improves the category primer and tutorial, based on feedback from Sage Days 20.\n\nThere is still much work to do, but since this patch tends to conflict with many others, let's get this in as is as a first step.\n\nDepends on: #9056, #8881\n\nIssue created by migration from https://trac.sagemath.org/ticket/9105\n\n",
    "closed_at": "2010-06-09T03:34:19Z",
    "created_at": "2010-05-31T16:13:56Z",
    "labels": [
        "component: categories"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Improve the category primer and tutorial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9105",
    "user": "https://github.com/nthiery"
}
```
Assignee: @nthiery

CC:  sage-algebra

Keywords: category primer

The attached patch improves the category primer and tutorial, based on feedback from Sage Days 20.

There is still much work to do, but since this patch tends to conflict with many others, let's get this in as is as a first step.

Depends on: #9056, #8881

Issue created by migration from https://trac.sagemath.org/ticket/9105





---

archive/issue_comments_084469.json:
```json
{
    "body": "Patch under review on sage-combinat's patch server.",
    "created_at": "2010-05-31T16:17:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9105#issuecomment-84469",
    "user": "https://github.com/nthiery"
}
```

Patch under review on sage-combinat's patch server.



---

archive/issue_comments_084470.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-31T21:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9105#issuecomment-84470",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084471.json:
```json
{
    "body": "Attachment [trac_9105-categories-primer-improvements-nt.patch](tarball://root/attachments/some-uuid/ticket9105/trac_9105-categories-primer-improvements-nt.patch) by @hivert created at 2010-05-31 21:33:06\n\nAs Nicolas said there is a lot of work to do on that doc but I think it's good to have those two draft into Sage's doc => Positive review.",
    "created_at": "2010-05-31T21:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9105#issuecomment-84471",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_9105-categories-primer-improvements-nt.patch](tarball://root/attachments/some-uuid/ticket9105/trac_9105-categories-primer-improvements-nt.patch) by @hivert created at 2010-05-31 21:33:06

As Nicolas said there is a lot of work to do on that doc but I think it's good to have those two draft into Sage's doc => Positive review.



---

archive/issue_comments_084472.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-31T21:33:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9105#issuecomment-84472",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084473.json:
```json
{
    "body": "Attachment [trac_9105-categories-primer-improvements-nt.2.patch](tarball://root/attachments/some-uuid/ticket9105/trac_9105-categories-primer-improvements-nt.2.patch) by @nthiery created at 2010-06-07 21:44:08\n\nThe updated patch is refreshed w.t.r. 4.4.3, and rebased upon a trivial change (semirings in the list of categories) in #9056.\n\nAll test pass on massena with Sage 4.4.3 and the following patches applied:\n\n```\ntrac_8704-integer_range_print-fh.patch\ntrac_9104_freemod_name-fix-nt.patch\ntrac_8881-functorial_constructions-nt.patch\ntrac_8742-lazy_format-fh.patch\ntrac_8742-lazy_format-review-nt.patch\ntrac_8930-enumerated_set_deprecate-fh.patch\n8691_permutation_plainchange_tjb.patch\ntrac_8926_family_repr-fh.patch\ntrac_8902-subsets_call_fix-fh.patch\ntrac_8888_partition_rim-fh.patch\ntrac_8888_reviewer_jb.patch\ntrac_8811_reduced_word_of_translations-nt.patch\ntrac_8500_transitive_groups-final.patch\ntrac_8549_cycle_enumerator-nb.patch\ntrac_8490_square_free-vd.patch\ntrac_9096_disj_union_sphinx_fix-fh.patch\ntrac_8954-nilTemperley-as.patch\ntrac_8913-cayley_graph_twosided_labels-nt.patch\ntrac_8887-typo_monoid_prod-fh.patch\ntrac_9106-UniqueRep_sphinx_fix-fh.patch\ntrac_8876-triangular_morphisms_improve-fh.patch\ntrac_8876-reviewer_patch-jb.patch\nsage-5.0.patch\ntrac_9178-attrcall_hash_fix-nt.patch\ngap3_interface_v4.3.3.patch\ngap3_interface_patch2.patch\ntrac_8747-testsuite-speedup-fh.patch\ntrac_9056_semirings_category-nb.patch\ntrac_9056_semirings_category-review-nt.patch\ntrac_8911_categorification_crystals-as.patch\ntrac_9105-categories-primer-improvements-nt.patch\n```\n\nI therefore leave the positive review.",
    "created_at": "2010-06-07T21:44:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9105#issuecomment-84473",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_9105-categories-primer-improvements-nt.2.patch](tarball://root/attachments/some-uuid/ticket9105/trac_9105-categories-primer-improvements-nt.2.patch) by @nthiery created at 2010-06-07 21:44:08

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

archive/issue_comments_084474.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-09T03:34:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9105#issuecomment-84474",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_022344.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-09T03:34:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9105",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9105#event-22344"
}
```
