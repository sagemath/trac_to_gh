# Issue 9534: add base method for permutation groups

Issue created by migration from https://trac.sagemath.org/ticket/9534

Original creator: jasonbhill

Original creation time: 2010-07-17 23:33:27

Assignee: jasonbhill

Keywords: base

Patch to add a (working) base method for permutation groups.


---

Comment by jasonbhill created at 2010-07-18 22:03:28

The existing base method returned "Integer Ring" for all permutation groups as it was inherited from ParentWithBase. This new base method uses GAP's base from stabilizer chain method to return an actual base, with an optional seed.

The patch was placed in the combinat queue as it depends on Mike Hansen's domain modifications.


---

Comment by mhansen created at 2010-11-26 06:05:27

This is actually Jason's code, and it looks good to me.


---

Comment by mhansen created at 2010-11-26 06:05:27

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-11-26 06:05:38

Changing status from needs_review to positive_review.


---

Attachment


---

Comment by jdemeyer created at 2011-07-22 12:49:09

Resolution: fixed


---

Comment by jdemeyer created at 2011-08-01 11:37:36

Resolution changed from fixed to 


---

Comment by jdemeyer created at 2011-08-01 11:37:36

Unmerged because of an issue with #10335.


---

Comment by jdemeyer created at 2011-08-01 11:37:36

Changing status from closed to new.


---

Comment by jdemeyer created at 2011-08-01 11:37:47

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2011-08-01 11:37:56

Changing status from needs_review to positive_review.


---

Comment by leif created at 2011-09-23 10:48:37

Does this now have to be rebased on (the rebased) #10335?

In case it does, one should set it to "needs work", otherwise the milestone should be changed to Sage 4.7.2 again.


---

Comment by jdemeyer created at 2011-10-07 19:11:06

Resolution: fixed
