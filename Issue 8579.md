# Issue 8579: Add the categories of magmas and additive magmas

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2010-03-22 16:33:34

Assignee: nthiery

CC:  sage-combinat roed

This patch adds the categories Magmas() and AdditiveMagmas()
(sets with a plain binary operation * or +).

It factors out some of the code previously in Semigroups / CommutativeAdditiveSemigroups.


---

Comment by nthiery created at 2010-03-22 20:50:52

Changing status from new to needs_review.


---

Comment by nthiery created at 2010-03-22 20:50:52

Changing keywords from "" to "categories, magma".


---

Comment by rbeezer created at 2010-03-23 04:28:26

Hi Nicolas,

I get about 10 "hunk failures" trying to apply this to a stock 4.3.4.

I noticed a "-git" in the diff commands in the patch, which I don't see in the patches I usually make.  Is it it me, or does this patch need some attention?

Rob


---

Comment by rbeezer created at 2010-03-23 14:35:47

Thanks, Nicolas, I'll test tonight with #7880.


---

Attachment

This updated patch fixes the copyright headers


---

Comment by rbeezer created at 2010-03-24 14:50:23

This passes all tests on 4.3.4.final and docs build without any problems.  It also works well when the fairly extensive #7555 is applied on top of it.  So there should be no surprises for the interested reviewer.

I can't say at the moment that I know enough about implementing categories to verify its completeness, so right now it either (a) needs a quick review from a knowledgeable category specialist, or (b) I need to get more education on categories so #7555 can go in.

Rob


---

Comment by was created at 2010-03-29 07:33:44

Finally, Magma gets included in Sage!!


---

Comment by hivert created at 2010-03-31 10:06:25

Hi Rob,

Replying to [comment:5 rbeezer]:
> This passes all tests on 4.3.4.final and docs build without any problems.  It also works well when the fairly extensive #7555 is applied on top of it.  So there should be no surprises for the interested reviewer.

Thanks for checking this.

> I can't say at the moment that I know enough about implementing categories to verify its completeness, so right now it either (a) needs a quick review from a knowledgeable category specialist, or (b) I need to get more education on categories so #7555 can go in.

From the category implementation point of view, everything looks fine upto the
following small problem which can be left for a future patch: the
`SubQuotient` code in `Semigroups()` is sufficiently general to work
in magmas (computing product by lifting/retracting). It should be moved in
`Magmas()`.

Otherwise, I'm okay to give a positive review. I'll ask Nicolas directly.

Florent


---

Comment by nthiery created at 2010-04-01 12:12:25

Replying to [comment:7 hivert]:
> From the category implementation point of view, everything looks fine upto the
> following small problem which can be left for a future patch: the
> `SubQuotient` code in `Semigroups()` is sufficiently general to work
> in magmas (computing product by lifting/retracting). It should be moved in
> `Magmas()`.

Ah, right, I forgot to mention that. I decided to implement this moving in the upcoming functorial construction patch instead, in order to avoid potential conflicts between the two patches.


---

Comment by hivert created at 2010-04-01 15:14:25

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2010-04-01 15:14:25

Replying to [comment:8 nthiery]:
> Ah, right, I forgot to mention that. I decided to implement this moving in the upcoming functorial construction patch instead, in order to avoid potential conflicts between the two patches.

Then It's ok ! positive review.


---

Comment by rbeezer created at 2010-04-01 17:01:08

Replying to [comment:10 hivert]:
> Then It's ok ! positive review.

Florent,

Thanks for finishing this one off!

Rob


---

Comment by jhpalmieri created at 2010-04-15 20:14:02

Merged "trac_8579-category-magmas-nt.patch" in 4.4.alpha0


---

Comment by jhpalmieri created at 2010-04-15 20:14:02

Resolution: fixed
