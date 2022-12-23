# Issue 9068: remove redundant sgn function from quadratic_forms/extras

Issue created by migration from https://trac.sagemath.org/ticket/9068

Original creator: cremona

Original creation time: 2010-05-27 21:00:41

Assignee: AlexGhitza

CC:  kcrisman

Keywords: sgn sign

There is a sgn() function defined in sage/quadratic_forms/extras.py which just duplicates the one in sage/functions/generalized.py, so I have removed it and adjusted imports accordingly.

May depend on #7828.


---

Attachment

Applies to 4.4.3.alpha0


---

Comment by cremona created at 2010-05-27 21:14:41

Changing status from new to needs_review.


---

Comment by AlexGhitza created at 2010-06-05 01:32:17

Changing status from needs_review to positive_review.


---

Comment by AlexGhitza created at 2010-06-05 01:32:17

Looks good.


---

Comment by mhansen created at 2010-06-06 01:16:46

Resolution: fixed
