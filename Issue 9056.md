# Issue 9056: Add the category of SemiRings with an example : NonNegativeIntegers()

Issue created by migration from Trac.

Original creator: nborie

Original creation time: 2010-05-26 14:26:00

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



---

Comment by nborie created at 2010-05-27 13:19:16

Changing status from new to needs_review.


---

Attachment


---

Comment by nthiery created at 2010-05-27 14:55:19

I reviewed this patch while Nicolas was writting it. I'll run the tests shortly, and report.

Florent: please have a look to see if you agree with the concept, and if yes set a positive review.


---

Comment by nthiery created at 2010-05-27 15:48:17

Hi Nicolas B.,

There are a couple failures in the category tests (due to the new test and new category); please fix them. Note that I made a small change to your patch, so you should make sure to first pull.

You might get a conflict with the primer improvement; in that case, move your patch just after it.


---

Comment by nthiery created at 2010-05-27 15:48:17

Changing status from needs_review to needs_work.


---

Comment by nthiery created at 2010-05-27 16:02:16

Replying to [comment:5 nthiery]:
> There are a couple failures in the category tests (due to the new test and new category); please fix them. Note that I made a small change to your patch, so you should make sure to first pull.

A couple failures in combinat/sf as well due to the new _test_distributivity.


---

Comment by nborie created at 2010-05-27 20:50:37

Changing status from needs_work to needs_review.


---

Comment by nborie created at 2010-05-27 20:50:37

As I did manage to run ALL TESTS on sagemath, I found files this patch affect... I didn't touch the primer (modified on combinat queue). This patch will have yo be updated if your primer improvements go in sage earlier.

I update the patch (without .2.patch, forget this one.)

Thank for your help for massive tests.


---

Comment by nborie created at 2010-05-27 20:57:53

Sorry and please wait, this local patch will break your queue Nicolas.


---

Comment by nborie created at 2010-05-28 12:39:37

This last update should be fine...


---

Comment by nborie created at 2010-05-31 13:35:10

One more update :

After advises form English speaker people, I change the name from NonNegativeIntegersSemiring to NonNegativeIntegerSemiring. See http://groups.google.com/group/sage-devel/browse_thread/thread/ffaf01ffb941078

I linked my module to the reference manual and fix a :class: ref in the doc thanks to Florent.

I am still ready for deeper review.


---

Comment by nthiery created at 2010-06-07 16:37:02

Hi Nicolas,

Thanks for finalizing this!

I just pushed a small reviewer's patch on sage-combinat. Please review, and if ok fold and reupload here.


---

Comment by nborie created at 2010-06-07 17:09:03

Changing status from needs_review to positive_review.


---

Attachment

I am ok with your reviewer patch. I will try to delete ending blanks on my own since you made work well coloring with my hg qdiff. I qfolded your patch in mine and uploaded it...

Thanks for the review.

For the release manager ,apply only 
attachment:trac_9056_semirings_category-nb.patch


---

Comment by nthiery created at 2010-06-07 19:41:23

I did not yet say to set a positive review on my behalf :-)
Actually one test was failing in the primer. I am rerunning all tests.


---

Comment by nthiery created at 2010-06-07 19:41:23

Changing status from positive_review to needs_work.


---

Comment by nthiery created at 2010-06-07 20:58:20

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2010-06-07 20:58:20

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

Comment by nthiery created at 2010-06-07 20:59:07

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

Attachment


---

Comment by mhansen created at 2010-06-09 03:07:33

Things look good to me.  Could I get a quick review of the patch I just posted.  Without this, llt.py times out.


---

Comment by ddrake created at 2010-06-09 03:29:16

Replying to [comment:17 mhansen]:
> Things look good to me.  Could I get a quick review of the patch I just posted.  Without this, llt.py times out.

On my copy of 4.4.4.alpha0, with attachment:trac_9056_semirings_category-nb.patch applied, I got the timeout without your reviewer patch, and it takes about 8 seconds with your patch. I don't like disabling our doctest coverage, but this seems reasonable. Positive review to your reviewer patch. I'm leaving this as needs_review; Mike, you can change this if everything else is okay.


---

Comment by mhansen created at 2010-06-09 03:30:54

Resolution: fixed


---

Comment by mhansen created at 2010-06-09 03:30:54

I've folded together the two #9056 patches on the combinat server together and merged the llt patch here.


---

Comment by ddrake created at 2010-06-09 04:16:21

Just as a little data point, on my machine, without Mike's patch, doctesting llt.py takes nearly 24 minutes (and passes!).


---

Comment by nborie created at 2010-06-09 07:45:37

Thanks Mike for the fix!

For now, I still don't really manage to integrate completely such patch which touch so many things in Sage. Dependencies are not trivial when you begin to modify categories.

For Nicolas Thiéry : This patch go in Sage before I fold your second reviewer patch :

```
diff --git a/sage/categories/primer.py b/sage/categories/primer.py
--- a/sage/categories/primer.py
+++ b/sage/categories/primer.py
`@``@` -122,6 +122,7 `@``@` Example of mathematical information::
          Category of rings,
          Category of rngs,
          Category of commutative additive groups,
+         Category of semirings,
          Category of commutative additive monoids,
          Category of commutative additive semigroups,
          Category of additive magmas,
`@``@` -503,6 +504,7 `@``@` This gives the following order::
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

Comment by nthiery created at 2010-06-09 08:02:05

Replying to [comment:21 nborie]:
> For now, I still don't really manage to integrate completely such patch which touch so many things in Sage. Dependencies are not trivial when you begin to modify categories.

Don't worry, you are doing a great job.

> For Nicolas Thiéry : This patch go in Sage before I fold your second reviewer patch :

Mike said above that he took the two patches right away from the Sage-Combinat queue and folded them together. So all is fine.


---

Comment by nthiery created at 2010-06-09 08:03:39

Replying to [comment:19 mhansen]:
> I've folded together the two #9056 patches on the combinat server together and merged the llt patch here.

Thanks Mike!

For later reference, do you mind uploading here the exact patches that you merged, if you still have them under hand?
