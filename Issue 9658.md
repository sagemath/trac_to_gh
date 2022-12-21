# Issue 9658: mpz_clear->mpq_clear (typo)

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-08-01 05:00:21

Assignee: jason, was

CC:  robertwb

We can't include vector_rational_sparse_c.pxi in a cython file because of a typo.  This patch fixes this.


---

Comment by jason created at 2010-08-01 05:02:40

Changing status from new to needs_review.


---

Attachment


---

Comment by jason created at 2010-08-01 05:15:11

I thought the typo prevented someone from loading the file, but it seems like I can include it with the typo.  Regardless, it is still pretty clear it is a typo (look at the declaration of z).


---

Comment by jason created at 2010-09-28 20:33:24

robert, or someone: ping about a review.  This is really a trivial typo fix.


---

Comment by leif created at 2010-09-28 21:59:23

Obviously.


---

Comment by leif created at 2010-09-28 21:59:23

Changing status from needs_review to positive_review.


---

Comment by leif created at 2010-09-28 22:04:03

P.S.: Applied to Sage 4.6.alpha1 without problems.


---

Comment by mpatel created at 2010-09-29 04:23:36

Resolution: fixed


---

Comment by robertwb created at 2010-09-29 07:27:56

Why did this even compile before? Yes, the fix is good.
