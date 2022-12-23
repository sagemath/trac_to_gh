# Issue 7585: Fast function field arithmatic

archive/issues_007585.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  roed\n\nWrapping flint directly should be much faster than the current implementation of `Frac(GF(p)['t'])`\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7585\n\n",
    "created_at": "2009-12-02T19:00:33Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "Fast function field arithmatic",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7585",
    "user": "robertwb"
}
```
Assignee: AlexGhitza

CC:  roed

Wrapping flint directly should be much faster than the current implementation of `Frac(GF(p)['t'])`



Issue created by migration from https://trac.sagemath.org/ticket/7585





---

archive/issue_comments_064650.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-12-02T19:03:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64650",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_064651.json:
```json
{
    "body": "First pass, 4-40x faster.",
    "created_at": "2009-12-02T19:03:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64651",
    "user": "robertwb"
}
```

First pass, 4-40x faster.



---

archive/issue_comments_064652.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2009-12-02T19:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64652",
    "user": "robertwb"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_064653.json:
```json
{
    "body": "Still has a lot of work (better integration, doctests, testing...)",
    "created_at": "2009-12-02T19:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64653",
    "user": "robertwb"
}
```

Still has a lot of work (better integration, doctests, testing...)



---

archive/issue_comments_064654.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-12-05T17:54:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64654",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_064655.json:
```json
{
    "body": "Attachment\n\napply on top of previous",
    "created_at": "2009-12-08T08:09:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64655",
    "user": "robertwb"
}
```

Attachment

apply on top of previous



---

archive/issue_comments_064656.json:
```json
{
    "body": "I've added some doctests.  I'll try to split the work on FpT off from the rest of the things I've been doing on residue fields and post a patch tomorrow.",
    "created_at": "2009-12-11T21:09:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64656",
    "user": "roed"
}
```

I've added some doctests.  I'll try to split the work on FpT off from the rest of the things I've been doing on residue fields and post a patch tomorrow.



---

archive/issue_comments_064657.json:
```json
{
    "body": "Attachment\n\nRebased against 4.3.rc0",
    "created_at": "2009-12-15T16:51:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64657",
    "user": "roed"
}
```

Attachment

Rebased against 4.3.rc0



---

archive/issue_comments_064658.json:
```json
{
    "body": "Attachment\n\nRebased against 4.3.rc0",
    "created_at": "2009-12-15T16:51:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64658",
    "user": "roed"
}
```

Attachment

Rebased against 4.3.rc0



---

archive/issue_comments_064659.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-12-15T16:52:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64659",
    "user": "roed"
}
```

Attachment



---

archive/issue_comments_064660.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-12-15T16:52:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64660",
    "user": "roed"
}
```

Attachment



---

archive/issue_comments_064661.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-12-15T16:52:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64661",
    "user": "roed"
}
```

Attachment



---

archive/issue_comments_064662.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-12-15T16:52:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64662",
    "user": "roed"
}
```

Attachment



---

archive/issue_comments_064663.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-12-15T16:52:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64663",
    "user": "roed"
}
```

Attachment



---

archive/issue_comments_064664.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-12-15T16:53:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64664",
    "user": "roed"
}
```

Attachment



---

archive/issue_comments_064665.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-12-15T16:53:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64665",
    "user": "roed"
}
```

Attachment



---

