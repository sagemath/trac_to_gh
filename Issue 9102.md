# Issue 9102: Docstring improvements for strong generating systems of permutation groups

Issue created by migration from https://trac.sagemath.org/ticket/9102

Original creator: rbeezer

Original creation time: 2010-05-31 03:33:41

Assignee: AlexGhitza

CC:  nthiery nborie mpatel was mhansen jasonbhill

I put this together as a reviewer patch for a ticket that I thought needed review (#8030), but which was already reviewed.  Rather than letting it go to waste, here it is.

It will depend on #8030.


---

Comment by rbeezer created at 2010-05-31 03:37:29

Changing status from new to needs_review.


---

Attachment


---

Comment by mpatel created at 2010-06-03 09:17:01

The patch here _may_ cause a problem with building the PDF reference manual.  Please see [comment:ticket:8030:10 this comment] at #8030.


---

Comment by rbeezer created at 2010-06-03 15:33:59

Changing priority from trivial to blocker.


---

Attachment

Revised patch (version 2) addresses the failure to build the PDF version of the reference manual, as described at #8030.  The only difference in the v2 patch is to replace two "\leqslant" by "\leq".  However, there are other documentation changes here that need review (ie, the whole v2 patch)  Both PDF and HTML now build fine and look fine.

Long term, we should see why this AMS symbol is not present for the PDF, while is present for the HTML.

Misha - can you review?

I've marked this as a blocker as part of the 4.4.3 alpha series in hopes of having it make it into the final, since #8030 introduced the failure to build the PDF version and is merged already.

Rob


---

Comment by jasonbhill created at 2010-06-03 23:31:02

Changing status from needs_review to needs_work.


---

Comment by jasonbhill created at 2010-06-03 23:31:02

While looking at the amssymb issue, I came across a problem elsewhere in what has been added to the docstring.

"``base_of_group`` is a list of the  positions on which ``self`` acts,"

This is not correct. The base of a permutation group G is defined as a list L of points in the domain of the action such that no element of G fixes all points of L.

http://en.wikipedia.org/wiki/Base_(group_theory)

Computationally, this is equivalent to requiring no strong generator to fix all points of the base, and hence the size of a base corresponds directly to the length of the stabilizer chain given by the Schreier-Sims algorithm. (In fact, this algorithm yields a base and the strong generating system relative to that specific base.)

The assertion that the base is not unique is correct, but the specific base used must correspond to the stabilizer chain constructed from a strong generating set. Otherwise, the information of the strong generating set is of less computational value.

For instance, a symmetric group of degree n has base of size n-1. So, S_5 on points [1..5] has bases [1,2,4,5], [1,2,3,4], etc., depending on the SGS. At the same time, any cyclic group has a base of size 1.

You may of course artificially inflate the base and it will still follow the definition, but then anyone using the strong generating set for calculations (MANY invariants of a group follow from this) must recalculate the base and this will often result in a different SGS.


---

Comment by rbeezer created at 2010-06-05 03:21:43

Replying to [comment:5 jasonbhill]:
> While looking at the amssymb issue, I came across a problem elsewhere in what has been added to the docstring.

Hi Jason,

I've been thinking about this, and wondering if you could move this to a new ticket?  #8030 was about fixing the stabilizer routine, which meant changes in the docstring for strong generating systems.  The latex there is causing an error in building the documentation, which is being fixed on this ticket.

I'd really like to see the error corrected ASAP, and not held up by this discussion on content for strong generating systems.  I think the base_of_group description predates #8030 anyway.

So it'd be great if we use this ticket to fix formatting, and have the design discussion on a new ticket?  Would you mind?

Thanks,
Rob


---

Comment by nthiery created at 2010-06-05 14:02:31

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

Comment by nthiery created at 2010-06-05 14:12:51

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

Comment by jasonbhill created at 2010-06-05 17:40:50

As a result of the above discussion, I've changed the action back to "needs review."

I will migrate this BSGS issue to a new ticket once domains can be made arbitrary.

Thanks for your comments Nicolas! I have some comments and questions and I will post those once I have things organized the domain work is done. For now, can someone please explain (remember that I am relatively new to Sage) where/why/how self.base() is obtaining "Integer Ring"? This seems like an obvious and currently not helpful output. Why not simply ask GAP for a base if one does not wish to input one?


---

Comment by jasonbhill created at 2010-06-05 17:40:50

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2010-06-05 19:50:56

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

Comment by rlm created at 2010-07-06 03:29:15

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-07-06 03:37:39

Changing status from positive_review to needs_info.


---

Comment by rlm created at 2010-07-06 03:39:18

Rob,

Looks like I acted too soon. In fact, it looks like your ref patch at #8030 has already been merged. The patch here is completely redundant. I'll close it as duplicate, if you can verify that all is well now.


---

Comment by rbeezer created at 2010-07-06 04:18:10

Replying to [comment:13 rlm]:
> Looks like I acted too soon. In fact, it looks like your ref patch at #8030 has already been merged. The patch here is completely redundant. I'll close it as duplicate, if you can verify that all is well now.

Not totally redundant, but a mess-up.  I attached the reviewer-edit patch to #8030 *after* the rest of the ticket had been reviewed.  It shouldn't have been merged (my fault, I should have left clear instructions).  I had put it onto a new ticket (here, #9102).  Then it got revised (the v2 patch here).  So the original patch never got reviewed and the minor changes to make the v2 patch need to be made.

I'll make a small patch here for the modifications that realize the v2 version?  Without it, I think the PDF version of the docs fails?  (I'll check.)  I'm moving to "needs work".

Rob


---

Comment by rbeezer created at 2010-07-06 04:18:10

Changing status from needs_info to needs_work.


---

Attachment


---

Comment by rbeezer created at 2010-07-06 04:31:38

Version 3 patch only changes two \leqslant to simply \leq since the Sage/TeX/PDF documentation build complains about the former version of an inequality symbol.  I can't verify this right now, since the PDF version won't get past some `UniqueRepresentation.__classcall__` stuff that I think is known.

Since the v1 patch is merged, this replicates the effect of the v2 patch.  So apply *only* the v3 patch to 4.5.alpha3 to get everything back together.  Sorry for the confusion.

Rob


---

Comment by rbeezer created at 2010-07-06 04:31:38

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-07-06 08:07:15

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-07-06 08:07:15

Apply v3 only.


---

Comment by rlm created at 2010-07-06 08:09:09

Resolution: fixed


---

Comment by mpatel created at 2010-07-06 08:34:20

Belated note: With #9331 and V3, the PDF reference manual builds for me.


---

Comment by rbeezer created at 2010-07-06 15:58:06

Misha:  thanks for the check.

Robert: thanks for seeing that this needed some work and the review.

Rob
