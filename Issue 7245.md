# Issue 7245: sage -merge misses positively reviewed tickets

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-10-19 05:28:56

Assignee: tbd

CC:  craigcitro

Keywords: merge apply ticket

The ` sage -merge ` script doesn't detect tickets as being marked positively reviewed if they don't have "positive review" in the title.


---

Attachment

Apply to the scripts repository


---

Comment by mhansen created at 2009-10-19 05:30:30

Changing status from new to needs_review.


---

Comment by ddrake created at 2009-10-19 06:02:36

Correctly finds all tickets in the "positive review" report, and the code is just a little change to the regexps. Positive review.


---

Comment by ddrake created at 2009-10-19 06:02:36

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-19 06:03:43

Resolution: fixed
