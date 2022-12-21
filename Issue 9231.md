# Issue 9231: bring tachyon interface code to 100% coverage

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2010-06-13 12:40:15

Assignee: was

Currently 0/4 functions are tested in interfaces/tachyon.py.


---

Attachment

Adds basic documentation and doctests


---

Comment by mhampton created at 2010-06-15 00:06:12

Patch adds some basic documentation and tests.  I made some tiny changes to the code itself in order to allow help output to be printed rather than paged - this is similar to what is done for the GAP interface.


---

Comment by mhampton created at 2010-06-15 00:06:12

Changing status from new to needs_review.


---

Comment by rlm created at 2010-06-17 21:45:25

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-21 03:32:06

Resolution: fixed


---

Comment by leif created at 2010-09-03 05:10:35

Perhaps some of the people involved in this ticket are also interested in [upgrading Tachyon](http://trac.sagemath.org/sage_trac/ticket/5281)... (The *beta* version in Sage is dead old.)
