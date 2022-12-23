# Issue 7563: Interval Graphs : recognition and interval representation

Issue created by migration from https://trac.sagemath.org/ticket/7563

Original creator: ncohen

Original creation time: 2009-11-30 18:18:46

Assignee: rlm

CC:  dimpase mvngu rlm wdj jason

Recognition of interval graphs and representation of a given graph as a list of intervals


---

Comment by ncohen created at 2010-06-06 11:00:39

Changing status from new to needs_work.


---

Comment by ncohen created at 2010-06-12 15:19:30

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-06-12 15:22:39

Oh yes, and... There are many missing doctests, but as this algorithm heavily uses dictionaries I wondered whether this could be done without being platform-dependent ^^;

Any idea welcome, here too.. Even though those functions will never be needed directly by the users, and all of them are indirectly tested anyway through the docstrings of is_interval.

Nathann


---

Comment by jason created at 2010-06-12 17:15:35

Replying to [comment:3 ncohen]:
> Oh yes, and... There are many missing doctests

Ouch.  That's a problem.  I don't think the ticket should go into Sage without doctests on each python function.

(I haven't had time to look at the rest of the patch, though.)


---

Comment by ncohen created at 2010-06-12 20:38:34

"Your wish is my command" :-)

Nathann


---

Attachment


---

Comment by rlm created at 2010-06-18 23:53:05

Applies after #8284 and passes all its tests :). Coverage looks much better.


---

Comment by rlm created at 2010-06-18 23:53:05

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-06-29 16:43:58

Resolution: fixed
