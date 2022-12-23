# Issue 8639: Bug when defining a MIPVariable's  type

Issue created by migration from https://trac.sagemath.org/ticket/8639

Original creator: ncohen

Original creation time: 2010-04-01 14:06:28

Assignee: jason, jkantor

The variable's name was changed.... :-p

Nathann


---

Attachment


---

Comment by ncohen created at 2010-04-01 14:07:53

Changing status from new to needs_review.


---

Comment by wdj created at 2010-04-02 23:01:35

This seems to pass all tests on  sage 4.3.5 on a 10.6.2 mac (the only failure was that of the fresh copy of 4.3.5).


---

Comment by wdj created at 2010-04-02 23:01:35

Changing assignee from jason, jkantor to wdj.


---

Comment by wdj created at 2010-04-02 23:02:36

Seems like a very very minor change. As far as I can seen, positive review.


---

Comment by wdj created at 2010-04-02 23:02:36

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-16 18:55:52

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-16 18:55:52

Merged "trac_8639.patch" in 4.4.alpha0.
