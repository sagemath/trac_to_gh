# Issue 8402: Sanity check for Parent and Elemet

Issue created by migration from https://trac.sagemath.org/ticket/8402

Original creator: hivert

Original creation time: 2010-02-28 16:45:15

Assignee: nthiery

CC:  sage-combinat

Keywords: Parent, Element, equality, zero, one

Here is the summary of what was decided on [sage=devel](http://groups.google.com/group/sage-devel/t/5d9c32390ffe3c96):

1 - Any Parent or Element must have an equality methods such that
`self == self` and `self != None`. This is not required for general `SageObject`.

2 - Element construction should be idempotent. More precisely, for any element e within parent P, the equality `P(e) == e` must hold.

Case by case exception such as `RealIntervalField` are possible.

3 - element of a parent in the category `Monoid()` (respectively `CommutativeAdditiveMonoid()`) must have a `__hash__` method,
which may raise an error for mutable element but never on `.one()` (respectively `.zero()`)


---

Comment by hivert created at 2010-03-02 22:27:34

Changing assignee from nthiery to hivert.


---

Comment by hivert created at 2010-04-17 00:06:52

I'm preparing some patches on sage-combinat queue. I already caught some bug with it: see #8695.


---

Comment by nthiery created at 2010-04-18 23:22:01

Review in process on the Sage-Combinat queue.
All tests pass with sage-4.4-alpha0 (with the other patches under review applied as well)


---

Comment by nthiery created at 2010-04-19 22:28:36

Changing status from new to needs_review.


---

Comment by nthiery created at 2010-04-19 22:28:36

All test still pass, even after my reviewer's patch on the patch queue :-)

Florent: please double check it. If that's fine, fold everything together, post here and set a positive review!

Note: I ended up throwing away a bit of code in crystals/spins.py, which was the easiest way to fix equality :-)


---

Comment by hivert created at 2010-04-21 21:03:58

> Florent: please double check it. If that's fine, fold everything together, post here and set a positive review!

All tests passed on sage, I folded and set positive review.


---

Comment by hivert created at 2010-04-21 21:03:58

Changing status from needs_review to positive_review.


---

Attachment


---

Comment by was created at 2010-04-29 05:24:19

Resolution: fixed
