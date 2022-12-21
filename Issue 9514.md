# Issue 9514: sage/symbolic/random_tests.py wrongly depends on order of dict.values()

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2010-07-16 03:36:32

Assignee: cwitty

The variable sage.symbolic.random_tests.full_functions is ordered in the same order as the .values() method on a dict, which is not necessarily reproducible.  (I'm a little curious as to why the order in fact does seem to be reproducible, across multiple platforms, etc., but changes with the addition of seemingly unrelated code -- but not curious enough to investigate.)

Anyway, the current code is clearly wrong.  I'll have a fix in a few minutes.

This should fix the strange random_tests.py doctest issue from #8988, and possibly reduce the churn in the random_tests doctest results.


---

Attachment

This patch fixes the problem, and also seems to fix the random_tests.py problem with #8988 (as expected).


---

Comment by cwitty created at 2010-07-16 04:32:34

Changing status from new to needs_review.


---

Comment by novoselt created at 2010-07-16 15:26:31

Changing status from needs_review to positive_review.


---

Comment by novoselt created at 2010-07-16 15:26:31

Works for me and removes the necessity of interfering in #8988.


---

Comment by mpatel created at 2010-07-20 08:46:06

Resolution: fixed
