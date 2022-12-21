# Issue 7567: Fix typo in sage -advanced help text

Issue created by migration from Trac.

Original creator: wcauchois

Original creation time: 2009-12-01 05:56:33

Assignee: tbd

CC:  nthiery

As of sage-4.3.alpha0, there's a small typo in the help text you get by running sage -advanced: the line that starts with "-fixdoctest" should be "-fixdoctests", as the latter is the correct name for the command. This typo was introduced in #6354. The attached patch fixes this (apply to the repository in local/bin).


---

Attachment

based on sage 4.3.alpha0; apply to local/bin repository


---

Comment by wcauchois created at 2009-12-01 05:58:25

Changing status from new to needs_review.


---

Comment by fwclarke created at 2009-12-01 07:11:12

Changing status from needs_review to positive_review.


---

Comment by fwclarke created at 2009-12-01 07:11:12

Clearly corrects the problem.


---

Comment by mhansen created at 2009-12-01 08:17:24

Resolution: fixed


---

Comment by nthiery created at 2009-12-01 10:12:10

Replying to [comment:1 wcauchois]:

Thanks for fixing this!
