# Issue 7585: Fast function field arithmatic

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-12-02 19:00:33

Assignee: AlexGhitza

CC:  roed

Wrapping flint directly should be much faster than the current implementation of `Frac(GF(p)['t'])`




---

Attachment


---

Comment by robertwb created at 2009-12-02 19:03:54

First pass, 4-40x faster.


---

Comment by robertwb created at 2009-12-02 19:04:38

Changing status from new to needs_work.


---

Comment by robertwb created at 2009-12-02 19:04:38

Still has a lot of work (better integration, doctests, testing...)


---

Attachment


---

Attachment

apply on top of previous


---

Comment by roed created at 2009-12-11 21:09:26

I've added some doctests.  I'll try to split the work on FpT off from the rest of the things I've been doing on residue fields and post a patch tomorrow.


---

Attachment

Rebased against 4.3.rc0


---

Attachment

Rebased against 4.3.rc0


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment

This combines all of the above into one patch, for easy application.  Based against 4.3.rc0


---

Comment by roed created at 2009-12-15 17:01:16

A bit later than I said, but here are some patches.  I'm not sure if this is the right place to put all of them, but they're all related to GF(p)(t)... somehow (if only getting doctests that I broke fixed again)

I've subsumed Robert's patches into 7585_1_FpT-orig.patch and 7585_2_FpT-more.patch.  The third patch is mostly focused on fraction_field_FpT.pyx.  The rest are mostly consequences of the changes I made to residue_field.pyx, but they're pretty wide ranging.

7585_ALL.patch includes everything, but isn't viewable on trac since it's too big.


---

Comment by AlexGhitza created at 2010-01-01 23:12:42

Robert and David, is this ready for review yet?


---

Comment by roed created at 2010-01-01 23:21:23

I think Robert wanted to factor out some of the stuff I'd written and do some more work on the actual FpT stuff.  Robert, what all do you want to happen to this ticket before review?


---

Comment by robertwb created at 2010-01-03 07:13:14

Yes, that is correct. I've been busy out of town, but should get a chance to take a look at this sometime next week. Nothing stopping you from starting to read the code though :).


---

Comment by robertwb created at 2010-01-09 20:21:49

I've split this up as follows: 

#7880
7585_4_sets_with_partial_maps.patch

#7881
7585_6_gcd.patch

#7883
7585_7_ideal.patch

#7884
7585_5_finite_fields_to_new_coercion.patch
7585_8_parent_init.patch
7585_9_frac_and_coerce_updates.patch

#7885
7585_10_residue_field.patch
7585_11_tate_ff.patch
7585_12_fixes.patch


---

Comment by robertwb created at 2010-01-09 20:30:38

I'm wary of the changes in 7585_8_parent_init.patch -- could you explain?


---

Comment by roed created at 2010-01-12 18:07:23

I was a bit wary of them too, and wanted to ask a second opinion.

The goal is to make switching to the new coercion system as easy as possible.  Defining an _element_constructor_ method on a parent inheriting from parent_old.Parent currently has no effect, since the __init__ method on parent_old.Parent doesn't call the __init__ method on parent.Parent, nor does it set _element_constructor to be equal to _element_constructor_.  Ideally, parent_old.Parent's __init__ would call parent.Parent.__init__, but that change caused a ton of failures.  The change in parent_init.patch is more minor, just insuring that IF an _element_constructor_ method is defined, then self._element_constructor is appropriately set (and the coercion system thus believes that this parent uses the new coercion model)


---

Comment by robertwb created at 2010-02-05 07:30:29

FYI, I looked at this a bit during Sage days, but there were a lot of changes to the fraction field code in the alphas, so some rebasing needs to be done (and I didn't have a stable build to rebase on at the time).


---

Comment by robertwb created at 2010-05-27 07:37:12

I've split off the arithmatic into #9051.


---

Comment by davidloeffler created at 2010-09-23 14:07:52

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2010-09-23 14:07:52

David, Robert: what's the status of this ticket? Now that #9051 is in, and patches 4-12 have been split off into separate tickets, can we close this ticket as a duplicate? If this is true, please set it to "positive review" so the release manager can close it.


---

Comment by roed created at 2010-09-23 15:09:17

All of the patches here have found other homes.  I'm happy to make it duplicate.


---

Comment by roed created at 2010-09-23 15:09:17

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-28 11:13:54

Resolution: duplicate
