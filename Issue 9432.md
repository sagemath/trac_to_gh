# Issue 9432: remove remaining # optional - GLPK tags on doctests

Issue created by migration from https://trac.sagemath.org/ticket/9432

Original creator: rlm

Original creation time: 2010-07-05 23:19:19

Assignee: jason, jkantor

CC:  ncohen leif




---

Comment by rlm created at 2010-07-06 03:49:09

The following should also be addressed:


```
age -t -long "devel/sage-main/sage/numerical/mip.pyx"
**********************************************************************
File "/scratch/rlmill/release/sage-4.5.alpha2/devel/sage-main/sage/numerical/mip.pyx",
line 1055:
   sage: p.get_values(x)
Expected:
   {0: 0.0, 1: 1.3333333333333333}
Got:
   {1: 0.0, 2: 1.3333333333333333}
*********************************************************************
```



---

Comment by ncohen created at 2010-07-06 09:58:59

Changing status from new to needs_review.


---

Attachment

Updated ! There should not be any other trace of the optional GLPK package in Sage :-)

Nathann


---

Comment by rlm created at 2010-07-06 11:48:40

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-07-06 11:50:11

Resolution: fixed
