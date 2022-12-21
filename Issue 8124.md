# Issue 8124: Selmer groups for number fields

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2010-01-29 21:04:44

Assignee: davidloeffler

I forgot to include this function in my big S-units and S-class groups patch.

I've tested on my laptop and on sage.math, so I think this passes on 32 and 64 bit systems.


---

Comment by rlm created at 2010-01-29 21:05:16

Changing status from new to needs_review.


---

Comment by wuthrich created at 2010-01-31 01:29:08

Would it be much more work to make this function to give back a finite abelian group ? In the long run, we should make sure that these sort of functions return groups. It may be better to try get the correct type from the beginning as not to break later things that use it.

(Sorry to be criticising this again. I think you are doing a great job implementing all these things.)


---

Comment by cremona created at 2010-01-31 17:50:00

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-01-31 17:50:00

Looks good;  tests pass.  Building the docs (reference html) revealed a problem in polynomial_quotient_ring.py, preexisting in the selmer_group function:  the macro "\cross" was not recognised.  I could not get "\times" to work instead (which is what I normally use for this) but * does, so I put that in.

Regarding Chris's comment:  of course I agree, this should be a proper abelian group.  But even making it a semi-functional abelian group of the sort used for unit groups and class groups would require quite a bit of extra work, since this code finds generators but _not_ the group structure.  So I think that should be in another ticket.  (For example, I would like to use this function for m=4 and will try to do so.  In that case there will in general be generators of order 2 as well as some of order 4.)


---

Comment by wuthrich created at 2010-01-31 18:14:02

Ok, I see and I also understand that this less costly function should be available even if we had selmer_groups given as abelian groups. Maybe a renaming to selmer_group_gens() would be adequate then we can use it later and add later selmer_group without having to change the type return by a function.

But I won't oppose the positive review on this ticket, of course.


---

Comment by rlm created at 2010-02-04 19:46:28

It looks like someone has already fixed the issue John's patch here fixes, so the release manager should merge the original patch.

If there are no objections, I will remove the second patch.


---

Comment by rlm created at 2010-02-04 19:48:50

Replying to [comment:3 cremona]:
> I could not get "\times" to work instead (which is what I normally use for this) but * does, so I put that in.

Actually, it looks like someone changed this to `\times` in rc0, so I've updated the patch to change `\times` instead of `\cross` to `*`.


---

Comment by rlm created at 2010-02-04 19:49:18

Replaces previous (fixes latex glitch)


---

Attachment

Patch  trac_8124-selmer-nf.review.patch applies fine to 4.3.2.alpha1 and tests pass and doc build ok!

The tag was already at review, and I'm happy to leave it there.


---

Comment by cremona created at 2010-02-06 17:41:02

Replying to [comment:7 cremona]:
> Patch  trac_8124-selmer-nf.review.patch applies fine to 4.3.2.alpha1 and tests pass and doc build ok!
> 
> The tag was already at review, and I'm happy to leave it there.

That should have said "positive review".

I checked that this applies fine to 4.3.2 + #8184 spkg & patches + #8155 patches;  all tests pass (on 64-bit).


---

Comment by mpatel created at 2010-02-11 14:31:43

Resolution: fixed
