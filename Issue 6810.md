# Issue 6810: improve doctest coverage in schemes/homset.py

Issue created by migration from https://trac.sagemath.org/ticket/6810

Original creator: AlexGhitza

Original creation time: 2009-08-23 01:57:17

Assignee: was

CC:  vbraun

Keywords: doctest schemes homset

The current coverage is 8% and should be brought up to 100%.

Also, there are small but annoying bugs such as: the methods that enumerate the points on schemes over finite fields do not sort the list before returning it.


---

Comment by novoselt created at 2010-11-01 02:54:46

Changing type from defect to enhancement.


---

Comment by novoselt created at 2011-12-29 18:19:02

Should be fixed in #11599.


---

Comment by novoselt created at 2012-02-20 00:29:29

Changing status from new to needs_review.


---

Comment by novoselt created at 2012-02-20 00:29:29

Indeed, it is fixed there!


---

Comment by novoselt created at 2012-02-20 00:30:12

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-02-24 15:05:17

Resolution: duplicate
