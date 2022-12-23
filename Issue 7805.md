# Issue 7805: MixedIntegerLinearProgram.show should use the variables' and constraints' names

Issue created by migration from https://trac.sagemath.org/ticket/7805

Original creator: ncohen

Original creation time: 2010-01-01 14:33:09

Assignee: jkantor

As the title says, this function currently doesn't use them ;-)

Nathann


---

Comment by ncohen created at 2010-01-16 16:02:20

Changing status from new to needs_review.


---

Attachment

This seems to pass all tests on sage 4.3.5 on a 10.6.2 mac (the only failure was that of the fresh copy of 4.3.5). 

Like #8639, this seems like a very very minor change. As far as I can seen, positive review.


---

Comment by wdj created at 2010-04-03 06:07:16

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-15 23:42:55

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-15 23:42:55

Merged "trac_7805.patch" into 4.4.alpha0
