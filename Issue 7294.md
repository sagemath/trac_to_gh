# Issue 7294: Degree constrained subgraph

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-10-25 09:26:41

Assignee: rlm

There should be a way in Sage to find a degree-constrained subgraph. This should be done through LP ( there may be a better way to do it, but I am not aware of it )


---

Comment by ncohen created at 2009-11-01 17:07:39

Changing status from new to needs_review.


---

Attachment


---

Comment by rlm created at 2009-12-15 17:10:33

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2009-12-15 17:10:33

This looks good to me. I should note that you can use `if bounds is None`, since in Python the None type is unique.


---

Attachment


---

Comment by mhansen created at 2009-12-15 17:52:40

Resolution: fixed


---

Comment by mhansen created at 2009-12-15 17:52:40

I merged both patches above.
