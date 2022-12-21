# Issue 6584: Use pari to do ideal intersections

Issue created by migration from Trac.

Original creator: fwclarke

Original creation time: 2009-07-21 21:33:28

Assignee: davidloeffler

CC:  davidloeffler ncalexan

Keywords: ideal, intersecton, pari

As an addendum to #6457, I propose reworking the code to use the pari function `idealintersect`.   The patch does this.  The result is a significantly faster function. 


---

Comment by fwclarke created at 2009-07-21 21:35:15

patch against 4.1.1.alpha0


---

Attachment

The patch still applies to 4.3.1.rc0 (miracle!) and all tests in rings/number_field and libs/pari pass.


---

Comment by cremona created at 2010-01-18 20:34:03

Changing status from new to needs_review.


---

Comment by cremona created at 2010-01-18 20:34:13

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-19 00:56:17

Resolution: fixed
