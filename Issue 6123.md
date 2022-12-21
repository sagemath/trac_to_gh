# Issue 6123: [with patch, needs review] expose partition refinement functions to Python

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2009-05-24 07:41:34

Assignee: joyner

CC:  sage-combinat

The idea is that it would be nice to use the partition refinement functions for experimentation without having to recompile a lot of times.

It would be very good to get this into Sage-4.0, since this will allow for patches on the sage-combinat server which don't require excessive compilation time when pushing/popping.


---

Attachment


---

Comment by was created at 2009-05-28 07:17:18

better for 4.0.1.  Get this reviewed!


---

Comment by rlm created at 2009-05-28 08:00:29

`nthiery` promised a review in time for 4.0. I guess he can move it back over when he is done, if there is still time.


---

Comment by ncalexan created at 2009-06-14 22:45:19

craigcitro and ncalexan want this to go in 4.0.2.alpha0, so we're going to merge it.  The doctests look good but not great: can we get some more examples that verify the Cython implementations, and some explanations of the existing examples?


---

Comment by ncalexan created at 2009-06-14 22:45:19

Resolution: fixed


---

Comment by rlm created at 2009-06-16 08:25:29

Replying to [comment:3 ncalexan]:
> ...The doctests look good but not great: can we get some more examples that verify the Cython implementations, and some explanations of the existing examples?

Can you be a *lot* more specific?
