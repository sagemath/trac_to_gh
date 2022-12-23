# Issue 7531: Python interface to M4RI's LQUP function

Issue created by migration from https://trac.sagemath.org/ticket/7531

Original creator: malb

Original creation time: 2009-11-25 17:49:48

Assignee: was

All this patch does is to add a Python interface to `mzd_lqup` which might be handy for some people. It doesn't have any impact on existing functions etc. and thus should be a fairly low risk merge.


---

Comment by malb created at 2009-11-25 17:50:22

Changing status from new to needs_review.


---

Comment by ylchapuy created at 2009-11-26 02:00:31

Changing status from needs_review to needs_work.


---

Comment by ylchapuy created at 2009-11-26 02:00:31

Just a small remark: there is no mmpf algorithm available, this should be removed from the docstring.

(and it needs #7375 ...)


---

Comment by malb created at 2009-11-26 12:18:41

Fixed in updated patch.


---

Comment by ylchapuy created at 2009-11-26 12:56:44

typo in the pxd: assymptotically

isn't it recommended to add a doctest for each algorithm?
maybe just add `lqup(A)==lqup(A,algorithm="naive")` and `lqup(A)==lqup(A,algorithm="mmpf")`


---

Attachment

Thanks, fixed.


---

Comment by malb created at 2009-11-26 14:56:05

Changing status from needs_work to needs_review.


---

Comment by ylchapuy created at 2009-11-26 16:34:46

seems good to me now :)


---

Comment by ylchapuy created at 2009-11-26 16:34:46

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-29 05:50:00

Resolution: fixed
