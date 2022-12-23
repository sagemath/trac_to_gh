# Issue 7992: typo in sage/libs/mwrank/interface.py

Issue created by migration from https://trac.sagemath.org/ticket/7992

Original creator: rlm

Original creation time: 2010-01-19 04:46:19

Assignee: cremona

`A 2-descent didn't not complete successfully`


---

Comment by cremona created at 2010-01-19 09:21:03

Applies to 4.3.1.rc0


---

Comment by cremona created at 2010-01-19 09:22:05

Changing status from new to needs_work.


---

Attachment

Patch attached.  As far as I can see this message does not appear in a doctest.  Which means that I should add a doctest for it, hence not ready for review yet.


---

Comment by cremona created at 2010-01-19 09:35:56

replaces previous


---

Attachment

New patch adds doctest (one showing failure and one ok).

I don't know why the output of the RuntimeError does not include the string (the one where the typo was fixed).  Maybe the review does?


---

Comment by cremona created at 2010-01-19 09:38:00

Changing priority from major to minor.


---

Comment by cremona created at 2010-01-19 09:38:00

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-01-19 20:32:06

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-19 20:32:18

Resolution: fixed
