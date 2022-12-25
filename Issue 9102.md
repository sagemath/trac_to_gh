# Issue 9102: Docstring improvements for strong generating systems of permutation groups

archive/issues_009102.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @nthiery nborie @qed777 @williamstein @mwhansen jasonbhill\n\nI put this together as a reviewer patch for a ticket that I thought needed review (#8030), but which was already reviewed.  Rather than letting it go to waste, here it is.\n\nIt will depend on #8030.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9102\n\n",
    "created_at": "2010-05-31T03:33:41Z",
    "labels": [
        "component: algebra",
        "trivial"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "Docstring improvements for strong generating systems of permutation groups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9102",
    "user": "https://github.com/rbeezer"
}
```
Assignee: @aghitza

CC:  @nthiery nborie @qed777 @williamstein @mwhansen jasonbhill

I put this together as a reviewer patch for a ticket that I thought needed review (#8030), but which was already reviewed.  Rather than letting it go to waste, here it is.

It will depend on #8030.

Issue created by migration from https://trac.sagemath.org/ticket/9102





---

archive/issue_comments_084433.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-31T03:37:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9102#issuecomment-84433",
    "user": "https://github.com/rbeezer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084434.json:
```json
{
    "body": "Attachment [trac_9102-docstring-strong-generating-system.patch](tarball://root/attachments/some-uuid/ticket9102/trac_9102-docstring-strong-generating-system.patch) by @rbeezer created at 2010-05-31 03:37:29",
    "created_at": "2010-05-31T03:37:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9102#issuecomment-84434",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_9102-docstring-strong-generating-system.patch](tarball://root/attachments/some-uuid/ticket9102/trac_9102-docstring-strong-generating-system.patch) by @rbeezer created at 2010-05-31 03:37:29



---

archive/issue_comments_084435.json:
```json
{
    "body": "The patch here *may* cause a problem with building the PDF reference manual.  Please see [comment:ticket:8030:10 this comment] at #8030.",
    "created_at": "2010-06-03T09:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9102#issuecomment-84435",
    "user": "https://github.com/qed777"
}
```

The patch here *may* cause a problem with building the PDF reference manual.  Please see [comment:ticket:8030:10 this comment] at #8030.



---

archive/issue_comments_084436.json:
```json
{
    "body": "Changing priority from trivial to blocker.",
    "created_at": "2010-06-03T15:33:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9102#issuecomment-84436",
    "user": "https://github.com/rbeezer"
}
```

Changing priority from trivial to blocker.



---

archive/issue_comments_084437.json:
```json
{
    "body": "Attachment [trac_9102-docstring-strong-generating-system-v2.patch](tarball://root/attachments/some-uuid/ticket9102/trac_9102-docstring-strong-generating-system-v2.patch) by @rbeezer created at 2010-06-03 15:33:59\n\nRevised patch (version 2) addresses the failure to build the PDF version of the reference manual, as described at #8030.  The only difference in the v2 patch is to replace two \"\\leqslant\" by \"\\leq\".  However, there are other documentation changes here that need review (ie, the whole v2 patch)  Both PDF and HTML now build fine and look fine.\n\nLong term, we should see why this AMS symbol is not present for the PDF, while is present for the HTML.\n\nMisha - can you review?\n\nI've marked this as a blocker as part of the 4.4.3 alpha series in hopes of having it make it into the final, since #8030 introduced the failure to build the PDF version and is merged already.\n\nRob",
    "created_at": "2010-06-03T15:33:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9102#issuecomment-84437",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_9102-docstring-strong-generating-system-v2.patch](tarball://root/attachments/some-uuid/ticket9102/trac_9102-docstring-strong-generating-system-v2.patch) by @rbeezer created at 2010-06-03 15:33:59

Revised patch (version 2) addresses the failure to build the PDF version of the reference manual, as described at #8030.  The only difference in the v2 patch is to replace two "\leqslant" by "\leq".  However, there are other documentation changes here that need review (ie, the whole v2 patch)  Both PDF and HTML now build fine and look fine.

Long term, we should see why this AMS symbol is not present for the PDF, while is present for the HTML.

Misha - can you review?

I've marked this as a blocker as part of the 4.4.3 alpha series in hopes of having it make it into the final, since #8030 introduced the failure to build the PDF version and is merged already.

Rob



---

archive/issue_comments_084438.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-03T23:31:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9102#issuecomment-84438",
    "user": "https://trac.sagemath.org/admin/accounts/users/jasonbhill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_084439.json:
```json
{
    "body": "While looking at the amssymb issue, I came across a problem elsewhere in what has been added to the docstring.\n\n\"``base_of_group`` is a list of the  positions on which ``self`` acts,\"\n\nThis is not correct. The base of a permutation group G is defined as a list L of points in the domain of the action such that no element of G fixes all points of L.\n\nhttp://en.wikipedia.org/wiki/Base_(group_theory)\n\nComputationally, this is equivalent to requiring no strong generator to fix all points of the base, and hence the size of a base corresponds directly to the length of the stabilizer chain given by the Schreier-Sims algorithm. (In fact, this algorithm yields a base and the strong generating system relative to that specific base.)\n\nThe assertion that the base is not unique is correct, but the specific base used must correspond to the stabilizer chain constructed from a strong generating set. Otherwise, the information of the strong generating set is of less computational value.\n\nFor instance, a symmetric group of degree n has base of size n-1. So, S_5 on points [1..5] has bases [1,2,4,5], [1,2,3,4], etc., depending on the SGS. At the same time, any cyclic group has a base of size 1.\n\nYou may of course artificially inflate the base and it will still follow the definition, but then anyone using the strong generating set for calculations (MANY invariants of a group follow from this) must recalculate the base and this will often result in a different SGS.",
    "created_at": "2010-06-03T23:31:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9102#issuecomment-84439",
    "user": "https://trac.sagemath.org/admin/accounts/users/jasonbhill"
}
```

While looking at the amssymb issue, I came across a problem elsewhere in what has been added to the docstring.

"``base_of_group`` is a list of the  positions on which ``self`` acts,"

This is not correct. The base of a permutation group G is defined as a list L of points in the domain of the action such that no element of G fixes all points of L.

http://en.wikipedia.org/wiki/Base_(group_theory)

Computationally, this is equivalent to requiring no strong generator to fix all points of the base, and hence the size of a base corresponds directly to the length of the stabilizer chain given by the Schreier-Sims algorithm. (In fact, this algorithm yields a base and the strong generating system relative to that specific base.)

The assertion that the base is not unique is correct, but the specific base used must correspond to the stabilizer chain constructed from a strong generating set. Otherwise, the information of the strong generating set is of less computational value.

For instance, a symmetric group of degree n has base of size n-1. So, S_5 on points [1..5] has bases [1,2,4,5], [1,2,3,4], etc., depending on the SGS. At the same time, any cyclic group has a base of size 1.

You may of course artificially inflate the base and it will still follow the definition, but then anyone using the strong generating set for calculations (MANY invariants of a group follow from this) must recalculate the base and this will often result in a different SGS.



---

archive/issue_comments_084440.json:
```json
{
    "body": "Replying to [comment:5 jasonbhill]:\n> While looking at the amssymb issue, I came across a problem elsewhere in what has been added to the docstring.\n\nHi Jason,\n\nI've been thinking about this, and wondering if you could move this to a new ticket?  #8030 was about fixing the stabilizer routine, which meant changes in the docstring for strong generating systems.  The latex there is causing an error in building the documentation, which is being fixed on this ticket.\n\nI'd really like to see the error corrected ASAP, and not held up by this discussion on content for strong generating systems.  I think the base_of_group description predates #8030 anyway.\n\nSo it'd be great if we use this ticket to fix formatting, and have the design discussion on a new ticket?  Would you mind?\n\nThanks,\nRob",
    "created_at": "2010-06-05T03:21:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9102#issuecomment-84440",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:5 jasonbhill]:
> While looking at the amssymb issue, I came across a problem elsewhere in what has been added to the docstring.

Hi Jason,

I've been thinking about this, and wondering if you could move this to a new ticket?  #8030 was about fixing the stabilizer routine, which meant changes in the docstring for strong generating systems.  The latex there is causing an error in building the documentation, which is being fixed on this ticket.

I'd really like to see the error corrected ASAP, and not held up by this discussion on content for strong generating systems.  I think the base_of_group description predates #8030 anyway.

So it'd be great if we use this ticket to fix formatting, and have the design discussion on a new ticket?  Would you mind?

Thanks,
Rob



---

archive/issue_comments_084441.json:
```json
{
    "body": "Replying to [comment:5 jasonbhill]:\n> While looking at the amssymb issue, I came across a problem elsewhere in what has been added to the docstring.\n> \n> \"``base_of_group`` is a list of the  positions on which ``self`` acts,\"\n> \n> This is not correct. The base of a permutation group G is defined as a list L of points in the domain of the action such that no element of G fixes all points of L.\n> \n> http://en.wikipedia.org/wiki/Base_(group_theory)\n> \n> Computationally, this is equivalent to requiring no strong generator to fix all points of the base, and hence the size of a base corresponds directly to the length of the stabilizer chain given by the Schreier-Sims algorithm. (In fact, this algorithm yields a base and the strong generating system relative to that specific base.)\n> \n> The assertion that the base is not unique is correct, but the specific base used must correspond to the stabilizer chain constructed from a strong generating set. Otherwise, the information of the strong generating set is of less computational value.\n> \n> For instance, a symmetric group of degree n has base of size n-1. So, S_5 on points [1..5] has bases [1,2,4,5], [1,2,3,4], etc., depending on the SGS. At the same time, any cyclic group has a base of size 1.\n> \n> You may of course artificially inflate the base and it will still follow the definition, but then anyone using the strong generating set for calculations (MANY invariants of a group follow from this) must recalculate the base and this will often result in a different SGS.",
    "created_at": "2010-06-05T14:02:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9102#issuecomment-84441",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:5 jasonbhill]:
> While looking at the amssymb issue, I came across a problem elsewhere in what has been added to the docstring.
> 
> "``base_of_group`` is a list of the  positions on which ``self`` acts,"
> 
> This is not correct. The base of a permutation group G is defined as a list L of points in the domain of the action such that no element of G fixes all points of L.
> 
> http://en.wikipedia.org/wiki/Base_(group_theory)
> 
> Computationally, this is equivalent to requiring no strong generator to fix all points of the base, and hence the size of a base corresponds directly to the length of the stabilizer chain given by the Schreier-Sims algorithm. (In fact, this algorithm yields a base and the strong generating system relative to that specific base.)
> 
> The assertion that the base is not unique is correct, but the specific base used must correspond to the stabilizer chain constructed from a strong generating set. Otherwise, the information of the strong generating set is of less computational value.
> 
> For instance, a symmetric group of degree n has base of size n-1. So, S_5 on points [1..5] has bases [1,2,4,5], [1,2,3,4], etc., depending on the SGS. At the same time, any cyclic group has a base of size 1.
> 
> You may of course artificially inflate the base and it will still follow the definition, but then anyone using the strong generating set for calculations (MANY invariants of a group follow from this) must recalculate the base and this will often result in a different SGS.



---

archive/issue_comments_084442.json:
```json
{
    "body": "Hi Jason,\n\n(please ignore my previous comment which was a fumble)\n\nReplying to [comment:5 jasonbhill]:\n> While looking at the amssymb issue, I came across a problem elsewhere in what has been added to the docstring.\n> \n> \"``base_of_group`` is a list of the  positions on which ``self`` acts,\"\n> \n> This is not correct. The base of a permutation group G is defined as a list L of points in the domain of the action such that no element of G fixes all points of L.\n> \n> http://en.wikipedia.org/wiki/Base_(group_theory)\n> \n> Computationally, this is equivalent to requiring no strong generator to fix all points of the base, and hence the size of a base corresponds directly to the length of the stabilizer chain given by the Schreier-Sims algorithm. (In fact, this algorithm yields a base and the strong generating system relative to that specific base.)\n> \n> The assertion that the base is not unique is correct, but the specific base used must correspond to the stabilizer chain constructed from a strong generating set. Otherwise, the information of the strong generating set is of less computational value.\n> \n> For instance, a symmetric group of degree n has base of size n-1. So, S_5 on points [1..5] has bases [1,2,4,5], [1,2,3,4], etc., depending on the SGS. At the same time, any cyclic group has a base of size 1.\n> \n> You may of course artificially inflate the base and it will still follow the definition, but then anyone using the strong generating set for calculations (MANY invariants of a group follow from this) must recalculate the base and this will often result in a different SGS.\n\nWell, the code is correct: given a user-provided base, the code\nreturns a strong-generating-set with respect to this base. Indeed, the\ndefinition of `base` in the docstring is needlessly restrictive;\nit sure needs not contain all points.\n\nA patch fixing this would be very welcome. I agree with Rob though\nthat this would be best left in a followup ticket. It would also\nprobably be best to wait until Mike's patch for permutation groups on\nany set is merged in Sage to avoid conflicts, and not make his job\nharder. There are several little things that could be improved as well\nin the future:\n\n* Check that `base` is a subset of the domain of this group\n  (i.e. the set on which the group act)\n* Test that the final stabilizer set is indeed trivial\n* Use the current base of the group as default value, and return\n  directly the strong generating set that GAP already has computed\n  for this group.\n\nCheers,\n\t\t\tNicolas",
    "created_at": "2010-06-05T14:12:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9102#issuecomment-84442",
    "user": "https://github.com/nthiery"
}
```

Hi Jason,

(please ignore my previous comment which was a fumble)

Replying to [comment:5 jasonbhill]:
> While looking at the amssymb issue, I came across a problem elsewhere in what has been added to the docstring.
> 
> "``base_of_group`` is a list of the  positions on which ``self`` acts,"
> 
> This is not correct. The base of a permutation group G is defined as a list L of points in the domain of the action such that no element of G fixes all points of L.
> 
> http://en.wikipedia.org/wiki/Base_(group_theory)
> 
> Computationally, this is equivalent to requiring no strong generator to fix all points of the base, and hence the size of a base corresponds directly to the length of the stabilizer chain given by the Schreier-Sims algorithm. (In fact, this algorithm yields a base and the strong generating system relative to that specific base.)
> 
> The assertion that the base is not unique is correct, but the specific base used must correspond to the stabilizer chain constructed from a strong generating set. Otherwise, the information of the strong generating set is of less computational value.
> 
> For instance, a symmetric group of degree n has base of size n-1. So, S_5 on points [1..5] has bases [1,2,4,5], [1,2,3,4], etc., depending on the SGS. At the same time, any cyclic group has a base of size 1.
> 
> You may of course artificially inflate the base and it will still follow the definition, but then anyone using the strong generating set for calculations (MANY invariants of a group follow from this) must recalculate the base and this will often result in a different SGS.

Well, the code is correct: given a user-provided base, the code
returns a strong-generating-set with respect to this base. Indeed, the
definition of `base` in the docstring is needlessly restrictive;
it sure needs not contain all points.

A patch fixing this would be very welcome. I agree with Rob though
that this would be best left in a followup ticket. It would also
probably be best to wait until Mike's patch for permutation groups on
any set is merged in Sage to avoid conflicts, and not make his job
harder. There are several little things that could be improved as well
in the future:

* Check that `base` is a subset of the domain of this group
  (i.e. the set on which the group act)
* Test that the final stabilizer set is indeed trivial
* Use the current base of the group as default value, and return
  directly the strong generating set that GAP already has computed
  for this group.

Cheers,
			Nicolas



---

archive/issue_comments_084443.json:
```json
{
    "body": "As a result of the above discussion, I've changed the action back to \"needs review.\"\n\nI will migrate this BSGS issue to a new ticket once domains can be made arbitrary.\n\nThanks for your comments Nicolas! I have some comments and questions and I will post those once I have things organized the domain work is done. For now, can someone please explain (remember that I am relatively new to Sage) where/why/how self.base() is obtaining \"Integer Ring\"? This seems like an obvious and currently not helpful output. Why not simply ask GAP for a base if one does not wish to input one?",
    "created_at": "2010-06-05T17:40:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9102#issuecomment-84443",
    "user": "https://trac.sagemath.org/admin/accounts/users/jasonbhill"
}
```

As a result of the above discussion, I've changed the action back to "needs review."

I will migrate this BSGS issue to a new ticket once domains can be made arbitrary.

Thanks for your comments Nicolas! I have some comments and questions and I will post those once I have things organized the domain work is done. For now, can someone please explain (remember that I am relatively new to Sage) where/why/how self.base() is obtaining "Integer Ring"? This seems like an obvious and currently not helpful output. Why not simply ask GAP for a base if one does not wish to input one?



---

archive/issue_comments_084444.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-05T17:40:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9102#issuecomment-84444",
    "user": "https://trac.sagemath.org/admin/accounts/users/jasonbhill"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084445.json:
```json
{
    "body": "Replying to [comment:9 jasonbhill]:\n> Thanks for your comments Nicolas! I have some comments and questions and I will post those once I have things organized the domain work is done. For now, can someone please explain (remember that I am relatively new to Sage) where/why/how self.base() is obtaining \"Integer Ring\"? This seems like an obvious and currently not helpful output. Why not simply ask GAP for a base if one does not wish to input one?\n\nThis is a naming conflict. Permutation groups inherit from\nParentWithGens to handle its generators. This class itself inherits\nfrom ParentWithBase.  It should not be so: ParentWithBase are meant\nfor things like modules/algebras over a base ring, and there are\nparents with generators but no sensible base \"ring\". However the class\nhierarchy for parents was forced to be linear by the absence of\nmultiple inheritance in Cython, which produces a couple\nglitches/abuses like this one. Those glitches should progressively be\nfixed as the parents all get completely migrated to categories.\n\nIn short: the default implementation of base returning Integer Ring in\nPermutationGroups is meaningless, and would be best overridden,\ntypically by asking GAP as you suggest.",
    "created_at": "2010-06-05T19:50:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9102#issuecomment-84445",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:9 jasonbhill]:
> Thanks for your comments Nicolas! I have some comments and questions and I will post those once I have things organized the domain work is done. For now, can someone please explain (remember that I am relatively new to Sage) where/why/how self.base() is obtaining "Integer Ring"? This seems like an obvious and currently not helpful output. Why not simply ask GAP for a base if one does not wish to input one?

This is a naming conflict. Permutation groups inherit from
ParentWithGens to handle its generators. This class itself inherits
from ParentWithBase.  It should not be so: ParentWithBase are meant
for things like modules/algebras over a base ring, and there are
parents with generators but no sensible base "ring". However the class
hierarchy for parents was forced to be linear by the absence of
multiple inheritance in Cython, which produces a couple
glitches/abuses like this one. Those glitches should progressively be
fixed as the parents all get completely migrated to categories.

In short: the default implementation of base returning Integer Ring in
PermutationGroups is meaningless, and would be best overridden,
typically by asking GAP as you suggest.



---

archive/issue_comments_084446.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-06T03:29:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9102#issuecomment-84446",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084447.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2010-07-06T03:37:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9102#issuecomment-84447",
    "user": "https://github.com/rlmill"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_084448.json:
```json
{
    "body": "Rob,\n\nLooks like I acted too soon. In fact, it looks like your ref patch at #8030 has already been merged. The patch here is completely redundant. I'll close it as duplicate, if you can verify that all is well now.",
    "created_at": "2010-07-06T03:39:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9102#issuecomment-84448",
    "user": "https://github.com/rlmill"
}
```

Rob,

Looks like I acted too soon. In fact, it looks like your ref patch at #8030 has already been merged. The patch here is completely redundant. I'll close it as duplicate, if you can verify that all is well now.



---

archive/issue_comments_084449.json:
```json
{
    "body": "Replying to [comment:13 rlm]:\n> Looks like I acted too soon. In fact, it looks like your ref patch at #8030 has already been merged. The patch here is completely redundant. I'll close it as duplicate, if you can verify that all is well now.\n\nNot totally redundant, but a mess-up.  I attached the reviewer-edit patch to #8030 *after* the rest of the ticket had been reviewed.  It shouldn't have been merged (my fault, I should have left clear instructions).  I had put it onto a new ticket (here, #9102).  Then it got revised (the v2 patch here).  So the original patch never got reviewed and the minor changes to make the v2 patch need to be made.\n\nI'll make a small patch here for the modifications that realize the v2 version?  Without it, I think the PDF version of the docs fails?  (I'll check.)  I'm moving to \"needs work\".\n\nRob",
    "created_at": "2010-07-06T04:18:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9102#issuecomment-84449",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:13 rlm]:
> Looks like I acted too soon. In fact, it looks like your ref patch at #8030 has already been merged. The patch here is completely redundant. I'll close it as duplicate, if you can verify that all is well now.

Not totally redundant, but a mess-up.  I attached the reviewer-edit patch to #8030 *after* the rest of the ticket had been reviewed.  It shouldn't have been merged (my fault, I should have left clear instructions).  I had put it onto a new ticket (here, #9102).  Then it got revised (the v2 patch here).  So the original patch never got reviewed and the minor changes to make the v2 patch need to be made.

I'll make a small patch here for the modifications that realize the v2 version?  Without it, I think the PDF version of the docs fails?  (I'll check.)  I'm moving to "needs work".

Rob



---

archive/issue_comments_084450.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2010-07-06T04:18:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9102#issuecomment-84450",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_084451.json:
```json
{
    "body": "Attachment [trac_9102-docstring-strong-generating-system-v3.patch](tarball://root/attachments/some-uuid/ticket9102/trac_9102-docstring-strong-generating-system-v3.patch) by @rbeezer created at 2010-07-06 04:27:04",
    "created_at": "2010-07-06T04:27:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9102#issuecomment-84451",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_9102-docstring-strong-generating-system-v3.patch](tarball://root/attachments/some-uuid/ticket9102/trac_9102-docstring-strong-generating-system-v3.patch) by @rbeezer created at 2010-07-06 04:27:04



---

archive/issue_comments_084452.json:
```json
{
    "body": "Version 3 patch only changes two \\leqslant to simply \\leq since the Sage/TeX/PDF documentation build complains about the former version of an inequality symbol.  I can't verify this right now, since the PDF version won't get past some `UniqueRepresentation.__classcall__` stuff that I think is known.\n\nSince the v1 patch is merged, this replicates the effect of the v2 patch.  So apply *only* the v3 patch to 4.5.alpha3 to get everything back together.  Sorry for the confusion.\n\nRob",
    "created_at": "2010-07-06T04:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9102#issuecomment-84452",
    "user": "https://github.com/rbeezer"
}
```

Version 3 patch only changes two \leqslant to simply \leq since the Sage/TeX/PDF documentation build complains about the former version of an inequality symbol.  I can't verify this right now, since the PDF version won't get past some `UniqueRepresentation.__classcall__` stuff that I think is known.

Since the v1 patch is merged, this replicates the effect of the v2 patch.  So apply *only* the v3 patch to 4.5.alpha3 to get everything back together.  Sorry for the confusion.

Rob



---

archive/issue_comments_084453.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-06T04:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9102#issuecomment-84453",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084454.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-06T08:07:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9102#issuecomment-84454",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084455.json:
```json
{
    "body": "Apply v3 only.",
    "created_at": "2010-07-06T08:07:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9102#issuecomment-84455",
    "user": "https://github.com/rlmill"
}
```

Apply v3 only.



---

archive/issue_comments_084456.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-06T08:09:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9102#issuecomment-84456",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_084457.json:
```json
{
    "body": "Belated note: With #9331 and V3, the PDF reference manual builds for me.",
    "created_at": "2010-07-06T08:34:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9102#issuecomment-84457",
    "user": "https://github.com/qed777"
}
```

Belated note: With #9331 and V3, the PDF reference manual builds for me.



---

archive/issue_comments_084458.json:
```json
{
    "body": "Misha:  thanks for the check.\n\nRobert: thanks for seeing that this needed some work and the review.\n\nRob",
    "created_at": "2010-07-06T15:58:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9102#issuecomment-84458",
    "user": "https://github.com/rbeezer"
}
```

Misha:  thanks for the check.

Robert: thanks for seeing that this needed some work and the review.

Rob
