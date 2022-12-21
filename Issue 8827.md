# Issue 8827: Cache heights of points on elliptic curves

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-04-30 06:38:15

Assignee: cremona

I've found myself taking the height of the same points over and over again, and have been starting to wish they were cached (especially over number fields). This patch does it. 


---

Comment by robertwb created at 2010-04-30 06:39:41

Changing status from new to needs_review.


---

Attachment


---

Comment by cremona created at 2010-04-30 08:17:47

I can't believe that we never cached heights before!  (Perhaps we did when they were only implemented over QQ, but I'm not going to go back and check).

Note that this is one case where the caching is slightly less trivial since we need to recompute of the desired precision is > the cached precision.  The patched code does that properly.

Applies fine to 4.4 and all elliptic_curves tests pass.


---

Comment by cremona created at 2010-04-30 08:17:47

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-05-08 21:55:03

Resolution: fixed
