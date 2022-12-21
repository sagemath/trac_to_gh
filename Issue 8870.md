# Issue 8870: Multiflow

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2010-05-04 17:27:20

Assignee: jason, ncohen, rlm

* Requires #8364


---

Comment by ncohen created at 2010-05-08 16:53:48

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-05-08 22:02:28

Changing assignee from jason, ncohen, rlm to ncohen.


---

Comment by ncohen created at 2010-05-08 22:18:00

In this patch, the method multi-commodity flow is defined. The code is also refactored as this method shares many common points with flow. The new code is more compact and (I hope) easier to understand ! :-)

Nathann


---

Comment by rlm created at 2010-06-21 20:40:18

1. Needs rebasing (applying on top of #9269, #8781, and #9230).

2. `# optional` tags need to follow the correct format.


---

Comment by rlm created at 2010-06-21 20:40:18

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2010-06-21 21:06:36

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-06-21 21:06:36

Updated ! A nasty piece to rebase... ;-)

Nathann


---

Attachment


---

Comment by rlm created at 2010-06-21 21:50:44

Changing status from needs_review to positive_review.


---

Attachment

Looks good to me. Apply both patches.


---

Comment by rlm created at 2010-06-29 16:46:07

Resolution: fixed
