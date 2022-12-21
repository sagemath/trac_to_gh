# Issue 8610: fix caching bug in modular/modsym/element.pyx (very easy to review!)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-03-26 02:00:35

Assignee: craigcitro

There is a bug in caching, which this fixes.  Also, I add a missing doctest to get coverage to 100% on that file.


---

Comment by was created at 2010-03-26 02:01:36

Changing status from new to needs_review.


---

Comment by was created at 2010-03-26 02:51:04

rebased against 4.3.4


---

Comment by AlexGhitza created at 2010-03-26 03:52:11

Changing status from needs_review to positive_review.


---

Attachment

Looks good to me.  Passes tests, etc.


---

Comment by jhpalmieri created at 2010-04-16 18:53:02

Merged "trac_8610.patch" in 4.4.alpha0.


---

Comment by jhpalmieri created at 2010-04-16 18:53:02

Resolution: fixed
