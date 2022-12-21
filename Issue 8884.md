# Issue 8884: Inefficiency in isogeny_class function

Issue created by migration from Trac.

Original creator: kimi

Original creation time: 2010-05-05 09:08:26

Assignee: cremona

CC:  cremona

We found inefficiency in isogeny_class function for elliptic curves over rational field. The patch will improve this.


---

Attachment


---

Comment by cremona created at 2010-05-11 10:36:55

Replaces previous patch; applies to 4.4.1


---

Attachment

The second version of the patch just adds a useful comment and fixes some docstrings.


---

Comment by cremona created at 2010-05-11 10:38:25

Changing status from new to needs_review.


---

Comment by wuthrich created at 2010-05-23 23:04:05

All tests pass and it improves the code indeed. Thanks for the work.

Only the second patch has to be applied.


---

Comment by wuthrich created at 2010-05-23 23:04:05

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-06 08:45:01

Resolution: fixed
