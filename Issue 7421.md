# Issue 7421: Weaker precondition for registering a new coercion.

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-11-10 01:02:16

Assignee: robertwb

CC:  sage-combinat robertwb

Keywords: coercion

With the attached patch, the precondition for registering a new
coercion from P to Q with register_coercion becomes: 

 "no over coercion from P to Q has been registered or discovered earlier"

Which is a bit weaker than the previous:

 "no coercion into P has been queried"

This should still be quite safe, while covering all the formerly
problematic practical use cases coming up in the category code #5981.


---

Comment by nthiery created at 2009-11-10 01:03:32

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-11-10 05:28:23

I think is probably okay.  After thinking about it for a bit, I could come up with a situation where this change would make the coercion graph non-commutatitve.

I'll run all the tests with it here in a bit.


---

Comment by robertwb created at 2009-11-11 18:30:34

There is one way this can go wrong. Suppose one has B -> C, and one wants to register A -> B. If A -> C was previously requested, its non-existence will be cached. 

Now I don't think this will be an issue in practice, nor does `_unset_coercions_used` solve it.


---

Comment by nthiery created at 2009-11-11 21:51:50

With the updated patch register_coercion also does not bark if _coercions_used is false.

Otherwise, this triggered to failing doctests in sage/modules/fg_pid/fgp_module.py
and sage/modules/fg_pid/fgp_morphism.py. An expert should investigate why a coercion gets registered twice in those modules, and whether this is not a bug. But I vote for postponing that for later.


---

Comment by nthiery created at 2009-11-11 21:55:46

Replying to [comment:4 robertwb]:
> There is one way this can go wrong. Suppose one has B -> C, and one wants to register A -> B. If A -> C was previously requested, its non-existence will be cached. 
> 
> Now I don't think this will be an issue in practice, nor does `_unset_coercions_used` solve it. 

I agree.

So, is this positive review?


---

Comment by nthiery created at 2009-11-11 21:56:20

The previous version was missing a patch header.


---

Attachment

I'm going to move this to 4.3 where it's more relevant.


---

Comment by robertwb created at 2009-11-14 07:19:57

Yes, positive review.


---

Comment by robertwb created at 2009-11-14 07:19:57

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-17 05:53:42

Resolution: fixed
