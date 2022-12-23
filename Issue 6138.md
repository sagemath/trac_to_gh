# Issue 6138: SymmetricGroupAlgebra: updates w.r.t. categories and free modules

Issue created by migration from https://trac.sagemath.org/ticket/6138

Original creator: nthiery

Original creation time: 2009-05-27 05:38:44

Assignee: nthiery

CC:  sage-combinat

Keywords: symmetric group, free module

See: http://combinat.sagemath.org/patches/file/tip/categories-symmetric_group_algebra-6138-nt.patch

Depends on #6136


---

Comment by hivert created at 2009-10-16 11:10:33

Changing status from new to needs_review.


---

Attachment


---

Comment by hivert created at 2009-10-16 11:11:35

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-31 16:52:32

For this, isn't it possible to lazily add the coercion using coerce_map_from?


---

Comment by nthiery created at 2009-11-01 12:47:31

Replying to [comment:3 mhansen]:
> For this, isn't it possible to lazily add the coercion using coerce_map_from?

Probably so. It would be best handled by some "templated coercion declarations", as I had started to implement in MuPAD. Let's just leave it as is for the moment, until we have enough use cases to come up with the right design.


---

Comment by nthiery created at 2009-11-06 14:13:10

Updated patch fixes two missing doctests (apply only this one)


---

Comment by mhansen created at 2009-11-19 17:00:03

Resolution: fixed


---

Attachment
