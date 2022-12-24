# Issue 9056: Add the category of SemiRings with an example : NonNegativeIntegers()

archive/issues_009056.json:
```json
{
    "body": "Assignee: nborie\n\nCC:  sage-combinat nthiery\n\nKeywords: semiring\n\nAll is in the title, we want :\n\n\n```\nsage: SemiRings()\nsage: Category of semi rings\nsage: NN = NonNegativeIntegers()\nsage: NN.category()\nCategory of semi rings\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9056\n\n",
    "created_at": "2010-05-26T14:26:00Z",
    "labels": [
        "categories",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Add the category of SemiRings with an example : NonNegativeIntegers()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9056",
    "user": "nborie"
}
```
Assignee: nborie

CC:  sage-combinat nthiery

Keywords: semiring

All is in the title, we want :


```
sage: SemiRings()
sage: Category of semi rings
sage: NN = NonNegativeIntegers()
sage: NN.category()
Category of semi rings
```


Issue created by migration from https://trac.sagemath.org/ticket/9056





---

archive/issue_comments_084009.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-27T13:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9056#issuecomment-84009",
    "user": "nborie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084010.json:
```json
{
    "body": "Attachment [trac_9056_semirings_category-nb.2.patch](tarball://root/attachments/some-uuid/ticket9056/trac_9056_semirings_category-nb.2.patch) by nborie created at 2010-05-27 14:51:21",
    "created_at": "2010-05-27T14:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9056#issuecomment-84010",
    "user": "nborie"
}
```

Attachment [trac_9056_semirings_category-nb.2.patch](tarball://root/attachments/some-uuid/ticket9056/trac_9056_semirings_category-nb.2.patch) by nborie created at 2010-05-27 14:51:21



---

archive/issue_comments_084011.json:
```json
{
    "body": "I reviewed this patch while Nicolas was writting it. I'll run the tests shortly, and report.\n\nFlorent: please have a look to see if you agree with the concept, and if yes set a positive review.",
    "created_at": "2010-05-27T14:55:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9056#issuecomment-84011",
    "user": "nthiery"
}
```

I reviewed this patch while Nicolas was writting it. I'll run the tests shortly, and report.

Florent: please have a look to see if you agree with the concept, and if yes set a positive review.



---

archive/issue_comments_084012.json:
```json
{
    "body": "Hi Nicolas B.,\n\nThere are a couple failures in the category tests (due to the new test and new category); please fix them. Note that I made a small change to your patch, so you should make sure to first pull.\n\nYou might get a conflict with the primer improvement; in that case, move your patch just after it.",
    "created_at": "2010-05-27T15:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9056#issuecomment-84012",
    "user": "nthiery"
}
```

Hi Nicolas B.,

There are a couple failures in the category tests (due to the new test and new category); please fix them. Note that I made a small change to your patch, so you should make sure to first pull.

You might get a conflict with the primer improvement; in that case, move your patch just after it.



---

archive/issue_comments_084013.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-27T15:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9056#issuecomment-84013",
    "user": "nthiery"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_084014.json:
```json
{
    "body": "Replying to [comment:5 nthiery]:\n> There are a couple failures in the category tests (due to the new test and new category); please fix them. Note that I made a small change to your patch, so you should make sure to first pull.\n\nA couple failures in combinat/sf as well due to the new _test_distributivity.",
    "created_at": "2010-05-27T16:02:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9056#issuecomment-84014",
    "user": "nthiery"
}
```

Replying to [comment:5 nthiery]:
> There are a couple failures in the category tests (due to the new test and new category); please fix them. Note that I made a small change to your patch, so you should make sure to first pull.

A couple failures in combinat/sf as well due to the new _test_distributivity.



---

archive/issue_comments_084015.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-27T20:50:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9056#issuecomment-84015",
    "user": "nborie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084016.json:
```json
{
    "body": "As I did manage to run ALL TESTS on sagemath, I found files this patch affect... I didn't touch the primer (modified on combinat queue). This patch will have yo be updated if your primer improvements go in sage earlier.\n\nI update the patch (without .2.patch, forget this one.)\n\nThank for your help for massive tests.",
    "created_at": "2010-05-27T20:50:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9056#issuecomment-84016",
    "user": "nborie"
}
```

As I did manage to run ALL TESTS on sagemath, I found files this patch affect... I didn't touch the primer (modified on combinat queue). This patch will have yo be updated if your primer improvements go in sage earlier.

I update the patch (without .2.patch, forget this one.)

Thank for your help for massive tests.



---

archive/issue_comments_084017.json:
```json
{
    "body": "Sorry and please wait, this local patch will break your queue Nicolas.",
    "created_at": "2010-05-27T20:57:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9056#issuecomment-84017",
    "user": "nborie"
}
```

Sorry and please wait, this local patch will break your queue Nicolas.



---

archive/issue_comments_084018.json:
```json
{
    "body": "This last update should be fine...",
    "created_at": "2010-05-28T12:39:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9056#issuecomment-84018",
    "user": "nborie"
}
```

This last update should be fine...



---

archive/issue_comments_084019.json:
```json
{
    "body": "One more update :\n\nAfter advises form English speaker people, I change the name from NonNegativeIntegersSemiring to NonNegativeIntegerSemiring. See http://groups.google.com/group/sage-devel/browse_thread/thread/ffaf01ffb941078\n\nI linked my module to the reference manual and fix a :class: ref in the doc thanks to Florent.\n\nI am still ready for deeper review.",
    "created_at": "2010-05-31T13:35:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9056#issuecomment-84019",
    "user": "nborie"
}
```

One more update :

After advises form English speaker people, I change the name from NonNegativeIntegersSemiring to NonNegativeIntegerSemiring. See http://groups.google.com/group/sage-devel/browse_thread/thread/ffaf01ffb941078

I linked my module to the reference manual and fix a :class: ref in the doc thanks to Florent.

I am still ready for deeper review.



---

archive/issue_comments_084020.json:
```json
{
    "body": "Hi Nicolas,\n\nThanks for finalizing this!\n\nI just pushed a small reviewer's patch on sage-combinat. Please review, and if ok fold and reupload here.",
    "created_at": "2010-06-07T16:37:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9056#issuecomment-84020",
    "user": "nthiery"
}
```

Hi Nicolas,

Thanks for finalizing this!

I just pushed a small reviewer's patch on sage-combinat. Please review, and if ok fold and reupload here.



---

archive/issue_comments_084021.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-07T17:09:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9056#issuecomment-84021",
    "user": "nborie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084022.json:
```json
{
    "body": "Attachment [trac_9056_semirings_category-nb.patch](tarball://root/attachments/some-uuid/ticket9056/trac_9056_semirings_category-nb.patch) by nborie created at 2010-06-07 17:09:03\n\nI am ok with your reviewer patch. I will try to delete ending blanks on my own since you made work well coloring with my hg qdiff. I qfolded your patch in mine and uploaded it...\n\nThanks for the review.\n\nFor the release manager ,apply only \nattachment:trac_9056_semirings_category-nb.patch",
    "created_at": "2010-06-07T17:09:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9056#issuecomment-84022",
    "user": "nborie"
}
```

Attachment [trac_9056_semirings_category-nb.patch](tarball://root/attachments/some-uuid/ticket9056/trac_9056_semirings_category-nb.patch) by nborie created at 2010-06-07 17:09:03

I am ok with your reviewer patch. I will try to delete ending blanks on my own since you made work well coloring with my hg qdiff. I qfolded your patch in mine and uploaded it...

Thanks for the review.

For the release manager ,apply only 
attachment:trac_9056_semirings_category-nb.patch



---

archive/issue_comments_084023.json:
```json
{
    "body": "I did not yet say to set a positive review on my behalf :-)\nActually one test was failing in the primer. I am rerunning all tests.",
    "created_at": "2010-06-07T19:41:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9056#issuecomment-84023",
    "user": "nthiery"
}
```

I did not yet say to set a positive review on my behalf :-)
Actually one test was failing in the primer. I am rerunning all tests.



---

archive/issue_comments_084024.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-06-07T19:41:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9056#issuecomment-84024",
    "user": "nthiery"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_084025.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-07T20:58:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9056#issuecomment-84025",
    "user": "nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084026.json:
```json
{
    "body": "With my reviewer patch all test pass on Sage-4.4.3, with the following patches applied:\n\ntrac_8704-integer_range_print-fh.patch\ntrac_9104_freemod_name-fix-nt.patch\ntrac_8881-functorial_constructions-nt.patch\ntrac_8742-lazy_format-fh.patch\ntrac_8742-lazy_format-review-nt.patch\ntrac_8930-enumerated_set_deprecate-fh.patch\n8691_permutation_plainchange_tjb.patch\ntrac_8926_family_repr-fh.patch\ntrac_8902-subsets_call_fix-fh.patch\ntrac_8888_partition_rim-fh.patch\ntrac_8888_reviewer_jb.patch\ntrac_8811_reduced_word_of_translations-nt.patch\ntrac_8500_transitive_groups-final.patch\ntrac_8549_cycle_enumerator-nb.patch\ntrac_8490_square_free-vd.patch\ntrac_9096_disj_union_sphinx_fix-fh.patch\ntrac_8954-nilTemperley-as.patch\ntrac_8913-cayley_graph_twosided_labels-nt.patch\ntrac_8887-typo_monoid_prod-fh.patch\ntrac_9106-UniqueRep_sphinx_fix-fh.patch\ntrac_8876-triangular_morphisms_improve-fh.patch\ntrac_8876-reviewer_patch-jb.patch\nsage-5.0.patch\ntrac_9178-attrcall_hash_fix-nt.patch\ngap3_interface_v4.3.3.patch\ngap3_interface_patch2.patch\ntrac_8747-testsuite-speedup-fh.patch\ntrac_9056_semirings_category-nb.patch\ntrac_9056_semirings_category-review-nt.patch\n\n(note: actually interfaces/expect and interfaces/ecm failed, but those seem to be usual random failures on massena which would need to be investigated at some point).\n\nNicolas: please fold, and reupload, and set positive review on my behalf!",
    "created_at": "2010-06-07T20:58:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9056#issuecomment-84026",
    "user": "nthiery"
}
```

With my reviewer patch all test pass on Sage-4.4.3, with the following patches applied:

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

(note: actually interfaces/expect and interfaces/ecm failed, but those seem to be usual random failures on massena which would need to be investigated at some point).

Nicolas: please fold, and reupload, and set positive review on my behalf!



---

archive/issue_comments_084027.json:
```json
{
    "body": "Arr, here is the list of patches in a more readable format:\n\n```\ntrac_8704-integer_range_print-fh.patch\ntrac_9104_freemod_name-fix-nt.patch\ntrac_8881-functorial_constructions-nt.patch\ntrac_8742-lazy_format-fh.patch\ntrac_8742-lazy_format-review-nt.patch\ntrac_8930-enumerated_set_deprecate-fh.patch\n8691_permutation_plainchange_tjb.patch\ntrac_8926_family_repr-fh.patch\ntrac_8902-subsets_call_fix-fh.patch\ntrac_8888_partition_rim-fh.patch\ntrac_8888_reviewer_jb.patch\ntrac_8811_reduced_word_of_translations-nt.patch\ntrac_8500_transitive_groups-final.patch\ntrac_8549_cycle_enumerator-nb.patch\ntrac_8490_square_free-vd.patch\ntrac_9096_disj_union_sphinx_fix-fh.patch\ntrac_8954-nilTemperley-as.patch\ntrac_8913-cayley_graph_twosided_labels-nt.patch\ntrac_8887-typo_monoid_prod-fh.patch\ntrac_9106-UniqueRep_sphinx_fix-fh.patch\ntrac_8876-triangular_morphisms_improve-fh.patch\ntrac_8876-reviewer_patch-jb.patch\nsage-5.0.patch\ntrac_9178-attrcall_hash_fix-nt.patch\ngap3_interface_v4.3.3.patch\ngap3_interface_patch2.patch\ntrac_8747-testsuite-speedup-fh.patch\ntrac_9056_semirings_category-nb.patch\ntrac_9056_semirings_category-review-nt.patch\n```\n",
    "created_at": "2010-06-07T20:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9056#issuecomment-84027",
    "user": "nthiery"
}
```

Arr, here is the list of patches in a more readable format:

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
```




