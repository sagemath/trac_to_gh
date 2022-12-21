# Issue 8073: deprecation version number should say "After version ..."

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-01-26 07:42:16

Assignee: tbd

The docs to misc/misc.py, deprecation() say to put the current version of Sage, but the message that is printed says that the function has been deprecated "Since Sage <version>".  The "since" can be construed as >=, instead of just >.  I suggest we change "Since" to "After" to make the meaning more clear.


---

Comment by kcrisman created at 2012-06-14 14:43:00

Changing status from new to needs_review.


---

Comment by kcrisman created at 2012-06-14 14:43:00

Superseded by #13109.


---

Comment by kcrisman created at 2012-06-14 14:43:11

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-06-28 08:34:36

Resolution: duplicate
