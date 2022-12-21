# Issue 4943: make sage -tp run sage -t when only one file is specified

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-01-05 22:35:56

Assignee: mabshoff

Keywords: parallel doctest testing

sage -tp is great, except it doesn't print synchronously when only one file is being tested.  It's irritating to wait for output when there are no race problems due to only a single parallel process.  Could we make sage -tp detect a single file and just run sage -t when that's the case?


---

Comment by AlexGhitza created at 2009-01-22 18:25:58

Changing type from defect to enhancement.


---

Comment by roed created at 2013-03-14 20:37:50

Changing status from new to needs_review.


---

Comment by roed created at 2013-03-14 20:37:50

This is resolved by #12415.


---

Comment by roed created at 2013-03-14 20:38:00

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-03-15 13:01:09

Resolution: duplicate
