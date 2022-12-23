# Issue 7357: Add non-offset logarithmic integral, Li

Issue created by migration from https://trac.sagemath.org/ticket/7357

Original creator: myurko

Original creation time: 2009-10-30 16:49:49

Assignee: burcin

CC:  myurko benjaminfjones

Add the logarithmic integral, Li, with integration starting at 0 rather than 2.


---

Attachment


---

Comment by myurko created at 2009-10-30 16:53:13

Changing status from new to needs_review.


---

Comment by kcrisman created at 2009-11-10 13:18:32

This is nice, but like #3401, should have some doctests indicating it works for complex input (I assume it does).   The patch also depends on #3401.


---

Comment by kcrisman created at 2009-11-10 13:18:32

Changing status from needs_review to needs_work.


---

Attachment

This patch adds these tests.  It still depends on the (newest) patch at #3401, and in fact gets rid of one final thing which was only needed by the previous implementation of Li.


---

Comment by kcrisman created at 2010-01-18 17:11:39

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-01-18 17:12:04

Changing status from needs_review to positive_review.


---

Comment by burcin created at 2010-01-18 18:19:03

Changing status from positive_review to needs_work.


---

Comment by burcin created at 2010-01-18 18:19:03

This needs more work. See my comments about the prec parameter at comment:10:ticket:3401.

Two different functions whose names differ only in capitalization (`li` and `Li`) is also very confusing. We need to come up with a better name for this.


---

Comment by burcin created at 2010-08-28 16:15:55

Changing keywords from "" to "beginner".


---

Comment by kcrisman created at 2011-10-09 01:28:29

This seems to be addressed in the context of a much bigger overhaul by #11143.  But there the name is... more complicated.


---

Comment by benjaminfjones created at 2011-10-09 01:41:14

Yes, this would duplicate work done in #11143. The function added there is a fully symbolic function with numerical evaluation handled by mpmath. I think that is superior to the one defined here which is just a wrapper for the mpmath call. 

The function added in #11143 is really a class called ``Function_exp_integral_li`` and it has an alias ``exp_integral_li`` to match the other exponential integrals. #11143 also moves all the exponential integrals to a new module under sage/functions so this would conflict with that design decision too.


---

Comment by kcrisman created at 2011-10-10 02:17:54

So this can be closed as duplicate, correct?  Except I really would love it to be called `Li` instead of something horribly long... either way, feel free to review this as positive; I'm changing the milestone.


---

Comment by kcrisman created at 2012-05-26 17:19:24

This is definitely and definitively duplicated by the much more comprehensive #11143.


---

Comment by kcrisman created at 2012-05-26 17:19:24

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2012-06-19 13:28:24

Resolution: duplicate
