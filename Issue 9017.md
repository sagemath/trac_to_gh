# Issue 9017: Use lowercase i for latex symbolic sqrt(-1)

Issue created by migration from https://trac.sagemath.org/ticket/9017

Original creator: robertwb

Original creation time: 2010-05-22 15:46:55

Assignee: burcin




---

Attachment


---

Comment by robertwb created at 2010-05-22 15:48:20

Changing status from new to needs_review.


---

Comment by burcin created at 2010-05-22 16:03:04

Wow! Thanks for the quick patch.

There are a few minor looking doctest problems. I'll post a review patch and change to positive review soon.


---

Comment by burcin created at 2010-05-22 16:03:04

Changing status from needs_review to needs_work.


---

Comment by robertwb created at 2010-05-22 16:34:06

Here's one fix.


---

Attachment

See also #9018.


---

Comment by robertwb created at 2010-05-22 16:34:42

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by burcin created at 2010-05-22 18:12:16

Changing status from needs_review to positive_review.


---

Comment by burcin created at 2010-05-22 18:12:16

Surprisingly not much else is needed. attachment:trac_9017-doctest_fixes.patch fixes two doctests.

All patches on this ticket should be applied. In this order:
 * attachment:9017-latex-sqrt-neg1.patch
 * attachment:9017-fixes.patch
 * attachment:trac_9017-doctest_fixes.patch


---

Comment by robertwb created at 2010-06-05 09:16:58

Changing type from defect to enhancement.


---

Comment by mhansen created at 2010-06-06 01:29:48

Resolution: fixed
