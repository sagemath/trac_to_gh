# Issue 7083: Improve a few special functions

Issue created by migration from https://trac.sagemath.org/ticket/7083

Original creator: kcrisman

Original creation time: 2009-09-30 15:03:10

Assignee: burcin

A few functions in functions/special.py need a little help to actually accept valid input.  Also, exp_int is duplicated in its functionality.


---

Attachment

Based on 4.1.2.alpha4


---

Comment by kcrisman created at 2009-09-30 15:05:47

Another option to deprecating exp_int() is to just make it call exponential_integral_1, and I would be happy to implement either way as a reviewer indicates is useful.


---

Comment by wdj created at 2009-10-25 13:41:10

Changing status from needs_review to positive_review.


---

Comment by wdj created at 2009-10-25 13:41:10

Passes sage -testall on ubuntu 9.04 32 bit. It seems to pass on an imac running 10.6 but there are so many other failures, I'm not sure. Does what it claims to do and adds nice functionality.


---

Comment by mhansen created at 2009-10-31 15:31:28

Resolution: 


---

Comment by kcrisman created at 2009-11-23 14:25:38

Resolution: fixed
