# Issue 6597: [with patch, needs review] SetMorphism: 100% doctest + equality + pickling

Issue created by migration from https://trac.sagemath.org/ticket/6597

Original creator: nthiery

Original creation time: 2009-07-23 08:51:13

Assignee: robertwb

CC:  sage-combinat cwitty saliola

Keywords: doctest, SetMorphism, pickling

This patch raises SetMorphism to 100% doctest, and implements equality and pickling.


---

Comment by nthiery created at 2009-09-02 15:12:33

Changing assignee from robertwb to nthiery.


---

Comment by nthiery created at 2009-09-02 15:12:33

Changing status from new to assigned.


---

Attachment


---

Comment by mhansen created at 2009-09-08 19:10:12

Looks good to me.  All tests pass with it once #6343 is applied to Sage 4.1.1.

Note it takes awhile to build everything.


---

Comment by nthiery created at 2009-09-08 20:26:29

Replying to [comment:3 mhansen]:
> Looks good to me.  All tests pass with it once #6343 is applied to Sage 4.1.1.

Thanks Mike for the review!

> Note it takes awhile to build everything.

Yeah, I had to modify the .pxd of Map (or Morphism) to get pickling to work.

I am glad this will be soon in so that we don't have this patch anymore in Sage-Combinat.


---

Comment by mvngu created at 2009-09-09 08:55:01

Resolution: fixed