archive/issue_comments_064666.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-12-15T16:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64666",
    "user": "roed"
}
```

Attachment



---

archive/issue_comments_064667.json:
```json
{
    "body": "Attachment\n\nThis combines all of the above into one patch, for easy application.  Based against 4.3.rc0",
    "created_at": "2009-12-15T16:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64667",
    "user": "roed"
}
```

Attachment

This combines all of the above into one patch, for easy application.  Based against 4.3.rc0



---

archive/issue_comments_064668.json:
```json
{
    "body": "A bit later than I said, but here are some patches.  I'm not sure if this is the right place to put all of them, but they're all related to GF(p)(t)... somehow (if only getting doctests that I broke fixed again)\n\nI've subsumed Robert's patches into 7585_1_FpT-orig.patch and 7585_2_FpT-more.patch.  The third patch is mostly focused on fraction_field_FpT.pyx.  The rest are mostly consequences of the changes I made to residue_field.pyx, but they're pretty wide ranging.\n\n7585_ALL.patch includes everything, but isn't viewable on trac since it's too big.",
    "created_at": "2009-12-15T17:01:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64668",
    "user": "roed"
}
```

A bit later than I said, but here are some patches.  I'm not sure if this is the right place to put all of them, but they're all related to GF(p)(t)... somehow (if only getting doctests that I broke fixed again)

I've subsumed Robert's patches into 7585_1_FpT-orig.patch and 7585_2_FpT-more.patch.  The third patch is mostly focused on fraction_field_FpT.pyx.  The rest are mostly consequences of the changes I made to residue_field.pyx, but they're pretty wide ranging.

7585_ALL.patch includes everything, but isn't viewable on trac since it's too big.



---

archive/issue_comments_064669.json:
```json
{
    "body": "Robert and David, is this ready for review yet?",
    "created_at": "2010-01-01T23:12:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64669",
    "user": "AlexGhitza"
}
```

Robert and David, is this ready for review yet?



---

archive/issue_comments_064670.json:
```json
{
    "body": "I think Robert wanted to factor out some of the stuff I'd written and do some more work on the actual FpT stuff.  Robert, what all do you want to happen to this ticket before review?",
    "created_at": "2010-01-01T23:21:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64670",
    "user": "roed"
}
```

I think Robert wanted to factor out some of the stuff I'd written and do some more work on the actual FpT stuff.  Robert, what all do you want to happen to this ticket before review?



---

archive/issue_comments_064671.json:
```json
{
    "body": "Yes, that is correct. I've been busy out of town, but should get a chance to take a look at this sometime next week. Nothing stopping you from starting to read the code though :).",
    "created_at": "2010-01-03T07:13:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64671",
    "user": "robertwb"
}
```

Yes, that is correct. I've been busy out of town, but should get a chance to take a look at this sometime next week. Nothing stopping you from starting to read the code though :).



---

archive/issue_comments_064672.json:
```json
{
    "body": "I've split this up as follows: \n\n#7880\n7585_4_sets_with_partial_maps.patch\n\n#7881\n7585_6_gcd.patch\n\n#7883\n7585_7_ideal.patch\n\n#7884\n7585_5_finite_fields_to_new_coercion.patch\n7585_8_parent_init.patch\n7585_9_frac_and_coerce_updates.patch\n\n#7885\n7585_10_residue_field.patch\n7585_11_tate_ff.patch\n7585_12_fixes.patch",
    "created_at": "2010-01-09T20:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64672",
    "user": "robertwb"
}
```

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

archive/issue_comments_064673.json:
```json
{
    "body": "I'm wary of the changes in 7585_8_parent_init.patch -- could you explain?",
    "created_at": "2010-01-09T20:30:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64673",
    "user": "robertwb"
}
```

I'm wary of the changes in 7585_8_parent_init.patch -- could you explain?



---

archive/issue_comments_064674.json:
```json
{
    "body": "I was a bit wary of them too, and wanted to ask a second opinion.\n\nThe goal is to make switching to the new coercion system as easy as possible.  Defining an _element_constructor_ method on a parent inheriting from parent_old.Parent currently has no effect, since the __init__ method on parent_old.Parent doesn't call the __init__ method on parent.Parent, nor does it set _element_constructor to be equal to _element_constructor_.  Ideally, parent_old.Parent's __init__ would call parent.Parent.__init__, but that change caused a ton of failures.  The change in parent_init.patch is more minor, just insuring that IF an _element_constructor_ method is defined, then self._element_constructor is appropriately set (and the coercion system thus believes that this parent uses the new coercion model)",
    "created_at": "2010-01-12T18:07:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64674",
    "user": "roed"
}
```

I was a bit wary of them too, and wanted to ask a second opinion.

The goal is to make switching to the new coercion system as easy as possible.  Defining an _element_constructor_ method on a parent inheriting from parent_old.Parent currently has no effect, since the __init__ method on parent_old.Parent doesn't call the __init__ method on parent.Parent, nor does it set _element_constructor to be equal to _element_constructor_.  Ideally, parent_old.Parent's __init__ would call parent.Parent.__init__, but that change caused a ton of failures.  The change in parent_init.patch is more minor, just insuring that IF an _element_constructor_ method is defined, then self._element_constructor is appropriately set (and the coercion system thus believes that this parent uses the new coercion model)



---

archive/issue_comments_064675.json:
```json
{
    "body": "FYI, I looked at this a bit during Sage days, but there were a lot of changes to the fraction field code in the alphas, so some rebasing needs to be done (and I didn't have a stable build to rebase on at the time).",
    "created_at": "2010-02-05T07:30:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64675",
    "user": "robertwb"
}
```

FYI, I looked at this a bit during Sage days, but there were a lot of changes to the fraction field code in the alphas, so some rebasing needs to be done (and I didn't have a stable build to rebase on at the time).



---

archive/issue_comments_064676.json:
```json
{
    "body": "I've split off the arithmatic into #9051.",
    "created_at": "2010-05-27T07:37:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64676",
    "user": "robertwb"
}
```

I've split off the arithmatic into #9051.



---

archive/issue_comments_064677.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-23T14:07:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64677",
    "user": "davidloeffler"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064678.json:
```json
{
    "body": "David, Robert: what's the status of this ticket? Now that #9051 is in, and patches 4-12 have been split off into separate tickets, can we close this ticket as a duplicate? If this is true, please set it to \"positive review\" so the release manager can close it.",
    "created_at": "2010-09-23T14:07:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64678",
    "user": "davidloeffler"
}
```

David, Robert: what's the status of this ticket? Now that #9051 is in, and patches 4-12 have been split off into separate tickets, can we close this ticket as a duplicate? If this is true, please set it to "positive review" so the release manager can close it.



---

archive/issue_comments_064679.json:
```json
{
    "body": "All of the patches here have found other homes.  I'm happy to make it duplicate.",
    "created_at": "2010-09-23T15:09:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64679",
    "user": "roed"
}
```

All of the patches here have found other homes.  I'm happy to make it duplicate.



---

archive/issue_comments_064680.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-23T15:09:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64680",
    "user": "roed"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064681.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-09-28T11:13:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7585#issuecomment-64681",
    "user": "mpatel"
}
```

Resolution: duplicate