---

archive/issue_comments_084028.json:
```json
{
    "body": "Attachment [trac_9056-disable-llt-test.patch](tarball://root/attachments/some-uuid/ticket9056/trac_9056-disable-llt-test.patch) by mhansen created at 2010-06-09 03:06:45",
    "created_at": "2010-06-09T03:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9056#issuecomment-84028",
    "user": "mhansen"
}
```

Attachment [trac_9056-disable-llt-test.patch](tarball://root/attachments/some-uuid/ticket9056/trac_9056-disable-llt-test.patch) by mhansen created at 2010-06-09 03:06:45



---

archive/issue_comments_084029.json:
```json
{
    "body": "Things look good to me.  Could I get a quick review of the patch I just posted.  Without this, llt.py times out.",
    "created_at": "2010-06-09T03:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9056#issuecomment-84029",
    "user": "mhansen"
}
```

Things look good to me.  Could I get a quick review of the patch I just posted.  Without this, llt.py times out.



---

archive/issue_comments_084030.json:
```json
{
    "body": "Replying to [comment:17 mhansen]:\n> Things look good to me.  Could I get a quick review of the patch I just posted.  Without this, llt.py times out.\n\nOn my copy of 4.4.4.alpha0, with attachment:trac_9056_semirings_category-nb.patch applied, I got the timeout without your reviewer patch, and it takes about 8 seconds with your patch. I don't like disabling our doctest coverage, but this seems reasonable. Positive review to your reviewer patch. I'm leaving this as needs_review; Mike, you can change this if everything else is okay.",
    "created_at": "2010-06-09T03:29:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9056#issuecomment-84030",
    "user": "ddrake"
}
```

Replying to [comment:17 mhansen]:
> Things look good to me.  Could I get a quick review of the patch I just posted.  Without this, llt.py times out.

On my copy of 4.4.4.alpha0, with attachment:trac_9056_semirings_category-nb.patch applied, I got the timeout without your reviewer patch, and it takes about 8 seconds with your patch. I don't like disabling our doctest coverage, but this seems reasonable. Positive review to your reviewer patch. I'm leaving this as needs_review; Mike, you can change this if everything else is okay.



---

archive/issue_comments_084031.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-09T03:30:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9056#issuecomment-84031",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_084032.json:
```json
{
    "body": "I've folded together the two #9056 patches on the combinat server together and merged the llt patch here.",
    "created_at": "2010-06-09T03:30:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9056#issuecomment-84032",
    "user": "mhansen"
}
```

I've folded together the two #9056 patches on the combinat server together and merged the llt patch here.



---

archive/issue_comments_084033.json:
```json
{
    "body": "Just as a little data point, on my machine, without Mike's patch, doctesting llt.py takes nearly 24 minutes (and passes!).",
    "created_at": "2010-06-09T04:16:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9056#issuecomment-84033",
    "user": "ddrake"
}
```

Just as a little data point, on my machine, without Mike's patch, doctesting llt.py takes nearly 24 minutes (and passes!).



---

archive/issue_comments_084034.json:
```json
{
    "body": "Thanks Mike for the fix!\n\nFor now, I still don't really manage to integrate completely such patch which touch so many things in Sage. Dependencies are not trivial when you begin to modify categories.\n\nFor Nicolas Thi\u00e9ry : This patch go in Sage before I fold your second reviewer patch :\n\n```\ndiff --git a/sage/categories/primer.py b/sage/categories/primer.py\n--- a/sage/categories/primer.py\n+++ b/sage/categories/primer.py\n@@ -122,6 +122,7 @@ Example of mathematical information::\n          Category of rings,\n          Category of rngs,\n          Category of commutative additive groups,\n+         Category of semirings,\n          Category of commutative additive monoids,\n          Category of commutative additive semigroups,\n          Category of additive magmas,\n@@ -503,6 +504,7 @@ This gives the following order::\n      Category of algebras over Rational Field,\n      Category of rings,\n      Category of rngs,\n+     Category of semirings,\n      Category of monoids,\n      Category of semigroups,\n      Category of magmas,\n```\n\n\nI don't no the status about your improvements of the category primer but be aware about this fact. As I don't want to produce some chaos in the queue, I didn't touch your reviewer patch \"trac_9056_semirings_category-review-nt.patch\".\n\nSorry to being late to fold it.\n\nNicolas (the little).",
    "created_at": "2010-06-09T07:45:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9056#issuecomment-84034",
    "user": "nborie"
}
```

Thanks Mike for the fix!

For now, I still don't really manage to integrate completely such patch which touch so many things in Sage. Dependencies are not trivial when you begin to modify categories.

For Nicolas Thiéry : This patch go in Sage before I fold your second reviewer patch :

```
diff --git a/sage/categories/primer.py b/sage/categories/primer.py
--- a/sage/categories/primer.py
+++ b/sage/categories/primer.py
@@ -122,6 +122,7 @@ Example of mathematical information::
          Category of rings,
          Category of rngs,
          Category of commutative additive groups,
+         Category of semirings,
          Category of commutative additive monoids,
          Category of commutative additive semigroups,
          Category of additive magmas,
@@ -503,6 +504,7 @@ This gives the following order::
      Category of algebras over Rational Field,
      Category of rings,
      Category of rngs,
+     Category of semirings,
      Category of monoids,
      Category of semigroups,
      Category of magmas,
```


I don't no the status about your improvements of the category primer but be aware about this fact. As I don't want to produce some chaos in the queue, I didn't touch your reviewer patch "trac_9056_semirings_category-review-nt.patch".

Sorry to being late to fold it.

Nicolas (the little).



---

archive/issue_comments_084035.json:
```json
{
    "body": "Replying to [comment:21 nborie]:\n> For now, I still don't really manage to integrate completely such patch which touch so many things in Sage. Dependencies are not trivial when you begin to modify categories.\n\nDon't worry, you are doing a great job.\n\n> For Nicolas Thi\u00e9ry : This patch go in Sage before I fold your second reviewer patch :\n\nMike said above that he took the two patches right away from the Sage-Combinat queue and folded them together. So all is fine.",
    "created_at": "2010-06-09T08:02:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9056#issuecomment-84035",
    "user": "nthiery"
}
```

Replying to [comment:21 nborie]:
> For now, I still don't really manage to integrate completely such patch which touch so many things in Sage. Dependencies are not trivial when you begin to modify categories.

Don't worry, you are doing a great job.

> For Nicolas Thiéry : This patch go in Sage before I fold your second reviewer patch :

Mike said above that he took the two patches right away from the Sage-Combinat queue and folded them together. So all is fine.



---

archive/issue_comments_084036.json:
```json
{
    "body": "Replying to [comment:19 mhansen]:\n> I've folded together the two #9056 patches on the combinat server together and merged the llt patch here.\n\nThanks Mike!\n\nFor later reference, do you mind uploading here the exact patches that you merged, if you still have them under hand?",
    "created_at": "2010-06-09T08:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9056#issuecomment-84036",
    "user": "nthiery"
}
```

Replying to [comment:19 mhansen]:
> I've folded together the two #9056 patches on the combinat server together and merged the llt patch here.

Thanks Mike!

For later reference, do you mind uploading here the exact patches that you merged, if you still have them under hand?
