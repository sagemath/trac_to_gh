# Issue 6863: Implement cusps over number fields

Issue created by migration from https://trac.sagemath.org/ticket/6863

Original creator: cremona

Original creation time: 2009-09-02 13:00:01

Assignee: craigcitro

CC:  mtaranes

Keywords: number field modular

This is related to, but not dependent on, #6829.

Cusps over a number field K are elements of `P^1(K)`.  Support for these is to be provided as part of the general implementation of modular symbols and related matters over number fields.

A patch which will be available shortly will supply this implementation, together with related utilities such as testing Gamma_0(N)-equivalence etc.

This work has been done by Maite Aranes, under the supervision of John Cremona.


---

Comment by mtaranes created at 2009-09-02 17:00:39

Patch based on 4.1.1


---

Attachment


---

Comment by cremona created at 2009-12-10 21:29:14

I just checked that the patch applies fine to 4.3.alpha 1, and it does.


---

Comment by craigcitro created at 2010-01-17 23:40:27

So this code looks *really* nice -- I'm really happy to see this functionality in Sage, and I'm very impressed with the completeness of the functionality, and the documentation/doctests.

However, I think this code does need some purely cosmetic changes before we merge it. Here are my first thoughts:

 * I think that we shouldn't provide a separate "NFCusp" function to the user -- they should just call Cusp, which could deduce the base ring from the arguments, and take an optional `base_ring=` parameter.

 * For that matter, we should probably just have a `Cusp_rationals` and `Cusp_number_field` class which both inherit from a `Cusp_generic`, and unify as much of this code as possible with the existing cusps code. 

 * Similar comments to the previous two also apply to `NFCusps`, i.e. the parent for cusps. 

 * I really like that there are convenient functions for getting a corresponding number field element from a cusp -- however, we should probably do the extra work to make the coercion framework know about these, so that you could simply do something like `K(c)` to get a representative for the cusp. 

 * In fact, I might go one step further and say that we shouldn't really need to add any new functions into the global namespace -- i.e. `sage/modular/all.py` shouldn't need to import anything directly, except maybe the `_clear_cache` functions. All of the things that do get imported are analogues for number fields of existing bits, which should be able to be handled transparently. As far as the `_clear_cache` stuff, maybe we could just have those be available as methods on the parents? I wouldn't mind `_Cusp_clear_cache_` or something at top-level, as long as it was prefixed with `_`. 

I think that's it at a first go, but it's probably enough to get started moving in the right direction. John and/or Maite, do you want to make these changes, or would you rather I do it? I won't get to it for about two weeks, but I'm happy to do it if you won't have time before then.


---

Comment by craigcitro created at 2010-01-17 23:40:27

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2010-01-18 09:16:35

Craig, Thanks for your comments.  Since it's quite a long time since Maite actually wrote this I don't think we are in a hurry to start reorganising the code as you suggest.  I think that, while we realised that the best thing in the long term would be to unify code as you suggest, we did not want to do anything which made classical cusps slower, hence the parallel implementation.  So if you unify the cusps code (which I would like to see in the long run) it will be necessary to test carefully that there is no speed regression for Q-cusps.


---

Comment by cremona created at 2010-01-18 09:37:20

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-01-18 09:37:20

On second thoughts, why don't we let this code get merged now, and make a new ticket for the refactoring?  That way this code will not languish any longer just in case we don't get around to making your suggested improvements for a while.

To assist this process I'm putting it back to "needs review".  Craig, you can signal your answer by either moving it back to "needs work" or on to "positive review" :)


---

Comment by craigcitro created at 2010-01-20 20:08:51

Yeah, that's a good point. I'd rather have this code merged and waiting on a cleanup than have it sitting and waiting for the same cleanup. I've made #8015 as a reminder to merge these two.

(John, I'm listing you as a reviewer because I know you reviewed much of the content of this code as it was being developed.)


---

Comment by craigcitro created at 2010-01-20 20:08:51

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-01-20 20:28:12

Replying to [comment:6 craigcitro]:
> Yeah, that's a good point. I'd rather have this code merged and waiting on a cleanup than have it sitting and waiting for the same cleanup. I've made #8015 as a reminder to merge these two.
> 
> (John, I'm listing you as a reviewer because I know you reviewed much of the content of this code as it was being developed.)
That's fair.  My involvement should be recorded somewhere, but it was Maite who did all the code writing.

Thanks for the review!


---

Comment by mvngu created at 2010-01-24 02:51:34

Resolution: fixed
