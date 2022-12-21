# Issue 7919: Doctest in sage/misc/test_class_pickling.py doesn't test anything

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2010-01-13 09:40:22

Assignee: nthiery

CC:  nthiery

There's a doctest in `sage/misc/test_class_pickling.py` that doesn't actually test anything. I was a reviewer for this patch, which means it's my bad for letting it through. Of course, this code gets tested anyway, so it's not so serious, but we should fix it anyway. Patch attached.


---

Comment by craigcitro created at 2010-01-13 09:43:37

Changing status from new to needs_review.


---

Attachment


---

Comment by nthiery created at 2010-01-13 11:44:51

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2010-01-13 11:44:51

Good catch. That actually was a relic from a former (failed) attempt at getting c1 and c2 to be garbage collected by putting them out of scope, and see if this had any influence.

Replacing it by an equality test is sure better. Thanks!


---

Comment by rlm created at 2010-01-14 06:52:38

Resolution: fixed
